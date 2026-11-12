from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/students",methods = ["GET"])
def get_students():
    students = [
        {
            "id":1,
            "name":"rahul"
        },
        {
            "id":2,
            "name":"anjali"
        }
    ]
    return jsonify(students)
app.run(