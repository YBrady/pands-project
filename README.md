
<img align="left" src="/images/GMIT-logo.png" alt="GMIT" width="200"/>                               <img align="right" src="/images/data-analytics.png" alt="HDipDA" width="300"/>  

# Programming &amp; Scripting Fishers Iris Dataset Project Semester 1 2019


___________________________________________

**Module Name**: Programming & Scripting  
**Module Number**: 52445  
**Student Name**: Yvonne Brady  
**Student ID**: G00376355  
___________________________________________


## 1. The Background ##
In 1936 Robert Fisher published a paper _The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis_ [1] introducing the now famous Iris Data Set. This data set comprises the width and length measurements of the sepals and petals of three different Iris varieties. 50 samples of each variety were collected on the same day, by the same person (Edgar Anderson) and measured using the same instruments. As it was Anderson who actually collected the flowers from the Gaspé Penninsula in Canada, this dataset is sometimes called the Anderson Data Set.

The dataset comprises of 150 records each containing 5 no attributes - each of the petal and sepal measurements and also the variety of Iris the measurements related to. This dataset is widely used as a reference for Data Analytics amd Machine Learning see the references section below for a small subset of the analysis performed on this dataset. As part of this project I have reviewed each of the references listed.

<img align="left" src="/images/iris-varieties.png" alt="Iris Varieties"/>

### 1.1 The Project Brief ###
The following project concerns the well-known Fisher’s Iris data set. The project entails you researching the data set, and then writing documentation and code in the Python programming language based on that research.

## 2. Initial Exploration ##
Initial exploration of the dataset consisted of finding out about the data in broad terms. A number python commands helped in getting an overall feel for the data:

### 2.1 Data Familiarisation ###
Firstly, to get an idea of the size and shape of the dataset the following command can be run:

```python
data.shape
``` 
<img align="right" src="/images/Screen Shots/dataShape.png" alt="Data Shape"/>

As can be seen from the results of this command, the dataset comprises 150 rows each with five attributes.

```python
data.info()
``` 
<img align="left" src="/images/Screen Shots/dataInfo.png" alt="Data Info"/>
The data.info command showed that there are 150 entries in the dataset, each with 5 columns. Of the five columns, four are numeric in nature (floating point) reflecting the sepal and petal lenth and width measurements respectively. The fifth column "class" is of data type object. 

```python
data.head()
```
<img align="right" src="/images/Screen Shots/dataHead.png" alt="First Five Rows"/>
The data.head() command gives a flavour of the data contained in the dataset, returning the first five rows worth of data. This snippet of the data shows us that these numbers are similar in size for each attribute and all are for the class Iris-setosa.

```python
data.tail()
```
<img align="left" src="/images/Screen Shots/dataTail.png" alt="Last Five Rows"/>
The data.tail() command displays the last five rows. Here we see a little more variation in each of the values, but all are still within the same order of magnitude. As with the data.head() command, there is only one class identified in this snippet of the dataset, but this time it is the Iris-virginica. It would appear likely from the last two commands that the dataset is ordered by class, but this is by no means proven.

```python
data.sample(5)
```
<img align="left" src="/images/Screen Shots/dataSample.png" alt="Random Five rows"/>
The data.sample(5) command chooses 5 random rows to display. The rows returned in this instance again are of the same order of magnitude for each of the numeric results. Between all the measurements, the greatest relative variation is in the petal width measurements. Unlike the head or tail rows, in the random sample there are three different iris classes returned. We can also see the attribute with the greatest variation appears to be the petal width. Now we must ask ourselves - how many classes are in this dataset?

```python 
data["class"].value_counts()
```
<img align="left" src="/images/Screen Shots/classes.png" alt="Random Five rows"/>
The value_counts() returns the count of all the various instances of the class attribute. This can be used to determine the number of distinct classes and the frequency by which they occur. The resultant data shows that there are three distinct classes, namely:
* Iris virginica
* Iris-setosa
* Iris-versicolor
All three iris varieties appear in the dataset with the same frequency - 50 readings each.

### 2.2 Initial Statistical Analysis ###
Now we know a little bit abou the data in the dataset, ets look at some broad statistics.

'''python
data.describe()
'''
<img align="left" src="/images/Screen Shots/describe.png" alt="Overall Stats"/>
The data.describe() function returns the overall statistics for each numeric attribute. It is evident from the results to date that there are 150 rows with every attribute filled, as in there are no null values. This also corresponds to the earlier finding of 3 x iris classes each of 50 readings. A further check could be done using the following command which returns False, meaning there are no null values.

```python
data.isnull().values.any()
```

The general description however provides information on all iris classes together. From our head, tail and random measurements above, it would appear that there are differences between the iris classes and it would be more benficial to get this information per iris class.

```python
data.groupby("class").describe()
```

<img src="/images/Screen Shots/describeClass.png" alt="Class by Class Stats"/>
While the above command would appear to be what is required, the resultant data comprosies 32 columns and is therefore of limited value as it is hard / impossible to read in its entirety. Given these contraints it is better to break the data down to more manageable parts. 

We can do this in a number of ways, two of which are described below.
* Using the describe method for each class of iris where xxx is the class in question

``` python
data.loc[data['class'] == "Iris-xxxx"].describe()
```
<img align="right" src="/images/Screen Shots/class1Describe.png" alt="Describe one class"/>

* Grouping the classes together and looking at the max, min, mean, std in isolation for each attribute
``` python
 data.groupby("class").mean() # substitute min / max / std for minimum, maximum and standard deviation values respectively
```
<img align="right" src="/images/Screen Shots/classMean.png" alt="Mean values per class"/>

