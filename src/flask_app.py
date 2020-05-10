from flask import Flask, render_template, url_for
import socket 
from netifaces import interfaces, ifaddresses, AF_INET

app = Flask(__name__)

@app.route("/")
def home():
    host = get_host_details()
    return render_template('base.html', host=host)

def get_host_details():
    host = {}
    host["name"] = socket.gethostname()
    host['addresses'] = []
    for interfacename in interfaces():
        address = {}
        for ifaddress in ifaddresses(interfacename)[AF_INET]:
            address['ifacename'] = interfacename
            address['ipv4address'] = ifaddress['addr']
            host['addresses'].append(address)
    host["ip"] = socket.gethostbyname(host["name"])
    return host

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

