# PyKeylogger
🛡PyKeylogger
A simple and lightweight Python Keylogger that records all keystrokes typed on the keyboard and saves them into a log file (log.txt). This project is designed for educational and awareness purposes only, such as learning about ethical hacking, cybersecurity, or demonstrating how keyloggers work.

⚠️ Disclaimer: This tool is for educational purposes only. Do not use it to track or monitor others without their knowledge or permission. Unauthorized usage may violate privacy laws.


## Features
Captures every keystroke typed by the user.

Stores keystrokes in a log.txt file in real-time.

Logs special keys (e.g., space, enter, shift) in a readable format.

Lightweight and easy to use.

Can be run silently in the background.


## Project Structure
bash
Copy
Edit
PyKeylogger/
│
├── main.py           # Main script to start keylogging
├── log.txt           # Stores all captured keystrokes
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation


## How to Run
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Tejagundeti/PyKeylogger.git
cd PyKeylogger

3. Create and Activate a Virtual Environment (Optional but recommended)
bash
Copy
Edit
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

5. Run the Keylogger
bash
Copy
Edit
python main.py

6. View the Logs
Check the log.txt file generated in the same directory to see the captured keystrokes.


## How It Works
The script uses the pynput library to listen to keyboard inputs.

Every key press is recorded using the on_press() callback.

Special keys like Key.space, Key.enter, etc., are handled to be human-readable.

All keystrokes are written to log.txt continuously.


## Example Log Output
vbnet
Copy
Edit
H
e
l
l
o
 Key.space 
W
o
r
l
d
 Key.enter 

 
## Dependencies
pynput: Used to listen and capture keyboard inputs.

Install using:

bash
Copy
Edit
pip install pynput


## Use Cases
Learning about how keyloggers work.

Demonstrating security vulnerabilities.

Ethical hacking and cybersecurity awareness.


## Important Notice
This software should never be used for malicious purposes. Installing or using a keylogger on someone's device without their explicit consent is illegal and unethical. Always get permission before testing this tool on any machine.

📄 License
This project is licensed under the MIT License. See the LICENSE file for more information.

