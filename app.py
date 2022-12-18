from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response.json()['teams']
    return render_template('index.html',teams = sorted(teams))

@app.route('/teamvteam')
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = requests.get('http://127.0.0.1:5000/api/teamvteam?team1={}&team2={}'.format(team1,team2))
    response = response.json()

    response1 = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response1.json()['teams']

    return render_template('index.html',result = response,teams = sorted(teams))

app.run(debug=True,port=7000)