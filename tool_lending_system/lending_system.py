from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from tool_lending_system.auth import login_required
from tool_lending_system.db import get_db

from tool_lending_system.models.User import User
from tool_lending_system.models.Tool import Tool
from tool_lending_system.models.Loan import Loan

bp = Blueprint('lending_system', __name__)


@bp.route('/index', methods=('GET', ))
@login_required
def index():
    return render_template('lending_system/index.html')


@bp.route('/tools', methods=('GET', ))
@login_required
def tools():
    if request.method == 'GET':
        return render_template('lending_system/tools.html')


@bp.route('/tools/search_tools', methods=('GET', 'POST'))
@login_required
def search_tools():
    if request.method == 'GET':
        return render_template('lending_system/tools/search_tools.html')

    elif request.method == 'POST':
        print(request.form['description'])
        print(request.form['available'])
        print(request.form['location'])

        tool_obj = Tool(description=request.form['description'],
                        location=request.form['location'],
                        available=int(request.form['available'])
                        )
        tools_list = tool_obj.get_tools()
        return render_template('lending_system/tools/search_tools.html', tools=tools_list)


@bp.route('/tools/to_loan/<int:id>', methods=('GET', 'POST'))
@login_required
def to_loan(id):
    if request.method == 'GET':
        return render_template('lending_system/tools/to_loan.html')

    elif request.method == 'POST':
        return render_template('lending_system/tools/search_tools.html')


@bp.route('/tools/edit_tool/<int:id>', methods=('GET', 'POST'))
@login_required
def edit_tool(id):
    if request.method == 'GET':
        return render_template('lending_system/tools/edit_tool.html')

    elif request.method == 'POST':
        return render_template('lending_system/tools/search_tools.html')


@bp.route('/tools/add_tool', methods=('GET', 'POST'))
@login_required
def add_tool():
    if request.method == 'GET':
        return render_template('lending_system/tools/add_tool.html')

    elif request.method == 'POST':
        tool = Tool(description=request.form['description'],
                    location=request.form['location'],
                    code=request.form['code'],
                    available=1
                    )
        error = tool.create()
        if error is not None:
            flash(error)
        else:
            flash("Ferramenta inserida com sucesso!")

        return render_template('lending_system/tools/add_tool.html')

