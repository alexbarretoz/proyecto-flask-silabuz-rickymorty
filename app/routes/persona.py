from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db import db
from app.models.persona import Personaje
import requests


#ALEX BARRETO / SILABUZ/ PERSONAJES

bp_personaje = Blueprint('bp_personaje', __name__)


@bp_personaje.route('/')
def index():
    
    URL = 'https://rickandmortyapi.com/api/character?page=n' 

    data = requests.get(URL).json() 

    for valor in data['results']:
        
        new_personaje = Personaje(
            valor["id"],
            valor["name"],
            valor["status"],
            valor["species"],
            valor["type"],       
            valor["gender"],
            valor["image"],
        )
        db.personajes.insert_one(new_personaje.to_json())
    


    personajes = db.personajes.find()
    return render_template('index.html', personajes=personajes)


