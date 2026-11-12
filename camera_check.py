"""Check the laptop camera before adding gesture controls."""

import cv2


def main():
    camera = cv2.VideoCapture(0)
    try:
        if not camera.isOpened():
            print('Could not open the camera. Close other camera apps and check Windows camera permissions.')
            return

        print('Camera preview started. Press Q in the preview window to quit.')
        while True:
            success, frame = camera.read()
            if not success:
                print('Could not read a camera frame. Check that the camera is connected and available.')
                break

            frame = cv2.flip(frame, 1)
            cv2.putText(frame, 'Air Guitar | Press Q to quit', (20, 35),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.imshow('Air Guitar - Camera Check', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
