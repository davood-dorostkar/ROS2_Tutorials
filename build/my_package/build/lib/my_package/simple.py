##### FIRST FUNCTION #####

# import rclpy
# from rclpy.node import Node


# def main(args=None):
#     # initialize the ROS communication
#     rclpy.init(args=args)
#     print("executed once")
#     # shutdown the ROS communication
#     rclpy.shutdown()


# if __name__ == '__main__':
#     main()


##### SECOND FUNCTION #####

import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self):
        # call super() in the constructor in order to initialize the Node object
        # the parameter we pass is the node name
        super().__init__("publisher_node")
        # create a timer sending two parameters:
        # - the duration between 2 callbacks (0.2 seeconds)
        # - the timer function (timer_callback)
        self.create_timer(3, self.timer_callback)

    def timer_callback(self):
        # print a ROS2 log on the terminal with a great message!
        self.get_logger().info("Hi! I am alive... ")


def main(args=None):
    # initialize the ROS communication
    rclpy.init(args=args)
    # declare the node constructor
    node = MyNode()
    # pause the program execution, waits for a request to kill the node (ctrl+c)
    rclpy.spin(node)
    # shutdown the ROS communication
    rclpy.shutdown()


if __name__ == "__main__":
    main()
