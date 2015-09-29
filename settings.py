import socket
import datetime


# EXTERNAL_IPS = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]

# https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib#answer-166589
#EXTERNAL_IP = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) \
#               for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]

EXTERNAL_IP = "106.185.49.44"

DB_NAME = "position-log.sqlite3"

# TIMEOUT_INTERVAL = datetime.timedelta(minutes = 2)
TIMEOUT_INTERVAL = datetime.timedelta(days = 2)
