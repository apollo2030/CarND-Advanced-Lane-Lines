import itertools
import random
from itertools import starmap

def endpoints(rho, theta):
    a = np.cos(theta)
    b = np.sin(theta)
    x_0 = a * rho
    y_0 = b * rho
    x_1 = int(x_0 + 10000 * (-b))
    y_1 = int(y_0 + 10000 * (a))
    x_2 = int(x_0 - 10000 * (-b))
    y_2 = int(y_0 - 10000 * (a))

    return ((x_1, y_1), (x_2, y_2))

def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


# Find intersection point of two lines (not segments!)
def line_intersection(line1, line2):
    x_diff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    y_diff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    div = det(x_diff, y_diff)
    if div == 0:
        return None  # Lines don't cross

    d = (det(*line1), det(*line2))
    x = det(d, x_diff) / div
    y = det(d, y_diff) / div

    return x, y

# Find intersections between multiple lines (not line segments!)
def find_intersections(lines):
    intersections = []
    for i, line_1 in enumerate(lines):
        for line_2 in lines[i + 1:]:
            if not line_1 == line_2:
                intersection = line_intersection(line_1, line_2)
                if intersection:  # If lines cross, then add
                    intersections.append(intersection)

    return intersections

# Perform edge detection
def hough_transform(img):
    gaussian_blur = cv2.GaussianBlur(img,(5,5),0)
    edges = cv2.Canny(gaussian_blur, 50, 150, apertureSize=7)  # Canny edge detection
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)  # Hough line detection

    hough_lines = []
    # Lines are represented by rho, theta; converted to endpoint notation
    if lines is not None:
        for line in lines:
            hough_lines.extend(list(starmap(endpoints, line)))
    
    

    return hough_lines

# Given intersections, find the grid where most intersections occur and treat as vanishing point
def find_vanishing_point(img, intersections):
    # Image dimensions
    grid_size = min(img.shape[0], img.shape[1]) // 25
    image_height = img.shape[0]
    image_width = img.shape[1]

    # Grid dimensions
    grid_rows = (image_height // grid_size) + 1
    grid_columns = (image_width // grid_size) + 1

    # Current cell with most intersection points
    max_intersections = 0
    best_cell = (0.0, 0.0)

    for i in range(grid_columns):
        for j in range(grid_rows):
            cell_left = i * grid_size
            cell_right = (i + 1) * grid_size
            cell_bottom = j * grid_size
            cell_top = (j + 1) * grid_size
            cv2.rectangle(img, (cell_left, cell_bottom), (cell_right, cell_top), (0, 0, 255), 2)

            current_intersections = 0  # Number of intersections in the current cell
            for x, y in intersections:
                if cell_left < x < cell_right and cell_bottom < y < cell_top:
                    current_intersections += 1

            # Current cell has more intersections that previous cell (better)
            if current_intersections > max_intersections:
                max_intersections = current_intersections
                best_cell = ((cell_left + cell_right) / 2, (cell_bottom + cell_top) / 2)
                print("Best Cell:", best_cell)

    cv2.circle(img,(int(best_cell[0]), int(best_cell[1])),6,(0, 255, 0), 2)

    return best_cell

def get_vanishing_point(img):
    lines = hough_transform(img)
    intersections = find_intersections(lines)
    return find_vanishing_point(img, intersections)