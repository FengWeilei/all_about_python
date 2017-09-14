from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, validators
from weather import get_weather

app = Flask(__name__)

@app.route("/<name>")
def index(name):
    return render_template('index.html',name=name)

#使用了wtforms，虽然web form内容很少
class WeatherForm(FlaskForm):
    city = StringField('City', [validators.Length(min=0, max=10)])

@app.route("/weather",methods=['GET','POST'])
def weather():
    form = WeatherForm(request.form)
    if request.method == 'POST':
        city = form.city.data
        result = get_weather(city) # 调用get_weather函数来抓取天气信息，同时将结果传递到weather.html模板中。
        return render_template('weather.html',form=form,result=result)
    return render_template('weather.html',form=form)

if __name__ == '__main__':
    app.secret_key="It doesn't matter"
    app.run(debug=True)
