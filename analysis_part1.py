
# --------------------------------------------------------------
# Fischers Iris Dataset
# 
# Written by Yvonne Brady
# GMIT ID; G00376355
#---------------------------------------------------------------

import pandas
import numpy as np
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

sns.set(color_codes=True)

#%matplotlib inline
#%pylab inline


# Declaring and setting the dataset as a global variable - saves going back and forth all the time
data = pandas.read_csv("iris_csv.csv") # All Irises
dataVirg = data.loc[data['class'] == "Iris-virginica"] # Just the Iris-virginica
dataVers = data.loc[data['class'] == "Iris-versicolor"]# Just the Iris-versicolor
dataSeto = data.loc[data['class'] == "Iris-setosa"] # Just the Iris-setosa
spices = data['class'].unique()


# Main function
def main():
	#Show the options
	display_menu()
	
	while True: # always un this
		choice = input("Enter choice: ")
		print("")		
		if (choice == "1"):
			display_raw_menu()
			display_menu()
		elif (choice == "2"):
			display_plot_menu()
			display_menu()
		elif (choice == "3"):
			predictor()
			display_menu()
		elif (choice == "4"):
			break
		else:
			display_menu()
			
			
			
def display_raw_menu():
	print("Raw Data Menu")
	print("=" * 20)
	print("1 - Iris-Virginica Data")
	print("2 - Iris-Setosa Data")
	print("3 - Iris-Versicolor Data")
	print("4 - All Iris Data")
	print("5 - Statistical Summary (Iris-Virginica)")
	print("6 - Statistical Summary (Iris-Setosa)")
	print("7 - Statistical Summary (Iris-Versicolor)")
	print("8 - Statistical Summary (All Iris Data)")
	print("9 - Return to Main Menu")


	choice = input("Enter choice: ")
	print("")

	if (choice == "1"):
		print(dataVirg)
		display_raw_menu()
	elif (choice == "2"):
		print(dataSeto)
		display_raw_menu()
	elif (choice == "3"):
		print(dataVers)
		display_raw_menu()
	elif (choice =="4"):
		print(data)
		display_raw_menu()
	elif (choice == "5"):
		print(dataVirg.describe())
		display_raw_menu()
	elif (choice == "6"):
		print(dataSeto.describe())
		display_raw_menu()
	elif (choice == "7"):
		print(dataVers.describe())
		display_raw_menu()
	elif (choice == "8"):
		print(data.describe())
		data.groupby('class').size()
		display_raw_menu()
	elif (choice == "9"):
		display_menu()		
	else:
		display_raw_menu()



def display_plot_menu():
	print("Plot Menu")
	print("=" * 20)
	print("1 - Iris-Virginica BoxPlot")
	print("2 - Iris-Setosa BoxPlot")
	print("3 - Iris-Versicolor BoxPlot")
	print("4 - All Iris BoxPlot")
	print("5 - Compare BoxPlot")
	print("6 - Boxplot of 4 measurements")
	print("7 - Histogram of 4 measurements")
	print("8 - Histogram of 4 measurements per iris class")
	print("9 - Boxplot of 4 measurements per iris class")
	print("10 - Violin plot - Petal Length")
	print("11 - Scatterplot")
	print("12 - Colour Scatterplot")
	print("13 - Line and Scatterplot (Colour)")
	print("0 - Return to Main Menu")

	choice = input("Enter plot choice: ")
	print("")

	if (choice == "0"):
		display_menu()
	else:
	    # box and whisker plots
		if (choice == "1"):
			dataVirg.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
		elif (choice == "2"):
			dataSeto.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
		elif (choice == "3"):
			dataVers.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
		elif (choice == "4"):
			data.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
		elif (choice == "5"):
			compare_box()
		elif (choice == "6"):
			#box and whisker plots for different numerical columns
			data.plot(kind='box')
		elif (choice == "7"):
			#HIST PLOT OF ALL NUMERICAL COLUMNS
			data.hist(figsize=(10,5))
		elif (choice == "8"):
			for spice in spices:
				data[data['class']==spice].hist(figsize=(10,5))
		elif (choice == "9"):
			data.boxplot(by='class',figsize=(15,15))
		elif (choice == "10"):
			sns.violinplot(data=data,x='class',y='petallength')
		elif (choice == "11"):
			pandas.plotting.scatter_matrix(data,figsize=(15,10))
		elif (choice == "12"):
			sns.pairplot(data,hue="class")
		elif (choice == "13"):
			sns.pairplot(data,diag_kind='kde',hue='class')
		else:
			display_plot_menu()

		plt.show() # show the plot created
		display_plot_menu() # return to plot menu


def predictor():
    print("Predictor")

def display_menu():
    print("")
    print("Fischers Iris Data Set Analysis Menu")
    print("=" * 37)
    print("1 - Examine Raw Data")
    print("2 - Review Plots")
    print("3 - Iris Species Predictor")
    print("4 - Exit")


def compare_box():
	# COMPARING THE DIFFERENT NUMERICAL COLUMNS IN THE GIVEN DATASET 
	listOfColumns = data.columns
	listOfNumericalColumns = []

	for column in listOfColumns:
		if (data[column].dtype == np.float64):
			listOfNumericalColumns.append(column)

	print('listOfNumericalColumns :',listOfNumericalColumns)
#	spices = data['class'].unique()
	print('spices :',spices)

	fig, axs = plt.subplots(nrows=len(listOfNumericalColumns),ncols=len(spices),figsize=(15,15))

	for i in range(len(listOfNumericalColumns)):
		for j in range(len(spices)):  
			print(listOfNumericalColumns[i]," : ",spices[j])
			axs[i,j].boxplot(data[listOfNumericalColumns[i]][data['class']==spices[j]])
			axs[i,j].set_title(listOfNumericalColumns[i]+""+spices[j])

if __name__ == "__main__":
	# execute only if run as a script 
	main()
