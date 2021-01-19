from flask import Flask, render_template, request, json, jsonify, current_app as app 
import requests
import os

app = Flask(__name__)


album_info  = os.path.join(app.static_folder,'data','album.json')
with open(album_info,'r') as json_data:
        albums = json.load(json_data)
        

@app.route('/api/v1/albums', methods= ['GET'])
def album_json():
    return jsonify(albums)

@app.route('/api/v1/albums/pretty')
def albums_display():
    return render_template('albums.html',albums = albums)

@app.route('/api/v1/albums/search', methods= ['GET'])
def albums_search():  
    results = []

    if 'artist' in request.args:
        artist = request.args['artist']
        for album in albums:
            if artist in album['artist']:
                results.append(album)
    if 'year' in request.args:
        year = request.args['year']
        for album in albums:
            if(year == str(album['year'])):
                results.append(album)
    
    if 'song' in request.args:
        song = request.args['song'].lower()
        for album in albums:
            for s in album['songs']:
                if song in s.lower():
                    results.append(album)

    if(len(results) < 1 ):
        return "No matches found"
    else:
        return render_template("albums.html", albums = results)

if __name__ == '__main__':
	app.run(debug =True, host = "0.0.0.0")
