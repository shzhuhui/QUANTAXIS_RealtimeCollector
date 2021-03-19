import os


mongo_ip = os.environ.get('MONGODB', '192.168.0.151')
eventmq_ip = os.environ.get('EventMQ_IP', '192.168.0.151')
market_data_user = 'admin'
market_data_password = 'admin'