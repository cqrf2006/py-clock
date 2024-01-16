import turtle  
import time  
  
# 创建turtle对象  
clock = turtle.Turtle()  
clock.speed(0)  # 最快速度  
  
# 设置画布背景  
turtle.bgcolor("black")  
  
# 设置画笔颜色和宽度  
clock.color("white")  
clock.pensize(3)  
  
# 绘制时钟的外圈  
clock.circle(150)  
  
# 绘制时针、分针和秒针  
clock.color("blue")  # 时针颜色  
draw_hour_hand(30)  
  
clock.color("red")  # 分针颜色  
draw_minute_hand(180)  
  
clock.color("green")  # 秒针颜色  
draw_second_hand(360)  
  
# 隐藏turtle对象  
clock.hideturtle()  
  
# 开始更新时间并绘制指针  
while True:  
    update_time()  
    clock.clear()  
    draw_hour_hand(30)  
    draw_minute_hand(180)  
    draw_second_hand(360)  
    time.sleep(1)  # 等待1秒再更新时间  
  
def draw_hour_hand(angle):  
    clock.right(90)  # 初始方向朝上，向右旋转90度使其朝向右下方  
    clock.forward(75)  # 绘制时针长度为75个单位  
    clock.right(angle)  # 旋转到对应的小时位置  
    clock.forward(75)  # 继续向前绘制，完成时针的绘制  
    clock.left(360 - angle)  # 将角度调整回初始状态，准备下一次绘制  
  
def draw_minute_hand(angle):  
    clock.right(90)  # 初始方向朝上，向右旋转90度使其朝向右下方  
    clock.forward(120)  # 绘制分针长度为120个单位  
    clock.right(angle)  # 旋转到对应的分钟位置  
    clock.forward(120)  # 继续向前绘制，完成分针的绘制  
    clock.left(360 - angle)  # 将角度调整回初始状态，准备下一次绘制  
  
def draw_second_hand(angle):  
    clock.right(90)  # 初始方向朝上，向右旋转90度使其朝向右下方  
    clock.forward(150)  # 绘制秒针长度为150个单位，稍微长一点以便于区分时针和分针  
    clock.right(angle)  # 旋转到对应的秒位置  
    clock.forward(150)  # 继续向前绘制，完成秒针的绘制  
    clock.left(360 - angle)  # 将角度调整回初始状态，准备下一次绘制  
  
def update_time():  
    current_time = time.localtime()  # 获取当前时间的小时、分钟和秒数  
    hour = current_time.tm_hour % 12  # 取余数得到小时数，考虑了12小时制的情况  
    minute = current_time.tm_min % 60  # 取余数得到分钟数，考虑了分钟数小于60的情况  
    second = current_time.tm_sec % 60  # 取余数得到秒数，考虑了秒数小于60的情况  
    angle_hour = (hour * 30 + minute // 2) % 360  # 根据时间计算时针应该指向的角度（每小时30度）  
    angle_minute = (minute * 6) % 360  # 根据时间计算分针应该指向的角度（每分钟6度）  
    angle_second = (second * 6) % 360  # 根据时间计算秒针应该指向的角度（每秒6度）
