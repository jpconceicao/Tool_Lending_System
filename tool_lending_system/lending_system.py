from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from tool_lending_system.auth import login_required
from tool_lending_system.db import get_db


bp = Blueprint('lending_system', __name__)


@bp.route('/index')
@login_required
def index():
    return render_template('lending_system/index.html')
