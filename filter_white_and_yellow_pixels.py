# example taken from stack overflow to filter out pixel that are not yellow nor white
from show_original_and_result import *
import cv2

def filter_colors_hsv(img):
    """
    Convert image to HSV color space and suppress any colors
    outside of the defined color ranges
    """
    img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    yellow_dark = np.array([15, 127, 10], dtype=np.uint8)
    yellow_light = np.array([25, 255, 255], dtype=np.uint8)
    yellow_range = cv2.inRange(img, yellow_dark, yellow_light)

    white_dark = np.array([0, 0, 150], dtype=np.uint8)
    white_light = np.array([255, 30, 255], dtype=np.uint8)
    white_range = cv2.inRange(img, white_dark, white_light)
    yellows_or_whites = yellow_range | white_range
    img = cv2.bitwise_or(img, img, mask=yellows_or_whites)
    return img

img = cv2.imread('bad_original_frames/project_video_Moment4.jpg')
show_original_and_result(img, filter_colors_hsv(img))
