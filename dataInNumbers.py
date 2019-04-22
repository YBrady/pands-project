
# --------------------------------------------------------------
# Fischers Iris Dataset
# 
# Written by Yvonne Brady
# GMIT ID: G00376355
# 
# This python program looks after the data analysis / review 
# of the actual numbers.
#---------------------------------------------------------------

# Import pandas library
import pandas

# Declaring and setting the dataset as a global variable - saves going back and forth all the time
data = pandas.read_csv("iris_csv.csv") # All Irises
dataVirg = data.loc[data['class'] == "Iris-virginica"] # Just the Iris-virginica
dataVers = data.loc[data['class'] == "Iris-versicolor"]# Just the Iris-versicolor
dataSeto = data.loc[data['class'] == "Iris-setosa"] # Just the Iris-setosa


# Displays the Data Menu			
def display_num_menu():
    print("")
    # Creating the menu heading
    print("=" * 20)
    print("Raw Data Menu")
    print("=" * 20)
    print("1 - Display Raw Data ...")
    print("2 - Display Data Shape and Size")
    print("3 - Display Data Info")
    print("4 - Display First x Rows")
    print("5 - Display Last x Rows")
    print("6 - Display Random x Rows")
    print("7 - Display Statistical Summary Data ...")
    print("8 - Display Statistical Data by Iris Class ...")
    print("0 - Return to Main Menu")
    
    # Allow the user a choice of what they want reported
    print("")
    choice = input("Enter choice: ")
    print("")
    
    # If the raw data is selected
    if (choice == "1"):
        # Calls a function where the user is asked which class they want to report on
        iris = pick_iris_class()
        # Prints the data related to Iris-Virginica class
        if (iris == "1"):
            print(dataVirg)
        # Prints the data related to Iris-Setosa class
        elif (iris =="2"):
            print(dataSeto)
        # Prints the data related to Iris-Versicolor class
        elif (iris =="3"):
            print(dataVers)
        # Prints the all iris data
        elif (iris == "4"):
            print(data)
        # Anything else return an error
        else:
            print("Invalid selection")
        # Displays the menu again
        display_num_menu()
        
        # Displays the shape of the data
    elif (choice == "2"):
        print("The dataset has",data.shape[0], "rows each with", data.shape[1], "attributes.")
        print("Altogether there are", data.size, "data values in the dataset.")
        print("The Iris class breakdown is as follows:")
        print(data.groupby('class').size())
        # Returns to the numbers menu
        display_num_menu()

        # Displays the data info
    elif (choice == "3"):
        print("The following is information on the attributes in the dataset:")
        print(data.info())
        # Returns to the numbers menu
        display_num_menu()
    
    elif (choice =="4"):
        num = int(input("How many rows do you wish to return? "))
        print("The following are the first",num,"rows of the dataset:")
        print(data.head(num))
        # Returns to the numbers menu
        display_num_menu()
        
    elif (choice == "5"):
        num = int(input("How many rows do you wish to return? "))
        print("The following are the last",num,"rows of the dataset:")
        print(data.tail(num))
        # Returns to the numbers menu
        display_num_menu()
    elif (choice == "6"):
        num = int(input("How many rows do you wish to return? "))
        print("The following are",num,"random rows of the dataset:")
        print(data.sample(num))
        # Returns to the numbers menu
        display_num_menu()
    elif (choice == "7"):
        iris = pick_iris_class()
        if (iris == "1"):
            print("The following is summary statistical data relating to the Iris-Virginica class of Iris:")
            print(dataVirg.describe())
        elif (iris == "2"):
            print("The following is summary statistical data relating to the Iris-Setosa class of Iris:")
            print(dataSeto.describe())
        elif (iris == "3"):
            print("The following is summary statistical data relating to the Iris-Versicolor class of Iris:")
            print(dataVers.describe())
        elif (iris == "4"):
            print("The following is summary statistical data relating to all classes of Iris:")
            print(data.describe())
        else:
            print("Invalid selection")
        # Returns to the numbers menu
        display_num_menu()
    elif (choice == "8"):
        print("Which of the following do you wish to see :")
        stat = input("1 for Minimum; 2 for Maximum, 3 for Mean, 4 for Standard Deviation : ")
        if (stat == "1"):
            print("The following are the minimum values for each measurement by Iris class:")
            print(data.groupby("class").min())
        elif (stat == "2"):
            print("The following are the maximum values for each measurement by Iris class:")
            print(data.groupby("class").max())
        elif (stat == "3"):
            print("The following are the mean values for each measurement by Iris class:")
            print(data.groupby("class").mean())
        elif (stat == "4"):
            print("The following are the standard deviation values for each measurement by Iris class:")
            print(data.groupby("class").std())
        else:
            print("Invalid input")
        # Returns to the numbers menu
        display_num_menu()
    elif (choice == "0"):
        # Returns to main menu
        return		
    else:
        # Returns to the numbers menu
        display_num_menu()

def pick_iris_class():
    print("Which Iris class do you wish to report on?")
    return input("Press 1 for Iris-virginica, 2 for Iris-Setosa or 3 for Iris-Versicolor or 4 for All Iris Classes: ")

# This part is used for testing only, or if not being called from the menus.py file
if __name__ == "__main__":
    # execute only if run as a script 
    display_num_menu()

