import cv2

imgpath = r"C:\Users\zh99\Desktop\database\VOC2007\JPEGImages\trainval_seq2_0008.jpg"
box = [679, 567, 695, 583]

def draw_box(img, box):
    """

    :param imgpath: the path of the img
    :param box: [xmin, ymin, xmax, ymax]
    :return:
    """

    img = cv2.imread(imgpath)
    cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 1) #坐标必须是int
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    draw_box(imgpath, box)