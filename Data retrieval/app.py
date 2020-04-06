from flask import Flask ,render_template ,request ,redirect
# render_template is to add html files

from flask_bootstrap import Bootstrap

#import database

from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)
Bootstrap(app)  #enable bootastrap

#connection
db= yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS']= 'DictCursor' # This will laid us to pass in dictionary 
                                              # format in users.html file
mysql = MySQL(app)



#Display All Data from Database 
@app.route('/')

def display():
    
    cur =mysql.connection.cursor()
    result =cur.execute("select * from entry")
    if result >0:
        display_data= cur.fetchall()
        return render_template('users.html' ,display=display_data)




#Insertion Of Data
@app.route('/contact' , methods =['GET' ,'POST'])
def hello():

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





# Error handling in Python 
@app.errorhandler(404)   #page not found

def handling(e):
    return  " 404 Page not found"


if __name__ == '__main__':
    app.run(debug=True ,port=5000);    

