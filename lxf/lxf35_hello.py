# -*- coding: utf-8 -*-

# 创建一个HTTP处理函数，接收两个参数，
# environ：一个包含所有HTTP请求信息的 dict 对象
# start_response：一个发送HTTP响应的函数

def application(environ, start_response):
	# 调用start_response()发送HTTP响应的Header. 
	# 接收两个参数，第一个HTTP响应码，第二个list表示的HTTP Header，这里指明了响应内容的类型
	start_response('200 OK', [('Content-Type', 'text/html')])
	body = '<h1> Hello, %s!' % (environ['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')]  # 函数返回值作为HTTP响应的Body发送给浏览器。



# 有了WSGI，我们关心的就是如何从environ这个dict对象拿到HTTP请求信息，然后构造HTML，
# 通过start_response()发送Header，最后返回Body。
# 整个application()函数本身没有涉及到任何解析HTTP的部分，也就是说，底层代码不需要我们自己编写，
# 我们只负责在更高层次上考虑如何响应请求就可以了。
# 不过，等等，这个application()函数怎么调用？
# 如果我们自己调用，两个参数environ和start_response我们没法提供，返回的bytes也没法发给浏览器。
# 所以application()函数必须由WSGI服务器来调用。有很多符合WSGI规范的服务器，我们可以挑选一个来用。
# 但是现在，我们只想尽快测试一下我们编写的application()函数真的可以把HTML输出到浏览器，
# 所以，要赶紧找一个最简单的WSGI服务器，把我们的Web应用程序跑起来。
# 好消息是Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。
# 所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。