# CODESOFT
This repository displays four finished projects from the CodSoft AI Internship. They are the rule-based chatting bot, the AI Tic-Tac-Toe, the face detection and recognition system, and the image captioning model. The repository contains the major projects done during the internship and welcomes anyone willing to contribute to it.


Task 1:RULE-BASE-CHATBOT-RESPONSE

This project features a simple rule-based chatbot developed using Python and Flask, with a user interface built using HTML. The chatbot engages users by responding to various queries and prompts, including greetings, questions about its identity, and topics like weather, food, and hobbies. It uses predefined responses based on specific keywords and phrases detected in the user's input.
The core functionality is encapsulated in the chatbot_response function, which processes user input through a series of conditional statements and regular expressions. The chatbot can recognize greetings and respond with friendly messages, answer questions about its name, and provide information based on keywords such as "weather," "time," "hobby," and more.
The user interface allows for seamless interaction, enabling users to converse with the chatbot through a web page until they choose to end the interaction. The code is designed to be extensible, allowing for further enhancements to the chatbot’s capabilities and response diversity.
Overall, this project serves as a foundation for building more advanced conversational agents and demonstrates basic principles of natural language processing and web development.



Task 2:FACE-DETECTION-AND-RECOGNITION-SYSTEM

The Face Recognition and Detection System utilizes the OpenCV library, which provides tools for image processing and computer vision tasks. The code consists of two main parts: face detection in an image and live face detection through a webcam feed.
For image-based face detection, the code reads an image file specified by the image_path, detects faces using a pre-trained Haar cascade classifier (haarcascade_frontalface_default.xml), and draws rectangles around the detected faces. The detect_faces_image function displays the image with detected faces using OpenCV's imshow function.
For live face detection, the code captures video frames from the webcam using the VideoCapture function. It then applies the same face detection technique to each frame, drawing rectangles around detected faces in real-time. The process continues until the user presses the 'q' key to exit the application.
Overall, this system provides a simple yet effective way to detect and recognize faces in both static images and live video streams, leveraging the power of OpenCV's computer vision capabilities.



Task 3:TIC-TAC-TOE-AI-GAME

This  Tic-Tac-Toe AI game utilizes Python's Tkinter library for creating the graphical user interface. 
Tkinter simplifies the development of GUI applications and provides tools for creating buttons, frames, and event handling. 
Functions are used to manage various aspects of the game, including changing game modes (single player or multiplayer), updating the game board, and checking for win or draw conditions. 
The minimax algorithm is employed to determine the computer player's moves in single-player mode, ensuring optimal gameplay. 
This algorithm recursively evaluates possible moves to find the best strategy while considering the opponent's moves. 
Overall, the code offers an interactive gaming experience, allowing users to play Tic-Tac-Toe against a computer opponent or with another player, enhancing their understanding of GUI development and game logic implementation in Python.



Task 4:AI-BASED-IMAGE-CAPTIONING-MODEL

