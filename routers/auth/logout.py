from flask import session, flash, redirect, url_for
from . import auth_bp

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Вы вышли', 'info')
    return redirect(url_for('auth.login'))