from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
# from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash, check_password_hash

from tool_lending_system.auth import login_required, login_adm_required
from tool_lending_system.db import get_db

from tool_lending_system.models.User import User
from tool_lending_system.models.Tool import Tool
from tool_lending_system.models.Loan import Loan

bp = Blueprint('admin', __name__)


@bp.route('/dashboard', methods=('GET', ))
@login_required
@login_adm_required
def dashboard():
    return render_template('admin/dashboard.html')


@bp.route('/dashboard/users', methods=('GET', ))
@login_required
@login_adm_required
def usuarios():
    return render_template('admin/users.html')


@bp.route('/dashboard/search_user', methods=('GET', 'POST'))
@login_required
@login_adm_required
def search_user():
    if request.method == 'GET':
        return render_template('admin/users/search_user.html')

    if request.method == 'POST':
        user = User(email=request.form['email'])
        users = user.get_users()
        return render_template('admin/users/search_user.html', users=users)


@bp.route('/dashboard/add_user', methods=('GET', 'POST'))
@login_required
@login_adm_required
def add_user():
    if request.method == 'GET':
        return render_template('admin/users/add_user.html')

    elif request.method == 'POST':
        user = User(name=request.form['name'],
                    email=request.form['email'],
                    password=request.form['password'],
                    status='active'
                    )
        error = user.create()

        if error is not None:
            flash(error)
        else:
            print('Usuário cadastrado')  # DEBUG
            flash('Usuário cadastrado com sucesso!')

        return render_template('admin/users/add_user.html')


@bp.route('/dashboard/edit_user/<int:id>', methods=('GET', 'POST'))
@login_required
@login_adm_required
def edit_user(id):
    if request.method == 'GET':
        user_obj = User(id=id)
        user = user_obj.get_user_by_id()
        return render_template('admin/users/edit_user.html', user=user)

    elif request.method == 'POST':
        return render_template('admin/users/edit_user.html')


@bp.route('/dashboard/location', methods=('GET', ))
@login_required
@login_adm_required
def location():
    return render_template('admin/location.html')


@bp.route('/dashboard/logs', methods=('GET', ))
@login_required
@login_adm_required
def logs():
    return render_template('admin/logs.html')


@bp.route('/dashboard/my_account', methods=('GET', 'POST'))
@login_required
@login_adm_required
def my_account():
    if request.method == 'GET':
        return render_template('admin/my_account.html', user=g.user)

    elif request.method == 'POST':
        user = User(id=g.user['id'])
        error = None

        if request.form['password'] == "":
            user.name = request.form['name']
            user.email = request.form['email']
            error = user.update_without_password()

        else:
            user.name = request.form['name']
            user.email = request.form['email']
            user.password = request.form['password']
            error = user.update_with_password()

        if error is not None:
            flash(error)
        else:
            flash('Edição do seu usuário realizada com sucesso!')
            g.user = user.get_user_by_id()

        return redirect(url_for('admin.my_account'))
