from autobahn.twisted.websocket import WebSocketClientProtocol, \
                                       WebSocketClientFactory
from PIL import Image

# import the base64 module
import base64



class MyClientProtocol(WebSocketClientProtocol):
   result_file = "1"

   def onConnect(self, response):
      print("Server connected: {0}".format(response.peer))

   def onOpen(self):
      print("WebSocket connection open.")
      self.sendMessage(bytes.fromhex("7342"))


   def onMessage(self, payload, isBinary):
      if isBinary:
         self.result_file = self.result_file + "1"
         print("Binary message received: {0} bytes".format(len(payload)))
         with open(self.result_file+".png", 'wb') as file:
              file.write(payload)
         self.sendMessage(bytes.fromhex("7342"))
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

   factory = WebSocketClientFactory("ws://localhost:9000")
   factory.protocol = MyClientProtocol

   reactor.connectTCP("127.0.0.1", 9000, factory)
   reactor.run()
