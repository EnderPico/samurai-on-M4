import cv2

def extract_first_frame(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return None

    # Read the first frame
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Error: Could not read the first frame.")
        return None

    return frame

def draw_rectangle(event, x, y, flags, param):
    global top_left, bottom_right, drawing, frame

    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Mouse Down at: ({x}, {y})")
        top_left = (x, y)
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        temp_frame = frame.copy()
        cv2.rectangle(temp_frame, top_left, (x, y), (0, 255, 0), 2)
        cv2.imshow("Draw Bounding Box", temp_frame)

    elif event == cv2.EVENT_LBUTTONUP:
        print(f"Mouse Up at: ({x}, {y})")
        bottom_right = (x, y)
        drawing = False
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
        print(f"Bounding Box: {top_left}, {bottom_right}")
        cv2.imshow("Draw Bounding Box", frame)

# File path to the video
video_path = input("Enter the path to your video file: ")

# Extract the first frame from the video
frame = extract_first_frame(video_path)
if frame is None:
    exit()

# Initialize variables
top_left, bottom_right, drawing = (0, 0), (0, 0), False

# Display the frame and set the mouse callback
cv2.imshow("Draw Bounding Box", frame)
cv2.setMouseCallback("Draw Bounding Box", draw_rectangle)

cv2.waitKey(0)
cv2.destroyAllWindows()