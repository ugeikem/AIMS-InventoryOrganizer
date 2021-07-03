# Program By: CDT Uge Ikemefune
#AIMS (ARMY INVENTORY MANAGEMENT SYSTEM) PROGRAM FOR INVENTORY MANAGEMENT
import qrcode
import pandas as pd
import os


#************************SECTION 1: FILE MANAGMENT AND SETUP***************************************************
# **********Import needed File***************************************
currentFolderPath = os.getcwd()
excelFile = input('Please input the name of the inventory list: ')
# data = pd.read_excel(r'/Users/ikem/PycharmProjects/InventoryOrganizer/inventoryList.xlsx',engine='openpyxl')
data = pd.read_excel(currentFolderPath+'/'+excelFile,engine='openpyxl')
df=pd.DataFrame(data)
row = next(df.iterrows())
inventoryFilePath = '/Users/ikem/PycharmProjects/InventoryOrganizer/Inventory Barcodes/'
keysFilePath = '/Users/ikem/PycharmProjects/InventoryOrganizer/Key Barcodes/'
pd.set_option("display.max_rows", None, "display.max_columns", None)
#***************************************************************************

#******************************SECTION 2: HELPER FUNCTIONs*********************************************
# Iterate through the entire list
def barcode_maker():
    for index, row in df.iterrows():
        itemVal = (index,row)
        temp = pd.DataFrame(itemVal)
        itemString = temp.to_string()
        img_name = qrcode.make(itemString)
        key_name = qrcode.make(itemString)
        key_name.save(keysFilePath+'key_'+row['Item Name']+'_'+row['Box Number']+'.jpg','JPEG')
        img_name.save(inventoryFilePath+row['Item Name']+'.jpg','JPEG')
    print("Barcodes generated please see (Key Barcodes & Inventory Barcodes folders)")

def run_inventory():
    while True:
        try:
            # Search and Retrieve User Needed Data
            print("Welcome to AIMS (ARMY INVENTORY MANAGEMENT)")
            print("Please follow the prompts below:")
            itemName = (input("Item Name :")).lower()
            storageLocation = (input("Storage Location:")).lower()
            nsnIdentifyer = (input("NSN number (NSN format: xxx-xxxx):")).lower()
            platoonNumber = (input("Platoon Number:")).lower()
            # Create a list of words
            includeKeyWords = [itemName, storageLocation, nsnIdentifyer, platoonNumber]
            # Check Values given for possible results
            filteredValues = df[df.stack().str.lower().str.contains('|'.join(includeKeyWords)).any(level=0)]
            if filteredValues.values.size != 0:
                print(filteredValues)
                print("Please see the barcode sheet for more detail.Use unique identiyer given!")
                tryAgain = input("Would you like to search the inventory again (Y/N):")
                if tryAgain.upper() == 'Y':
                    continue
                else:
                    break
            print(
                '*******************************************************************************************************')
            print(
                "************Unfortunately the parameters you entered does not match any item in our inventory*********")
            print(
                '*******************************************************************************************************')
        except Exception as e:
            print(e)
#****************************************************************************************************

#***************************SECTION 3: RUN PROGRAM************************************************
run_inventory()
barcode_maker()

#****************************************************************************************************