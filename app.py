from flask import Flask ,render_template
# render_template is to add html files

from flask_bootstrap import Bootstrap



app = Flask(__name__)
Bootstrap(app)  #enable bootastrap



@app.route('/')   #'/' it denotes the end point

def index():

    fruits=['Apple' ,'Mango' ,'Orange']
    return render_template('index.html' ,fruits_in_index=fruits)


@app.route('/contact')

def hello():
    return render_template('contact.html')

@app.route('/css')

def css():
     return render_template('css.html')


if __name__ == '__main__':
    app.run(debug=True ,port=5000);    




