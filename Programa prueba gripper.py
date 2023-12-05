import minimalmodbus
import serial
import binascii
import time
import robotiqGripper as rq

instrument = minimalmodbus.Instrument('COM5', 9, debug = True)

# instrument.serial.port                     # this is the serial port name
instrument.serial.baudrate = 115200         # Baud
# instrument.serial.bytesize = 8
# instrument.serial.parity   = serial.PARITY_NONE
# instrument.serial.stopbits = 1
# instrument.serial.timeout  = 0.2          # seconds
# instrument.address = 9                         # this is the slave address number
# instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
# instrument.clear_buffers_before_each_transaction = True
#
# print(instrument)

# instrument.write_registers(1000,[0,0,0]) # Reset the gripper
# instrument.write_registers(1000,[256,0,0]) #Activate the gripper


myGripper = rq.RobotiqGripper(portname='COM5',slaveaddress=9)
myGripper.activate()
myGripper.openGripper(1,1)
myGripper.closeGripper(1,1)
time.sleep(5)
myGripper.openGripper(255,255)
myGripper.closeGripper(255,255)
time.sleep(2)
myGripper.goTo(0)
time.sleep(1)
myGripper.goTo(125)
time.sleep(1)
myGripper.goTo(255)
time.sleep(2)
myGripper.goTo(0)