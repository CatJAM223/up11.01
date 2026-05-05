from config import create_app
from utils.crud import (
    init_db as create_table,
    index,
    admin_panel as panel,
    task_create as create,
    task_edit as edit,
    task_save as save,
    apply_task as apply
)
                        

app = create_app()

@app.route('/')
def main():
    return index()

@app.route('/admin')
def admin_panel():
    return panel()

@app.route('/tasks/create')
def task_create():
    return create()

@app.route('/tasks/edit/<int:task_id>')
def task_edit():
    return edit()

@app.route('/tasks/save', methods=['POST'])
def task_save():
    return save()

@app.route('/apply/<int:task_id>')
def apply_task():
    return apply()

if __name__ == '__main__':
    create_table()
    app.run(debug=True)