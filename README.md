
<img align="left" src="/images/GMIT-logo.png" alt="GMIT" width="200"/>                               <img align="right" src="/images/data-analytics.png" alt="HDipDA" width="300"/>  

# Programming &amp; Scripting Fishers Iris Dataset Project Semester 1 2019


___________________________________________

**Module Name**: Programming & Scripting  
**Module Number**: 52445  
**Student Name**: Yvonne Brady  
**Student ID**: G00376355  
___________________________________________

<img align="left" src="/images/iris-varieties.png" alt="Iris Varieties"/>

## 1. The Background ##
In 1936 Robert Fisher published a paper _The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis_ [1] introducing the now famous Iris Data Set. This data set comprises the width and length measurements of the sepals and petals of three different Iris varieties. 50 samples of each variety were collected on the same day, by the same person (Anderson) and measured using the same instruments. 

The resultant dataset comprised of 150 records each containing 5 no attributes - each of the petal and sepal measurements and also the variety of Iris the measurements related to. This dataset is widely used as a reference for Data Analytics amd Machine Learning.

### 1.1 The Project Brief ###
The following project concerns the well-known Fisher’s Iris data set. The project entails you researching the data set, and then writing documentation and code in the Python programming language based on that research.

## 2. Initial Exploration ##
Initial exploration of the dataset consisted of finding out about the data in broad terms. A number python commands helped in getting an overall feel for the data:

### 2.1 Data Familiarisation ###
''' python
data.info
''' 
<img align="left" src="/images/Screen Shots/dataInfo.png" alt="Data Info"/>
The data.info command showed that there are 150 entries in the dataset, each with 5 columns. Of the five columns, ,four are numeric in nature (floating point) reflecting the sepal and petal lenth and width measurements respectively. The fifth column "class" is of data type object. 

'''python
data.head()
'''
<img align="right" src="/images/Screen Shots/dataHead.png" alt="First Five Rows"/>
The data.head() command gives a flavour of the data contained in the dataset, returning the first five rows worth of data. This snippet of the data shows us that these numbers are similar in size for each attribute and all are for the class Iris-setosa.

'''python
data.tail()
'''
<img align="left" src="/images/Screen Shots/dataTail.png" alt="Last Five Rows"/>
The data.tail() command displays the last five rows. Here we see a little more variation in each of the values, but all are still within the same order of magnitude. As with the data.head() command, there is only one class identified in this snippet of the dataset, but this time it is the Iris-virginica. It would appear likely from the last two commands that the dataset is ordered by class, but this is by no means proven.

'''python
data.sample(5)
'''
<img align="left" src="/images/Screen Shots/dataSample.png" alt="Random Five rows"/>
The data.sample(5) command chooses 5 random rows to display. The rows returned in this instance again are of the same order of magnitude for each of the numeric results. Between all the measurements, the greatest relative variation is in the petal width measurements. Unlike the head or tail rows, in the random sample there are three different iris classes returned. We can also see the attribute with the greatest variation appears to be the petal width. Now we must ask ourselves - how many classes are in this dataset?

'''python 
data["class"].value_counts()
'''
<img align="left" src="/images/Screen Shots/classes.png" alt="Random Five rows"/>
The value_counts() returns the count of all the various instances of the class attribute. This can be used to determine the number of distinct classes and the frequency by which they occur. The resultant data shows that there are three distinct classes, namely:
* Iris virginica
* Iris-setosa
* Iris-versicolor
All three iris varieties appear in the dataset with the same frequency - 50 readings each.

Now we know a little bit abou the data in the dataset, ets look at some broad statistics.

''' python
data.describe()
'''
<img align="left" src="/images/Screen Shots/describe.png" alt="Overall Stats"/>
The data.describe() function returns the overall statistics for each numeric attribute. It is evident from the results to date that there are 150 rows with every attribute filled as in there are no null values. This also corresponds to the earlier finding of 3 x iris classes each of 50 readings.

## 3. Plotting of the Data ##

### 3.1 Boxplots ###
<img align="right" src="images/box-plot-explained.gif">
A boxplot or box and whisker plot is a graphical representation of data whereby a rectangle is drawn around the middle two quartiles of the data. The median, the point at which 50% of values are higher and 50% of values are lower, is represented in the rectangle or box. The whiskers extend out of the box to represent the maximum and minimum values of the data with the exclusion of outliers. For this purpose the outlier is defined as any value outside 3/2 times the upper / lower quartile. Essentially, it gives a good overview of the data's distribution. [2]


### 3.2 Histograms ###


### 3.3 Violin Plots ###

### 3.4 Scattergrams ###


## 4. The Python Program ##

### 2.1 Importing the Dataset ###
The dataset was downloaded from  ..... To import


### 4.x Modules Imported ###
A number of modules were required to perform this analysis, namely:
* pandas - 
 - scatter_matrix
* numpy 
* matplotlib
 - pyplot
* seaborn


## References ##
[1] Fisher,R.A. "The use of multiple measurements in taxonomic problems" Annual Eugenics, 7, Part II, 179-188 (1936);
[2] https://flowingdata.com/2008/02/15/how-to-read-and-use-a-box-and-whisker-plot




[y] https://chartio.com/learn/data-analytics/what-is-exploratory-data-analysis/  
[z] https://www.geeksforgeeks.org/python-pandas-dataframe/
