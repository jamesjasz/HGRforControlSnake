HGRforControlSnake
Hand Gesture Recognition (HGR) using Convolutional Neural Networks to Control a Snake Game

📷 Project Screenshot

(Replace this path if the image file name differs.)

Table of Contents
Overview

Features

Tech Stack

Installation & Usage

Gesture Recognition Details

Project Structure

Contributing

License & Acknowledgements

Overview
HGRforControlSnake is a Python-based computer vision project that captures hand gestures via webcam and uses a CNN model to control a Snake game in real time. It merges classic gameplay with modern gesture-based input methods for an engaging, hands-free experience 
This Dot Labs
IJRASET
+4
SpringerLink
+4
SpringerLink
+4
.

Features
🎮 Real-time control of a Snake game using hand gestures

Gesture detection powered by a CNN implemented with OpenCV

Keyboard automation for game control enabled via gesture recognition

Plug-and-play: webcam-based interaction without additional peripherals

Tech Stack
Python – Core application logic

OpenCV – Video capture, gesture detection and processing

PyAutoGUI – Automates keyboard input for gameplay

Pygame – The Snake game framework

Additional libraries defined in requirements.txt 
SpringerLink
+1
SpringerLink
+1

Installation & Usage
Clone the repository

bash
Copy
Edit
git clone https://github.com/jamesjasz/HGRforControlSnake.git
cd HGRforControlSnake
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run gesture-recognition module
Execute the script designed to detect gestures and map them to controls (e.g. coba10c.py).

Run the Snake game
Launch the in-repo Snake game using:

bash
Copy
Edit
python SnakeFun.py
Make gestures in front of your webcam
Detected gestures will simulate game key presses (up, down, left, right).

Gesture Recognition Details
The system detects hand movements via webcam using HSV color-space filtering, then processes contours and directionality. A Convolutional Neural Network classifies gestures which PyAutoGUI translates into keystrokes to control the Snake game automatically 
x.com
+5
IJRASET
+5
Medium
+5
This Dot Labs
.

Project Structure
bash
Copy
Edit
/HGRforControlSnake
├── README.md
├── requirements.txt
├── image.png
├── coba10c.py           # Main gesture recognition
├── coba10c_page23.py    # Alternative or testing version
├── SnakeFun.py          # Pygame-based snake game
├── settingsSnakeFun.py  # Snake configuration parameters
└── Artikel Ilmiah ...pdf# Project documentation
Contributing
Contributions are welcome! Open to improvements in gesture accuracy, new gesture mappings, or enhancements to the Snake game itself. Feel free to open a pull request.

