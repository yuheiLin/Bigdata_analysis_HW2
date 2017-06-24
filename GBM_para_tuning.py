#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 14:33:22 2017

@author: hangpinglin
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier  #GBM algorithm
from sklearn import cross_validation, metrics   #Additional scklearn functions
from sklearn.grid_search import GridSearchCV   #Perforing grid search
from sklearn.model_selection import cross_val_score

import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from datetime import datetime,date,time

start_time = datetime.now()
rcParams['figure.figsize'] = 12, 4

train = pd.read_csv('/Users/hangpinglin/big/dataset/LargeTrain.csv')
predictors = train.columns[:10]
X=train[predictors]
y=train['Class']
print train.shape
print X.shape
print y.shape

'''
param_test1 = {'n_estimators':range(450,651,50)}
gsearch1 = GridSearchCV(estimator = GradientBoostingClassifier(learning_rate=0.2, min_samples_split=500,min_samples_leaf=50,max_depth=8,max_features='sqrt',subsample=0.8,random_state=10), 
param_grid = param_test1,n_jobs=4,iid=False, cv=5)
gsearch1.fit(X,y)
print gsearch1.grid_scores_
print gsearch1.best_params_,
print gsearch1.best_score_
'''

'''
param_test2 = {'max_depth':range(5,16,2), 'min_samples_split':range(200,1001,200)}
gsearch2 = GridSearchCV(estimator = GradientBoostingClassifier(learning_rate=0.2, n_estimators=500, max_features='sqrt', subsample=0.8, random_state=10), 
param_grid = param_test2,n_jobs=4,iid=False, cv=5)
gsearch2.fit(X,y)
print gsearch2.grid_scores_
print gsearch2.best_params_,
print gsearch2.best_score_
'''

'''
param_test3 = {'min_samples_leaf':range(70,201,20)}
gsearch3 = GridSearchCV(estimator = GradientBoostingClassifier(learning_rate=0.2, n_estimators=500,max_depth=9,max_features='sqrt', subsample=0.8, random_state=10), 
param_grid = param_test3,n_jobs=4,iid=False, cv=5)
gsearch3.fit(X,y)
print gsearch3.grid_scores_
print gsearch3.best_params_,
print gsearch3.best_score_
'''

'''
param_test4 = {'max_features':range(2,11,2)}
gsearch4 = GridSearchCV(estimator = GradientBoostingClassifier(learning_rate=0.2, n_estimators=500,max_depth=9, min_samples_split=200, min_samples_leaf=70, subsample=0.8, random_state=10),
param_grid = param_test4,n_jobs=4,iid=False, cv=5)
gsearch4.fit(X,y)
print gsearch4.grid_scores_
print gsearch4.best_params_,
print gsearch4.best_score_
'''

'''
param_test5 = {'subsample':[0.6,0.7,0.75,0.8,0.85,0.9]}
gsearch5 = GridSearchCV(estimator = GradientBoostingClassifier(learning_rate=0.2, n_estimators=500,max_depth=9,min_samples_split=200, min_samples_leaf=70, random_state=10,max_features=8),
param_grid = param_test5,n_jobs=4,iid=False, cv=5)
gsearch5.fit(X,y)
print gsearch5.grid_scores_
print gsearch5.best_params_,
print gsearch5.best_score_
'''

the_GBM=GradientBoostingClassifier(learning_rate=0.2, n_estimators=500,max_depth=9,min_samples_split=200, min_samples_leaf=70, random_state=10,max_features=8,subsample=0.8)
cv_score = cross_val_score(the_GBM, X, y,cv=5)
print "CV Score : \nMean - %.7g | Std - %.7g \nMin - %.7g | Max - %.7g" % (np.mean(cv_score),np.std(cv_score),np.min(cv_score),np.max(cv_score))

end_time=datetime.now()
elapsed_time=end_time-start_time
print 'cost time:',
print str(elapsed_time)

#GBM0=GradientBoostingClassifier()
#cv_score = cross_val_score(GBM0, X, y,cv=5)
#print "CV Score : \nMean - %.7g | Std - %.7g \nMin - %.7g | Max - %.7g" % (np.mean(cv_score),np.std(cv_score),np.min(cv_score),np.max(cv_score))


#modelfit(gbm0, train, predictors)
'''
k = 5
n_samples = len(X)
fold_size = n_samples // k
scores = []
masks = []
for fold in range(k):
    print fold,
    print '...'
    # generate a boolean mask for the test set in this fold
    test_mask = np.zeros(n_samples, dtype=bool)
    test_mask[fold * fold_size : (fold + 1) * fold_size] = True
    # store the mask for visualization
    masks.append(test_mask)
    # create training and test sets using this mask
    X_test, y_test = X[test_mask], y[test_mask]
    X_train, y_train = X[~test_mask], y[~test_mask]
    # fit the classifier
    GBM0 = GradientBoostingClassifier(random_state=10)
    GBM0.fit(X_train, y_train)
    # compute the score and record it
    scores.append(GBM0.score(X_test, y_test))
plt.matshow(masks, cmap='gray_r')
print(scores)
print(np.mean(scores))
'''
