from autobahn.twisted.websocket import WebSocketClientProtocol, \
                                       WebSocketClientFactory
from PIL import Image

# import the base64 module
import base64
from datetime import datetime
import numpy as np
import cv2
import codecs
import time


class MyClientProtocol(WebSocketClientProtocol):


   def onConnect(self, response):
      print("Server connected: {0}".format(response.peer))

   def onOpen(self):
      print("WebSocket connection open.")
      message = "Connection opened....".encode()
      message = codecs.encode(message, "hex")
      self.sendMessage(message)


   def onMessage(self, payload, isBinary):
      if isBinary:
         face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

         eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
         result_file = str(datetime.now())
         print("Binary message received: {0} bytes".format(len(payload)))
         with open("img/" + result_file+".jpg", 'wb') as file:
              file.write(payload)


         img = cv2.imread("img/"+result_file + ".jpg")
         print (img)
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         print (gray)
         faces = face_cascade.detectMultiScale(gray, 1.3, 5)
         print (faces)
         if len(faces) == 4:
                  print (faces[0])
                  message = "Face Detected".encode()
                  message = codecs.encode(message, "hex")
                  self.sendMessage(message)
         else:
                  message = "Face Not Detected".encode()
                  message = codecs.encode(message, "hex")
                  self.sendMessage(message)
      else:
         # printing the size of the encoded image which is received
         print("Encoded size of the received image: {0} bytes".format(len(payload)))

   def onClose(self, wasClean, code, reason):

      print("WebSocket connection closed: {0}".format(reason))



if __name__ == '__main__':

   import sys

   from twisted.python import log
   from twisted.internet import reactor

   log.startLogging(sys.stdout)

   factory = WebSocketClientFactory("ws://192.168.2.2:9000")
   factory.protocol = MyClientProtocol

   reactor.connectTCP("192.168.2.2", 9000, factory)
   reactor.run()
