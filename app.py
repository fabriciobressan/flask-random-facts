#!/usr/bin/env python3
import os
import random
import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'facts.db')
db = SQLAlchemy(app)

# Database Model
class Fact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(80), nullable=False)
    text = db.Column(db.String(250), nullable=False)
    def __repr__(self):
        return f'<Fact {self.id}>'

# Your API key
api_key = "yaJNs0Tk1dWA7yzE9O2PgA==9jzwlAmWbUXTZ5sO"
api_url = "https://api.api-ninjas.com/v1/facts"

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        new_fact = request.form['new_fact']
        db.session.add(Fact(topic='User Submitted', text=new_fact))
        db.session.commit()
    
    # We now have two options for where to get a fact
    fact_source = random.choice(['database', 'api'])

    if fact_source == 'database':
        all_facts = Fact.query.all()
        random_fact_object = random.choice(all_facts)
        topic = random_fact_object.topic
        fact = random_fact_object.text
    else:
        try:
            response = requests.get(
                api_url,
                headers={'X-Api-Key': api_key}
            )
            response.raise_for_status()
            data = response.json()
            topic = "API Fact"
            fact = data[0]['fact']
        except requests.exceptions.RequestException:
            # If the API fails, we fall back to the database
            all_facts = Fact.query.all()
            random_fact_object = random.choice(all_facts)
            topic = random_fact_object.topic
            fact = random_fact_object.text

    return render_template('home.html', topic=topic, fact=fact)

@app.route('/api-fact')
def api_fact():
    try:
        response = requests.get(
            api_url,
            headers={'X-Api-Key': api_key}
        )
        response.raise_for_status()
        data = response.json()
        fact = data[0]['fact']
        return f"<h1>Random API Fact</h1><p>{fact}</p>"
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return "Failed to retrieve fact from API."


if __name__ == '__main__':
    app.run(debug=True, port=8000)