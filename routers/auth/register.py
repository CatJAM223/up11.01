from flask import Blueprint, request, render_template, redirect, url_for
from services.user_service import UserService
from . import auth_bp

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        
        user, message = UserService.register_user(name, login, password)
        
        if user:
            return redirect(url_for('auth.login'))
        else:
            return render_template('register.html', error=message)
    
    return render_template('register.html')

