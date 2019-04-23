
# --------------------------------------------------------------
# Fischers Iris Dataset
# 
# Written by Yvonne Brady
# GMIT ID: G00376355
# 
#---------------------------------------------------------------

import pandas
import numpy as np
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib


# Also need to import the other python programs that make up the whole solution
import dataInNumbers
import dataInPlots
import predictor

sns.set(color_codes=True)

# Declaring and setting the dataset as a global variable - saves going back and forth all the time
data = pandas.read_csv("iris_csv.csv") # All Irises
dataVirg = data.loc[data["class"] == "Iris-virginica"] # Just the Iris-virginica
dataVers = data.loc[data["class"] == "Iris-versicolor"]# Just the Iris-versicolor
dataSeto = data.loc[data["class"] == "Iris-setosa"] # Just the Iris-setosa
spices = data["class"].unique()


# Main function
def main():
	#Show the options
	display_menu()
	
	while True: # always un this
		choice = input("Enter choice: ")
		print("")		
		if (choice == "1"):
			dataInNumbers.display_num_menu()
			display_menu()
		elif (choice == "2"):
			dataInPlots.display_plot_menu()
			display_menu()
		elif (choice == "3"):
			machineLearning.main()
			display_menu()
		elif (choice == "0"):
			break
		else:
			display_menu()			
			
def display_menu():
    print("")
    print("Fischers Iris Data Set Analysis Menu")
    print("=" * 37)
    print("1 - Examine Raw Data")
    print("2 - Review Plots")
    print("3 - Iris Species Predictor")
    print("0 - Exit")

if __name__ == "__main__":
	# execute only if run as a script 
	main()
