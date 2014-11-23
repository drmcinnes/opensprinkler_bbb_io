#modified file from OSPi software for OpenSprinkler, only works with BeagleBone Black running directly to i/o pins
import gv

try:
    import RPi.GPIO as GPIO  # Required for accessing General Purpose Input Output pins on Raspberry Pi
    gv.platform = 'pi'
except ImportError:
    try:
        import Adafruit_BBIO.GPIO as GPIO  # Required for accessing General Purpose Input Output pins on Beagle Bone Black
        gv.platform = 'bo'
    except ImportError:
        gv.platform = ''  # if no platform, allows program to still run.
        print 'No GPIO module was loaded from GPIO Pins module'
        # Makes it runnable on machines other than RPi
        #GPIO = None

try:
    GPIO.setwarnings(False)
    GPIO.cleanup()
except Exception:
    pass

  #### pin defines ####
try:
    if gv.platform == 'pi':  # If this will run on Raspberry Pi:
        GPIO.setmode(GPIO.BOARD)  # IO channels are identified by header connector pin numbers. Pin numbers are always the same regardless of Raspberry Pi board revision.
        pin_sr_dat = 13
        pin_sr_clk = 7
        pin_sr_noe = 11
        pin_sr_lat = 15
        pin_rain_sense = 8
        pin_relay = 10
    elif gv.platform == 'bo':  # If this will run on Beagle Bone Black:
	pin_ch0 = "P8_46"
        pin_ch1 = "P8_44"
        pin_ch2 = "P8_42"
        pin_ch3 = "P8_40"
        pin_ch4 = "P8_38"
        pin_ch5 = "P8_36"
        pin_ch6 = "P8_34"
        pin_ch7 = "P8_32"
        pin_rain_sense = "P9_15"
        pin_relay = "P9_16"
except AttributeError:
    pass

#### setup GPIO pins as output or input ####
try:
    GPIO.setup(pin_ch0, GPIO.OUT)
    GPIO.setup(pin_ch1, GPIO.OUT)
    GPIO.setup(pin_ch2, GPIO.OUT)
    GPIO.setup(pin_ch3, GPIO.OUT)
    GPIO.setup(pin_ch4, GPIO.OUT)
    GPIO.setup(pin_ch5, GPIO.OUT)
    GPIO.setup(pin_ch6, GPIO.OUT)
    GPIO.setup(pin_ch7, GPIO.OUT)
    GPIO.setup(pin_rain_sense, GPIO.IN)
    GPIO.setup(pin_relay, GPIO.OUT)
except NameError:
    pass


def disableShiftRegisterOutput():
    """Disable output from shift register."""
#    print 'Disable output'
    try:
        GPIO.output(pin_ch0, GPIO.LOW)
        GPIO.output(pin_ch1, GPIO.LOW)
        GPIO.output(pin_ch2, GPIO.LOW)
        GPIO.output(pin_ch3, GPIO.LOW)
        GPIO.output(pin_ch4, GPIO.LOW)
        GPIO.output(pin_ch5, GPIO.LOW)
        GPIO.output(pin_ch6, GPIO.LOW)
        GPIO.output(pin_ch7, GPIO.LOW)
    except NameError:
        pass


def enableShiftRegisterOutput(srvals):
#    print 'Enable output'
    """Enable output from shift register."""
    try:
	print 'debug:'
#	print srvals
#	print srvals[0]
#	print srvals[1]
	xTmp = srvals[0]
	if xTmp == 0:
#		print 'Ch0 low'
		GPIO.output(pin_ch0, GPIO.LOW)
	else:
#		print 'Ch0 high'
                GPIO.output(pin_ch0, GPIO.HIGH)
	xTmp = srvals[1]
        if xTmp == 0:
#		print 'Ch1 low'
                GPIO.output(pin_ch1, GPIO.LOW)
        else:
#		print 'Ch1 high'
                GPIO.output(pin_ch1, GPIO.HIGH)

        xTmp = srvals[2]
        if xTmp == 0:
                GPIO.output(pin_ch2, GPIO.LOW)
        else:
                GPIO.output(pin_ch2, GPIO.HIGH)

        xTmp = srvals[3]
        if xTmp == 0:
                GPIO.output(pin_ch3, GPIO.LOW)
        else:
                GPIO.output(pin_ch3, GPIO.HIGH)

        xTmp = srvals[4]
        if xTmp == 0:
                GPIO.output(pin_ch4, GPIO.LOW)
        else:
                GPIO.output(pin_ch4, GPIO.HIGH)

        xTmp = srvals[5]
        if xTmp == 0:
                GPIO.output(pin_ch5, GPIO.LOW)
        else:
                GPIO.output(pin_ch5, GPIO.HIGH)

        xTmp = srvals[6]
        if xTmp == 0:
                GPIO.output(pin_ch6, GPIO.LOW)
        else:
                GPIO.output(pin_ch6, GPIO.HIGH)

        xTmp = srvals[7]
        if xTmp == 0:
#		print 'Ch7 low'
                GPIO.output(pin_ch7, GPIO.LOW)
        else:
#		print 'Ch7 high'
                GPIO.output(pin_ch7, GPIO.HIGH)


    except NameError:
        pass
#	print 'Error'

def setShiftRegister(srvals):
#    print ("Set shift register")
#    global pin_ch
    """Set the state of each output pin on the shift register from the srvals list."""
    try:
	sss=0
        for s in range(gv.sd['nst']):
#            print srvals
            if srvals[gv.sd['nst']-1-s]:
                pin_ch[sss] = 1
            else:
                pin_ch[sss] = 0
	    sss=sss+1
    except NameError:
        pass


def set_output():
    """Activate triacs according to shift register state."""
    disableShiftRegisterOutput()
    setShiftRegister(gv.srvals)  # gv.srvals stores shift register state
    enableShiftRegisterOutput(gv.srvals)

