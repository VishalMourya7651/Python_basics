import cv2
image=cv2.imread(r"C:\Users\Ashish\OneDrive\Pictures\f86faf7f-033f-41ae-8c20-3bc11fc03bc0.jpeg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
if image is not None:
   #  print("image fetch successful")
   #gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
   hi=0
else:
    print("error")
print("Press 0 to display image or 1 to save image")
a=int(input())
if a==0:
    cv2.imshow("assigment imagen show",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindow()
elif a==1:
    print("enter image name to save: ")
    s=str(input())
    cv2.imwrite(f"{s}.jpeg",gray)
