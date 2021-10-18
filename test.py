from locale import windows_locale
import easyocr
import cv2
import matplotlib.pyplot as plt
import wikipedia
import pyttsx3

def speak(info):
    engine.say(info)
    engine.runAndWait()

FamousMedicines = ["Amoxicillin", "Ibuprofen","Cetirizinehydrochloride",
                "Azithromycin","Amlodipinebesylate", "AlbuterolsulfateHFA",
                "Cyclobenzaprinehydrochloride","cephalexin","Hydrochlorothiazide"]
 
engine = pyttsx3.init()
speak("Please show your medicine to the camera")
cap = cv2.VideoCapture(0)

while True:
    isTrue, frame = cap.read()
    reader = easyocr.Reader(['en'], gpu=False)
    medicine = reader.readtext(frame)
    print(medicine[0][1])
    try:
        Med_Name = medicine[0][1]
        if Med_Name in FamousMedicines:
            print(Med_Name)
            info = wikipedia.summary("when is "+Med_Name+" used?", 2)
            print(info)
            speak(info)
            plt.imshow(frame)
            plt.show()
        else:
            speak("Medicine is not found please try again")
        break
    except:
        pass
