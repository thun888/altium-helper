import cv2
import pandas as pd
import PIL.ImageGrab


# 导入图片
path = input("请输入图片路径:")
if path == "":
    img = PIL.ImageGrab.grabclipboard()
    img.save("temp.png","png")
    path= "temp.png"
img = cv2.imread(path)
# 建立空列表存放像素坐标
a =[]
b = []


def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    # 点击鼠标左键
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        a.append(x)
        b.append(y)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image", img)


cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.imshow("image", img)
cv2.waitKey(0)

# print(a[0],b[0])
if a == [] or b == []:
    print("没有数据")
    exit()

length = int(input("输入坐标内代表的长度:"))
method = input("输入所需比较坐标(x/y):")
if method == "x":
    pic = abs(a[0]-a[1])
    pic_a = abs(a[2]-a[3])
elif method == "y":
    pic = abs(b[0]-b[1])
    pic_a = abs(b[2]-b[3])
else:
    print("输入错误")
    exit()

#print("Pic:"+str(pic))
#print("Pic_a:"+str(pic_a))
raw = pic_a/pic*length
print("Raw:"+str(raw))

# if __name__ == '__main__':
