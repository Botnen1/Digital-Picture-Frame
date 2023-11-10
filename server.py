"""
Server side code for the digital picture frame
"""
import os
import random
#flask imports
from flask import Flask, jsonify, send_from_directory, abort


#create the flask app
app = Flask(__name__)
PHOTO_DIR = "YOUR PHOTO FOLDER HERE"

@app.route('/photos', methods=['GET'])
def list_photos():
    if not os.path.exists(PHOTO_DIR):
        abort(404, description="Photo directory not found")

    photos = os.listdir(PHOTO_DIR)
    random_photos = random.sample(photos, min(len(photos), 20))  # Get 20 random photos
    return jsonify(random_photos)

@app.route('/photos/<filename>', methods=['GET'])
def get_photo(filename):
    if not os.path.isfile(os.path.join(PHOTO_DIR, filename)):
        abort(404, description="Photo not found")

    return send_from_directory(PHOTO_DIR, filename)
#running the app
if __name__ == "__main__":
    app.run(debug=True)
    print('App is running...')
