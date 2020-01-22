# cam-image-transfre-websockets
Client and Server to transfer web cam image files through websockets.


<p>We have two files that  we need for the complete transaction to occur: client.py and server.py. Server.py is for computer which 
streams data which in our case is the raspberry pi. And client.py is the script for client computer which receives the image stream.</p>

<h3>Steps-</h3>
<h4>For server side:</h4>
<ul>
  <li>Clone the repository with the command: <i>git clone https://github.com/surajbeston/cam-image-transfre-websockets.git</i>(Make sure git is installed)</li>
  <li>Move to the directory and then run: python server.py(This runs the server. Make sure python3 is installed. On system with both versions installed use python3.)</li>
</ul>  
<h4>For client side:</h4>
<ul>
  <li>Also clone the repo in the client computer to run.</li>
  <li>Edit the client.py file and add ip address of computer running the server.py script.</li>
  <li>Make sure the computer running server.py and client is on the same local network.</li>
  <li>Move to the repository and then run: python client.py</li>
</ul>
  
