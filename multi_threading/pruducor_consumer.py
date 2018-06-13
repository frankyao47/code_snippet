# coding: utf-8

import threading
import random
import collections

# Basic: 单mutex

def produce(queue, mutex):
	while True:
		mutex.acquire()
		if len(queue) < 10:
			val = random.randrange(10)
			queue.append(val)
			print 'produce {}'.format(val)
		mutex.release()

def consume(queue, mutex):
	while True:
		mutex.acquire()
		if len(queue) > 0:
			val = queue.popleft()
			print 'consume {}'.format(val)
		mutex.release()


if __name__ == '__main__':
	mutex = threading.Lock()
	queue = collections.deque()
	producer = threading.Thread(target=produce, args=(queue, mutex, )).start()
	consumer = threading.Thread(target=consume, args=(queue, mutex, )).start()