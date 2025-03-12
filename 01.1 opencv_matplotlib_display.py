"""
Description: The code below shows a demonstration of loading, displaying, and controlling images using two popular Python libraries: OpenCV (cv2) and Matplotlib (plt). Let’s summarize what it does overall:
    Imports and Image Loading
    It imports OpenCV and Matplotlib, then loads two images (checkboard_color.png and coca-cola-logo.png) using cv2.imread().

    Image Display with Matplotlib
    It displays one image using Matplotlib's plt.imshow(). However, OpenCV loads images in BGR format (Blue-Green-Red), so the colors may appear incorrect unless converted to RGB.

    OpenCV Window Handling
    It creates named windows and displays the images using OpenCV’s cv2.imshow(). Several techniques are shown:
        Timed display (cv2.waitKey(8000)): Show the image for 8 seconds.
        Wait until a key is pressed (cv2.waitKey(0)): Keeps the window open until you press any key.
        Continuous display in a loop: The last window runs in a loop and checks for the 'q' key to exit.

    Window Cleanup
    It cleans up windows properly using cv2.destroyWindow() or cv2.destroyAllWindows(), though there’s a small typo (destroyAlllWindows).

🎯 What this code demonstrates:

    Image loading and displaying with two libraries (OpenCV & Matplotlib)
    Different ways to handle user input and window behavior
    Keyboard interaction with OpenCV (like exiting with 'q')
    Basic loop control for live displays
"""
import cv2
import matplotlib.pyplot as plt

# Load images
cb_img = cv2.imread("checkboard_color.png")
coke_img = cv2.imread("coca-cola-logo.png")

# Use matplotlib imshow()
plt.imshow(cb_img)
plt.title("matplotlib_imshow")
plt.show()

# Use OpenCV imshow()
window1 = cv2.namedWindow("w1")
cv2.imshow(window1, cb_img) 	# OpenCV reads in BGR format
cv2.waitKey(8000)  				# Display for 8 sec
cv2.destroyWindow(window1)  	# Close OpenCV windows

# Use OpenCV imshow()
window2 = cv2.namedWindow("w2")
cv2.imshow(window2, coke_img)
cv2.waitKey(8000)
cv2.destroyWindow(window2)

# Use OpenCV imshow(), display until any key is pressed
window3 = cv2.namedWindow("w3")
cv2.imshow(window3, cb_img)
cv2.waitKey(0)  				#  wait until any key is pressed
cv2.destroyWindow(window3)

window4 = cv2.namedWindow("w4")

Alive = True
while Alive:
	# Use OpenCV imshow(), display unitl 'q' key is pressed
	cv2.imshow(window4, cb_img)
	keypress = cv2.waitKey(1)  				#  wait until any key is pressed
	if keypress == ord('q'):
		Alive = False

cv2.destroyWindow(window4)

cv2.destroyAlllWindows()
stop = 1
