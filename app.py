from flask import Flask

app=Flask(__name__)

@app.route("/", methods=['GET', 'POS'])
def index():
    return "Starting a machine leanring project"

if __name__=="__main__":
    app.run(debug=True)