from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuring the SQLAlchemy database

uri = os.environ.get('DATABASE_URL', 'postgresql://user:password@db:5432/todo_db')
print(f"Using database URI: {uri}")  # Debugging line to check the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = uri
db = SQLAlchemy(app)

# TodoItem model representing a table in the database
class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<TodoItem {self.id}>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Creating a new TodoItem object and adding it to the database
        content = request.form['content']
        if content.strip() != '':
            new_item = TodoItem(content=content)
            db.session.add(new_item)
            db.session.commit()
        return redirect('/')
    else:
        # Querying all TodoItem objects from the database and rendering the template
        items = TodoItem.query.all()
        return render_template('index.html', items=items)


@app.route('/complete/<int:item_id>')
def complete(item_id):
    # Retrieving a TodoItem object by ID, marking it as completed, and committing the changes
    item = TodoItem.query.get_or_404(item_id)
    item.completed = True
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:item_id>')
def delete(item_id):
    # Retrieving a TodoItem object by ID, deleting it, and committing the changes
    item = TodoItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    # Creating the database tables
    with app.app_context():
        db.create_all()
    
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
    # app.run(debug=True)