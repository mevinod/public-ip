from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    ip_address = request.remote_addr
    return f"<div style='text-align: center; font-size: 36px; margin-top: 20%;'>Your public IP address is: {ip_address}</div>"

if __name__ == '__main__':
    app.run(debug=True)

