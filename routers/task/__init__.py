from flask import Blueprint

tasks_bp = Blueprint('tasks', __name__)

from . import create, edit, apply, change_status, my_task
