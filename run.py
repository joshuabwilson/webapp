from flask import Flask, render_template
import sqlite3
import random

app = Flask(__name__)

MENUDB = 'videos.db'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def result():

    db = sqlite3.connect(MENUDB)
    # pick a random number between 1 and 10 (there are 10 videos right now)
    random_number = random.randint(1,10)

    # connect to database
    con = sqlite3.connect(MENUDB)

    # query the database
    cur = con.execute('SELECT title,url,category FROM videos WHERE id=?', (random_number,))


    # convert the result to a list
    cur = list(cur)[0]

    # assign the result values to variables
    title = cur[0]
    url = cur[1]
    category = cur[2]

    # close the database connection
    con.close()

    # print the results
    print('the title of the video is: ' + title)
    print('the video url is: ' + url)
    print('the video category is: ' + category)

    return render_template('result.html', title=title, url=url, category=category)
