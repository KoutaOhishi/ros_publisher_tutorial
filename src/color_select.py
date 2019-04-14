#! /usr/bin/env python
# coding:utf-8
import sys
import time
import rospy
from std_msgs.msg import Bool, String

console = """
Color List.
1. Black
2. Red
3. Green
4. Yellow
5. Blue
6. Purple
7. Cyan
8. White
9. exit
---
"""


def main():
    color_publisher = rospy.Publisher("/publisher_tutorial/color", String, queue_size=1)

    while not rospy.is_shutdown():
        try:
            print console
            input_number = input("Please input number -> ")

            if input_number == 1:
                color_publisher.publish("Black")

            elif input_number == 2:
                color_publisher.publish("Red")

            elif input_number == 3:
                color_publisher.publish("Green")

            elif input_number == 4:
                color_publisher.publish("Yellow")

            elif input_number == 5:
                color_publisher.publish("Blue")

            elif input_number == 6:
                color_publisher.publish("Purple")

            elif input_number == 7:
                color_publisher.publish("Cyan")

            elif input_number == 8:
                color_publisher.publish("White")

            elif input_number == 9:
                break

            else:
                pass

        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    rospy.init_node("color_select")
    main()
