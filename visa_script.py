#Kiuran Naidoo
import visa
import datetime
import time
if __name__ == "__main__":
    rm = visa.ResourceManager();
    ip_add = raw_input('Enter ip address -->')
    print "Attempting to connect to " + ip_add
    device = rm.open_resource("TCPIP0::" + ip_add + "::inst0::INSTR")
    print "Connected to:"
    print device
    print(device.query("*IDN?"))
    device.write("MMEM:STOR:FDAT \"MyFile.csv\"")
    data =  device.query("MMEM:DATA? \"MyFile.csv\"")
    device.write("MMEM:DEL \"MyFile.csv\"")
    times = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H.%M.%S')
    file_ = open('Data: ' + times + '.csv', 'w')
    file_.write(data)
    file_.close()
