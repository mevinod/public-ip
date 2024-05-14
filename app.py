from flask import Flask, request

app = Flask(__name__)

def get_visitor_ip():
    # Check if request is coming from a proxy
    if request.headers.get('X-Forwarded-For'):
        # Return the first IP address in the list (client's IP)
        return request.headers.get('X-Forwarded-For').split(',')[0]
    else:
        # Return the direct IP address of the client
        return request.remote_addr

@app.route('/')
def index():
    ip_address = get_visitor_ip()
    return f"<div style='text-align: center; font-size: 36px; margin-top: 20%;'>Your public IP address is: {ip_address}</div>"

if __name__ == '__main__':
    app.run(debug=True)

