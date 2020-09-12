import cv2
import face_recognition

imgElon = face_recognition.load_image_file("Resources/elon musk.jpg")
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

imgElonTest = face_recognition.load_image_file("Resources/elon musk test.jpg")
imgElonTest = cv2.cvtColor(imgElonTest, cv2.COLOR_BGR2RGB)

imgBillGates = face_recognition.load_image_file("Resources/bill gates.jpg")
imgBillGates = cv2.cvtColor(imgBillGates, cv2.COLOR_BGR2RGB)

imgBurak = face_recognition.load_image_file("Resources/burak.png")
imgBurak = cv2.cvtColor(imgBurak, cv2.COLOR_BGR2RGB)

imgBurak2 = face_recognition.load_image_file("Resources/burak2.png")
imgBurak2 = cv2.cvtColor(imgBurak2, cv2.COLOR_BGR2RGB)

imgBurak5 = face_recognition.load_image_file("Resources/burak5.png")
imgBurak5 = cv2.cvtColor(imgBurak5, cv2.COLOR_BGR2RGB)

imgBurakKimlik = face_recognition.load_image_file("Resources/burakKimlik.jpg")
imgBurakKimlik = cv2.cvtColor(imgBurakKimlik, cv2.COLOR_BGR2RGB)

imgBurakEhliyet = face_recognition.load_image_file("Resources/burakEhliyet.jpg")
imgBurakEhliyet = cv2.cvtColor(imgBurakEhliyet, cv2.COLOR_BGR2RGB)

imgBurakAkbil = face_recognition.load_image_file("Resources/burakAkbil.jpg")
imgBurakAkbil = cv2.cvtColor(imgBurakAkbil, cv2.COLOR_BGR2RGB)

imgEmre = face_recognition.load_image_file("Resources/emre.png")
imgEmre = cv2.cvtColor(imgEmre, cv2.COLOR_BGR2RGB)

imgEmre2 = face_recognition.load_image_file("Resources/emre2.png")
imgEmre2 = cv2.cvtColor(imgEmre2, cv2.COLOR_BGR2RGB)

imgEmre3 = face_recognition.load_image_file("Resources/emre3.JPG")
imgEmre3 = cv2.cvtColor(imgEmre3, cv2.COLOR_BGR2RGB)

imgIhsan = face_recognition.load_image_file("Resources/ihsan.png")
imgIhsan = cv2.cvtColor(imgIhsan, cv2.COLOR_BGR2RGB)

imgMert1 = face_recognition.load_image_file("Resources/mert.png")
imgMert1 = cv2.cvtColor(imgMert1, cv2.COLOR_BGR2RGB)

imgMert2 = face_recognition.load_image_file("Resources/mert2.jpg")
imgMert2 = cv2.cvtColor(imgMert2, cv2.COLOR_BGR2RGB)

imgIrfan1 = face_recognition.load_image_file("Resources/irfan1.jpeg")
imgIrfan1 = cv2.cvtColor(imgIrfan1, cv2.COLOR_BGR2RGB)

imgIrfan2 = face_recognition.load_image_file("Resources/irfan2.png")
imgIrfan2 = cv2.cvtColor(imgIrfan2, cv2.COLOR_BGR2RGB)



faceLocationElon = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLocationElon[3], faceLocationElon[0]), (faceLocationElon[1], faceLocationElon[2]), (255,0,255), 2)

faceLocationElonTest = face_recognition.face_locations(imgElonTest)[0]
encodeElonTest = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElonTest, (faceLocationElonTest[3], faceLocationElonTest[0]), (faceLocationElonTest[1], faceLocationElonTest[2]), (255,0,255), 2)

faceLocationBillGates = face_recognition.face_locations(imgBillGates)[0]
encodeBillGates = face_recognition.face_encodings(imgBillGates)[0]
cv2.rectangle(imgBillGates, (faceLocationBillGates[3], faceLocationBillGates[0]), (faceLocationBillGates[1], faceLocationBillGates[2]), (255,0,255), 2)

faceLocationBurak = face_recognition.face_locations(imgBurak)[0]
encodeBurak = face_recognition.face_encodings(imgBurak)[0]
cv2.rectangle(imgBurak, (faceLocationBurak[3], faceLocationBurak[0]), (faceLocationBurak[1], faceLocationBurak[2]), (255,0,255), 2)

faceLocationBurak2 = face_recognition.face_locations(imgBurak2)[0]
encodeBurak2 = face_recognition.face_encodings(imgBurak2)[0]
cv2.rectangle(imgBurak2, (faceLocationBurak2[3], faceLocationBurak2[0]), (faceLocationBurak2[1], faceLocationBurak2[2]), (255,0,255), 2)

faceLocationBurak5 = face_recognition.face_locations(imgBurak5)[0]
encodeBurak5 = face_recognition.face_encodings(imgBurak5)[0]
cv2.rectangle(imgBurak5, (faceLocationBurak5[3], faceLocationBurak5[0]), (faceLocationBurak5[1], faceLocationBurak5[2]), (255,0,255), 2)

