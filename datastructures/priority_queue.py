from abc import ABCMeta, abstractmethod

class PriorityQueue:
	__metaclass__ = ABCMeta

	@abstractmethod
	def insert(self, id, value, priority):
		pass
	
	@abstractmethod
	def delete(self, id):
		pass

	@abstractmethod
	def pop(self):
		pass

	@abstractmethod
	def peak(self):
		pass

	@abstractmethod
	def update(self, id, priority):
		pass
