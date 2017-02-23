#Kiuran Naidoo
import visa
import datetime
import time
if __name__ == "__main__":
    #Create resource manager for visa
    rm = visa.ResourceManager();
    #IP Address of deivce
    ip_add = raw_input('Enter ip address -->')
    print "Attempting to connect to " + ip_add
    #connect to device
    device = rm.open_resource("TCPIP0::" + ip_add + "::inst0::INSTR")
    print "Connected to:"
    print device
    #Query Device info
    print(device.query("*IDN?"))
    #Write data to device memory
    device.write("MMEM:STOR:FDAT \"MyFile.csv\"")
    #Query data from device
    data =  device.query("MMEM:DATA? \"MyFile.csv\"")
    #Delete data from device internal memory
    device.write("MMEM:DEL \"MyFile.csv\"")
    #Time Stamp
    times = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H.%M.%S')
    #Write File
    file_ = open('Data: ' + times + '.csv', 'w')
    file_.write(data)
    file_.close()
