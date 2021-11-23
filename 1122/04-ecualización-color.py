import cv2 as cv

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

while True:
    # Leemos la imagen de l camara
    ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    yuv = cv.cvtColor(imagen, cv.COLOR_BGR2YCrCb);
    canales = cv.split(yuv)
    cv.equalizeHist(canales[0], canales[0])
    cv.merge(canales, yuv)
    ecualizada = cv.cvtColor(yuv, cv.COLOR_YCR_CB2BGR)

    cv.imshow("Camara", imagen)
    cv.imshow("Camara Ecualizada", ecualizada)

    # Al oprimir ESC salimos del programa
    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()