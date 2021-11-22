import cv2 as cv

camara = cv.VideoCapture(0)

detector = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

while True:
    # Leemos la imagen de l camara
    ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    grises = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)

    caras = detector.detectMultiScale(grises, 1.1, 4)

    for (x,y, w,h) in caras:
        cv.rectangle(imagen, (x,y), (x+w, y+h), (255,0,0), 2)

    cv.imshow("Camara", imagen)

    # Al oprimir ESC salimos del programa
    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()