import pandas
import numpy
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
# 
# Fischers Iris Dataset
# 

# Declaring and setting the dataset as a global variable - saves going back and forth all the time
data = pandas.read_csv("iris_csv.csv") # All Irises
dataVirg = data.loc[data['class'] == "Iris-virginica"] # Just the Iris-virginica
dataVers = data.loc[data['class'] == "Iris-versicolor"]# Just the Iris-versicolor
dataSeto = data.loc[data['class'] == "Iris-setosa"] # Just the Iris-setosa


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
	print("5 - Return to Main Menu")

	choice = input("Enter plot choice: ")
	print("")

	if (choice == "5"):
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






if __name__ == "__main__":
	# execute only if run as a script 
	main()
