'''
Created on Sep 10, 2017

@author: Azda Firmansyah
'''
def getShoeFeature():
    X = [
     [181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],[177, 70, 40], [159, 55, 37], [171, 75, 42], 
     [181, 85, 43]
    ]
    return X

def getShoeLabel():
    Y = [
     'male', 'male', 'female', 'female', 'male', 'male', 
     'female', 'female','female', 'male', 'male']
    return Y

def getShoeFeaturesTest():
    X_test=[
        [188, 70, 38],[189, 94, 34],[180, 70, 42],[159, 61, 37],[165, 58, 39],
        [162, 54, 34],[171, 60, 40],[170, 70, 40],[143, 45, 37],[153, 48, 39] 
        ]
    return X_test

def getShoeLabelTest():
    Y_test=['male','male','male','female','male',
            'female','male','male','female','female']
    return Y_test
