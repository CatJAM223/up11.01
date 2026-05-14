from flask import session, flash, redirect, url_for, Blueprint

logout_bp = Blueprint('logout', __name__)

def logout():
    session.clear()
    flash('Вы вышли', 'info')
    return redirect(url_for('login'))