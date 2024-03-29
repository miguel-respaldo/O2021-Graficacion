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

    imagen_flip = cv.flip(imagen, 1)

    grises = cv.cvtColor(imagen_flip, cv.COLOR_BGR2GRAY)
    #  0 de Cabeza
    #  1 Espejo
    # -1 de Cabeza espejo

    cv.imshow("Camara", grises)
    cv.imshow("Camara Flip", imagen_flip)

    # Al oprimir ESC salimos del programa
    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()