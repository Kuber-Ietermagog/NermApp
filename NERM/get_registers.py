__version__ = '0.10'
# version 0.10 is the first release - 4 May 2018. All changes and versions must be logged here!
import sys
import os
import json
import time
from time import strftime, localtime

global di_old
di_old = 0
global meter_alarm
meter_alarm = [False, False, False, False]
global meter_trip
meter_trip = [False, False, False, False]
global trip_data

def getJsonData(filename):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    JSON_DIR = os.path.join(BASE_DIR, 'static', 'json', filename)
    try:
        with open(JSON_DIR, 'rt') as my_file:
            data = json.load(my_file)
            my_file.close()
        return data
    except IOError as err:
        print(err)

def setJsonData(filename, data):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    JSON_DIR = os.path.join(BASE_DIR, 'static', 'json', filename)
    try:
        with open(JSON_DIR, 'wt') as my_file:
            new_data = json.dumps(data)
            my_file.write(new_data)
        my_file.close()
    except IOError as err:
        print(err)

def analogEvent_Hi_to_Lo(i, value):
    global meter_alarm
    global meter_trip
    analog_data = getJsonData('analogs.json')
    label = analog_data['lables'][i]
    alarm_level = float(analog_data['alarm_level'][i])
    trip_level = float(analog_data['trip_level'][i])
    unit_is = analog_data['unit'][i]
    if value < alarm_level and value > trip_level and not meter_alarm[i]:
        try:
            event_data = getJsonData('events.json')
        except:
            event_data = {'eventNo': [], 'eventTime': [], 'eventDesc': [], 'eventState': [], 'eventType': [], 'alarm_on':[]}
        event_no = len(event_data['eventNo'])
        event_desc = label + " < " + str(alarm_level) + " " + unit_is
        get_time = strftime("%Y-%m-%d-%H:%M:%S", localtime())
        event_data['eventNo'].append(event_no)
        event_data['eventTime'].append(get_time)
        event_data['eventDesc'].append(event_desc)
        event_data['eventState'].append(1)
        event_data['alarm_on'].append(1)
        event_data['eventType'].append("Alarm")
        setJsonData('events.json', event_data)
        meter_alarm[i] = True
    if value < trip_level and not meter_trip[i]:
        try:
            event_data = getJsonData('events.json')
        except:
            event_data = {'eventNo': [], 'eventTime': [], 'eventDesc': [], 'eventState': [], 'eventType': [], 'alarm_on':[]}
        event_no = len(event_data['eventNo'])
        event_desc = label + " < " + str(trip_level) + " " + unit_is
        get_time = strftime("%Y-%m-%d-%H:%M:%S", localtime())
        event_data['eventNo'].append(event_no)
        event_data['eventTime'].append(get_time)
        event_data['eventDesc'].append(event_desc)
        event_data['eventState'].append(1)
        event_data['alarm_on'].append(1)
        event_data['eventType'].append("Trip")
        setJsonData('events.json', event_data)
        meter_trip[i] = True
    if value > trip_level and meter_trip[i]:
        try:
            event_data = getJsonData('events.json')
        except:
            event_data = {'eventNo': [], 'eventTime': [], 'eventDesc': [], 'eventState': [], 'eventType': [], 'alarm_on':[]}
        event_no = len(event_data['eventNo'])
        event_desc = label + " < " + str(alarm_level) + " " + unit_is
        get_time = strftime("%Y-%m-%d-%H:%M:%S", localtime())
        event_data['eventNo'].append(event_no)
        event_data['eventTime'].append(get_time)
        event_data['eventDesc'].append(event_desc)
        event_data['eventState'].append(1)
        event_data['alarm_on'].append(1)
        event_data['eventType'].append("Alarm")
        setJsonData('events.json', event_data)
        meter_trip[i] = False
    if value > alarm_level and meter_alarm[i]:
        try:
            event_data = getJsonData('events.json')
        except:
            event_data = {'eventNo': [], 'eventTime': [], 'eventDesc': [], 'eventState': [], 'eventType': [], 'alarm_on':[]}
        event_no = len(event_data['eventNo'])
        event_desc = label + " > " + str(alarm_level) + " " + unit_is
        get_time = strftime("%Y-%m-%d-%H:%M:%S", localtime())
        event_data['eventNo'].append(event_no)
        event_data['eventTime'].append(get_time)
        event_data['eventDesc'].append(event_desc)
        event_data['eventState'].append(0)
        event_data['alarm_on'].append(1)
        event_data['eventType'].append("Alarm")
        setJsonData('events.json', event_data)
        meter_alarm[i] = False

