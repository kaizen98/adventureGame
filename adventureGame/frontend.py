from flask import Flask, render_template, jsonify
from backend import adventureGame

app = Flask(__name__)

# map = [['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
# 	   ['|',' ',' ',' ',' ','|',' ',' ',' ',' ','|',' ',' ',' ','|'],
# 	   ['|',' ',' ',' ',' ','|',' ',' ',' ',' ','|',' ',' ',' ','|'],
# 	   ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ','|'],
# 	   ['|','-','-','-','-','|',' ',' ',' ',' ','|',' ',' ',' ','|'],
# 	   ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ','|'],
# 	   ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
# 	   ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ','|'],
# 	   ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ','|','-','-','-','|'],
# 	   ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
# 	   ['|','x',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ','|'],
# 	   ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
# 	   ]
map = [['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
	   ['|',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ','|'],
	   ['|',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ','|'],
	   ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ','|'],
	   ['|','-','-','-','-',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ','|'],
	   ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ','|'],
	   ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
	   ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ','|'],
	   ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|','-','-','-','|'],
	   ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
	   ['|','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ','|'],
	   ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
	   ]
game = adventureGame()

@app.route("/")
def home():
	game.startGame(map)
	print("*********************************************started")
	return render_template("index.html")

@app.route("/getStatus", methods=["GET"])
def getStatus():
	print(game.getStatus())
	return jsonify(game.getStatus())

if __name__ == "__main__":
	app.run(debug=True)