<p align="center">
<img src="https://i.imgur.com/wUwON6o.jpeg" alt="Honeypot Logo"/>
</p>


<h1>Building an SSH and HTTP honeypot using Python in Visual Studio Code</h1>
This project details the what, design, development, and deployment of a honeypot framework built in Python, capable of emulating both SSH and HTTP services. The goal of this project is to capture simulated attacker behavior, credentials, and commands in a controlled environment for learning purposes.<br />

<h2>What is a honeypot?</h2>
A honeypot is a deliberately vulnerable system that lures threat actors to attack it instead of legitimate targets. It can be modeled just like a regular, important digital asset, designed to look very convincing to attackers. However, it contains nothing of value to the organization.   
</p> 
Think of it as two houses. A threat actor sees two houses that look the exact same, but one has the door unlocked. The threat actor goes to that house, as it provides no defenses against an attack. But once inside, the attacker finds that there is nothing of value within it. And on top of that, there are plenty of tools inside that record everything about the attacker. 
</p> 
The second benefit of a honeypot, besides distracting attackers, is its ability to be built to record information about attackers. Once a threat actor is inside, the honeypot records their IP address, port number, username, and password used to get in, commands used, sites visited, and more. The honeypots' benefit is learning more about threat actors, while also keeping them away from your valuable assets. 

<h2>Environments and Technologies Used</h2>

- Python 3
- Visual Studio Code
- Paramiko (SSH server emulation)
- Flask (HTTP web server)
- Socket Programming
- Threading
- argparse
- Logging with RotatingFileHandler

<h2>Operating Systems Used </h2>

- Windows 24H2
- Linux (recommended for deployment)

<h2>Deployment and Configuration Steps</h2>

<h3>Step 1 </h3>
Clone the repository and navigate to the project directory. Ensure Python 3 is installed and available in your PATH. 
</p>
Install the required dependencies with this command: pip install paramiko flask

<h3>Step 2</h3>
Generate an SSH host key for the SSH honeypot. This key is required for the Paramiko SSH server to function properly. 
</p>
Command: ssh-keygen -t rsa -f host.key
</p>
Place the generated host.key in the same directory as the SSH honeypot script. 

<h3>Step 3</h3>
The project uses argument parsing to control how the honeypot runs. Using this, you can specify:</p> 
- Listening address</p>
- Port number</p>
- Honeypot type (SSH or HTTP)</p>
- Optional username and password 
</p>
This allows a single entry point to deploy multiple honeypot services without modifying the code.

<h3>Step 4</h3>
Now, to start the honeypot, enter this command: python main.py -a 127.0.0.1 -p --ssh
</p>
This command will slightly change based on your operating system (for example, macOS uses "python3" instead of just "python". Make sure you know the commands for your operating system before entering exactly what I have listed here. 
</p>
By default, the SSH honeypot accepts any username and password, allowing attackers to immediately access the fake shell. 
</p>
Once connected, attackers are presented with:</p>
- A spoofed OpenSSH banner</p>
- A fake system welcome message</p>
- An emulated shell environment</p>
All authentication attempts are logged to audits.log, while executed commands are recorded in cmd_audits.log.
</p>
The emulated shell responds to common commands such as:</p>
- whoami</p>
- pwd</p>
- ls</p>
- cat</p>
- mkdir</p>
- rmdir</p>
- cd</p>
Any unknown commands are logged and return "command not found".
</p>
For additional clarification, why am I using the IP address "127.0.0.1" and port number "2223"? 127.0.0.1 limits the access of the honeypot to the local device, so only your machine will be able to access it. If you were using this in the professional space where you wanted to catch threat actors, you would use the IP address of "0.0.0.0", which allows anyone to access it. 
</p> 
Port number 2223 was chosen since it is a very common alternate SSH port that attackers often scan for. It will look believable to threat actors, who may believe it was a misconfigured SSH port, or admins trying to "hide" their SSH. 

<h3>Step 5</h3>
To start the HTTP honeypot, enter the command: python main.py -p 5000 --http
</p>
By default:</p>
- Username: admin</p>
- Password: password
</p>
The honeypot hosts a fake WordPress admin login page and captures all submitted credentials.
</p>
Each login attempt records:</p>
- Attacker IP address</p>
- Submitted username</p>
- Submitted password
</p>
All data is written to http_audtis.log using a rotating log handler.
</p>
The server listens on all interfaces (0.0.0.0), making it suitable for deployment on a public-facing VM.
</p>

<h3>Step 6</h3>
Once either honeypot is running, activity is logged in real time. These logs can be:</p>
- Reviewed manually</p>
- Ingested into a SIEM</p>
- Used for behavioral analysis</p>
- Correlated with firewall or IDS alerts
</p>
This project shows hands-on experience for understanding attacker behavior and integrating deception-based security techniques into a defensive strategy

