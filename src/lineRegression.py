import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model, discriminant_analysis, cross_validation


def load_data():
    diabetes = datasets.load_diabetes()
    return diabetes


if __name__ == '__main__':
    print(load_data())
