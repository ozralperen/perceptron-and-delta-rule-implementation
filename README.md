# Perceptron and Delta Rule Python Implementation

This project is about implementation of perceptrons and delta rule in python. Goal is to predict letters from a spesific dataset according to their pixel values. 

## About the Data
Full data can't be shared but an example, which has 5 pixels distortion, is shared in bipolar folder.\
Letters have 63 pixel values (7x9). Letters' pixel values are either binary or bipolar and letter files are in the same named directories. If a file is binary, it must have binary in file name. And code uses 4th character to find the right label for the letter. So 4th character from the last must be the file's corresponding letter. Letters are a,b,c,d,e,j,k.

## About the Code
Code is written with Python 3.7.8 in windows. Numpy and OS libraries are used so they must be installed in order to code to run.\
Program prints weight changes, predicted letters and success rates for each epoch if user wants a detailed report. Otherwise just predicted letters and success rates will be printed.
