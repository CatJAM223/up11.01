from flask import request, render_template, redirect, url_for, session, flash
from services.auth_service import AuthService
from . import auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        role = request.form.get('role')
        
        user, error = AuthService.authenticate(login, password, role)
        
        if user:
            session['user_id'] = user.id
            session['role'] = role
            if role == 'admin':
                return redirect(url_for('admin.admin_panel'))
            else:
                return redirect(url_for('user.view'))
        else:
            flash(error, 'error')
    
    return render_template('login.html')