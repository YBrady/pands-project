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
dataVirg = data.loc[data["class"] == "Iris-virginica"] # Just the Iris-virginica
dataVers = data.loc[data["class"] == "Iris-versicolor"]# Just the Iris-versicolor
dataSeto = data.loc[data["class"] == "Iris-setosa"] # Just the Iris-setosa
irisClasses = data["class"].unique() # A list of the Iris Classes

# Get a full listing of columns
# This is a list of the attributes
listOfColumns = data.columns
listOfNumericalColumns = []

# Populate a list of columns that have numerical data (float64)
for column in listOfColumns:
	if (data[column].dtype == np.float64):
		listOfNumericalColumns.append(column)


# Displays a menu from which the user can select what plots to view
def display_plot_menu():
    print("=" * 20)
    print("Plot Menu")
    print("=" * 20)
    print("1 - BoxPlots ...")
    print("2 - Violin Plots ...")
    print("3 - Histograms ...")
    print("4 - Scattergrams ...")
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
        elif (choice == "3"):
            # Histograms
            hist_menu()
        elif (choice == "4"):
            # Scattergrams / Pairplots
            scat_menu()
        else:
            # Any other value print error message and re-display the menu
            print("*** Invalid Selection ***")
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
        dataVirg.plot(kind="box", subplots=True, layout=(2,2), sharex=False, sharey=False)
        plt.suptitle("Iris Virginica")
    elif choice == "2":
        # Boxplot of Iris-Setosa data
        dataSeto.plot(kind="box", subplots=True, layout=(2,2), sharex=False, sharey=False)
        plt.suptitle("Iris Setosa")
    elif choice == "3":
        # Boxplot of Iris-Versicolor data
        dataVers.plot(kind="box", subplots=True, layout=(2,2), sharex=False, sharey=False)
        plt.suptitle("Iris Versicolor")
    elif choice == "4":
        # Boxplot of All data
        data.plot(kind="box", subplots=True, layout=(2,2), sharex=False, sharey=False)
        plt.suptitle("All Irises")
    elif choice == "5":
        # Boxplot of all data on multiple graphs
        compare("b")
        plt.suptitle("Values for each Iris Class")
    elif choice == "6":        
        # Boxplots for different numerical columns on single plot
        data.plot(kind="box")
    elif (choice == "7"):
        # Boxplot of four measurements grouped by Iris class
        data.boxplot(by="class",figsize=(15,15))
    else:
        print("*** Invalid choice ***")

def compare(plotType):  
	# Using matplotlib to create a number of subplots - No of columns with Numbers x No of Iris Classes
	fig, axs = plt.subplots(nrows=len(listOfNumericalColumns),ncols=len(irisClasses),figsize=(15,15), sharex="col")

	# Iterates through each numerical column (sepal amd petal lengths and widths)
	for i in range(len(listOfNumericalColumns)):
        
		# Iterates through each Iris Class
		for j in range(len(irisClasses)):  
			if plotType == "b":
				# Create a boxplot of the numerical column for the relevant Iris Class
				axs[i,j].boxplot(data[listOfNumericalColumns[i]][data["class"]==irisClasses[j]])
			elif plotType =="h":
				# Create a boxplot of the numerical column for the relevant Iris Class
				axs[i,j].hist(data[listOfNumericalColumns[i]][data["class"]==irisClasses[j]])
			# Title the plot appropriately
			axs[i,j].set_title(irisClasses[j])
			axs[i,j].set_ylabel(listOfNumericalColumns[i])

