import math
import lib601.util as util
import lib601.sm as sm
import lib601.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
     def getNextValues(self,state,inp):
          return (state,io.Action(fvel=0.05,rvel=0.5))

mySM=MySMClass()
#mySM.name='

def plotSonar(sonarNum):
     robot.gfx.addDynamicPlotFunction(y=('sonar'+str(sonarNum),
                                         lambda:
                                         io.SensorInput().sonars[sonarNum]))

def setup():
     robot.gfx=gfx.RobotGraphics(drawSlimeTrail=False,
                                 sonarMonitor=False)
     robot.behavior=mySM

def brainStart():
     robot.behavior.start(traceTasks=robot.gfx.tasks())

def step():
     inp=io.SensorInput()
     robot.behavior.step(inp).execute()
     io.done(robot.behavior.isDone())

def brainStop():
     pass

def shutdown():
     pass
