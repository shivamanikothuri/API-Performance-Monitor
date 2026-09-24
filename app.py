from flask import Flask, render_template, request, jsonify
from monitor import check_api
from database import create_database, save_result, get_results

app = Flask(__name__)

create_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    url = data.get("url", "").strip()

    if not url:
        return jsonify({
            "error": "Please enter an API URL."
        })

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    result = check_api(url)
    save_result(result)

    return jsonify(result)


@app.route("/results")
def results():
    return jsonify(get_results())


if __name__ == "__main__":
    app.run(debug=True)