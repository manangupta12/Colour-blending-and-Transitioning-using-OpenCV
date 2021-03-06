import cv2
import numpy as np
import time

imgpath1="4.2.01.tiff"
imgpath2="4.2.07.tiff"

img1=cv2.imread(imgpath1,1)
img2=cv2.imread(imgpath2,1)

for i in np.linspace(0, 1, 200):
    alpha=i
    beta=1-alpha
    out=cv2.addWeighted(img1, alpha, img2, beta, 0)
    cv2.imshow("Transition",out)
    time.sleep(0.01)
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()
