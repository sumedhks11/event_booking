from flask import Blueprint,render_template
from .models import Event
main=Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/events')
def events():
    all_events=Event.query.all()
    return render_template('events.html',events=all_events)