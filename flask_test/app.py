from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POvenuST":
        score = int(request.form["score"])
        result = f"入力された点数は {score} 点です"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
