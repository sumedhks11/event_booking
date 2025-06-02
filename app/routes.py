from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Event, Booking
from forms import LoginForm, RegisterForm, EventForm

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    events = Event.query.all()
    return render_template('home.html', events=events)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('main.home'))
        flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.', 'info')
    return redirect(url_for('main.home'))

@bp.route('/event/new', methods=['GET', 'POST'])
@login_required
def create_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(
            title=form.title.data,
            description=form.description.data,
            date=form.date.data,
            location=form.location.data,
            seats_available=form.seats_available.data
        )
        db.session.add(event)
        db.session.commit()
        flash('Event created successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_event.html', form=form)

@bp.route('/event/<int:event_id>/book')
@login_required
def book_event(event_id):
    event = Event.query.get_or_404(event_id)
    if event.seats_available <= 0:
        flash('No seats available!', 'warning')
        return redirect(url_for('main.home'))
    
    booking = Booking(user_id=current_user.id, event_id=event.id)
    event.seats_available -= 1
    db.session.add(booking)
    db.session.commit()
    flash('Event booked!', 'success')
    return redirect(url_for('main.home'))
