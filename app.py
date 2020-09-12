from flask import Flask
from flask import jsonify
from flask import request
from face_recognition import face_detection_cli

import cv2
import face_recognition
import base64
import os

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello Burak'

@app.route('/compareFaces')
def compareFaces():  






    firstImg = request.json['firstImg']
    secondImg = request.json['secondImg']
    firstImgName = request.json['firstImgName']
    secondImgName = request.json['secondImgName']

    imgdata = base64.b64decode(firstImg)
    firstImgFilePath = 'Resources/faces/' + firstImgName + '.jpg'
    with open(firstImgFilePath, 'wb') as f:
        f.write(imgdata)

    imgdata = base64.b64decode(secondImg)
    secondImgFilePath = 'Resources/faces/' + secondImgName + '.jpg'
    with open(secondImgFilePath, 'wb') as f:
        f.write(imgdata)


    firstImgToRecognition = face_recognition.load_image_file(firstImgFilePath)
    secondImgToRecognition = face_recognition.load_image_file(secondImgFilePath)

    encodeFirstImg = face_recognition.face_encodings(firstImgToRecognition)[0]
    encodeSecondImg = face_recognition.face_encodings(secondImgToRecognition)[0]



    # myResult = face_detection_cli.process_images_in_process_pool(["Resources/burakKimlik.jpg", "Resources/burakEhliyet.jpg"], 4, 'hog') 

    # print("Multi Core Res: ")
    # print(myResult)

    #imgBurakKimlik = face_recognition.load_image_file("Resources/burakKimlik.jpg")
    #imgBurakKimlik = cv2.cvtColor(imgBurakKimlik, cv2.COLOR_BGR2RGB)

    #faceLocationBurakKimlik = face_recognition.face_locations(imgBurakKimlik)[0]
    #encodeBurakKimlik = face_recognition.face_encodings(imgBurakKimlik)[0]
    #print("encodeBurakKimlik: ")
    #print(encodeBurakKimlik)
    #cv2.rectangle(imgBurakKimlik, (faceLocationBurakKimlik[3], faceLocationBurakKimlik[0]), (faceLocationBurakKimlik[1], faceLocationBurakKimlik[2]), (255,0,255), 2)


    #imgBurakEhliyet = face_recognition.load_image_file("Resources/burakEhliyet.jpg")
    #imgBurakEhliyet = cv2.cvtColor(imgBurakEhliyet, cv2.COLOR_BGR2RGB)




    #faceLocationBurakEhliyet = face_recognition.face_locations(imgBurakEhliyet)[0]
    #encodeBurakEhliyet = face_recognition.face_encodings(imgBurakEhliyet)[0]
    #print("encodeBurakEhliyet")
    #print(encodeBurakEhliyet)
    #cv2.rectangle(imgBurakEhliyet, (faceLocationBurakEhliyet[3], faceLocationBurakEhliyet[0]), (faceLocationBurakEhliyet[1], faceLocationBurakEhliyet[2]), (255,0,255), 2)

    #results = face_recognition.compare_faces([encodeBurakKimlik], encodeBurakEhliyet)
    #faceDistance = face_recognition.face_distance([encodeBurakKimlik], encodeBurakEhliyet)
    faceDistance = face_recognition.face_distance([encodeFirstImg], encodeSecondImg)

    convertedDistance = (1 - float(faceDistance[0])) * 100

    if os.path.isfile(firstImgFilePath):
            os.remove(firstImgFilePath)
    else:    ## Show an error ##
        print("Error: %s file not found" % firstImgFilePath)

    if os.path.isfile(secondImgFilePath):
            os.remove(secondImgFilePath)
    else:    ## Show an error ##
        print("Error: %s file not found" % secondImgFilePath)

    jsonResult = [
        {
            #'algoritmBoolResult' : bool(results[0])
            'comperasionResult' : float(format(convertedDistance, '2f'))
        }
    ]

    return jsonify(jsonResult)


if __name__ == "__main__":
    app.run(debug=True)