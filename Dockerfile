FROM opensuse/leap:latest
RUN zypper ref 
RUN zypper -n update
RUN zypper in -y tcpdump iproute2 iptables sudo openssh curl python3 python3-pip
RUN pip install --upgrade pip
RUN zypper in -y iputils
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
EXPOSE 5000
ADD src /src
CMD ["python3", "/src/flask_app.py"]
