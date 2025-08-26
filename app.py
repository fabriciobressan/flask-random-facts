#!/usr/bin/env python3
# Import the Flask class
from flask import Flask, render_template, request
import random

themed_facts = {
    "Animals": "A group of flamingos is called a flamboyance.",
    "Space": "There are more trees on Earth than stars in the Milky Way.",
    "Food": "Honey never spoils.",
    "User Submitted": [] # This is a new entry to hold user-submitted facts
}

# Create an instance of the class
app = Flask(__name__)

# Define a route for the homepage ('/')
@app.route('/', methods=['GET', 'POST'])                         
def hello_world():
    if request.method == 'POST':
        new_fact = request.form['new_fact']
        themed_facts['User Submitted'].append(new_fact)
        print("New fact submitted:", new_fact)
    
    # We'll now secect a random fact from all the available facts
    all_facts = []
    for topic, facts in themed_facts.items():
        if isinstance(facts, list):
            for fact in facts:
                all_facts.append((topic, fact))
        else:
            all_facts.append((topic, facts))
            
    random_topic, random_fact = random.choice(all_facts)

    return render_template('home.html', topic=random_topic, fact=random_fact)

# Run the application
if __name__ == '__main__':
    app.run(debug=True, port=8000)
    
