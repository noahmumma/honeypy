<p align="center">
<img src="https://i.imgur.com/wUwON6o.jpeg" alt="Honeypot Logo"/>
</p>


<h1>Building an SSH and HTTP honeypot using Python</h1>
This tutorial shows how the honeypot functions and .<br />

<h2>The Four Questions</h2>
1. What is the date of this network traffic?
</p> 
2. Which downloaded files were infected, and what are their file hashes?
</p>
3. What is the domain name that delivered the exploit kit and malware?
</p>
4. What is the IP address, MAC address, and host name of the infected machine?

<h2>What is Wireshark?</h2>
Wireshark is a tool that presents captured packet data in a digestible format, allowing a security team to analyze it effectively. It's known as a "network packet analyzer" (NPA).  
</p> 
Imagine an NPA as a tool to help examine exactly what's happening inside a network cable. Whenever a packet is sent through the network cable, Wireshark can present that data to an analyst, showing them everything about it. 
</p> 
But this is not limited to just analysts. Network administrators can use this to troubleshoot network problems, developers can use it to debug protocol implementations, and engineers can use it to examine security problems. 


<h2>Environments and Technologies Used</h2>

- Kali Linux
- VMware Workstation
- Visual Studio Code
- Python 13.2

<h2>Operating Systems Used </h2>

- Linux 6.18

<h2>High-Level Deployment Steps</h2>

- Step 1: Change the format of the "Time Column" to reveal the date.
- Step 2: Filter packets to just "http.request", use "md5sum" to get the hash values from those that contained executables, run them through virustotal[.]com to find which are malicious.
- Step 3: Head back to the content type section of the executable files, and further inspect them to find the hostname. 
- Step 4: Clear all filters, then apply "Dynamic Host Configuration Protocol" as a filter,  select "User Datagram Protocol", and scroll down to find the hostname, IP and MAC address of the infected machine. 

<h2>Deployment and Configuration Steps</h2>

<p>
<img src="https://i.imgur.com/GxroCJH.jpeg" height="80%" width="80%" alt="Step 1"/>
</p>
<p>
The first question, "What is the date of this network traffic?" is solved easily. All you need to do is. Select “View --> Time Display Format --> Date and Time of Day”. Selecting this brings up the date of the network traffic: November 16, 2014.  
<br />

</p>

