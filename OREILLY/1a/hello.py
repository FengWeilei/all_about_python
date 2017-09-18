from flask import Flask   #从flask库中导入Flask类

app = Flask(__name__)   #实例化一个app对象（面向对象编程），传递了__name__参数（__name__变量中存储着当前模块名字，让Flask知道应用路径）

@app.route('/')  # 绑定了 / 到 hello函数的映射关系，访问'/'会调用hello函数。
def hello():
	return "Hello world!"  # hello函数返回了一个文本"Hello World!"

if __name__ == '__main__':   # 上面一样，__name__是当前模块名，当前模块被直接运行（python hello.py）而不是被其他模块导入时，__name__变量会变成"__main__"
	app.run(debug=True)   # 这里会创建本地服务器，用来处理客户端（即浏览器）的请求，打开了debug模式，服务器会一直运行，等待处理下一个请求