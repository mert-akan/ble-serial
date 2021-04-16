from concurrent.futures import ThreadPoolExecutor
from hm11_at_config import set_module_baud
from serial_handler import read_serial, write_serial

# Interfaces
PORT_UART = '/dev/ttyUSB0'
PORT_BLE = '/tmp/ttyBLE'

with open('../README.md', 'rb') as f:
    CONTENT = f.read()
    # print(CONTENT)


baud_to_test = [9600, 19200, 57600, 230400]
prev = baud_to_test[0]

for baud in baud_to_test:
    print(f'Testing baud: {baud}')
    set_module_baud(PORT_UART, prev, baud)

    with ThreadPoolExecutor(max_workers=2) as executor:
        futw = executor.submit(write_serial, PORT_UART, baud, CONTENT, 8, 0.0)
        futr = executor.submit(read_serial, PORT_BLE, baud, CONTENT)
        print(futr.result())

set_module_baud(PORT_UART, prev, baud_to_test[0])