import cv2

# print(cv2.__version__)

cap = cv2.VideoCapture('E:\\python_project\\sss_0\\ks_076.mp4')

#動画のプロパティを取得
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if (cap.isOpened()== False):  
  print("ビデオファイルを開くとエラーが発生しました") 

while(cap.isOpened()):

    ret, frame = cap.read()
    if ret == True:
        
        frame = cv2.resize(frame, dsize=(int(width/4), int(height/4)))
        cv2.imshow("Video", frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
    
    else:
        break

cap.release()

cv2.destroyAllWindows()