<p align="center">
<img src="https://i.imgur.com/wUwON6o.jpeg" alt="Honeypot Logo"/>
</p>


<h1>Building an SSH and HTTP honeypot using Python</h1>
This tutorial shows the functions and logs of the SSH and HTTP honeypots.<br />

<h2>What is a honeypot?</h2>
A honeypot is a cybersecurity tool that lures threat actors to attack it instead of legitimate targets. It can be modeled just like a regular, important digital asset, designed to look very convincing to attackers. However, it contains nothing of value to the organization.   
</p> 
Think of it as two houses. A threat actor sees two houses that look the exact same, but one has the door unlocked. The threat actor goes to that house, as it provides no defenses against an attack. But once inside, the attacker finds that there is nothing of value within it. And on top of that, there are plenty of tools inside that record everything about the attacker. 
</p> 
The second benefit of a honeypot, besides distracting attackers, is its ability to be built to record information about attackers. Once a threat actor is inside, the honeypot records their IP address, port number, username and password used to get in, commands used, sites visited, and more. The honeypots' benefit is learning more about threat actors, while also keeping them away from your valuable assets. 

<h2>Environments and Technologies Used</h2>

- VMware Workstation
- Visual Studio Code
- Python 13.2

<h2>Operating Systems Used </h2>

- Windows 24H2

<h2>What Will Be Shown.</h2>
For this post, I will only be showing the terminal responses of the honeypot, the HTTP page, and the logs that I receive from my interactions with the honeypot.  

<h2>SSH Honeypot terminal</h2>

<p>
<img src="https://i.imgur.com/GxroCJH.jpeg" height="80%" width="80%" alt="Step 1"/>
</p>
<p>
The first question, "What is the date of this network traffic?" is solved easily. All you need to do is. Select “View --> Time Display Format --> Date and Time of Day”. Selecting this brings up the date of the network traffic: November 16, 2014.  
<br />

</p>

