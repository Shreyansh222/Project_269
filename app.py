# Download the helper library from https://www.twilio.com/docs/python/install

# Import Libraries
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


# Initilize the Flask
app = Flask(__name__)


# Route and define the index function to render the home.html.
@app.route('/')
def index():
    return render_template('home.html')


if __name__ == "__main__":
    app.run()

