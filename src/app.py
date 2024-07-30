from flask import Flask, jsonify
from user import user

app = Flask(__name__)

# Routes
@app.route("/python", methods=["GET"])
def ping():
    return jsonify({"response": "SERVER PYTHON ABRAHAM USER"})


@app.route("/users")
def usershandler():
    return jsonify({"user": user})

# Start the Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)