def analogEvent_Lo_to_Hi(i, value):
    global meter_alarm
    global meter_trip
    analog_data = getJsonData('analogs.json')
    label = analog_data['lables'][i]
    alarm_level = float(analog_data['alarm_level'][i])
    trip_level = float(analog_data['trip_level'][i])
    unit_is = analog_data['unit'][i]
    if value > alarm_level and value < trip_level and not meter_alarm[i]:
        try:
            event_data = getJsonData('events.json')
        except:
            event_data = {'eventNo': [], 'eventTime': [], 'eventDesc': [], 'eventState': [], 'eventType': [], 'alarm_on':[]}
        event_no = len(event_data['eventNo'])
        event_desc = label + " > " + str(alarm_level) + " " + unit_is
        get_time = strftime("%Y-%m-%d-%H:%M:%S", localtime())
        event_data['eventNo'].append(event_no)
        event_data['eventTime'].append(get_time)
        event_data['eventDesc'].append(event_desc)
        event_data['eventState'].append(1)
        event_data['alarm_on'].append(1)
        event_data['eventType'].append("Alarm")
        setJsonData('events.json', event_data)
        meter_alarm[i] = True
    if value > trip_level and not meter_trip[i]:
        try:
            event_data = getJsonData('events.json')
        except:
            event_data = {'eventNo': [], 'eventTime': [], 'eventDesc': [], 'eventState': [], 'eventType': [], 'alarm_on':[]}
        event_no = len(event_data['eventNo'])
        event_desc = label + " > " + str(trip_level) + " " + unit_is
        get_time = strftime("%Y-%m-%d-%H:%M:%S", localtime())
        event_data['eventNo'].append(event_no)
        event_data['eventTime'].append(get_time)
        event_data['eventDesc'].append(event_desc)
        event_data['eventState'].append(1)
        event_data['alarm_on'].append(1)
        event_data['eventType'].append("Trip")
        setJsonData('events.json', event_data)
        meter_trip[i] = True
    if value < trip_level and meter_trip[i]:
        try:
            event_data = getJsonData('events.json')
        except:
            event_data = {'eventNo': [], 'eventTime': [], 'eventDesc': [], 'eventState': [], 'eventType': [], 'alarm_on':[]}
        event_no = len(event_data['eventNo'])
        event_desc = label + " > " + str(alarm_level) + " " + unit_is
        get_time = strftime("%Y-%m-%d-%H:%M:%S", localtime())
        event_data['eventNo'].append(event_no)
        event_data['eventTime'].append(get_time)
        event_data['eventDesc'].append(event_desc)
        event_data['eventState'].append(1)
        event_data['alarm_on'].append(1)
        event_data['eventType'].append("Alarm")
        setJsonData('events.json', event_data)
        meter_trip[i] = False
    if value < alarm_level and meter_alarm[i]:
        try:
            event_data = getJsonData('events.json')
        except:
            event_data = {'eventNo': [], 'eventTime': [], 'eventDesc': [], 'eventState': [], 'eventType': [], 'alarm_on':[]}
        event_no = len(event_data['eventNo'])
        event_desc = label + " < " + str(alarm_level) + " " + unit_is
        get_time = strftime("%Y-%m-%d-%H:%M:%S", localtime())
        event_data['eventNo'].append(event_no)
        event_data['eventTime'].append(get_time)
        event_data['eventDesc'].append(event_desc)
        event_data['eventState'].append(0)
        event_data['alarm_on'].append(1)
        event_data['eventType'].append("Alarm")
        setJsonData('events.json', event_data)
        meter_alarm[i] = False


def logEvent(word):
    global di_old
    di_chk = []
    di_old_chk = []
    if di_old != word:
        operator = 0x0001
        for digits in range(0,16):
            if word & operator != 0:
                di_chk.append(1)
            else:
                di_chk.append(0)
            if di_old & operator != 0:
                di_old_chk.append(1)
            else:
                di_old_chk.append(0)
            operator = operator<<1
        labels_alarms = getJsonData('digitals.json')
        for items in range(0,16):
            if di_chk[items] != di_old_chk[items] and labels_alarms['used'][items]:
                try:
                    event_data = getJsonData('events.json')
                except:
                    event_data = {'eventNo': [], 'eventTime': [], 'eventDesc': [], 'eventState': [], 'eventType': [], 'alarm_on':[]}
                event_desc = labels_alarms['input_lbl']
                alarms = labels_alarms['alarm_on']
                event_no = len(event_data['eventNo'])
                get_time = strftime("%Y-%m-%d-%H:%M:%S", localtime())
                event_data['eventNo'].append(event_no)
                event_data['eventTime'].append(get_time)
                event_data['eventDesc'].append(event_desc[items])
                event_data['eventState'].append(di_chk[items])
                event_data['alarm_on'].append(alarms[items])
                if items < 8:
                    event_data['eventType'].append("Trip")
                else:
                    event_data['eventType'].append("Alarm")
                setJsonData('events.json', event_data)
        di_old = word

def word_to_bool(word):
    di = []
    operator = 0x0001
    for digits in range(0,16):
        if word & operator != 0:
            di.append(1)
        else:
            di.append(0)
        operator = operator<<1
    return di

