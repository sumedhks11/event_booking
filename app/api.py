from flask import Blueprint,jsonify,request
from .models import Event
from . import db

api=Blueprint('api',__name__)

@api.route('/events',methods=['GET'])
def get_events():
    events=Event.query.all()
    return jsonify([{'id':e.id,'title':e.title,'date':e.date,'location':e.location,'description':e.description} for e in events])

@api.route('/events',methods=['POST'])
def add_event():
    data=request.get_json()
    new_event=Event(
        title=data['title'],
        date=data['date'],
        location=data['location'],
        description=data['description']
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message':'Eevnt created'}), 201