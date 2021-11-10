import cv2
import numpy as np
import random


def color_generator():
    color_array = []

    for i in range(20):
        R_random = random.randint(0,255)
        G_random = random.randint(0,255)
        B_random = random.randint(0,255)
        temp = []
        temp.append(R_random)
        temp.append(G_random)
        temp.append(B_random)
        color_array.append(temp)
    
    return color_array
    
threshold = 0.5
NMSthreshold = 0.4
net = cv2.dnn.readNet("yolo_weight.weights", "yolo_config.cfg")
classes = open("MS_coco.names", "r").read().split("\n")
layers = net.getLayerNames()
layer_out = [layers[i[0] - 1] for i in net.getUnconnectedOutLayers()]
color_bag = color_generator()


cap = cv2.VideoCapture(0)

while True:
    void,img = cap.read()
    height, width, channels = img.shape
    bin_data = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(bin_data)
    all_var = net.forward(layer_out)
    class_ids, confidences, boxes = [], [], []


    for var in all_var:
        for obj_detect in var:
            point = obj_detect[5:]
            class_id = np.argmax(point)
            confidence = point[class_id]
            if confidence > 0.5:
                center_xAxis = int(obj_detect[0] * width)
                center_yAxis = int(obj_detect[1] * height)
                w = int(obj_detect[2] * width)
                h = int(obj_detect[3] * height)
    

                x = int(center_xAxis - w / 2)
                y = int(center_yAxis - h / 2)
    
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, threshold, NMSthreshold)

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = color_bag[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), cv2.FONT_ITALIC, 1, color, 3)
    
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)

cv2.destroyAllWindows()
