from pickle import NONE

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def sigmoid(x):
    return 1/(1+np.exp(-x))

class LogisticRegression:
    
    def __init__(self,lr=0.001,n_iter=1000):
        self.lr=lr
        self.n_iter=n_iter
        self.weights=NONE
        self.bias=None

    def fit(self,X,y):
        n_samples,n_features=X.shape
        self.weights=np.zeros(n_features)
        self.bias=0

        for _ in range(self.n_iter):    
            y_pred=np.dot(X,self.weights)+self.bias
            y_pred=sigmoid(y_pred)
            dw=(1/n_samples)*(np.dot(X.T,(y_pred-y)))
            db=(1/n_samples)*np.sum(y_pred-y)

            self.weights-=self.lr*dw
            self.bias-=self.lr*db

    def predict(self,X):
        y_pred=np.dot(X,self.weights)+self.bias
        y_pred=sigmoid(y_pred)
        y_pred_cls=[1 if i>0.5 else 0 for i in y_pred]
        return np.array(y_pred_cls)

