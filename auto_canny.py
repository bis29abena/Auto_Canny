# Usage
# python auto_canny --images images

# import necessary packages
import numpy as np
import argparse
import glob
import cv2 as cv


def auto_canny(image, sigma=0.33):
    # compute he median of the single channel pixel intensity
    v = np.median(image)

    # apply the automatic canny detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv.Canny(image, lower, upper)

    # return the edged image
    return edged, lower, upper


# construct an argparse to parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help="path to input file", type=str)
args = vars(ap.parse_args())

# loop over the images
for imagePath in glob.glob(args["images"] + "/*.png"):
    # load the image and converte it grayscale and blur it slightly
    image = cv.imread(imagePath)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)

    # use a wide threshold, tight a threshold
    # and our auto canny threshold detection
    wide = cv.Canny(blur, 10, 200)
    tight = cv.Canny(blur, 225, 250)
    auto, low, high = auto_canny(blur)
    print(f"For image {imagePath} threshold1: {low}, threshold2: {high}")

    # show all the images
    cv.imshow("original", image)
    cv.imshow("Edges", np.hstack([wide, tight, auto]))
    cv.waitKey(0)