from flask import Flask ,render_template

# render_template is to add html files



app = Flask(__name__)

@app.route('/')   #'/' it denotes the end point

def index():
    return render_template('index.html')


@app.route('/contact')

def hello():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True ,port=3000);    