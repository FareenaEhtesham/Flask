from flask import Flask ,render_template ,request ,redirect
# render_template is to add html files

from flask_bootstrap import Bootstrap

#import database

from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)
Bootstrap(app)  #enable bootastrap


# db= yaml.safe_load(open('db.yaml'))

db= yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')   #'/' it denotes the end point

def index():  
   
    fruits=['Apple' ,'Mango' ,'Orange']
    return render_template('index.html' ,fruits_in_index=fruits)


@app.route('/contact' , methods =['GET' ,'POST'])


def hello():
 # we use mysql cursor to execute mysql queries
    if request.method =="POST":
        # return "SUCCESSFULLY REGISTERED"
        # return request.form["username"]
        userDetails = request.form
        name = userDetails['user_name']
        email = userDetails['email']
        password=userDetails['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO entry(user_name, email ,password) VALUES(%s, %s,%s)",(name, email ,password))
        mysql.connection.commit()
        cur.close()
        return redirect('/')

    return render_template('contact.html')

@app.route('/css')

def css():
     return render_template('css.html')


if __name__ == '__main__':
    app.run(debug=True ,port=5000);    




