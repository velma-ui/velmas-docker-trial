from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hey, this is Velma’s Docker trial application docker compose included!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