faceLocationBurakKimlik = face_recognition.face_locations(imgBurakKimlik)[0]
encodeBurakKimlik = face_recognition.face_encodings(imgBurakKimlik)[0]
cv2.rectangle(imgBurakKimlik, (faceLocationBurakKimlik[3], faceLocationBurakKimlik[0]), (faceLocationBurakKimlik[1], faceLocationBurakKimlik[2]), (255,0,255), 2)

faceLocationBurakEhliyet = face_recognition.face_locations(imgBurakEhliyet)[0]
encodeBurakEhliyet = face_recognition.face_encodings(imgBurakEhliyet)[0]
cv2.rectangle(imgBurakEhliyet, (faceLocationBurakEhliyet[3], faceLocationBurakEhliyet[0]), (faceLocationBurakEhliyet[1], faceLocationBurakEhliyet[2]), (255,0,255), 2)

faceLocationBurakAkbil = face_recognition.face_locations(imgBurakAkbil)[0]
encodeBurakAkbil = face_recognition.face_encodings(imgBurakAkbil)[0]
cv2.rectangle(imgBurakAkbil, (faceLocationBurakAkbil[3], faceLocationBurakAkbil[0]), (faceLocationBurakAkbil[1], faceLocationBurakAkbil[2]), (255,0,255), 2)


faceLocationEmre = face_recognition.face_locations(imgEmre)[0]
encodeEmre = face_recognition.face_encodings(imgEmre)[0]
cv2.rectangle(imgEmre, (faceLocationEmre[3], faceLocationEmre[0]), (faceLocationEmre[1], faceLocationEmre[2]), (255,0,255), 2)

faceLocationEmre2 = face_recognition.face_locations(imgEmre2)[0]
encodeEmre2 = face_recognition.face_encodings(imgEmre2)[0]
cv2.rectangle(imgEmre2, (faceLocationEmre2[3], faceLocationEmre2[0]), (faceLocationEmre2[1], faceLocationEmre2[2]), (255,0,255), 2)

faceLocationEmre3 = face_recognition.face_locations(imgEmre3)[0]
encodeEmre3 = face_recognition.face_encodings(imgEmre3)[0]
cv2.rectangle(imgEmre3, (faceLocationEmre3[3], faceLocationEmre3[0]), (faceLocationEmre3[1], faceLocationEmre3[2]), (255,0,255), 2)

faceLocationIhsan = face_recognition.face_locations(imgIhsan)[0]
encodeIhsan = face_recognition.face_encodings(imgIhsan)[0]
cv2.rectangle(imgIhsan, (faceLocationIhsan[3], faceLocationIhsan[0]), (faceLocationIhsan[1], faceLocationIhsan[2]), (255,0,255), 2)

faceLocationIhsan = face_recognition.face_locations(imgIhsan)[0]
encodeIhsan = face_recognition.face_encodings(imgIhsan)[0]
cv2.rectangle(imgIhsan, (faceLocationIhsan[3], faceLocationIhsan[0]), (faceLocationIhsan[1], faceLocationIhsan[2]), (255,0,255), 2)

faceLocationMert = face_recognition.face_locations(imgMert1)[0]
encodeMert = face_recognition.face_encodings(imgMert1)[0]
cv2.rectangle(imgMert1, (faceLocationMert[3], faceLocationMert[0]), (faceLocationMert[1], faceLocationMert[2]), (255,0,255), 2)

faceLocationMert2 = face_recognition.face_locations(imgMert2)[0]
encodeMert2 = face_recognition.face_encodings(imgMert2)[0]
cv2.rectangle(imgMert2, (faceLocationMert2[3], faceLocationMert2[0]), (faceLocationMert2[1], faceLocationMert2[2]), (255,0,255), 2)

faceLocationIrfan1 = face_recognition.face_locations(imgIrfan1)[0]
encodeIrfan1 = face_recognition.face_encodings(imgIrfan1)[0]
cv2.rectangle(imgIrfan1, (faceLocationIrfan1[3], faceLocationIrfan1[0]), (faceLocationIrfan1[1], faceLocationIrfan1[2]), (255,0,255), 2)

faceLocationIrfan2 = face_recognition.face_locations(imgIrfan2)[0]
encodeIrfan2 = face_recognition.face_encodings(imgIrfan2)[0]
cv2.rectangle(imgIrfan2, (faceLocationIrfan2[3], faceLocationIrfan2[0]), (faceLocationIrfan2[1], faceLocationIrfan2[2]), (255,0,255), 2)

results = face_recognition.compare_faces([encodeBurakKimlik], encodeBurakEhliyet)
faceDistance = face_recognition.face_distance([encodeBurakKimlik], encodeBurakEhliyet)
print(results, faceDistance)



# cv2.imshow("Elon Musk", imgElon)
# cv2.imshow("Elon Musk Test", imgElonTest)
# cv2.imshow("Bill Gates", imgBillGates)
# cv2.imshow("Burak1", imgBurak)
# cv2.imshow("Burak2", imgBurak2)
# cv2.imshow("Burak5", imgBurak5)
# cv2.imshow("Emre", imgEmre)
# cv2.imshow("Ihsan", imgIhsan)
# cv2.imshow("Emre2", imgEmre2)
# cv2.imshow("Emre3", imgEmre3)
# cv2.imshow("Burak Kimlik", imgBurakKimlik)
# cv2.waitKey(0)
