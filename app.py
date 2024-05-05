from flask import Flask,render_template,url_for,redirect
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import InputRequired, Length


app=Flask(__name__)
app.config['SECRET_KEY']="this is a secret key"

# Establish MySQL connection
connection = mysql.connector.connect(host="localhost", user="root", password="oranje57", database="flask")
cursor = connection.cursor()

class TodoForm(FlaskForm):
    activity=StringField(validators=[InputRequired(), Length(min=3)], render_kw={'placeholder': "Enter the Activity"})
    submit=SubmitField('add')
    
class EditTodoForm(FlaskForm):
    activity=StringField(validators=[InputRequired(), Length(min=3)], render_kw={'placeholder': "Update the Activity"})
    submit=SubmitField('update')
    
@app.route('/',methods=['GET','POST'])
def index():
    form=TodoForm()
    if form.validate_on_submit():
        activity=form.activity.data
        cursor.execute("select *from todo where activity=%s",(activity,))
        act=cursor.fetchall()
        if not act:
            cursor.execute('Insert into todo(activity) values(%s)',(activity,))
            connection.commit()
            form.activity.data=''
        else:
            cursor.execute('select * from todo')
            rows=cursor.fetchall()
            return render_template('todo.html',rows=rows,form=form,error="activity already exists")
    cursor.execute('select * from todo')
    rows=cursor.fetchall()
    return render_template('todo.html',rows=rows,form=form)
    


@app.route('/edittodo/<string:activity>',methods=['POST'])
def edittodo(activity):
    form=EditTodoForm()
    if form.validate_on_submit():
        update_activity=form.activity.data
        cursor.execute("update todo set activity=%s where activity=%s",(update_activity,activity))
        connection.commit()
        return redirect(url_for('index'))
    
    cursor.execute('select * from todo')
    rows=cursor.fetchall()
    return render_template('edit_todo.html',rows=rows,form=form)

@app.route('/deletetodo/<string:activity>',methods=['POST'])
def deletetodo(activity):
    cursor.execute("delete from todo where activity=%s",(activity,))
    connection.commit()
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)