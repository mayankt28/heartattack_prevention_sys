import string
import random
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import pygal


raw_data = string.ascii_letters + string.digits #+ string.punctuation




def generate_key():
	key = ""
	for i in range(0,25):
		key+=raw_data[random.randint(0,len(raw_data)-1)]

	return key	



def generate_graph():
	# X = np.array([1,2,3,4,5])
	# y = np.array([6,7,8,9,10])

	date_chart = pygal.Line(x_label_rotation=20)
	date_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), [
	 datetime(2013, 1, 2),
	 datetime(2013, 1, 12),
	 datetime(2013, 2, 2),
	 datetime(2013, 2, 22)])
	date_chart.add("Visits", [300, 412, 823, 672])
	graph = date_chart.render().decode("utf-8")
	return graph
