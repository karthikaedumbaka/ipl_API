from flask import Flask, request, jsonify
import ipl
import json
import new_feature

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
@app.route("/api/teams")
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)

@app.route("/api/teamvteam")

def teamvteam():
    team1=request.args.get("team1")
    team2=request.args.get("team2")
    respose = ipl.team_vs_team(team1,team2)
    print(respose)
    return jsonify(respose)

app.route('/api/team-record')
def team_record():
    team_name = request.args.get('team')
    response = jugaad.teamAPI(team_name)
    return response

@app.route('/api/batting-record')
def batting_record():
    batsman_name = request.args.get('batsman')
    response = jugaad.batsmanAPI(batsman_name)
    return response

@app.route('/api/bowling-record')
def bowling_record():
    bowler_name = request.args.get('bowler')
    response = jugaad.bowlerAPI(bowler_name)
    return response


app.run(debug=True)