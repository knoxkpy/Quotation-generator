import sys
import os
import math

################################
#Documentation:
#This script assumes that 'data.txt' is a not encrpted.
#If the txt file is not named exactly 'data.txt', then the file won't work.


################################
def instruction():
    print("How to use this calculator/quotation generator?\nWhen starting the script, type next if you want to skip the instruction.")
    print('The script itself does not store any data automatically. All data is gone after exiting the script/program. So make sure to save your quotation or new items to data.txt before leaving!')
    print('')

def readData():
    print('Reading data...')
    Data = {}

    #this shouldn't be triggered anymore as it automatically create a new file now.
    try:
        file_hndl = open('data.txt', 'r')
    except FileNotFoundError:
        print('The file does not exist or it is not named as "data.txt".\nProgram is exiting...')
        sys.exit(0)

    for line in file_hndl:
        parts = line.rsplit(maxsplit = 1)
        key = parts[0]
        value = parts[1]
        Data[key] = float(value)

    file_hndl.close()
    return Data

#creating data.txt by using open() function.
def createDatatxt():
    print('Creating data.txt...')
    file_hndl = open('data.txt', 'w')
    file_hndl.close()

def showExistingItems(Data):
    for key, value in Data.items():
        print(f'item: {key}, price: {value}')
    print('')

def printQuotation(quotation):
    #print the quotation
    #store the quotation/output the quotation.
    print(quotation)
    print('')

def saveNewData(newData):
    returnType = True
    file_hdl_read = open('data.txt', 'r')
    existing_data = set()
    for line in file_hdl_read:
        key = line.split()[0]
        existing_data.add(key)
    file_hdl_read.close()

    file_hdl_append = open('data.txt', 'a')
    for key in newData:
        if key not in existing_data:
            file_hdl_append.write(f'{key} {newData[key]}\n')
        else:
            returnType = False
    file_hdl_append.close()

    return returnType

#initialization of the script. Giving small instruction.
def initialization():
    while True:
        userInput = input("Input 'note' if you want to check how to use the calculator. Or input 'next' to proceed. Type in 'exit' if you want to exit the program.").upper()
        
        if (userInput == "NOTE"):
            instruction()
        elif (userInput == "NEXT"):
            #if data.txt doesn't exist, create it.
            if not os.path.exists('data.txt'):
                createDatatxt()
            break
        elif (userInput == "EXIT"):
            print('Program exiting...')
            sys.exit(0)

def main():
    print("Welcome to the quotation calculator/generator!")

    initialization()
    
    #dealing with data...storing the current data in a dict.
    data = readData()
    #existing items for quotation
    addedItemsForQuotation = {}
    #added new items.
    addedItemsForDataBase = {}

    while True:

        print('Please choose your action: \n1. Add new items to the database and also show all quotation items after adding it.')
        print('2. Show existing items.')
        print('3. Choose an items and add it to the quotation')
        print('4. Save the quotation and export the quotation and exit.')
        print('5. Updated an existing items.')
        print('6. Print current quotation and calculate total.\n')

        try:
            userSelection = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a correct integer.")
            continue

        if (userSelection == 1):
            #Add new items to the database and also show all quotation items after adding it.
            print('You will be adding new items to the database...\n')
            while True:
                newItem = input('Please enter the name of the new item, type in "end" or "END" to finish the process:')
                if (newItem == 'end' or newItem == 'END'):
                    break
                
                newItemPrice = input('Please input the price of the new items: $')

                try:
                    newItemPrice = float(newItemPrice)
                    print("Valid number entered.")
                except ValueError:
                    print("Invalid number. Please enter a valid integer or float.")
                    continue

                addedItemsForDataBase[newItem] = newItemPrice
            
            #adddata
            print('Adding data to the database...\n')
            if saveNewData(addedItemsForDataBase):
                print('All items are successfully added to the database.')
            else:
                print('Duplicated items detected. Some items already exist in database. Duplicated items was not saved but others were saved successfully.')

            #readdata again
            data = readData()
            #print data
            print('Printing the quotation items...')
            showExistingItems(data)

        elif (userSelection == 2):
            if (len(data) == 0):
                print('There is no data right now. Try to add something before checking the existing items!')
            else:
                showExistingItems(data)
        elif (userSelection == 3):
            print()
        elif (userSelection == 4):
            #save the quotation and output the quotation
            #save the
            break
        elif (userSelection == 5):
            if (len(data) == 0):
                print('There is nothing to update! Please add something to the database before doing this!')
                continue
            else:
                print('do something here...')
        else:
            print("Please enter a valid integer!")

    print('Exiting the program...')

main()