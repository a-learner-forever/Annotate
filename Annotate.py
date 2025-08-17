import cv2

# Step 1: Read an image
img = cv2.imread("input.jpg")   # make sure input.jpg exists in same folder

# Step 2: Draw a rectangle (x1,y1) to (x2,y2)
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 2)  # green rectangle

# Step 3: Draw a circle (center, radius)
cv2.circle(img, (300, 150), 50, (255, 0, 0), 2)  # blue circle

# Step 4: Draw a line (x1,y1) to (x2,y2)
cv2.line(img, (400, 50), (550, 200), (0, 0, 255), 2)  # red line

# Step 5: Add measurements (text)
cv2.putText(img, "Width: 150px", (50, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
cv2.putText(img, "Radius: 50px", (280, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
cv2.putText(img, "Length: 212px", (400, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

# Step 6: Save and Show result
cv2.imwrite("annotated.jpg", img)
cv2.imshow("Annotated Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
