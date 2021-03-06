from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def show_mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def show_motto():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return '<br>'.join(['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                        'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
                        'Присоединяйся!'])


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                        <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1">
                                <title>Привет, Марс!</title>
                            </head>
                            <body>
                                <h1>Жди нас, Марс!</h1>
                                <img src="{url_for('static', filename='img/mars.png')}">
                                <p>Вот она какая, красная планета</p>
                            </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
