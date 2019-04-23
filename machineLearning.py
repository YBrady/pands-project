# --------------------------------------------------------------
# Fischers Iris Dataset
# 
# Written by Yvonne Brady
# GMIT ID: G00376355
# 
# This python program looks after the application of machine 
# learning to the dataset
#---------------------------------------------------------------

# Import the relevant libraries
import pandas
import numpy as np
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# Declaring and setting the dataset as a global variable - saves going back and forth all the time
data = pandas.read_csv("iris_csv.csv") # All Irises
dataVirg = data.loc[data["class"] == "Iris-virginica"] # Just the Iris-virginica
dataVers = data.loc[data["class"] == "Iris-versicolor"]# Just the Iris-versicolor
dataSeto = data.loc[data["class"] == "Iris-setosa"] # Just the Iris-setosa
irisClasses = data["class"].unique() # A list of the Iris Classes

# Get a full listing of columns
listOfColumns = data.columns
listOfNumericalColumns = []

# Populate a list of columns that have numerical data (float64)
# This is a list of the attributes
for column in listOfColumns:
	if (data[column].dtype == np.float64):
		listOfNumericalColumns.append(column)

def main():
    # ----------Splitting the dataset into train and test data ---------------
    # Setting the split parameters:
    # Convert the dataset values into an array
    array = data.values
    # Splitting out the numeric columns from the dataset (now array)
    X = array[:,0:4]
    # The classes
    Y = array[:,4]
    # Setting out the validation / training sizes
    validation_size = 0.20
    # Seed value used by the model random number generator
    seed = 7
    # Performing the split using sklearn functions
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
    # Evaluation metric 
    scoring = "accuracy"


    # ----------Build Algorithm Models -------------------------
    models = []
    # Logistic Regression (LR) Model
    models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
    # Linear Discriminant Analysis (LDA)
    models.append(('LDA', LinearDiscriminantAnalysis()))
    # K-Nearest Neighbors (KNN)
    models.append(('KNN', KNeighborsClassifier()))
    # Classification and  regression Tress (CART)
    models.append(('CART', DecisionTreeClassifier()))
    # Gaussian Naive Bayes (NB)
    models.append(('NB', GaussianNB()))
    # Support Vector Machines (SVM)
    models.append(('SVM', SVC(gamma='auto')))

    # ---------Evaluate Models --------------------------------
    results = []
    names = []
    print("")
    print("-----------------Results from training of 6 no Algorithms---------------")
    print("Model", "     Mean Accuracy", "       Std Dev.")
    for name, model in models:
        # 10-fold cross validation (n_splits = 10)
        kfold = model_selection.KFold(n_splits=10, random_state=seed)
        # Cross validation results
        cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        msg = "%f          %f" % (cv_results.mean(), cv_results.std())
        print(name, ":", " "* (10-len(name)),  msg)
    print("------------------------------------------------------------------------")
    print("")
    print("")
    # ----------- Compare Algorithms ---------------------------
    fig = plt.figure()
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    # Plot all results
    plt.boxplot(results)
    # According to Algorithm
    ax.set_xticklabels(names)
    plt.show()
    
    #--------------Make Predictions on Validation Dataset
    # Just using knn algorithm
    knn = KNeighborsClassifier()
    # Test using the test train X = Values, Y = class
    knn.fit(X_train, Y_train)
    # Record the predictions
    predictions = knn.predict(X_validation)
    # Print the results
    print("Using the Testing Dataset with the KNN Model as Predictor:")
    print("")
    print("The accuracy from the test dataset was scored at", accuracy_score(Y_validation, predictions), "%")
    print("")
    # The confusion matrix
    print("The confusion matrix is as follows:")
    print(confusion_matrix(Y_validation, predictions))
    print("")
    print("Classification Report:")
    print(classification_report(Y_validation, predictions))





# This is used so this code can be run in isolation for testing
if __name__ == "__main__":
	# execute only if run as a script 
	main()
