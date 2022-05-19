#inputs
from csv import reader
import numbers
import math
from tkinter import X, Variable

#importing the data set
def load_csv(HeartDiesease):
	dataset = list()
	with open(HeartDiesease,'r') as file:
		csv_reader = reader(HeartDiesease)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
