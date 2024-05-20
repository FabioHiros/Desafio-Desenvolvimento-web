#!/bin/bash


apt-get update -y
mkdir /home/ubuntu/app
apt install curl
apt install docker.io -y
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
sudo chown ubuntu:ubuntu /usr/local/bin/docker-compose


git clone https://github.com/FabioHiros/Desafio-Desenvolvimento-web.git /home/ubuntu/app


chown -R ubuntu:ubuntu /home/ubuntu/app



cd /home/ubuntu/app

/usr/local/bin/docker-compose up -d


usermod -aG docker $USER

bash -c 'cat <<EOF > /etc/systemd/system/docker-compose-app.service
[Unit]
Description=Docker Compose Application Service
Requires=docker.service
After=docker.service

[Service]
WorkingDirectory=/home/ubuntu/app
ExecStart=/usr/bin/docker compose up
ExecStop=/usr/bin/docker compose down
Restart=always
User=ubuntu

[Install]
WantedBy=multi-user.target
EOF'

systemctl daemon-reload
systemctl enable docker-compose-app.service

systemctl start docker-compose-app.service
