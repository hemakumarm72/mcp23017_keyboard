from machine import Pin, SoftI2C, WDT
import time
import mcp23017
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
mcp = mcp23017.MCP23017(i2c, 0x20)

print("starting")
# wdt = WDT(timeout=20000)  # enable it with a timeout of 2s
keys = [
        ['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D']
        
        ]

rows = [0,1,2,3]
cols = [4,5,6,7]
print("intial")


# row_pin = [mcp[pin_no].output(0) for pin_no in rows]
cols_pin = [mcp[pin_no].input(pull=1) for pin_no in cols]

mcp[1].output(0)
data = 1




def scan(row, col):
    
    mcp[rows[row]].output(0)
    key = None
    if mcp[cols[col]].value() == 1:
        
       key = 1
   
    if mcp[cols[col]].value() == 0:
        
       key = 0
        
   
    mcp[rows[row]].output(1)
    return key    

data = None
def letterfind(row, col):
    global data
    if data !=  keys[row][col]:
       data = keys[row][col]
       print(data)
       time.sleep(0.1)
       data = None
       time.sleep(0.1)
        
while True:
    try:
     
       for row in range(4):
           for col in range(4):
               key =  scan(row, col)
             
               if key == 0:
                 letterfind(row, col)
     
      
   
    except OSError as e:
       print("erro while" , e)
       time.sleep(5)
     

