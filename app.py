from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, login_manager
from forms import LoginForm, RegisterForm, TaskForm
from models import User, Task
from werkzeug.security import generate_password_hash, check_password_hash
from config import app, db


@app.route('/')
def index():
    return render_template('base.html', )


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid email or password')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful, please login')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    # Obtém todas as tarefas, não apenas as tarefas do usuário atual
    tasks = Task.query.all()
    return render_template('dashboard.html', tasks=tasks)


@app.route('/task', methods=['GET', 'POST'])
@login_required
def task():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, description=form.description.data, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully')
        return redirect(url_for('dashboard'))
    return render_template('task.html', form=form)


@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id and not current_user.is_admin:
        flash('Você não tem permissão para editar esta tarefa.')
        return redirect(url_for('dashboard'))

    form = TaskForm(obj=task)
    if form.validate_on_submit():
        form.populate_obj(task)
        db.session.commit()
        flash('Tarefa atualizada com sucesso!')
        return redirect(url_for('dashboard'))

    return render_template('edit_task.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
