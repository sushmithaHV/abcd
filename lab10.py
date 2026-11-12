from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return "server is running send POST request to /n8n_webhook"
@app.route('/n8n_webhook',methods=['POST'])
def n8n_webhook():
    data = request.get_json()
    print("recived from n8n:",data)
    return jsonify({"states":"received","data":data})

if __name__=='__main__':
    app.run(debug=True,port=5000)