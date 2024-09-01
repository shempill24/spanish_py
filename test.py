import math
def dB2(param1, param2):
 dB_calc = 20 * math.log10(param1/param2)
 if dB_calc > 6:
  return "High SNR"
 elif dB_calc > 0:
  return "Low SNR"
 return "Noise"
  
print(dB2(7,5))