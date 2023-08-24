# Save the routes where our users can go to on our page
# Everything that isn't related to authentication (like login) comes in here

from flask import Blueprint, render_template

views = Blueprint('views', __name__) 

# Define a view
@views.route('/')
def home():
    return  render_template('index.html')