'''
Program Name: Network_Analytics_Capstone
Prgram Description: This program reads a domain from the web and displays domain information.
Programmer: Ray, Stephen
Date: 02/06/2022
Course: CSC233-1L1
'''

import urllib.parse, http.client
import json

#Explain the program to the user
def explainProgram():
    print("This program reads a domain from the web and displays domain information.")

#The domainName() function receives input from the user and assigns this value to the userDomain variable
def domainName():

    userDomain = input("Enter the name of the domain you would like to check. For example enter frontrange.edu:")

    return userDomain

#The licenseKey() function recieves input from the user and assigns this value to the userLicense variable
def licenseKey():

    userLicense = input("Enter api license key. For example enter 1SKMQVHJWKCYOLVEZXKD7R4INRUEIVLW:")

    return userLicense

#The readDomain() function accepts the userDomain and userLicense variables as arguments and reads the domain information
def readDomain(userDomain, userLicense):

    p = { 'key': userLicense, 'domain': userDomain, 'format': 'json' }

    conn= http.client.HTTPSConnection("api.ip2whois.com")
    conn.request("GET", "/v2?" + urllib.parse.urlencode(p))
    res = conn.getresponse()

    pit = res.read()

    #Use the json load string function and assign the result to the p_dict dictionary to return
    p_dict = json.loads(pit)

    return p_dict

#The displayResults function accepts the p_dict dictionary varaible as an argument and prints resluts to the console for the user
def displayResults(p_dict):
    
    print("-----------------------")
    print("Domain Information")
    print("-----------------------")
    
    #Print the keys and values in the p_dict dictionary to display the domain information
    for key, value in p_dict.items():
        print(key, ':', value, "\n")
      
#The main function calls all relevant functions and assigns variables userDomain, userLicense, and p_dict to their appropriate returned values
def main():
    explainProgram()

    userDomain = domainName()
    userLicense = licenseKey()
    p_dict = readDomain(userDomain, userLicense)
    
    displayResults(p_dict)
    
#Call the main() function
main()