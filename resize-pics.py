import cv2
import glob
def resize(image):
    return cv2.resize(image, (350, 350))
images = glob.glob("img/hpt/*.jpg")
images.sort()
counter = 0
for image_name in images:
    if "thumbnail" in image_name:
        continue
    image = cv2.imread(image_name)
    resized = resize(image)
    if counter < 10:
        cv2.imwrite('img/hpt/350x350/0{}.jpg'.format(counter), resized)
    else:
        cv2.imwrite('img/hpt/350x350/{}.jpg'.format(counter), resized)
    counter = counter + 1