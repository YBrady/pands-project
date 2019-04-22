# --------------------------------------------------------------
# Fischers Iris Dataset
# 
# Written by Yvonne Brady
# GMIT ID: G00376355
# 
# This python program looks after the visualisation of the data  
# from the dataset.
#---------------------------------------------------------------

# Import the relevant libraries
import pandas
import numpy as np
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

sns.set(color_codes=True)


# Declaring and setting the dataset as a global variable - saves going back and forth all the time
data = pandas.read_csv("iris_csv.csv") # All Irises
dataVirg = data.loc[data['class'] == "Iris-virginica"] # Just the Iris-virginica
dataVers = data.loc[data['class'] == "Iris-versicolor"]# Just the Iris-versicolor
dataSeto = data.loc[data['class'] == "Iris-setosa"] # Just the Iris-setosa
irisClasses = data['class'].unique() # A list of the Iris Classes

# Displays a menu from which the user can select what plots to view
def display_plot_menu():
    print("=" * 20)
    print("Plot Menu")
    print("=" * 20)
    print("1 - BoxPlots ...")
    print("2 - Violin Plots ...")
    print("6 - Boxplot of 4 measurements")
    print("7 - Histogram of 4 measurements")
    print("8 - Histogram of 4 measurements per iris class")
    print("10 - Violin plot - Petal Length")
    print("11 - Scatterplot")
    print("12 - Colour Scatterplot")
    print("13 - Line and Scatterplot (Colour)")
    print("0 - Return to Main Menu")
    
    print("")
    choice = input("Enter plot choice: ")
    print("")
    
    if (choice == "0"):
        # Returns to main menu if called from menus program. Ends if run as a standalone program
        return
    else:
        if (choice == "1"):
            # Box and whisker plots
            box_menu()
        elif (choice == "2"):
            # Violin plots
            violin_menu()
        elif (choice == "7"):
            # Histogram of the four measurements using all data
            data.hist(figsize=(10,5))
            plt.suptitle("All Iris Classes")
        elif (choice == "8"):
            # 3 Histograms of the four measurements per Iris class
            for irisClass in irisClasses:
                data[data['class']==irisClass].hist(figsize=(10,5))
                plt.suptitle(irisClass)
        elif (choice == "9"):
            # Boxplot of four measurements grouped by Iris class
            data.boxplot(by='class',figsize=(15,15))
        elif (choice == "10"):
            # Violin plot of petal length per class
            sns.violinplot(data=data,x='class',y='petal length (cm)')
        elif (choice == "11"):
            # Scatter matrix using pandas
            pandas.plotting.scatter_matrix(data,figsize=(15,10))
        elif (choice == "12"):
            # Plot of pairwise relationships of dataset with Histograms on diagonal
            sns.pairplot(data,hue="class")
        elif (choice == "13"):
            # Plot of pairwise realationships of dataset with kde (kernel density estimate) on diagonal
            sns.pairplot(data, diag_kind='kde',hue='class')
        else:
            # Any other value re-display the menu
            display_plot_menu()
        
        plt.show() # show the plot created
        display_plot_menu() # return to plot menu

def box_menu():
    print("=" * 20)
    print("Boxplot Menu")
    print("=" * 20)
    print("1 - Iris-Virginica")
    print("2 - Iris-Setosa")
    print("3 - Iris-Versicolor")
    print("4 - All Iris Data")
    print("5 - All plots")
    print("6 - All plots on Single Graph")
    print("7 - Compare All Classes")
    print("")
    choice = input("Please select which item(s) you want to plot : ")
    print("")
    if choice == "1":
        # Boxplot of Iris-Virginica data
        dataVirg.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
        plt.suptitle("Iris Virginica")
    elif choice == "2":
        # Boxplot of Iris-Setosa data
        dataSeto.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
        plt.suptitle("Iris Setosa")
    elif choice == "3":
        # Boxplot of Iris-Versicolor data
        dataVers.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
        plt.suptitle("Iris Versicolor")
    elif choice == "4":
        # Boxplot of All data
        data.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
        plt.suptitle("All Irises")
    elif choice == "5":
        # Boxplot of all data on multiple graphs
        compare("b")
        plt.suptitle("Values for each Iris Class")
    elif choice == "6":        
        # Boxplots for different numerical columns on single plot
        data.plot(kind='box')
    elif (choice == "7"):
        # Boxplot of four measurements grouped by Iris class
        data.boxplot(by='class',figsize=(15,15))
    else:
        print("Invalid choice - showing all data")
    plt.show

def compare(plotType):
	# Get a full listing of columns
	listOfColumns = data.columns
	listOfNumericalColumns = []

    # Populate a list of columns that have numerical data (float64)
	for column in listOfColumns:
		if (data[column].dtype == np.float64):
			listOfNumericalColumns.append(column)
    
	if plotType =="b":
		# Using matplotlib to create a number of subplots - No of columns with Numbers x No of Iris Classes
		fig, axs = plt.subplots(nrows=len(listOfNumericalColumns),ncols=len(irisClasses),figsize=(15,15), sharex="col")
	elif plotType =="v":
		# Using matplotlib to create a number of subplots - No of columns with Numbers x No of Iris Classes
		fig, axs = plt.subplots(nrows=len(listOfNumericalColumns),figsize=(15,15))

	# Iterates through each numerical column (sepal amd petal lengths and widths)
	for i in range(len(listOfNumericalColumns)):
        
		# Iterates through each Iris Class
		for j in range(len(irisClasses)):  
			if plotType == "b":
				# Create a boxplot of the numerical column for the relavant Iris Class
				axs[i,j].boxplot(data[listOfNumericalColumns[i]][data['class']==irisClasses[j]])
				# Title the plot appropriately
				axs[i,j].set_title(irisClasses[j])
				axs[i,j].set_ylabel(listOfNumericalColumns[i])
			elif plotType =="v":
				# Create a violin of the numerical column for the relevant Iris Class
				axs[i].violinplot(data = data, x = "class", y = [listOfNumericalColumns[i]])
				axs[i].set_ylabel(listOfNumericalColumns[i])

def violin_menu():
    print("=" * 20)
    print("Violin Plot Menu")
    print("=" * 20)
    print("1 - Sepal Length")
    print("2 - Sepal Width")
    print("3 - Petal Length")
    print("4 - Petal Width")

    print("5 - All plots")
    print("6 - All plots on Single Graph")
    print("7 - Compare All Classes")
    print("")
    choice = input("Please select which item(s) you want to plot : ")
    print("")
    if choice == "1":
        # Violin plot of sepal length per class
        sns.violinplot(data=data,x='class',y='sepal length (cm)')
    elif choice == "2":
        # Violin plot of sepal width per class
        sns.violinplot(data=data,x='class',y='sepal width (cm)')
    elif choice == "3":
        # Violin plot of petal length per class
        sns.violinplot(data=data,x='class',y='petal length (cm)')
    elif choice == "4":
        # Violin plot of petal width per class
        sns.violinplot(data=data,x='class',y='petal width (cm)')
    elif choice == "5":
        # All violin plots
        compare("v")
    elif choice == "6":
        #All violin plots on single graph
        print("")
    elif choice == "7":
        #Compare all classes
        print("")
    else:
        print("invalid choice - plotting all violin plots instead")
        # Add default plot

# This is used so this code can be run in isolation for testing
if __name__ == "__main__":
	# execute only if run as a script 
	display_plot_menu()
