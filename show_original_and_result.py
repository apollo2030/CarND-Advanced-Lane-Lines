import matplotlib.pyplot as plt
import cv2

def show_original_and_result(image, result, cmap_result = 'viridis', result_type='BGR'):
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
    f.tight_layout()
    img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    ax1.imshow(img)
    ax1.set_title('Original Image', fontsize=40)
    
    if result_type == 'BGR':
        res = cv2.cvtColor(result,cv2.COLOR_BGR2RGB)
        ax2.imshow(res, cmap = cmap_result)
    else:
        ax2.imshow(result, cmap = cmap_result)
    ax2.set_title('Pipeline Result', fontsize=40)
    plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)