from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
# from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash, check_password_hash

from tool_lending_system.auth import login_required, login_adm_required
from tool_lending_system.db import get_db

bp = Blueprint('admin', __name__)
