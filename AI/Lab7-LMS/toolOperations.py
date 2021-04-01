import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model, metrics
from Persistence import *

reg = linear_model.LinearRegression()
reg.fit(trainX,trainY)
coef = reg.coef_
pred = reg.predict(testX)
toolMAE =metrics.mean_absolute_error(testY,pred)


