from flask import *
import sqlite3

DATABASE = 'books.db'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/admin')
def admin():
    g.db = connect_db()
    cur = g.db.execute('select rep_title,category from reps')
    books = [dict(rep_title=row[0],category=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('admin.html',books=books)
    
@app.route('/userlogin')
def userlogin():
    error = None
    if request.method == 'POST':
        if request.form['email'] == 'mukosh@yahoo.com' or request.form['password']== 'admin':
            return redirect (url_for('users'))
    return render_template('userlogin.html')

@app.route('/users')
def users():
    g.db = connect_db()
    cur = g.db.execute('select rep_title,category from reps')
    books = [dict(rep_title=row[0],category=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('users.html',books=books)
    
@app.route('/borrow')
def borrow():
    if request.method == 'POST':
        if request.form['book']:
            g.db = connect_db()
            cur = g.db.execute('select rep_title,category from reps')    
            books = [dict(rep_title=row[0],category=row[1]) for row in cur.fetchall()]
            g.db.close()
            return redirect('borrow.html',books=books)    


@app.route('/',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'mukosh@yahoo.com' or request.form['password']!= 'admin':
            error = 'Invalid credentials .please try again'
        else:
            return redirect (url_for('admin'))
        
    return render_template('login.html')
   
if __name__== '__main__':
    app.run()
    
    




