import os
import subprocess
import logging
from datetime import datetime

logging.basicConfig(filename='backup.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s: %(message)s')

SOURCE_DIRECTORY = '/path/to/source/directory'
REMOTE_SERVER = 'user@remote-server:/path/to/backup/directory'
SSH_KEY = '/path/to/ssh/key'

def perform_backup():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_command = [
        'rsync', '-avz', '-e', f'ssh -i {SSH_KEY}', SOURCE_DIRECTORY, REMOTE_SERVER
    ]

    try:
        result = subprocess.run(backup_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f'Backup successful: {result.stdout.decode("utf-8")}')
    except subprocess.CalledProcessError as e:
        logging.error(f'Backup failed: {e.stderr.decode("utf-8")}')

if __name__ == "__main__":
    perform_backup()