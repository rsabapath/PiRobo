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

	def backward(self):
		if(self.operation != "backward"):
			self.motorControl.setLeftBackwardHigh()
			self.motorControl.setRightBackwardHigh()
			self.operation = "backward"
			print "Operation set to Backward"
		else:
			print "Operation is already set to Backward"

	def turnLeft(self):
		if(self.operation != "left"):
			self.motorControl.setLeftBackwardHigh()
			self.motorControl.setRightForwardHigh()
			self.operation = "left"
			print "Operation set to Turn Left"
		else:
			print "Operation is already set to Turn Left"

	def turnRight(self):
		if(self.operation != "right"):
			self.motorControl.setLeftForwardHigh()
			self.motorControl.setRightBackwardHigh()
			self.operation = "right"
			print "Operation set to Turn Right"
		else:
			print "Operation is already set to Turn Right"

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