import cv2
import matplotlib.pyplot as plt
from skimage.feature import plot_matches


def plotMatches(im1,im2,matches,locs1,locs2):
    fig, ax = plt.subplots(nrows=1, ncols=1)
    im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    plt.axis('off')
    plot_matches(ax,im1,im2,locs1,locs2,matches,matches_color='r',only_matches=True)
    plt.show()
    return