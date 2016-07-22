#!/usr/bin/python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#"L":y = 1/x
#横坐标x_l
x_l = np.arange(-12, -5.9, 0.1)
#纵坐标y_l
y_l = [1 / (x + 12.1) for x in x_l] # why not 12, to avoid divide by zero

#"O":x^2 + y^2 = 9
#横坐标x_o
x_o = np.arange(-6, 0.1, 0.1)
#纵坐标y_o
y_o_top = np.sqrt(9 - (x_o + 3) ** 2) + 3
y_o_bottom = -np.sqrt(9 - (x_o + 3) ** 2) + 3

#"V":y = 2|x|
#横坐标x_v
x_v = np.arange(0, 6.1, 0.1)
#纵坐标y_v
y_v = 2 * np.abs(x_v - 3)

#"E":x = -3|sin(y)|
#纵坐标y_e
y_e = np.arange(0, 2 * np.pi + 0.1, 0.1)
#横坐标x_e
x_e = -3 * np.abs(np.sin(y_e)) + 9

#Heart
#横坐标:x_heart
x_heart = np.arange(-2, 2, 0.0001)
#Heart top fraction:y = sqrt(1 - (|x| - 1) ^ 2)
y_heart_top = np.sqrt(1 - (np.abs(x_heart) - 1) ** 2) - 1
#Heart bottom fraction:y = arccos(1 - |x|) - pi
y_heart_bottom = np.arccos(1 - np.abs(x_heart)) - np.pi - 1

#画图  Plot
plt.plot(x_l, y_l)
plt.plot(x_o, y_o_top)
plt.plot(x_o, y_o_bottom)
plt.plot(x_v, y_v)
plt.plot(x_e, y_e)
plt.plot(x_heart, y_heart_top)
plt.plot(x_heart, y_heart_bottom)
plt.xlabel('x')
plt.ylabel('y')
plt.title('L O V E')
plt.legend(['L', 'O Top', 'O Bottom', 'V', 'E', 'Heart Top', 'Heart Bottom'])
plt.show()
