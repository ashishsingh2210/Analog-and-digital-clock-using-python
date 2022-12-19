# Import the modules
import cv2
import datetime
import math

#radius of the clock
RADIUS = 260

#Center point of the clock
CENTER = (300,300)

while True:    
    
    image = cv2.imread(r"F:\chandigarh university\1 semester\Advance python programming\assignment\clock_1.jpg")
    image = cv2.resize(image,(600,600))
    
    time_now = datetime.datetime.now().time()
    dateToday = datetime.date.today()
    hour = math.fmod(time_now.hour, 12)
    minute = time_now.minute
    second = time_now.second

    cv2.putText(image,"ashish", (265,450), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (32,165,218), 1, cv2.LINE_AA)
    cv2.rectangle(image,(380,315),(490,285),(252,252,252),-1)
    cv2.putText(image,str(int(hour))+':'+str(minute)+':'+str(second), (390,310), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(image,str(dateToday.day), (140,310), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(image,str(dateToday.strftime('%b')), (145,335), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0, 0, 0), 1, cv2.LINE_AA)
    
    second_angle = math.fmod(second * 6 + 270, 360)
    minute_angle = math.fmod(minute * 6 + 270, 360)
    hour_angle = math.fmod((hour*30) + (minute/2) + 270, 360)
    
    second_x = int(CENTER[0] + (RADIUS-10) * math.cos(second_angle * math.pi / 180))
    second_y = int(CENTER[1] + (RADIUS-10) * math.sin(second_angle * math.pi / 180))
    cv2.line(image, CENTER, (second_x, second_y), (0, 0, 0), 2)
    
    minute_x = int(CENTER[0] + (RADIUS-60) * math.cos(minute_angle * math.pi / 180))
    minute_y = int(CENTER[1] + (RADIUS-60) * math.sin(minute_angle * math.pi / 180))
    cv2.line(image, CENTER, (minute_x, minute_y), (0, 0, 0), 3)
    
    hour_x = int(CENTER[0] + (RADIUS-150) * math.cos(hour_angle * math.pi / 180))
    hour_y = int(CENTER[1] + (RADIUS-150) * math.sin(hour_angle * math.pi / 180))
    cv2.line(image, CENTER, (hour_x, hour_y), (0,0,0), 9)
    
    cv2.imshow('image',image)

    if(cv2.waitKey(1)==ord('q')):
        break

cv2.destroyAllWindows()