import datetime
import time
import logging
import _thread
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
from opcode.library import snmpget
from opcode.snmp_query import *

while True:
    switch_core(5) #
    firewall_dc(5)
    firewall_campus(5)
    firewall_academic(5)
    wlc_8500(5)

