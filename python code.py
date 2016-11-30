{rtf1\ansi ansicpg1252 cocoartf1038 cocoasubrtf360
{fonttbl\f0\fswiss\fcharset0 ArialMT;}
{colortbl;\red255\green255\blue255;\red26\green26\blue26;\red255\green255\blue255;}
paperw11900\paperh16840\margl1440\margr1440\vieww10640\viewh12480\viewkind0
deftab720
pard\pardeftab720\ql\qnatural

\f0\fs26 \cf2 \cb3 from liblo import *\
import sys
import os
import time
import copy
import serial

ser = serial.Serial('/dev/tty.usbmodem1411', 9600)\

try:\
'a0 \'a0 ports = list(sys.argv)[1:]\
except:\
'a0 \'a0 ports = [5000]\


alpha_sums = []
beta_sums = []
theta_sums = []

ratio2 = []


class MuseServer(ServerThread):

def __init__(self, port=5432):\
self.signal = \{\}\
self.signal['eeg'] = []\
self.signal['alpha_rel'] = []\
self.signal['alpha_abs'] = []\
self.signal['conc'] = []\
self.signal['mel'] = []\
self.signal['mel'] = []\
self.signal['beta_abs'] = []\
self.signal['theta_abs'] = []\

ServerThread.__init__(self, port)

# receive accelrometer data
@make_method('/muse/acc', 'fff')
def acc_callback(self, path, args):
acc_x, acc_y, acc_z = args\
# print "%s %f %f %f" % (path, acc_x, acc_y, acc_z)\

# receive EEG data\
@make_method('/muse/eeg', 'ffff')\
def eeg_callback(self, path, args):\
self.signal['eeg'].append(args)\

# receive alpha relative data\
@make_method('/muse/elements/alpha_relative', 'ffff')\
\'a0 \'a0 def alpha_callback(self, path, args):\
\'a0 \'a0 \'a0 \'a0 self.signal['alpha_rel'].append(args)\
\
\'a0 \'a0 @make_method('/muse/elements/alpha_absolute', 'ffff')\
\'a0 \'a0 def alpha_abs_callback(self, path, args):\
\'a0 \'a0 \'a0 \'a0 self.signal['alpha_abs'].append(args)\
\
\'a0 \'a0 @make_method('/muse/elements/beta_absolute', 'ffff')\
\'a0 \'a0 def beta_abs_callback(self, path, args):\
\'a0 \'a0 \'a0 \'a0 self.signal['beta_abs'].append(args)\
\
\'a0 \'a0 @make_method('/muse/elements/theta_absolute', 'ffff')\
\'a0 \'a0 def theta_abs_callback(self, path, args):\
\'a0 \'a0 \'a0 \'a0 self.signal['theta_abs'].append(args)\
\
\'a0 \'a0 # receive alpha relative data\
\'a0 \'a0 @make_method('/muse/elements/experimental/concentration', 'f')\
\'a0 \'a0 def concentration_callback(self, path, args):\
\'a0 \'a0 \'a0 \'a0 self.signal['conc'].append(args[0])\
\
\'a0 \'a0 # receive mellow data - viewer is the same as concentration\
\'a0 \'a0 @make_method('/muse/elements/experimental/mellow', 'f')\
\'a0 \'a0 def mellow_callback(self, path, args):\
\'a0 \'a0 \'a0 \'a0 self.signal['mel'].append(args[0])\
\'a0 \'a0 # handle unexpected messages\
\
\'a0 \'a0 @make_method(None, None)\
\'a0 \'a0 def fallback(self, path, args, types, src):\
\'a0 \'a0 \'a0 \'a0 test = args\
\'a0 \'a0 \'a0 \'a0 # print "Unknown message \\n\\t Source: '%s' \\n\\t Address: '%s' \\n\\t Types: '%s ' \\n\\t Payload: '%s'" %\
\'a0 \'a0 \'a0 \'a0 # (src.url, path, types, args)\
\
\
servers = []\
for port in ports:\
\'a0 \'a0 try:\
\'a0 \'a0 \'a0 \'a0 server = MuseServer(port=port)\
\'a0 \'a0 except ServerError, err:\
\'a0 \'a0 \'a0 \'a0 raise\
\'a0 \'a0 \'a0 \'a0 print str(err)\
\'a0 \'a0 \'a0 \'a0 sys.exit()\
\'a0 \'a0 server.start()\
\'a0 \'a0 servers.append(server)\
\
if __name__ == "__main__":\
\'a0 \'a0# io_udp = MuseIOOSC()\
\'a0 \'a0# io_udp.starit()\
\'a0 \'a0 while True:\
\'a0 \'a0 \'a0 \'a0 last_alpha_index = 0\
\'a0 \'a0 \'a0 \'a0 last_beta_index = 0\
\'a0 \'a0 \'a0 \'a0 time.sleep(1)\
\'a0 \'a0 \'a0 \'a0 total_alpha = 0\
\'a0 \'a0 \'a0 \'a0 total_beta = 0\
\'a0 \'a0 \'a0 \'a0 total_theta = 0\
\'a0 \'a0 \'a0 \'a0 sensor_number = 0\
\'a0 \'a0 \'a0 \'a0 for server in servers:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 sensor_number += 1\
\'a0 \'a0 \'a0 \'a0 # print server.signal['conc']\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 alpha = copy.copy(server.signal['alpha_abs'])\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 beta = copy.copy(server.signal['beta_abs'])\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 theta = copy.copy(server.signal['theta_abs'])\
\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 server.signal['beta_abs'] = []\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 server.signal['alpha_abs'] = []\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 server.signal['theta_abs'] = []\
\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 alpha_sum = 0\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 beta_sum = 0\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 theta_sum = 0\
\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 for alhpa_result in alpha:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 alpha_sum += sum(alhpa_result)\
\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 for beta_result in beta:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 beta_sum += sum(beta_result)\
\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 for theta_result in theta:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 theta_sum += sum(theta_result)\
\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 alpha_sums.append(alpha_sum)\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 beta_sums.append(beta_sum)\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 theta_sums.append(theta_sum)\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0\'a0\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 if (beta_sums[-1] / (theta_sums[-1] + alpha_sums[-1])) > 0.7:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 if sensor_number == 1:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 ser.write("a")\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 if sensor_number == 2:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 ser.write("c")\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 if sensor_number == 3:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 ser.write("e")\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 if (beta_sums[-1] / (theta_sums[-1] + alpha_sums[-1])) < 0.7:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 if sensor_number == 1:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 ser.write("b")\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 if sensor_number == 2:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 ser.write("d")\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 if sensor_number == 3:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 ser.write("f")\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0\'a0\
\
\'a0 \'a0 \'a0 \'a0 # beta / alpha + theta 0.3\
\
\'a0 \'a0 \'a0 \'a0 \'a0 # \'a0print("alpha", alpha_sums[-1])\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0# print("beta", beta_sums[-1])\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 #print("theta", theta_sums[-1])\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 #print("theta/beta", theta_sums[-1] / beta_sums[-1])\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 #print("ration 2", beta_sums[-1] / (theta_sums[-1] + alpha_sums[-1]))\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0\
\'a0 \'a0 \'a0 \'a0# ratio2 = beta_sums[-1] / (theta_sums[-1] + alpha_sums[-1])\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 total_alpha += alpha_sums[-1]\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 total_beta += beta_sums[-1]\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 total_theta += theta_sums[-1]\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 print("group", total_beta / (total_alpha + total_theta))\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 if sensor_number == 1:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 print("sensor1", beta_sums[-1] / (alpha_sums[-1] + theta_sums[-1]))\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 if sensor_number == 2:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 print("sensor2", beta_sums[-1] / (alpha_sums[-1] + theta_sums[-1]))\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 if sensor_number == 3:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 print("sensor3", beta_sums[-1] / (alpha_sums[-1] + theta_sums[-1]))\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0\'a0\
\'a0 \'a0 \'a0 \'a0 if (total_beta / (total_alpha + total_theta)) > 0.7:\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 ser.write("g")\
\'a0 \'a0 \'a0 \'a0 if (total_beta / (total_alpha + total_theta)) < 0.7:\
ser.write("h")\
}
