import time
import board
import busio
import digitalio
import adafruit_rfm9x

CS = digitalio.DigitalInOut (board.CE1)
RESET = digitalio.DigitalInOut (board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_under = 23

rfm9x.send(bytes("Hi team\r\n", "utf-8")) #Sending packet out to be recieved
print("Sent message")

print("waiting for packets")
while True:
    packet = rfm9x.receive()
    print("Recieved nothing yet")
else:
    print("Recieved (raw bytes): {0}".format(packet))
    
    packet_text = str(packet, "ascii")
    print("Recieved (ASCII): {0}". format(packet_text))
    
    rssi = rfm9x.last_rssi
    print("Received signal strength: {0} dB".format(rssi))