import cv2
import numpy as np
import time
 
frameWith = 640
frameHeight = 480
cap = cv2.VideoCapture(0)  
##摄像头  0可以添加多个  代表调取摄像头资源，其中 0 代表电脑摄像头，1 代表外接摄像头
 
time.sleep(1)
 
cap.set(3, frameWith)  # 图像宽度
cap.set(4, frameHeight)  # 高度
cap.set(10, 150)  # 视频帧率

while True:
    _, img = cap.read()  # 一定要放在ture里面，不然视频动不了！！！
    # =============指定红色值的范围=============
    minRed = np.array([0,43,46])
    #minRed = np.array([0, 127, 128])  # 红色阈值下界
    maxRed = np.array([180, 255, 255])  # 红色阈值上界
    # =============指定蓝色色值的范围=============
    minBlue = np.array([90,55,0])
    maxBlue = np.array([130,255,149])
 
    # BGR -> HSV颜色空间
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 确定目标区域
    mask_red = cv2.inRange(img_hsv, minRed, maxRed)  # 过滤出红色部分，获得红色的掩膜
    result_red = cv2.bitwise_and(img, img, mask=mask_red)  # 输出掩膜部分  #第一个为输入图像，第二个为输出
    mask_blue = cv2.inRange(img_hsv, minBlue, maxBlue)  # 获得蓝色部分掩膜
    result_blue = cv2.bitwise_and(img, img, mask=mask_blue)  # 输出掩膜部分  #第一个为输入图像，第二个为输出
 
    # 查找轮廓
    contours1, hierarchy1 = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 轮廓检测 红
    contours2, hierarchy2 = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 轮廓检测 绿
 
    # 检测红桶
    for cnt in contours1:
        (x, y, w, h) = cv2.boundingRect(cnt)  # 该函数返回矩阵四个点
        if w * h < 20 * 20:  # 忽略20*20的框
            continue
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)  # 将检测到的颜色框起来
        cv2.putText(img, 'red_light', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        print('红中心坐标:', x + w / 2, y + h / 2)
 
 
    for cnt in contours2:
        area=cv2.contourArea(cnt)
        if area>600:
            (x, y, w, h) = cv2.boundingRect(cnt)  # 该函数返回矩阵四个点
            if w * h < 30 * 30:  # 忽略20*20的框
                continue
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)  # 将检测到的颜色框起来
            cv2.putText(img, 'blue_light', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            print('蓝中心坐标:', x + w / 2, y + h / 2)
 
 
    hstack=np.hstack([result_red,result_blue])
    cv2.imshow('result',hstack)
    # cv2.imshow('result1', result_red)
    # cv2.imshow('result2', result_blue)
 
    cv2.imshow('res', img)
 
    cv2.waitKey(1)
    #cv2.destroyAllWindows()
