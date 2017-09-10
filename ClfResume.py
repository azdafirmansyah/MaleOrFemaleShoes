'''
Created on Sep 10, 2017

@author: Azda Firmansyah
'''
from Data.BasicDataClf import getShoeFeature, getShoeLabel, getShoeFeaturesTest, getShoeLabelTest
from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X = getShoeFeature()
Y = getShoeLabel()
X_test = getShoeFeaturesTest()
Y_test = getShoeLabelTest()

#Adaboost
clf_adaboost = AdaBoostClassifier()
clf_adaboost.fit(X,Y)
clf_predict_adaboost = clf_adaboost.predict(X_test)
print("Predict Adaboost :", clf_predict_adaboost)

#DecTree
clf_tree = tree.DecisionTreeClassifier()
clf_tree.fit(X, Y)
clf_predict_tree = clf_tree.predict(X_test)
print("Predict DTree :", clf_predict_tree) 

#GaussianNB
clf_gaus = GaussianNB()
clf_gaus.fit(X, Y)
clf_predict_gaus = clf_gaus.predict(X_test)
print("Predict Gaussian :", clf_predict_gaus)

#KNeighbors
clf_kneighbors = KNeighborsClassifier()
clf_kneighbors.fit(X,Y)
clf_predict_neighbors = clf_kneighbors.predict(X_test)
print("Predict Neighbors :",clf_predict_neighbors)

#RandomForest
clf_ranfor = RandomForestClassifier()
clf_ranfor.fit(X,Y)
clf_predict_ranfor = clf_ranfor.predict(X_test)
print("Predict Random Forest :",clf_predict_ranfor)

#Accuracy Score for each classifier
acc_adaboost = accuracy_score(Y_test, clf_predict_adaboost)
print("Accuracy Adaboost :",acc_adaboost)

acc_dectree = accuracy_score(Y_test, clf_predict_tree)
print("Accuracy Decision Tree :",acc_dectree)

acc_gauss = accuracy_score(Y_test, clf_predict_gaus)
print("Accuracy Gaussian :",acc_gauss)

acc_neighbors = accuracy_score(Y_test, clf_predict_neighbors)
print("Accuracy Neighbors :",acc_neighbors)

acc_ranfor = accuracy_score(Y_test, clf_predict_ranfor)
print("Accuracy Random Forest :",acc_ranfor)
