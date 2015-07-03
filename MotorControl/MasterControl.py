from MotorControl import MotorControl

class MasterControl:
	motorControl = None
	operation = None
	#eventually I will read this from a config
	def __init__(self,L_F_GPIO,L_B_GPIO,R_F_GPIO,R_B_GPIO):
		self.motorControl = MotorControl(L_F_GPIO,L_B_GPIO,R_F_GPIO,R_B_GPIO)
		self.operation = None

	def forward(self):
		if(self.operation != "forward"):
			self.motorControl.setLeftForwardHigh()
			self.motorControl.setRightForwardHigh()
			self.operation = "forward"
			print "Operation set to Forward"
		else:
			print "Operation is already set to Forward"

	def stop(self):
		if(self.operation != "stop"):
			self.motorControl.setLeftForwardLow()
			self.motorControl.setRightForwardLow()
			self.motorControl.setLeftBackwardLow()
			self.motorControl.setRightBackwardLow()
			self.operation = "stop"
			print "Operation set to Stop"
		else:
			print "Operation is already set to Stop"

	def exit(self):
		self.motorControl.cleanUp()