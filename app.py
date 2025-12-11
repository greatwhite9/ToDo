from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)  # Creating app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Configuring database to app 
db = SQLAlchemy(app)  # Initializing database 

class Todo(db.Model):  # Creating Database 
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True) # First column for primary key
    content = db.Column(db.String(200), nullable=False) # Second column of content 
    date_created = db.Column(db.DateTime, default=datetime.utcnow) # Third column of date
    
    def __repr__(self): # For assigning primary key
        return '<task %r>' %self.id

with app.app_context():
    db.create_all() 


@app.route('/', methods=['POST', 'GET']) # First page
def index():
    if request.method == 'POST':
        task_content = request.form['content'] # Getting task from html page 
        new_task = Todo(content=task_content) # Creating instance of task in table
        try: 
            db.session.add(new_task) # Adding task to table
            db.session.commit() # Saving
            return redirect('/') 
        except:
            return 'There was an issue adding your task '
        
    else:
        task = Todo.query.order_by(Todo.date_created).all() # Showing table
        
        return render_template('index.html', tasks=task)

@app.route('/delete/<int:id>') 
def delete(id): 
    task_delete = Todo.query.get_or_404(id) # Getting id to delete from user
    
    try:
        db.session.delete(task_delete) # Query to delete
        db.session.commit() # Saving changes
        return redirect('/')
    except:
        return "Error" 
    
@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):    
    task = Todo.query.get_or_404(id) # getting id
    if request.method == 'POST': 
        task.content = request.form['content'] # changing value
        
        try: 
            db.session.commit() # Saving the changed value
            return redirect('/')
        except:
            return 'Error'
    else:
        return render_template('update.html', tasks=task)
    
if __name__ == "__main__":  
    app.run(debug=True)
    