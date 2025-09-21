import cv2
image = cv2.imread(r"C:\Users\Ashish\OneDrive\Desktop\Python\pandas\Little_Krishna.jpg")
if image is None:
    print("image not found")
else:
    print("image loaded")    
cv2.imshow("KRISHNA ",image)
cv2.waitKey(0)
cv2.destroyAllWindows()