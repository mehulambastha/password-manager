# Main module to integrate all data management
# Made By: Mehul Ambastha
# **Integrating encryption/decryption to work perfectly
from cryptography.fernet import Fernet
import json
from PyQt5 import QtWidgets
import os


def new_entry_from_ui(ui):  # ui is the 'self' object passed from the newEntry file
    serv = ui.lineEdit.text()
    usrname = ui.lineEdit_2.text()
    pswd = ui.lineEdit_3.text()
    cred = [usrname, pswd]

    # Pass credentials to encrypt_file function in encryption module
    encrypted_credentials = encrypt_file(cred)

    # Send the encrypted data to save_pass module to be saved in JSON
    save_data(serv, encrypted_credentials)

def save_data(service, credentials):
    # Data holds all the data
    data = []
    # Modifying the credentials list
    # Replacing ' by " so that the bytes get parsed to JSON correctly
    credentials = [str(d).replace("'", '"') for d in credentials]
    # Opening the JSON file to fetch already existing data

    if os.path.isfile('data/credentials'):
        with open("data/credentials", "r") as file:
            # If some data already exists
            if os.stat('data/credentials').st_size != 0:
                # setting file pointer at the start so as to read everything completely
                file.seek(0)
                t = file.read()
                # Saving the already existing data to 'data' variable
                data = json.loads(t)
            
            data.append({"service": service, "credentials": credentials})
        # Dumping all the data to credentials.json file
        with open("data/credentials", "w+") as f:
            json.dump(data, f, indent=4)
    else:
        with open('data/credentials', 'w') as new_file:
            pass


# Main function for encryption
def encrypt_file(credentials):
    # Credentials parameter is a list containing username/email and pwd

    if os.path.isfile('data/donotopen'):
        with open('data/donotopen', 'rb+') as filekey:
            # Checking if key already exists.
            if os.stat('data/donotopen').st_size !=0:
                key_str = filekey.read() # Read the encryption key
            else:
                key_str = Fernet.generate_key()
                filekey.write(key_str)

        # Generating the fernet key
        fernet = Fernet(key_str)

        # Encrypting the elements of credentials argument.
        encrypted_list = [fernet.encrypt(bytes(value, 'utf-8'))
                        for value in credentials]
        return encrypted_list
    else:
        with open('data/donotopen', 'w'):
            pass
        return []

def decrypt_data(credentials):  # credentials is a list of encrypted data

    if os.path.isfile('data/donotopen'):
        with open('data/donotopen', 'rb+') as filekey:
            # Checking if the key has been already generated.
            if os.stat('data/donotopen').st_size !=0:
                print("Key is generated already")
                # If key is already generated, don't generate new key
                # TODO: Fix the read bytes issue.
                key = filekey.read()
                print(key)
                fernet = Fernet(key)
                # create decrytped data from the argument
                decrypted_data = [fernet.decrypt(value) for value in credentials]
                # Return the decrypted data as a list.
                return decrypted_data
            else:
                print("Data is lost")
                # Key does not exist. Data is lost.
                key = Fernet.generate_key()
                filekey.write(key)
                with open('data/credentials', 'w') as c:
                    c.write('')
                data_lost = ["DATA IS LOST", "YOU DELETED THE KEY!"]
                return data_lost
    # key file does not exist. The user deleted it.
    else:
        # Creating the file if it does not exist.
        with open('data/donotopen', 'w') as x:
            pass

        with open('data/credentials', 'w') as c:
            c.write('')
        # Return error message.
        data_lost = ["DATA IS LOST", "YOU DELETED THE KEY!"]
        return data_lost    



# Responsible for loading the data from credentials.json to the main UI
def load(self, query):
   
    if os.path.isfile('data/credentials'):
        # Open the JSON file
        with open("data/credentials", "r") as file:            
            if os.stat('data/credentials').st_size != 0: 
                # setting file pointer at the start so as to read everything completely
                file.seek(0)
                t = file.read()
                # Saving the already existing data
                data = json.loads(t)
            else:
                data = []
                print('NO DATA')
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("NO DATA"))
    else: #Creating the file if it does not exist.
        with open('data/credentials', 'w'):
            pass
        if not os.path.isfile('data/donotopen'):
            with open('data/donotopen', 'w'):
                pass
        data = []
    
    
    if query == "":       
        # Set the number of rows to be equal to total number of entries in data 
        self.tableWidget.setRowCount(len(data))
                    
        # For loop to iterate through every item and set data to the table
        for i in range(0, len(data)):
                row = i # row equals the current iteration  
                        
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data[i]["service"]))
                # Converting data into valid bytes
                saved_cred = [eval(value) for value in data[i]["credentials"]]
                # Unpacking username and password
                usr, pwd = decrypt_data(saved_cred)

                if type(usr) == str and type(pwd) == str: # Returned string means the key has been deleted and error message has been returned in place of actual data
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem("CLICK THE RELOAD BUTTON"))                    
                else:
                    # Converting to strings
                    usr, pwd = usr.decode('utf-8'), pwd.decode('utf-8')
                    
                # Inserting username and password
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(usr))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(pwd))
    else:
        filtered_data = []
        for cred in data:
            if cred["service"].lower() == query:
                filtered_data.append(cred)
        
        if not filtered_data:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("NO MATCH"))
            self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(""))
        else:
            # Set the number of rows to be equal to total number of entries in data 
            self.tableWidget.setRowCount(len(filtered_data))
                        
            # For loop to iterate through every item and set data to the table
            for i in range(0, len(filtered_data)):
                row = i # row equals the current iteration  
                            
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(filtered_data[i]["service"]))
                # Converting data into valid bytes
                saved_cred = [eval(value) for value in filtered_data[i]["credentials"]]
                # Unpacking username and password
                usr, pwd = decrypt_data(saved_cred)
                # Converting to strings
                usr, pwd = usr.decode('utf-8'), pwd.decode('utf-8')
                # Inserting username and password
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(usr))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(pwd))