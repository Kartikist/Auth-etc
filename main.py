from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/info')
def info():
    return "Puppies are cute"

@app.route('/puppy_latin/<name>')
def name(name):
    pupname=''
    if name[-1] == 'y':
        pupname = name[:-1] + 'ful'
    else:
        pupname= name+'y'
        
        
    return "{} Puppies are cute".format(pupname.upper())


if __name__ == '__main__':
    app.run(debug=True)