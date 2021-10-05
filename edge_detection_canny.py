# Usage
# python edge_detection_canny --image "image file"

# import the necessary packages
import argparse
import cv2 as cv

# construt an argparser to parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image", type=str)
args = vars(ap.parse_args())

# load the image and convert it to gray scale and display it on the screen
# blurr it slightly using
image = cv.imread(args["image"])
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5, 5), 0)
cv.imshow("gray", image)
cv.imshow("Blurred", blurred)

# compute a wide, mid and tight threshold for the edges
# using the canny edge detector
wide = cv.Canny(blurred, 10, 200)
mid = cv.Canny(blurred, 30, 150)
tight = cv.Canny(blurred, 240, 250)

# show the output Canny edge maps
cv.imshow("Wide", wide)
cv.imshow("Mid", mid)
cv.imshow("tight", tight)
cv.waitKey(0)