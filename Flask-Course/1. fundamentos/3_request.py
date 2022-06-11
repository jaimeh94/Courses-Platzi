from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    user_ip = request.remote_addr
    return f'Hello World Flask, tu IP es: {user_ip}'
    # return
    
if __name__ == "__main__":
    app.run(debug=True)