#############################
#    Import dependencies    #
#############################
import html
import re

#############################
#        Print intro        #
#############################
print(str(
    "######################################################\n" + 
    "#                Welcome to PyDecode!                #\n" + 
    "######################################################\n" + 
    "# Please note that this program can only decode HTML #\n" + 
    "######################################################\n"))

#############################
# Get information from user #
#############################
fileName = str("./" + str(input("What is the name of the file you wish to decode?: ")))
outputFileName = str("./" + str(input("What would you like to name the file containing the result?: ")) + ".txt")

#############################
#     Validate fileName     #
#############################
while fileName.endswith(".html") == False:
    print("Detected invalid information!\nYou must add .html to the end of the file you wish to decode!")
    fileName = str("./" + str(input("Please try again: ")))

#############################
#   Decode HTML file and    #
#  put result in .txt file  #
#############################

print()
input("Press any key to close...")