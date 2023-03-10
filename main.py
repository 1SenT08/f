from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Миссия Колонизация Марса</h1>"

@app.route('/index')
def countdown():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


@app.route('/promotion')
def promation():
    countdown_list = ['<h1>Человечество вырастает из детства.</h1>', '<h1>Человечеству мала одна планета.</h1>',
                      '<h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>', '<h1>И начнем с Марса!</h1>',
                      '<h1>Присоединяйся!</h1>']
    return '</br>'.join(countdown_list)


@app.route('/image_mars')
def im():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/tmp.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')