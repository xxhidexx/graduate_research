import cv2
import time

def record_from_two_cameras(camera0_index=0, camera1_index=1, output0='output0.mp4', output1='output1.mp4', wait_time=5, record_duration=10):
    # Open the video capture streams for both cameras
    cap0 = cv2.VideoCapture(camera0_index)
    cap1 = cv2.VideoCapture(camera1_index)

    if not cap0.isOpened():
        print("Camera 0 could not be opened.")
        return
    if not cap1.isOpened():
        print("Camera 1 could not be opened.")
        return

    # Get the frame size and frame rate from the cameras
    frame_width0 = int(cap0.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height0 = int(cap0.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps0 = cap0.get(cv2.CAP_PROP_FPS)
    
    frame_width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps1 = cap1.get(cv2.CAP_PROP_FPS)

    print(f"camera 0 fps: {fps0}")
    print(f"camera 1 fps: {fps1}")

    # Use the obtained frame rates; if a camera doesn't return a valid FPS, set a default value
    fps0 = fps0 if fps0 > 5 else 10.0
    fps1 = fps1 if fps1 > 5 else 10.0

    # Define the codec and create VideoWriter objects
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out0 = cv2.VideoWriter(output0, fourcc, fps0, (frame_width0, frame_height0), True)
    out1 = cv2.VideoWriter(output1, fourcc, fps1, (frame_width1, frame_height1), True)

    print(f"Waiting for {wait_time} seconds before starting the recording...")
    time.sleep(wait_time)

    print("Starting recording...")

    start_time = time.time()
    while True:
        ret0, frame0 = cap0.read()
        ret1, frame1 = cap1.read()

        if not ret0 or not ret1:
            print("Could not capture frame.")
            break

        # Display the resulting frames
        cv2.imshow('Camera 0', frame0)
        cv2.imshow('Camera 1', frame1)

        # Write the frames to the video files
        out0.write(frame0)
        out1.write(frame1)

        # Record for the specified duration
        if time.time() - start_time > record_duration:
            break

        # Break the loop early if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the resources
    cap0.release()
    cap1.release()
    out0.release()
    out1.release()
    cv2.destroyAllWindows()

    print("Recording finished and files saved.")

# Call the function with desired settings
record_from_two_cameras()