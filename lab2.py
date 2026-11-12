from flask import Flask,jsonify
app = Flask( __name__ )
users = [{"id":1,"name":"ram","emai":"ram@example.com"},
       {"id":2,"name":"rahul","email":"rahul@example.com"},
       {"id":3,"name":"raju","email":"raju@examole.com"},
       {"id":4,"name":"rohan","email":"rohan@example.com"},
       {"id":5,"name":"dia","email":"dia@example.com"}
]
@app.route('/users',methods=['GET'])
def get_users():
    return jsonify(users)
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id),None)
    if user:
        return jsonify(user)
    return jsonify({"error":"user not found"}),404
if __name__== "__main__":
    app.run(debug=True)
    
