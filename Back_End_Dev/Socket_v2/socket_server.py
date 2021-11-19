import socket, cv2, pickle, struct, imutils, random
import numpy as np


#Server will never stop
#Don't close the server
#Only open/close the client



def stream():
    # Socket Create
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host_name  = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print('HOST IP:',host_ip)
    port = 9999
    socket_address = (host_ip,port)
    
    # Socket Bind
    server_socket.bind(socket_address)
    
    # Socket Listen
    server_socket.listen(5)
    print("LISTENING AT:",socket_address)
    
    
    
    
    # Socket Accept
    while True:
        try:
         	client_socket,addr = server_socket.accept()
         	print('GOT CONNECTION FROM:',addr)
         	if client_socket:
                  vid = cv2.VideoCapture(0)
                 
                  while(vid.isOpened()):
                      img,frame = vid.read()
                      frame = imutils.resize(frame,width=320)
                      a = pickle.dumps(frame)
                      message = struct.pack("Q",len(a))+a
                      client_socket.sendall(message)
                     
                      cv2.imshow('TRANSMITTING VIDEO',frame)
                      key = cv2.waitKey(1) & 0xFF
                      if key ==ord('q'):
                          client_socket.close()
                      print("test")

        except:
            vid.release()
            cv2.destroyAllWindows()
            client_socket.close()
    
    
    

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





def object_detect():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host_name  = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print('HOST IP:',host_ip)
    port = 9999
    socket_address = (host_ip,port)
    
    # Socket Bind
    server_socket.bind(socket_address)
    
    # Socket Listen
    server_socket.listen(5)
    print("LISTENING AT:",socket_address)
    
    
    threshold = 0.5
    NMSthreshold = 0.4
    net = cv2.dnn.readNet("yolo_weight.weights", "yolo_config.cfg")
    classes = open("MS_coco.names", "r").read().split("\n")
    layers = net.getLayerNames()
    layer_out = [layers[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    color_bag = color_generator()
    
    

    
    while True:
        try:
            client_socket,addr = server_socket.accept()
            print('GOT CONNECTION FROM:',addr)
            if client_socket:
                cap = cv2.VideoCapture(0)
                
                while (cap.isOpened()):
                    
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
            
                    
                    img = imutils.resize(img,width=320)
                    a = pickle.dumps(img)
                    message = struct.pack("Q",len(a))+a
                    client_socket.sendall(message)
                   
                    cv2.imshow('TRANSMITTING VIDEO',img)
                    key = cv2.waitKey(1) & 0xFF
                    if key ==ord('q'):
                        client_socket.close()
                    print("test")

        
        except:
            cap.release()
            cv2.destroyAllWindows()
            client_socket.close()   



class color:

    low = None
    up = None
    
    def red():
        color.low = np.array([100, 0, 0])
        color.up = np.array([255, 80, 80])
    
    def blue():
        print("Code here")
        
    def green():
        print("Code here")
    
    def white():
        print("Code here")
    
    def black():
        print("code here")
    
    def manual():
        print("Code here")
        





def color_detection():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host_name  = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print('HOST IP:',host_ip)
    port = 9999
    socket_address = (host_ip,port)
    
    # Socket Bind
    server_socket.bind(socket_address)
    
    # Socket Listen
    server_socket.listen(5)
    print("LISTENING AT:",socket_address)
    
    
    # Socket Accept
    while True:
        try:
         	client_socket,addr = server_socket.accept()
         	print('GOT CONNECTION FROM:',addr)
         	if client_socket:
                  vid = cv2.VideoCapture(0)
                 
                  while(vid.isOpened()):
                      img,frame = vid.read()
                      
                      
                      rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
                      #define the colour profiles
                      color.red()
                        
                      #Create a mask of your preferred colour
                      mask = cv2.inRange (rgb, color.low, color.up)
                      #looks at the mask and selected area. Then finds the extreme contours
                      redcnt = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
                        
                      #if there is some red in other words, more than 0,
                      #this block executes
                      if len(redcnt)>0:
                            red_area = max(redcnt, key=cv2.contourArea)
                            (xg,yg,wg,hg) = cv2.boundingRect(red_area)
                            cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)
                            
                      frame = imutils.resize(frame,width=320)
                      a = pickle.dumps(frame)
                      message = struct.pack("Q",len(a))+a
                      client_socket.sendall(message)
                     
                      cv2.imshow('TRANSMITTING VIDEO',frame)
                      key = cv2.waitKey(1) & 0xFF
                      if key ==ord('q'):
                          client_socket.close()
                      print("test")

        except:
            vid.release()
            cv2.destroyAllWindows()
            client_socket.close()
    
    
    
    
    
s = socket.socket()

s.bind(("192.168.1.12", 9999)) #Change to your server IP
s.listen(3)

print("waiting for connection")

while True:
    c, address = s.accept()
    print("Connected with", address)
    
    signal = c.recv(1024).decode()
    print(signal,type(signal))
    
    if signal == "1":
        s.close()
        stream()
    elif signal == "2":
        s.close()
        object_detect()
    elif signal == "3":
        s.close()
        color_detection()
    
    c.close()
