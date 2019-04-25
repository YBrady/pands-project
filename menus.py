
# --------------------------------------------------------------
# Fischers Iris Dataset
# 
# Written by Yvonne Brady
# GMIT ID: G00376355
# 
#---------------------------------------------------------------

# Need to import the other python programs that make up the whole solution
import dataInNumbers
import dataInPlots
import machineLearning

# Main function
def main():
	#Show the options
	display_menu()
	
	while True: # always do this
		choice = input("Enter choice: ")
		print("")		
		if (choice == "1"):
			# Calls the dataInNumbers program
			dataInNumbers.display_num_menu()
			display_menu()
		elif (choice == "2"):
			# Calls the dataInPlots program
			dataInPlots.display_plot_menu()
			display_menu()
		elif (choice == "3"):
			# Calls the machineLearning program
			machineLearning.main()
			display_menu()
		elif (choice == "0"):
			# Ends the program with 0
			break
		else:
			# In all other cases just display the menu again
			display_menu()			
			
def display_menu():
	# Just handles the menu messaging
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