def word_to_analog(word, max_value, i2c, lm35):
    ai = 0.0
    if i2c:
        if lm35:
            ai = float(max_value)*(float(word)/742)
        else:
            ai = float(max_value) * (float(word)/(1630))
    else:
        if lm35:
            ai = float(max_value) * ((float(word)/((1.5/4.096)*32767)))
        else:
            ai = float(max_value) * ((float(word)/((3.25/4.096)*32767)))
    ai = float("%.3f" % ai)
    return ai

def get_data_modbus(argv):
    try:
        ai = []
        client = mb(str(argv), port=502)
        rr0 = client.read_holding_registers(0,5)
        di = word_to_bool(rr0.registers[0])
        logEvent(rr0.registers[0])
        analog_data = getJsonData('analogs.json')
        analog_range = analog_data['qty_gauges']
        for i in range(1,analog_range+1):
            ai.append(word_to_analog(rr0.registers[i], analog_data['max_value'][i - 1], False, bool(analog_data['lm35'][i-1])))
            if analog_data['direction'][i-1] == 'hi-lo':
                analogEvent_Hi_to_Lo(i - 1, ai[i - 1])
            if analog_data['direction'][i-1] == 'lo-hi':
                analogEvent_Lo_to_Hi(i - 1, ai[i-1])
        scan_data = {'registers':rr0.registers, 'digitals':di, 'analogs':ai, 'error': "none"}
        setJsonData('reg.json', scan_data)
        client.close()
    except Exception as err:
        scan_data = {'registers':[], 'digitals':[], 'analogs':[], 'error': str(err)}
        setJsonData('reg.json', scan_data)
        client.close()
        time.sleep(2)

def get_data_i2c():
    try:
        ai = []
        rr0 = []
        di = 0
        #Raspberry Pi Analog setup
        import Adafruit_ADS1x15
        adc = Adafruit_ADS1x15.ADS1015() # Use address=0x49, 0x4A, and 0x4B to change divice address, default = 0x48

        #Raspberry Pi i2c-bus setup for Digitals
        from smbus import SMBus
        bus = SMBus(1)
        device = 0x20
        iodira = 0x00
        iodirb = 0x01
        gpioA = 0x12
        gpioB = 0x13

        # set both ports to inputs
        bus.write_byte_data(device, iodira, 0xFF)
        bus.write_byte_data(device, iodirb, 0xFF)

        #Scanning digital regiseters
        portA = bus.read_byte_data(device, gpioA)
        portB = bus.read_byte_data(device, gpioB)

        lo_byte = portA
        hi_byte = portB

        di_r = (hi_byte<<8 | lo_byte) & 0xFFFF
        rr0.append(di_r)
        di = word_to_bool(di_r)
        logEvent(di_r)

        #Scanning analog registers
        analog_data = getJsonData('analogs.json')
        analog_range = analog_data['qty_gauges']
        temperatue = [False, False, False, True]
        for i in range(analog_range):
            rr0.append(adc.read_adc(i, gain=1))
            ai.append(word_to_analog(adc.read_adc(i, gain=1), analog_data['max_value'][i], True, bool(analog_data['lm35'][i])))
            if analog_data['direction'][i] == 'hi-lo':
                analogEvent_Hi_to_Lo(i, ai[i])
            if analog_data['direction'][i] == 'lo-hi':
                analogEvent_Lo_to_Hi(i, ai[i])

        scan_data = {'registers':rr0, 'digitals':di, 'analogs':ai, 'error': "none"}
        setJsonData('reg.json', scan_data)

    except Exception as err:
        scan_data = {'registers':[], 'digitals':[], 'analogs':[], 'error': str(err)}
        setJsonData('reg.json', scan_data)

        time.sleep(2)

if __name__ == '__main__':
    time.sleep(0.1)
    try:
        event_data = getJsonData('events.json')
    except:
        event_data = {'eventNo': [], 'eventTime': [], 'eventDesc': [], 'eventState': [], 'eventType': [], 'alarm_on':[]}
    event_no = len(event_data['eventNo'])
    get_time = strftime("%Y-%m-%d-%H:%M:%S", localtime())
    event_data['eventNo'].append(event_no)
    event_data['eventTime'].append(get_time)
    event_data['eventDesc'].append("System Boot Complete!")
    event_data['eventState'].append(0)
    event_data['alarm_on'].append(1)
    event_data['eventType'].append("Alarm")
    setJsonData('events.json', event_data)
    job_data = getJsonData('jobinfo.json')
    job_data['info'][6] = __version__
    setJsonData('jobinfo.json', job_data)
    while True:
        if sys.argv[1] == 'modbus':
            from pymodbus.client.sync import ModbusTcpClient as mb
            get_data_modbus(sys.argv[2])
        if sys.argv[1] == 'i2c':
            get_data_i2c()
        time.sleep(0.05)
