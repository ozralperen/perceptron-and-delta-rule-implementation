import os
import numpy as np

letters = ['A', 'B', 'C', 'D', 'E', 'J', 'K']
weight_changes = [] #array that will keep weight changes to show difference between epochs

def activation(pixels, weights, bias, bipolar): #activation function
        active = 0
        for pixel, weight in zip(pixels, weights): #each input pixel is multiplied by their corresponding weights in the network and sum of the results are kept
            active += (pixel*weight)
        active += bias #bias is added
        if active > 1: #if activation is positive, returns 1 as node is activated
            return 1
        elif (bipolar == 1 and active < 0): #if input is bipolar, then returns -1 as node is not activated
            return -1
        else: #otherwise returns 0 as node is not activated
            return 0

def predict(inp, weights, bias,bipolar): #for a given input, finds all possible letters that input can be
    predictions = []
    for i in range(7): #for each output node, feeds the input and finds which nodes are activated
        if (activation(inp, weights[i], bias, bipolar) == 1): #if given input activates current node
            predictions.append(i) #current node's label is saved in 'predictions' array
    return predictions #prediction array returns

def predict_letters(predictions): #the function used for finding which letters correspond to given node labels
        predicted_letters = []
        for prediction in predictions:
                predicted_letters.append(letters[prediction])
        return predicted_letters

def calculate_accuracy(inps, labels, weights, bias, bipolar): #calculates how accurate the system is
    right_guesses = 0 #keeps how many right guesses are made
    total_guesses = 0 #keeps how many guesses are made in total
    for inp, label in zip(inps, labels): #for each input and label
        prediction = predict(inp, weights, bias, bipolar) #keeps the predictions made by this input
        if (len(prediction) ==1 and prediction[0]==label): #if there is only one prediction and it matches the label of input
            right_guesses+=1 # increments number of right guess by one
        total_guesses+=1 #increments number of guess by one
    success_rate = right_guesses/total_guesses #the ratio of the number of correct guesses to the total number of guesses
    return success_rate #ratio is returned


def report(weights, success_rates, detail, inps, bias, bipolar): #for each epoch prints detailed information or just success rate depending on 'detail' value
        print("Weights")
        print_line = ""
        for i in range(len(weights)): #prints titles to print rest of the information as a table
                print_line += " " + str(i) + ". epoch |"
        print(print_line)
        if(detail): #used for printing weight changes for each epoch if detailed information is requested
                for i in range(7):
                        print("\n" + letters[i] + "\n----------------------------------------") 
                        for j in range(63):
                                progress = ""
                                for k in range(len(weights)):
                                        progress += "{:.4f}".format(weights[k][i][j]) + "\t"
                                print(progress)           
        print_line = ""
        print("\n" + "Success Rates:")
        for success_rate in success_rates: #for each epoch prints success rates
                print_line += "{:.4f}".format(success_rate) + "\t"
        print(print_line)
                        
        

def perceptron(bias, epoch, lr, pixels, labels, delta, bipolar, detail): #function used for operations of perceptron
    weights = np.zeros((7,63), dtype = np.float) #weights
    success_rates = []
    if (delta == 1): #if delta rule is used
        for epc in range(epoch): #for each epoch
            for i in range(len(pixels)): #for each file
                for j in range(7): #for each output node
                    activeness = activation(pixels[i], weights[j], bias, bipolar) #activeness is calculated using activation function
                    if(i%7 == j): #if current value and value of the current output node is the same, activeness is expected to be 1
                        expected_val = 1
                    else: #otherwise 0
                        expected_val = 0
                    for k in range(63): # for each connection weights are being updated
                        weights[j][k] += lr * (expected_val - activeness) *  pixels[i][k]
            print("Predictions in epoch " + str(epc) + " --------------") #for each input in each epoch, prints correct letter and letter(s) that system predicts
            for inp, label in zip(pixels, labels):
                    print_line = ""
                    print_line += "\nExpected predictions = " + letters[label] + "\n"
                    predictions=predict_letters(predict(inp, weights, bias, bipolar))
                    print_line += "Predictions = "
                    for prediction in predictions:
                            print_line += prediction + ", "
                    print(print_line)
            
            weight_changes.append(weights.copy()) #weights are saved to this array to be printed later on
            success_rates.append(calculate_accuracy(pixels, labels, weights, bias, bipolar)) # success rate is saved to this array to be printed later on
    else: #if delta rule is not going to be used, same processes are applied, but weight update formula is changed        for _ in range(epoch):
            for epc in range(epoch):
                    for i in range(len(pixels)):
                        for j in range(7):
                            activeness = activation(pixels[i], weights[j], bias, bipolar)
                            if(i%7 == j):
                                expected_val = 1
                            else:
                                expected_val = 0
                            for k in range(63):
                                weights[j][k] += lr * expected_val *  pixels[i][k] #rather than using (expected_value - activeness), only excepted_value is used for each update step
                    print("Predictions in epoch " + str(epc) + " --------------") #for each input in each epoch, prints correct letter and letter(s) that system predicts
                    for inp, label in zip(harf_pikselleri, labels):
                            print_line = ""
                            print_line += "\nExpected predictions = " + harfler[label] + "\n"
                            predictions=predict_letters(predict(inp, weights, bias, bipolar))
                            print_line += "Predictions = "
                            for prediction in predictions:
                                    print_line += prediction + ", "
                            print(print_line)
                    weight_changes.append(weights.copy())
                    success_rates.append(calculate_accuracy(pixels, labels, weights, bias, bipolar))
    
    report(weight_changes, success_rates, detail, pixels, bias, bipolar) #printing a report

def textToNum(text): #returns which number the given letter is
    for i in range(len(letters)):
        if (letters[i] == text):
            break
    return i
                

def main():
    print("Select data type (0 for binary letters, 1 for bipolar letters)")
    option = input()
    pixels = [] # array to keep the pixel values of each image
    labels = [] #array to keep correct labels
    print(os.getcwd())
    if option == '0':
            os.chdir("Binary") 
    else:
            os.chdir("Bipolar")
    files = os.listdir(os.getcwd()) #all files from the current directory are saved to this array
    for file in files: #for each filename
        print(file)
        if ("Font" in file): #if name contains 'Font' (in our example each file has 'Font' somewhere in their name)
            if("binary" in file):
                    bipolar = 0
            else:
                    bipolar = 1
            labels.append(textToNum(file[-5])) #4th character from the last is kept as label and added to correct labels array
            with open(file, "r") as opened_file: #each file is opened in readable only form
                pixels_in_file = [int(x) for x in opened_file.read().split(',')] #pixel values in each file is splitted by commas, int values are separated from commas and saved in an array
                pixels.append(pixels_in_file) #and this array is appended to another array

    print("Enter a float bias value: ") #a float bias value user chooses is assigned as bias value
    bias = float(input())
    print("Enter a float learning rate: ") #a float learning rate value user chooses is assigned as learning rate value
    lr = float(input())
    print("Enter how many epochs to do: ") #user choosen number of epochs is assigned as number of epochs
    epoch = int(input())
    print("To use delta rule please enter 1, to use perceptron rule press 0")
    delta = int(input())
    print("Do you want a detailed report (press 1 for yes, 0 for no)")
    if input() =='1':
            detail = True
    else:
            detail = False

    perceptron(bias, epoch, lr, pixels, labels, delta, bipolar, detail)


if __name__ == "__main__":
    main()
