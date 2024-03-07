import cv2 #importar a biblioteca OpenCV. caso n esteja instalada, usar 'pip install opencv-python' no terminal

detector_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #atribui;'ao do classifacador XML na variavel detector_face

webcam = cv2.VideoCapture(0) #'0' eh qual das cameras (dispositivos) esta a ser usada pelo programa, sendo 1 eh 0, 2 eh 1 e assim por diante...

while True:
#captura frame por frame

    ok, frame = webcam.read()
    imagem_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    deteccoes = detector_face.detectMultiScale(imagem_cinza, minSize=(100,100))

#DESENHAR O RETANGULO BODYING BOXES
    for (x, y, w, h) in deteccoes:
        print (w,h)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (120, 0, 50), 2)
    #RESUTLADO
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#libera memoria no final

webcam.release()
cv2.destroyAllWindows()