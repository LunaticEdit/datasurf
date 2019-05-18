import zmq
import logging

class DataSurfBroker():
	def __init__(self):
		self.context = zmq.Context()
		self.socket = self.context.socket(zmq.REP)
		self.running = True
		self.socket.bind("tcp://*:93155")
	
	def stop(self):
		self.running = False
		
	def run(self):
		while self.running:
			logging.info("Waiting for messages.")
			message = self.socket.recv()
			logging.info("Recieved: %s" % message)
			self.socket.send(b"hi")