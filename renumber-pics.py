import cv2
import glob
images = glob.glob("img/hpt/*.jpg")
images.sort()
counter = 0
for image_name in images:
    if "thumbnail" in image_name:
        continue
    image = cv2.imread(image_name)
    if counter < 10:
        cv2.imwrite('img/hpt/0{}.jpg'.format(counter), image)
    else:
        cv2.imwrite('img/hpt/{}.jpg'.format(counter), image)
    counter = counter + 1
