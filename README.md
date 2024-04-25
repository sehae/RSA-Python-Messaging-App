# Chat Application

This repository contains a simple PyQt5-based chat application that allows users to communicate securely in a private chat room. This application implements end-to-end encryption using RSA encryption for secure messaging.


## Usage

To use the Application, follow these steps:

1. **Run the Application**: Execute the `main.py` file to start the PairPal application.
   
2. **Join a Chat Room**: Enter your screen name and click the "Join" button to enter the chat room. The chat room can accommodate up to two participants.

3. **Send Messages**: Once in the chat room, type your message in the input box at the bottom and press the "Send" button to send your message to the other participant.

4. **Receive Messages**: Messages from the other participant will appear in the chat history area.

5. **Log Window**: Encryption and Decryption as well as Key generation will be logged in the System Log Window. A clear button is available to clear the logs.

6. **Close the Application**: Close the application when done chatting. This will allow another user to enter the chat room. Close the menu window to close all the windows running.


## Important Note

- The application generates RSA key pairs for each participant upon joining the chat room to facilitate secure messaging.

## Dependencies

The application has the following dependencies:

- Python 3.x
- PyQt5
- cryptography

## Flowchart of the Program
![RSA Python Messaging App Flowchart](https://github.com/sehae/RSA-Python-Messaging-App/assets/106131457/b7e35540-05f7-40f6-9c29-54d9863c85ad)
