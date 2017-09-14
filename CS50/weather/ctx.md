上篇笔记有了wsgi_app 的概念。
wsgi_app 用来连接WSGI服务器和客户端。
主要功能是调用各种函数来请求，然后将处理结果返回给服务器。

Flask 从客户端收到请求时，要让视图函数能访问一些对象，这样才能处理请求。视图函数需要知道它执行情况的请求信息（请求的 url，参数，方法等）以及应用信息（应用中初始化的数据库等），才能够正确运行。
最直观地做法是把这些信息封装成一个对象，作为参数传递给视图函数。但是这样的话，所有的视图函数都需要添加对应的参数，即使该函数内部并没有使用到它。Flask 中使用上下文把这些信息变成类似全局变量的东西。

```
    def wsgi_app(self, environ, start_response):
        ctx = self.request_context(environ)
        ctx.push()
        error = None
        try:
            try:
                response = self.full_dispatch_request()
            except Exception as e:
                error = e
                response = self.handle_exception(e)
            except:
                error = sys.exc_info()[1]
                raise
            return response(environ, start_response)
        finally:
            if self.should_ignore_error(error):
                error = None
            ctx.auto_pop(error)
```


从<code>wsgi_app()</code>函数内部的第一句<code>ctx = self.request_context(environ)</code>开始看：
<ol><li>ctx for context，这里就是上下文的意思。flask中上下文分为应用上下文和请求上下文。</li>
<li>使用<code>request_context() </code> 方法（RequestContext类）来实例化一个ctx对象。可以看出，ctx是使用栈（stack）结构来存储信息。</li>
<li>实例化ctx 后，<code>wsgi_app()</code>中接着使用了<code>ctx.push()</code>，把上下文内容进行压栈，放在了栈顶。</li>
</ol>

```
def request_context(self, environ):
	return RequestContext(self, environ)
```

到<code>RequestContext()</code>中看完整的<code>push()</code>:
<ol>
<li><code>_request_ctx_stack = LocalStack()</code>，<code>_request_ctx_stack </code>为实例化的<code>LocalStack()</code>类。</li>
<li><code>top = _request_ctx_stack.top</code> 即将栈顶的元素赋给top，<code>ctx.push()</code>语句没有传入数据，这里<code>top = None</code> 。 </li>
<li>同样的 <code>app_ctx = None</code>, 不会执行if 语句之后的内容。</li>
<li>关键的<code>_request_ctx_stack.push(self)</code>语句，这里self为上下文实例 ctx 本身，将上下文内容压缩到栈中，放在栈顶。</li>
</ol>
```
class RequestContext(object):
    """The request context contains all request relevant information.  It is
    created at the beginning of the request and pushed to the
    `_request_ctx_stack` and removed at the end of it.  It will create the
    URL adapter and request object for the WSGI environment provided.
    """
    ...
    def push(self):
        """Binds the request context to the current context."""
        top = _request_ctx_stack.top
        if top is not None and top.preserved:
            top.pop(top._preserved_exc)

        # Before we push the request context we have to ensure that there is an application context.
        app_ctx = _app_ctx_stack.top
        if app_ctx is None or app_ctx.app != self.app:
            app_ctx = self.app.app_context()
            app_ctx.push()
            self._implicit_app_ctx_stack.append(app_ctx)
        else:
            self._implicit_app_ctx_stack.append(None)

        if hasattr(sys, 'exc_clear'):
            sys.exc_clear()

        _request_ctx_stack.push(self)

        self.session = self.app.open_session(self.request)
        if self.session is None:
            self.session = self.app.make_null_session()
```

```
# context locals
_request_ctx_stack = LocalStack()
_app_ctx_stack = LocalStack()
current_app = LocalProxy(_find_app)
request = LocalProxy(partial(_lookup_req_object, 'request'))
session = LocalProxy(partial(_lookup_req_object, 'session'))
g = LocalProxy(partial(_lookup_app_object, 'g'))
```

有了上下文的概念，继续看<code>wsgi_app()</code>:

 <code>response = self.full_dispatch_request()</code>，将<code>full_dispatch_request()</code>方法的返回内容赋值给<code>response</code>，最后返回到服务器。

看<code>full_dispatch_request()</code>：

```
    def full_dispatch_request(self):
        """Dispatches the request and on top of that performs request
        pre and postprocessing as well as HTTP exception catching and
        error handling.

        .. versionadded:: 0.7
        """
        self.try_trigger_before_first_request_functions() #发生真实请求前的处理
        try:
            request_started.send(self)  #socket部分的操作
            rv = self.preprocess_request()  #请求的预处理
            if rv is None:
                rv = self.dispatch_request()
        except Exception as e:
            rv = self.handle_user_exception(e)
        return self.finalize_request(rv)
```
\__init__函数中设置了<code>self._got_first_request = False</code>，<code>try_trigger_before_first_request_functions()</code>的最后一句设置了<code>self._got_first_request = True</code>,即``got_first_request(self)`` 中描述的 This attribute is set to ``True`` if the application started handling the first request.
表明现在开始处理程序了。
```
    def try_trigger_before_first_request_functions(self):
        """Called before each request and will ensure that it triggers
        the :attr:`before_first_request_funcs` and only exactly once per
        application instance (which means process usually).

        :internal:
        """
        if self._got_first_request:
            return
        with self._before_request_lock:
            if self._got_first_request:
                return
            for func in self.before_first_request_funcs:
                func()
            self._got_first_request = True
```

```
    def got_first_request(self):
        """This attribute is set to ``True`` if the application started
        handling the first request.

        .. versionadded:: 0.8
        """
        return self._got_first_request
```

接着看<code>full_dispatch_request()</code> :

``try`` 中的 ``request_started.send(self)`` ：

```
request_started = _signals.signal('request-started')
```
