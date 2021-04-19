import speech_recognization as sr
import serial
import time

r = sr.Recognizer()
with sr.Microphone() as source:
  print("say anything")
  audio = r.listen(source)
  
try:
  print("Google speech recognization thinks you said", r.recognize_google(audio)
except sr.UnknownValueError:
  print("Google speech could not understand you")
except sr.UnknownValueError as e:
  print("Could not request results from Google speech recogination service; {0}".formet(e)
        
        
Port='COM3'
ser = serial.Serial(port, 38400, timeout = 1)
ser.close()
ser.open()
x = "r.recognize_google(audio)"
ser.write(x.encode('UTF/-8'))       
print(ser.readline(x.decode()))
ser.close()
