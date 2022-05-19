#inputs
from csv import reader
import numbers
import math
import csv
from random import randrange

#creating variables 
x= 0
y= 0

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

#assigning a variable to data set
#if x== 0:
 #   y== csv
 
#finding the min & max values
def dataset_minmax(dataset):
	minmax = list()
	stats = [[min(column), max(column)] for column in zip(*dataset)]
	return stats
#implementing the K-Fold method
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split
#Evaluatin an algorithm by the use of cross validation
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores
