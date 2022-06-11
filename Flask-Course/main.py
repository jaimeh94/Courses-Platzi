from flask import (
    Flask,
    request,
    make_response,
    redirect
)

app = Flask(__name__)

@app.route('/')
def index():

    user_ip = request.remote_addr
    make = redirect('/hello')
    response = make_response(make)
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/hello')
def hello():    

    mensaje = 'Hola Mundo!!'
    user_ip = request.cookies.get('user_ip')

    return mensaje + user_ip

if __name__ == "__main__":
    app.run(debug=True)

