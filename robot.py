# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:55:11 2019

@author: Raptor3200
"""

import wpilib, ctre

class MyRobot(wpilib.TimedRobot):
    
    def robotInit(self):
        self.motor = ctre.WPI_TalonSRX(0)

    def autonomousInit(self):
        self.motor.set(1)

if __name__ == "__main__":
    wpilib.run(MyRobot)