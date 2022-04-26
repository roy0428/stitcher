import cv2
import sys
import numpy as np
from warpImages import warpImages

def stitchimg(img1, img2, i):
    orb = cv2.ORB_create(nfeatures =10000)
    keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher_create(cv2.NORM_HAMMING)
    matches = bf.knnMatch(descriptors1, descriptors2,k=2)

    all_matches = []
    for m, n in matches:
        all_matches.append(m)

    good = []
    for m, n in matches:
        if m.distance < 0.6 * n.distance:
            good.append(m)
        
    MIN_MATCH_COUNT = 4

    if len(good) >= MIN_MATCH_COUNT:
        # Convert keypoints to an argument for findHomography
        src_pts = np.float32([ keypoints1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
        dst_pts = np.float32([ keypoints2[m.trainIdx].pt for m in good]).reshape(-1,1,2)

        # Establish a homography
        M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    
        result = warpImages(img2, img1, M)  
        output = 'result-%d' % i + '.jpg'
        cv2.imwrite(output, result)

    else:
        print('failed')
        sys.exit(-1)

