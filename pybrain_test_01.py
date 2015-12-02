from pybrain.tools.shortcuts import buildNetwork
import rospy
net = buildNetwork(2, 3, 1)
print(net)