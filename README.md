# COVInfo
Code Louisville January 2021 Python Project
Author: Nicholas Johnson
Date: April 2, 2021

This project is intended to complete the requirements of the Code Louisville January 2021 Python course.

The program COVInfo is designed to provide interactive information on COVID-19.
The features include recommendations if a user needs to quarantine or isolate based 
on the time of recent exposure/diagnosis, and a tool to track temperature readings 
and fever as a symptom. The guidelines used in the application come from CDC-issued
guidance, including the temperature that is considered feverish, and the ever-changing 
duration recommendations for quarantine and isolation based on recent exposure and
diagnosis status. This application is not verified for clinical application, but 
represents an example of the features and logical template that could be implemented
for a useful application for patients in a non-healthcare setting.


The program includes 3 features to meet the project requirements:
1. Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
2. Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
3. Read data from an external file, such as text, JSON, CSV, etc and use that data in your application

Any special instructions required for the reviewer to run your project?
There are no special instructions required for the reviewer to run this project.
However, if you choose to do so, you may modify the cdc_info.txt file to change
the temperature that is considered to be a fever. This is an example of the ability
of a clinician to change diagnostic criteria the program uses based on updated 
guidance, specific patient care criteria, etc. Additionally, the temperature_log.txt 
file will contain the exported  temperature measurements supplied by the user so that 
they may save them after the program terminates.
