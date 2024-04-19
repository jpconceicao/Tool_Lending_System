import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from tool_lending_system.db import get_db
from tool_lending_system.models.User import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        level_acesso = request.form['level_acesso']
        status = 'ativo'

        db = get_db()
        error = None

        if not nome:
            error = 'nome é requerido.'
        elif not email:
            error = 'email é requerido.'
        elif not senha:
            error = 'senha é requerida'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO usuario (nome,  email, senha, level_acesso, status) VALUES (?, ?, ?, ?, ?)",
                    (nome, email, generate_password_hash(senha), level_acesso, status),
                )
                db.commit()

            except db.IntegrityError:
                error = f"usuario já está registrado."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        user = User(email=request.form['email'], password=request.form['password'])
        error_dict = user.auth()

        if error_dict['error'] is None:
            session.clear()
            session['user_id'] = error_dict['user']['id']
            return redirect(url_for('lending_system.index'))
        else:
            flash(error_dict['error'])

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


def login_adm_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user['level_acesso'] != 'admin':
            return redirect(url_for('estoque.index'))

        return view(**kwargs)

    return wrapped_view
