# EC2 Deployment Guide

## Prerequisites
- AWS EC2 t2.micro instance
- SSH access to the instance
- Domain name (if using)
- SSL certificate (if using HTTPS)

## Initial Setup

1. Connect to EC2 instance:
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

2. Update system packages:
   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

3. Install required packages:
   ```bash
   sudo apt install -y python3-pip python3-venv nginx postgresql postgresql-contrib
   ```

4. Create swap space (if not already done):
   ```bash
   sudo fallocate -l 2G /swapfile
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   sudo swapon /swapfile
   echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
   ```

## Application Setup

1. Create application directory:
   ```bash
   sudo mkdir -p /var/www/ai-training
   sudo chown ubuntu:ubuntu /var/www/ai-training
   ```

2. Clone repository:
   ```bash
   cd /var/www/ai-training
   git clone https://github.com/yourusername/ai-training-platform.git .
   ```

3. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. Create production environment file:
   ```bash
   nano .env.production
   ```
   Add the following content:
   ```
   FLASK_ENV=production
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgresql://username:password@localhost/ai_training
   ```

5. Initialize database:
   ```bash
   python setup_local_db.py
   python create_quiz.py
   ```

## Nginx Configuration

1. Create Nginx configuration:
   ```bash
   sudo nano /etc/nginx/sites-available/ai-training
   ```

2. Add the following configuration:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;  # or your IP address

       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }

       location /static {
           alias /var/www/ai-training/app/static;
           expires 30d;
           add_header Cache-Control "public, no-transform";
       }

       location /videos {
           alias /var/www/ai-training/app/static/modules;
           expires 30d;
           add_header Cache-Control "public, no-transform";
       }
   }
   ```

3. Enable the site:
   ```bash
   sudo ln -s /etc/nginx/sites-available/ai-training /etc/nginx/sites-enabled
   sudo nginx -t
   sudo systemctl restart nginx
   ```

## Systemd Service

1. Create systemd service file:
   ```bash
   sudo nano /etc/systemd/system/ai-training.service
   ```

2. Add the following content:
   ```ini
   [Unit]
   Description=AI Training Platform
   After=network.target

   [Service]
   User=ubuntu
   Group=ubuntu
   WorkingDirectory=/var/www/ai-training
   Environment="PATH=/var/www/ai-training/venv/bin"
   Environment="FLASK_ENV=production"
   ExecStart=/var/www/ai-training/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:5000 wsgi:app

   [Install]
   WantedBy=multi-user.target
   ```

3. Enable and start the service:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable ai-training
   sudo systemctl start ai-training
   ```

## File Permissions

1. Set proper permissions:
   ```bash
   sudo chown -R ubuntu:ubuntu /var/www/ai-training
   sudo chmod -R 755 /var/www/ai-training
   sudo chmod -R 644 /var/www/ai-training/app/static/modules/*.mp4
   sudo chmod -R 644 /var/www/ai-training/app/static/quizzes/*.json
   ```

## Deployment Process

1. Pull latest changes:
   ```bash
   cd /var/www/ai-training
   git pull
   ```

2. Update dependencies:
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Update database:
   ```bash
   python update_modules.py
   python create_quiz.py
   ```

4. Restart the service:
   ```bash
   sudo systemctl restart ai-training
   ```

## Monitoring

1. Check service status:
   ```bash
   sudo systemctl status ai-training
   ```

2. View logs:
   ```bash
   sudo journalctl -u ai-training -f
   ```

3. Check Nginx logs:
   ```bash
   sudo tail -f /var/log/nginx/error.log
   sudo tail -f /var/log/nginx/access.log
   ```

## Backup

1. Create backup script:
   ```bash
   nano backup.sh
   ```

2. Add the following content:
   ```bash
   #!/bin/bash
   TIMESTAMP=$(date +%Y%m%d_%H%M%S)
   BACKUP_DIR="/var/backups/ai-training"
   
   mkdir -p $BACKUP_DIR
   pg_dump ai_training > $BACKUP_DIR/db_$TIMESTAMP.sql
   tar -czf $BACKUP_DIR/static_$TIMESTAMP.tar.gz /var/www/ai-training/app/static
   ```

3. Make it executable:
   ```bash
   chmod +x backup.sh
   ```

4. Add to crontab:
   ```bash
   crontab -e
   ```
   Add:
   ```
   0 0 * * * /var/www/ai-training/backup.sh
   ```

## Troubleshooting

1. Check service status:
   ```bash
   sudo systemctl status ai-training
   ```

2. Check logs:
   ```bash
   sudo journalctl -u ai-training -f
   ```

3. Check Nginx configuration:
   ```bash
   sudo nginx -t
   ```

4. Check file permissions:
   ```bash
   ls -la /var/www/ai-training/app/static/modules/
   ls -la /var/www/ai-training/app/static/quizzes/
   ```

5. Check database connection:
   ```bash
   psql -U postgres -d ai_training
   ``` 