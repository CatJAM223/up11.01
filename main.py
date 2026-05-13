from config import create_app
from utils.crud import (
    init_db as create_table,
    index,
    admin_panel as panel,
    task_create as create,
    task_edit as edit,
    task_save as save,
    task_deactivate as deactivate,
    task_activate as activate,
    task_delete as delete,
    apply_task as apply,
    register as register_page,
    login as login_page,
    logout as logout_page
)

app = create_app()

@app.route('/')
def main():
    return index()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return register_page()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_page()

@app.route('/logout')
def logout():
    return logout_page()

@app.route('/admin')
def admin_panel():
    return panel()

@app.route('/tasks/create', methods=['GET', 'POST'])
def task_create():
    return create()

@app.route('/tasks/edit/<int:task_id>', methods=['GET', 'POST'])
def task_edit(task_id):
    return edit(task_id)

@app.route('/tasks/save', methods=['POST'])
def task_save():
    return save()

@app.route('/tasks/deactivate/<int:task_id>')
def task_deactivate(task_id):
    return deactivate(task_id)

@app.route('/tasks/activate/<int:task_id>')
def task_activate(task_id):
    return activate(task_id)

@app.route('/tasks/delete/<int:task_id>')
def task_delete(task_id):
    return delete(task_id)

@app.route('/apply/<int:task_id>')
def apply_task(task_id):
    return apply(task_id)

if __name__ == '__main__':
    create_table()
    app.run(debug=True)