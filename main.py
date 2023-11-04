from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/base')
def base():
    return render_template("base.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

# @app.route('/info')
# def info():
#     return "Puppies are cute"

# @app.route('/puppy_latin/<name>')
# def name(name):
#     pupname=''
#     if name[-1] == 'y':
#         pupname = name[:-1] + 'ful'
#     else:
#         pupname= name+'y'
        
        
#     return "{} Puppies are cute".format(pupname.upper())


if __name__ == '__main__':
    app.run(debug=True)