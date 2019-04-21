
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

sns.set(color_codes=True)


# Declaring and setting the dataset as a global variable - saves going back and forth all the time
data = pandas.read_csv("iris_csv.csv") # All Irises
dataVirg = data.loc[data['class'] == "Iris-virginica"] # Just the Iris-virginica
dataVers = data.loc[data['class'] == "Iris-versicolor"]# Just the Iris-versicolor
dataSeto = data.loc[data['class'] == "Iris-setosa"] # Just the Iris-setosa
spices = data['class'].unique()


			
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
		return		
	else:
		display_raw_menu()


if __name__ == "__main__":
	# execute only if run as a script 
	display_raw_menu()

