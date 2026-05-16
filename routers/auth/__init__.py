from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from .login import login
from .logout import logout
from .register import register