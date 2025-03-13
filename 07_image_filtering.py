# 07_image_filtering
"""
FILTERING 

    Laplacian filtering: Uses a kernel designed to detect edges by approximating the second derivatives. The values are not equal — they include positive, negative, and zero values 
                        (e.g., a typical kernel is [[0, 1, 0], [1, -4, 1], [0, 1, 0]]).
    Gaussian filtering: Uses a kernel based on a Gaussian function, where the center has the highest weight, and values decrease as you move away from the center.
                        The values are not equal.
    Box filtering: Applies a kernel where all values are equal — typically all 1/N, where N is the number of elements in the kernel (e.g., a 3x3 kernel would have all values as 1/9).
                        This performs simple averaging over the kernel area.
    Bilateral Filter: an advanced smoothing filter that helps reduce noise while keeping edges sharp — which regular Gaussian blurring can’t do as effectively. 
                        It is widely used for denoising or cartoonification.
"""
import cv2
import sys
import numpy

PREVIEW  = 0  # Preview Mode
BLUR     = 1  # Blurring Filter, usually applied to a noisy image to smoothen; act as a preprocessing step for feature extraction
FEATURES = 2  # Corner Feature Detector
CANNY    = 3  # Canny Edge Detector
BILATERAL = 4 # bilateral

# Corner Feature Detector param
feature_params = dict(maxCorners=500, 
                      qualityLevel=0.2,         # minimum quality of the image corners, the corner feature with the highest value is multiplied by this parameter
                      minDistance=15,           # minimum distance between adjacent corners
                      blockSize=9)              # size of the pixel neighborhood
s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

image_filter = PREVIEW
alive = True

win_name = "Camera Filters"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
result = None

source = cv2.VideoCapture(s)

while alive:
    has_frame, frame = source.read()
    if not has_frame:
        break

    frame = cv2.flip(frame, 1)

    if image_filter == PREVIEW:
        result = frame
    elif image_filter == CANNY:
        result = cv2.Canny(frame, 120, 150)
    elif image_filter == BLUR:
        result = cv2.blur(frame, (13, 13))
    elif image_filter == BILATERAL:
        result = cv2.bilateralFilter(frame, d=9, sigmaColor=75, sigmaSpace=75)
    elif image_filter == FEATURES:
        result = frame
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)     # computes the corner features
        if corners is not None:
            for x, y in numpy.float32(corners).reshape(-1, 2):              # annotate detected corners with circles
                cv2.circle(result, (int(x),int(y)), 10, (0, 255, 0), 1)

    cv2.imshow(win_name, result)

    key = cv2.waitKey(1)
    if key == ord("Q") or key == ord("q") or key == 27:
        alive = False
    elif key == ord("C") or key == ord("c"):
        image_filter = CANNY
    elif key == ord("B") or key == ord("b"):
        image_filter = BLUR
    elif key == ord("L") or key == ord("l"):
        image_filter = BILATERAL
    elif key == ord("F") or key == ord("f"):
        image_filter = FEATURES
    elif key == ord("P") or key == ord("p"):
        image_filter = PREVIEW

source.release()
cv2.destroyWindow(win_name)