import numpy as np
import cv2
import matplotlib.image as mpimg
import pickle
from show_original_and_result import *

def get_perspective_points(
    mtx, 
    dist, 
    distace_from_center = 1.9, # distance from the center of the lines 
    distance_meters = 30.0, # distance in the road ahead
    tvec_x_meters = 0, # translation on x axis of the camera
    tvec_y_meters = 1.3, # traslation on y axis (heigh above ground) of the camera
    tvec_z_meters = 4.7, # translation on z axis of the camera
):
    scale = 4.54 #units per meter
    zerorvecs = np.zeros((1,3))
    zerorvecs[0][1] = -.026
    zerorvecs[0][0] = -.03

    tvec = np.array([[tvec_x_meters], [tvec_y_meters], [tvec_z_meters]])*scale

    left_meters = distace_from_center
    right_meters = -distace_from_center

    pos_x_left = left_meters * scale
    pos_x_right = right_meters * scale
    distance = distance_meters * scale

    objectPoints = np.array([
        [pos_x_left, 0, distance], 
        [pos_x_left, 0, 0],
        [pos_x_right, 0, distance], 
        [pos_x_right, 0, 0]], 
        dtype=float)
    
    imgpts, jac = cv2.projectPoints(objectPoints, zerorvecs, tvec, mtx, dist)
    imgpts = np.int32(imgpts).reshape(-1,2)
    return imgpts

def get_perspective_points_test_bed(
    dfc = 1.9,
    dm = 30,
    tvec_x_meters = 0.0, 
    tvec_y_meters = 1.3, 
    tvec_z_meters = 4.7,
    ):
    
    tmp = mpimg.imread('output_images/undist_straight_lines2.jpg')
    camera_data = pickle.load( open( "camera_cal/distortion_matrix_pickle.p", "rb" ) )
    
    imgpts = get_perspective_points(camera_data['mtx'], camera_data['dist'], dfc, dm, tvec_x_meters, tvec_y_meters, tvec_z_meters)
    print(imgpts)
    cv2.line(tmp, tuple(imgpts[0]), tuple(imgpts[1]),[255,0,0],4)  #BGR
    cv2.line(tmp, tuple(imgpts[1]), tuple(imgpts[3]),[0,255,0],4)  #BGR
    cv2.line(tmp, tuple(imgpts[2]), tuple(imgpts[3]),[255,0,0],4)  #BGR
    cv2.line(tmp, tuple(imgpts[2]), tuple(imgpts[0]),[0,0,255],4)  #BGR

    show_original_and_result(tmp, tmp,'gray')

def get_dest_perspective_points(imgshape, src):
    rb=src[1]
    lb=src[3]
    height = imgshape[0]
    
    dest = np.float32([
        [rb[0], 0], 
        [rb[0], height], 
        [lb[0], height], 
        [lb[0], 0]])
    
    return dest


    