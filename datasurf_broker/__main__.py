import logging
from datasurf_broker import DataSurfBroker

if __name__ == '__main__':
	logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
	logging.info('DataSurf Broker is starting')
	broker = DataSurfBroker()
	broker.run()