def violin_menu():
    print("=" * 20)
    print("Violin Plot Menu")
    print("=" * 20)
    print("1 - Sepal Length")
    print("2 - Sepal Width")
    print("3 - Petal Length")
    print("4 - Petal Width")
    print("5 - All plots on a Single Graph")
    print("")
    choice = input("Please select which item(s) you want to plot : ")
    print("")
    if choice == "1":
        # Violin plot of sepal length per class
        sns.violinplot(data=data,x="class",y="sepal length (cm)")
    elif choice == "2":
        # Violin plot of sepal width per class
        sns.violinplot(data=data,x="class",y="sepal width (cm)")
    elif choice == "3":
        # Violin plot of petal length per class
        sns.violinplot(data=data,x="class",y="petal length (cm)")
    elif choice == "4":
        # Violin plot of petal width per class
        sns.violinplot(data=data,x="class",y="petal width (cm)")
    elif choice == "5":
        # All violin plots
	    # Using matplotlib to create a number of subplots - No of columns with Numbers x No of Iris Classes
        fig, axs = plt.subplots(nrows=2, ncols = 2, figsize=(10,5))

        # Populate the subplots with the appropriate graphs
        sns.violinplot(data=data, x="class", y = "sepal length (cm)", ax = axs[0,0])
        sns.violinplot(data=data, x="class", y = "sepal width (cm)", ax = axs[0,1])
        sns.violinplot(data=data, x="class", y = "petal length (cm)", ax = axs[1,0])
        sns.violinplot(data=data, x="class", y = "petal width (cm)", ax = axs[1,1])
        #fig.tight_layout()
        plt.suptitle("Violin Plots of All Measurements")
    else:
        print("*** Invalid choice ***")

def hist_menu():
    print("=" * 20)
    print("Histogram Menu")
    print("=" * 20)
    print("1 - Iris-Virginica")
    print("2 - Iris-Setosa")
    print("3 - Iris-Versicolor")
    print("4 - All Iris Data")
    print("5 - All plots")
    print("6 - Compare All Classes")
    print("")
    choice = input("Please select which item(s) you want to plot : ")
    print("")
    if choice == "1":
        # Histogram of Iris-Virginica data
        dataVirg.hist(figsize=(10,5))
        plt.suptitle("Iris Virginica")
    elif choice == "2":
        # Histogram of Iris-Setosa data
        dataSeto.hist(figsize=(10,5))
        plt.suptitle("Iris Setosa")
    elif choice == "3":
        # Histogram of Iris-Versicolor data
        dataVers.hist(figsize=(10,5))
        plt.suptitle("Iris Versicolor")
    elif choice == "4":
        # Histogram of All data
        data.hist(figsize=(10,5))
        plt.suptitle("All Irises")
    elif choice == "5":
        # Histogram of all data on multiple graphs
        compare("h")
        plt.suptitle("Values for each Iris Class")
    elif (choice == "6"):
        # Four subplots, one for each attribute, grouped by Iris class
        fig, axes = plt.subplots(nrows= 2, ncols=2, figsize=(10,10))
        data.groupby("class").hist(column = listOfNumericalColumns[0], ax = axes[0,0])
        data.groupby("class").hist(column = listOfNumericalColumns[1], ax = axes[0,1])
        data.groupby("class").hist(column = listOfNumericalColumns[2], ax = axes[1,0])
        data.groupby("class").hist(column = listOfNumericalColumns[3], ax = axes[1,1])
        # Add a legend, located at the upper right hand corner, in one column
        fig.legend(irisClasses, loc = 1, ncol = 1)
        # Add a title
        plt.suptitle("Histogram of all Iris Classes")

    else:
        print("*** Invalid choice ***")

def scat_menu():
    print("=" * 20)
    print("Scatter Matrix Menu")
    print("=" * 20)
    print("1 - Scatterplot from Pandas")
    print("2 - Pairplot from Seaborn with Histograms")
    print("3 - Pairplot from Seaborn with KDE Plotting")
    print("0 - Return to Main Menu")
    
    print("")
    choice = input("Enter plot choice: ")
    print("")
    
    if (choice == "0"):
        # Returns to main menu if called from menus program. Ends if run as a standalone program
        return
    else:
        if (choice == "1"):
            # Scatter matrix using pandas
            pandas.plotting.scatter_matrix(data,figsize=(15,10))
            plt.suptitle("Pandas Scatter Matrix")
        elif (choice == "2"):
            # Plot of pairwise relationships of dataset with Histograms on diagonal
            sns.pairplot(data, diag_kind = "hist",  hue="class")
            plt.suptitle("Seaborn Pair Plot with Histogram Plotting")
        elif (choice == "3"):
            # Plot of pairwise realationships of dataset with kde (kernel density estimate) on diagonal
            sns.pairplot(data, diag_kind="kde", hue="class")
            plt.suptitle("Seaborn Pair Plot with KDE Plotting")
        else:
            # Any other value print error message and re-display the menu
            print("*** Invalid Selection ***")

# This is used so this code can be run in isolation for testing
if __name__ == "__main__":
	# execute only if run as a script 
	display_plot_menu()
