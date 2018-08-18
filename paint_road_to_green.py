import numpy as np
import cv2

def paint_road_to_green(left_fitx, right_fitx, ploty, out_img):
    pts_left = np.array([np.transpose(np.vstack([left_fitx, ploty]))])
    pts_left1 = np.array([np.flipud(np.transpose(np.vstack([left_fitx + 128, ploty])))])
    pts_left2 = np.array([np.transpose(np.vstack([left_fitx + 256, ploty]))])    
    pts_left3 = np.array([np.flipud(np.transpose(np.vstack([left_fitx + 384, ploty])))])
    pts_left4 = np.array([np.transpose(np.vstack([left_fitx + 512, ploty]))])
    pts_left5 = np.array([np.flipud(np.transpose(np.vstack([left_fitx + 640, ploty])))])
    pts_left6 = np.array([np.transpose(np.vstack([left_fitx + 768, ploty]))])
    pts_right = np.array([np.flipud(np.transpose(np.vstack([right_fitx, ploty])))])

    pts = np.hstack((pts_left, pts_left1))        
    pts1 = np.hstack((pts_left1, pts_left2))        
    pts2 = np.hstack((pts_left2, pts_left3))        
    pts3 = np.hstack((pts_left3, pts_left4))        
    pts4 = np.hstack((pts_left4, pts_left5))        
    pts5 = np.hstack((pts_left5, pts_left6))        
    pts6 = np.hstack((pts_left6, pts_right))        

    cv2.fillPoly(out_img, np.int_([pts]), (75,25, 230))
    cv2.fillPoly(out_img, np.int_([pts1]), (48,130, 245))
    cv2.fillPoly(out_img, np.int_([pts2]), (25,255, 255))
    cv2.fillPoly(out_img, np.int_([pts3]), (75,180, 60))
    cv2.fillPoly(out_img, np.int_([pts4]), (200,130, 0))
    cv2.fillPoly(out_img, np.int_([pts5]), (230,50, 240))
    cv2.fillPoly(out_img, np.int_([pts6]), (180,30, 145))

    return out_img
