import cv2

# Open default camera (0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot access camera")
    exit()

# print("📷 Press 's' to save photo")
# print("❌ Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    # Show live camera feed
    cv2.imshow("Camera - Press 's' to save", frame)

    key = cv2.waitKey(1) & 0xFF

    # Save photo
    if key == ord('s'):
        cv2.imwrite("captured_person.jpg", frame)
        print("✅ Photo saved as captured_person.jpg")
        break

    # Quit without saving
    elif key == ord('q'):
        print("❌ Quit without saving")
        break

cap.release()
cv2.destroyAllWindows()
