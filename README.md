This repository contains two projects for gesture control using hand tracking and recognition. Below are brief descriptions of each project along with instructions on how to run them.

# Gesture_Control_Virtual_Mouse

This project implements a virtual mouse control system using hand gestures. It utilizes the Mediapipe library for hand tracking and recognition, OpenCV for image processing, and PyAutoGUI for mouse control. The system recognizes various hand gestures and translates them into corresponding mouse actions.

## Features

- Gesture Recognition: Recognizes a variety of hand gestures, including fist, V-gesture, pinch, and more.
- Virtual Mouse Control: Uses recognized gestures to control the computer's mouse, allowing for various actions such as left-click, right-click, scrolling, and dragging.
- System Control: Implements additional functionalities like adjusting system brightness and volume based on specific gestures.

- The code recognizes a set of basic gestures chosen for intuitiveness and ease of use:

Pointing finger: Used for cursor movement on the screen.
Fist: Simulates a left mouse click and tracks hand movement.
Open palm (mid-finger gesture with a flag): Used for a single left click after a pointing gesture (similar to a traditional mouse click).
Index finger: Simulates a right-click.
Two-finger closed: Triggers a double-click.
Pinch gestures (with additional logic):
Minor hand pinch: Controls horizontal or vertical scrolling.
Major hand pinch: Controls system functions like brightness (implemented) or volume (potential future implementation).

## Requirements
-Python 3.11
-OpenCV
-Mediapipe
-PyAutoGUI
-cvzone
-screen_brightness_control
-pycaw

# PowerPoint Presentation Control

This project enables the control of PowerPoint presentations using hand gestures. It uses the OpenCV library for image processing and the cvzone library for hand tracking. The system allows users to navigate through PowerPoint slides by recognizing specific hand gestures.

## Features

-Slide Navigation: Recognizes gestures for moving to the previous and next slides in a PowerPoint presentation.
-Pointer Mode: Implements a pointer mode that follows the index finger's movement for precise control.
-Simple Control: Control your PowerPoint slides with intuitive hand gestures.

## Requirements

-Python 3.11
-OpenCV
-cvzone
