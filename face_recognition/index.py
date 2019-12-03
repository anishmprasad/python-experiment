import face_recognition
import os
cwd = os.getcwd()
files = os.listdir(cwd)
f = open("dataset/416x416.jpg", "r")
print(f.read())
print('files', open("dataset/416x416.jpg"))
for file in files:
    print(file)
image = face_recognition.load_image_file("./dataset/416x416.jpg")
print('image', image)
face_locations = face_recognition.face_locations(image)
