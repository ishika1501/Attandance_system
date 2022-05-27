
# Face-Regonition Attendance System

Face detection has gained a lot of attention due to its real-time applications. A lot of research has been done and still going on for improved and fast implementation of the face detection algorithm.
This project is basically made to keep the Attendance of students in a file by recognising their faces.
This project is successfully created by using the libraries like cmake, face_recognition, numpy, opencv-python etc.





## Screenshot
![WhatsApp Image 2022-05-25 at 4 01 20 PM (3)](https://user-images.githubusercontent.com/86921052/170713884-5c081c2f-8c95-4726-9837-eac52433e7ea.jpeg)

This basically consist of 5 parts:
- **1.STUDENT DETAILS:** Where one can enter new student details, upadtte , dellete and reset the data for the respective student.
                         It has the feature to take photo sample of the student in realtime corrresponding to their details which can be used to mark their attendance.
- **2.TRAIN DATA:**      After taking the photo sample it train the data so the system can recognize the face.
- **3.FACE DETECTOR:**   It shows the details of the corresponding student who's details and photo samples are been trained bythe system.
                         It mark the other faces as Unknown (Those entries for which we have not collected the photo sample and has not been trained).
                         Create a csv file where the student's details along with date and time is marked as present if the camera is able to recognise the face.
- **4.ATTENDANCE:**      Here we can import the saved csv file where the attendance of the student has been marked.
                         It comes with the feature of Resting the data and Export the opened csv file in the desired location for keeping the record.                    
- **5.PHOTO FACE:**      Basic folder which have all the 100 sample photo for each student which has been captured.

                    
