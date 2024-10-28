import cv2
from constants import VIDEO, IMAGE

#Load the cascade classifier
facecascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
if facecascade.empty():
   print("Error: Unable to load the cascade classifier!")
def detect_faces_image(image_path):
    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(img_gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        resized_img = cv2.resize(img, (800, 600))
    
    cv2.imshow("Detected Faces", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    if IMAGE:
        image_path=r"img.jpg"
        detect_faces_image(image_path)

    if VIDEO:
        cap=cv2.VideoCapture(0)
        cap.set(3,640)  #width
        cap.set(4,480)  #height

        while True:
            sucess,img = cap.read()
            img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            face=facecascade.detectMultiScale(img_gray, 1.1,4)

            for (x,y,w,h) in face:
                cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),2)
            
            cv2.imshow("Face",img)    

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()