#!/bin/bash

# Update and install necessary packages
apt-get update -y
apt-get install -y python3-venv curl docker.io

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
chown ubuntu:ubuntu /usr/local/bin/docker-compose

# Clone your repository
git clone https://github.com/FabioHiros/Desafio-Desenvolvimento-web.git /home/ubuntu/app

# Adjust permissions
chown -R ubuntu:ubuntu /home/ubuntu/app

# Create and enable Docker Compose service
cat <<EOF > /etc/systemd/system/docker-compose-app.service
[Unit]
Description=Docker Compose Application Service
Requires=docker.service
After=docker.service

[Service]
WorkingDirectory=/home/ubuntu/app
ExecStart=/usr/local/bin/docker-compose up -d
ExecStop=/usr/local/bin/docker-compose down
Restart=always
User=ubuntu

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable docker-compose-app.service
systemctl start docker-compose-app.service
