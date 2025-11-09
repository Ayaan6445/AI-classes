import cv2
cap = cv2.VideoCapture(0)
mode = 'normal'
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if mode == 'gray':
        processed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif mode == 'blur':
        processed = cv2.GaussianBlur(frame, (15, 15), 0)
    elif mode == 'edge':
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        processed = cv2.Canny(gray, 100, 200)
    elif mode == 'red':
        processed = frame.copy()
        processed[:, :, 0] = 0
        processed[:, :, 1] = 0
    elif mode == 'green':
        processed = frame.copy()
        processed[:, :, 0] = 0
        processed[:, :, 2] = 0
    elif mode == 'blue':
        processed = frame.copy()
        processed[:, :, 1] = 0
        processed[:, :, 2] = 0
    else:
        processed = frame
    cv2.putText(processed, f"Mode: {mode.upper()}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Real-Time Image Processing', processed)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('g'):
        mode = 'gray'
    elif key == ord('b'):
        mode = 'blur'
    elif key == ord('e'):
        mode = 'edge'
    elif key == ord('r'):
        mode = 'red'
    elif key == ord('n'):
        mode = 'normal'
    elif key == ord('v'):
        mode = 'green'
    elif key == ord('l'):
        mode = 'blue'
cap.release()
cv2.destroyAllWindows()