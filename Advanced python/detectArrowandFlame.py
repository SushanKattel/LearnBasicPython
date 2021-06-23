import cv2
import image_slicer
import numpy as np

def slice_image(filepath):
    image_slicer.slice(filepath, 2)


def check_pixel(filepath):
    img = cv2.imread(filepath)
    boundaries = [([0, 0, 0], [53, 53, 53])]
    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(img, lower, upper)

    tot_pixel = mask.size
    black_pixel = np.count_nonzero(mask)
    percentage = round(black_pixel * 100 / tot_pixel, 2)
    return percentage


img_name = "samplefire.jpg"
a = img_name.split('.')[0]

identify = check_pixel(img_name)
if (identify > 23):
    print("Flame detected")

else:
    slice_image(img_name)
    parta = check_pixel(a + "_01_01.png")
    partb = check_pixel(a + "_01_02.png")
    if (parta > partb):
        print("Left Arrow Detected")
    elif (partb > parta):
        print("Right Arrow Detected")

