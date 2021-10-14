# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from math import *


class location:
    def __init__(self,k,w,theta,H): #k为无人机俯仰角、w为无人机偏航角、theta为无人机横滚角、H为无人机与目标高度差、f为焦距
        self.a1=cos(k)*cos(w)-sin(k)*sin(theta)*sin(w)
        self.a2=-cos(k)*sin(w)-sin(k)*sin(theta)*cos(w)
        self.a3=-sin(k)*cos(theta)
        self.b1=cos(theta)*sin(w)
        self.b2=cos(theta)*cos(w)
        self.b3=-sin(theta)
        self.c1=sin(k)*cos(w)+cos(k)*sin(theta)*sin(w)
        self.c2=-sin(k)*sin(w)+cos(k)*sin(theta)*cos(w)
        self.c3=cos(k)*cos(theta)
        self.H=H
        self.f_dx=636.06
        self.f_dy = 640.82
        self.u_0=306.8
        self.v_0 = 240.6


    def loation_target(self,u,v,X_u,Y_u):#像素坐标系下目标的坐标u,v,无人机当前坐标X_u,Y_u
        x_f=(u-self.u_0)/self.f_dx
        y_f = (v - self.v_0) / self.f_dy
        X=X_u-self.H*(self.a1*x_f-self.a2+self.a3*y_f)/(self.b1*x_f-self.b2+self.b3*y_f)#公式上下同时除以f
        Y=Y_u-self.H*(self.c1*x_f-self.c2+self.c3*y_f)/(self.b1*x_f-self.b2+self.b3*y_f)
        return X,Y

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A=location(0,0,0,0.4)
    X,Y=A.loation_target(428,69,0,0)
    print(X,Y)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