Given the likely requirement of the analysis is to discern the difference between the classes of iris, the methods that compare across the classes _i.e._ the second one above, would appear to be the most useful in this case. In fact looking at the results shown for the mean, and also borne out for the min, max and standard deviation (not shown), it would appear the Iris-setosa petal measurements do indeed hold a lot of promise as measurements to differentiate it from the other classes of iris.

They say that a picture tells a thousand words, so having looked at the numeric data, it is now time to look at the graphical representation of this data.


## 3. Plotting of the Data ##

### 3.1 Boxplots ###
<img align="right" src="images/box-plot-explained.gif">
A boxplot or box and whisker plot is a graphical representation of data whereby a rectangle is drawn around the middle two quartiles of the data. The median, the point at which 50% of values are higher and 50% of values are lower, is represented in the rectangle or box. The whiskers extend out of the box to represent the maximum and minimum values of the data with the exclusion of outliers. For this purpose the outlier is defined as any value outside 3/2 times the upper / lower quartile. Essentially, it gives a good overview of the data's distribution. [2]


### 3.2 Violin Plots ###

### 3.3 Histograms ###

### 3.4 Scattergrams ###

## 4. Applying Machine Learning ##

## 5. The Python Program ##
The overall project solution is divided into four separate programs. 
* **menus.py** - which is the starting point for the solution
* **dataInNumbers.py** - which serves to analyse / display the data in numerical format
* **dataInPlots.py** - which serves to display the data through lot visualisations
* **machineLearning.py** - which serves to apply some machine learning to the dataset to work as an Iris class predictor

The solution was broken down in this manner to facilitate troubleshooting and to make the application easier to adapt to other datasets in the future. Full exception handling is not done in the solution as it is designed for use with a knowledgeable user / the creator.

### 5.1 Modules Imported ###
A number of modules were required to perform this analysis, namely:
* pandas - 
 - scatter_matrix
* numpy 
* matplotlib
 - pyplot
* seaborn


### 5.2 menus.py ###
The menus program is a simple program but serves as a conduit and controller of the overall solution. This is the program that is required to be run initially and acts as an interface to all other functions. 

The menus program itself is split into two separate functions. 
* main()
* display_menu()
The main function is called when the program is first run. This calls the display menu which asks the user which option they would like to choose. The menus program is in effect the user interface.

When run initially the user is prompted to select one of the following options:
<img src="images//Screen Shots/initialMenu.png">

Depending on the user selection, a separate program is launched as evidenced by the table below. In the event of a any other key being pressed, the main menu is once more displayed. This functionality is controlled by the main function in the menu program.

| Selection                  | Program Launched                 |
|----------------------------|----------------------------------|
| 1 - Examine Raw Data       | dataInNumbers.display_num_menu() |
| 2 - Review Plots           | dataInPlots.display_plot_menu()  |
| 3 - Iris Species Predictor | machineLearning.main()           |
| 0 - Exit                   | Exits the Program                |


### 5.3 dataInNumbers.py ###


| Selection                                      | Program Launched                                                                                                |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| 1 - Display Raw Data ...                       | pick_iris_class() and then shows data depending on the selection there.                                         |
| 2 - Display Data Shape and Size                | Displays shape, size and class size information                                                                 |
| 3 - Display Data Info                          | Displays data information                                                                                       |
| 4 - Display First x Rows                       | Displays the first user specified number of rows                                                                |
| 5 - Display Last x Rows                        | Displays the last user specified number of rows                                                                 |
| 6 - Display Random x Rows                      | Displays a random user specified number of rows                                                                 |
| 7 - Display Statistical Summary Data ...       | pick_iris_class() and then shows data depending on the selection there.                                         |
| 8 - Display Statistical Data by Iris Class ... | Displays either the minimune, maximum, mean or standard deviation values by class according to user preference. |
| 0 - Return to Main Menu                        | Returns to the main menu (menu.py)                                                                              |

### 5.4 dataInPlots ###

### 5.5 machineLearning.py ###
The machine learning python program could be broken out into a number of distinct sections:
* Splitting the dataset into training and validation parts
* Applying six different algorithms to the training dataset to see which performed best
* Plotting the results of the evaluation of the six algorithms
* Using the validation dataset to test one algorithm
* Displaying the results of the testing.


### 2.1 Importing the Dataset ###
The dataset was downloaded from  ..... To import



## 6. References ##
[1] Fisher,R.A. "The use of multiple measurements in taxonomic problems" Annual Eugenics, 7, Part II, 179-188 (1936);
[2] https://flowingdata.com/2008/02/15/how-to-read-and-use-a-box-and-whisker-plot




[y] https://chartio.com/learn/data-analytics/what-is-exploratory-data-analysis/  
[z] https://www.geeksforgeeks.org/python-pandas-dataframe/

[] https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python
[] https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
[] https://github.com/RitRa/Project2018-iris

[] https://seaborn.pydata.org/generated/seaborn.pairplot.html


[] https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
[] https://diwashrestha.com/2017/09/18/machine-learning-on-iris/
[] https://realpython.com/python-histograms/

[] https://stackoverflow.com/questions/10824156/matplotlib-legend-location-numbers
[] https://seaborn.pydata.org/generated/seaborn.pairplot.html
[] https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
[] https://machinelearningmastery.com/index-slice-reshape-numpy-arrays-machine-learning-python/
[] https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

