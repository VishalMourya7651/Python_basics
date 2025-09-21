import cv2
image=cv2.imread(r"C:\Users\Ashish\OneDrive\Desktop\Python\pandas\Little_Krishna.jpg")

if image is not None:
    h,w,c=image.shape
    print(f"image loaded:\n height: {h} \n width: {w} \n chanel: {c}")#   Dimensions
else:
    print("failed to load image")    



#    GRAY COLOR CONVERSION
if image is not None:
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray scale image" ,gray)
    cv2.waitKey(0)
    cv2.destroyAllWindow()
