#!/usr/bin/python3
# A simple Python program to demonstrate  getpass.getpass() to read password 
import getpass 

def main():
    #print(f"Enter the password.\n")
    p = getpass.getpass()
    #p = input()
    
    print("Password entered:", p)
    
if __name__ == "__main__":
    main()
