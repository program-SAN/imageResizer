import os
#since say command is not present in windows we install pyttsx3
import pyttsx3

if __name__ == '__main__':
    #initialising the import package
    text_to_speech =pyttsx3.init()
    while(True):
        word = input("enter your command ")
        if (word=="q"):
            break
        text_to_speech.say(word)
        text_to_speech.runAndWait()