from ctypes import *
from sys import exit

# Define the structure
class TVARIABLES(Structure):
    _fields_ = [("numberOfPeaks", c_int16), 
                ("leftCutOff", c_int16), 
                ("rightCutOff", c_int16),
                ("pulseHeight", c_int16),
                ("pulseIntegral", c_int16)]

# Create instance of variables class
blah = TVARIABLES()              
              
# Make sure we can use the function from baseline.dll
baseline_dll = CDLL("../../../project/Baseline/Release/Baseline.dll")
trace_Variables = baseline_dll.traceVariables

trace = [192,194,195,193,191,195,195,198,193,196,194,195,194,195,194,195,193,197,192,195,194,193,192,196,194,194,194,198,193,195,193,194,192,197,194,196,193,195,194,195,195,196,195,196,193,196,195,195,192,193,193,194,192,197,192,195,195,194,192,192,194,193,194,193,195,195,193,193,195,196,192,196,195,193,193,195,195,196,195,197,193,195,195,195,192,193,194,196,195,196,194,195,195,193,191,194,195,196,194,194,194,193,193,195,192,195,193,197,194,195,195,193,192,197,194,195,196,196,193,192,194,193,196,195,194,196,194,194,195,196,194,195,194,193,194,194,193,194,195,197,193,194,194,196,193,194,194,195,194,195,195,196,193,195,196,195,194,195,194,195,194,195,195,194,193,194,194,196,195,195,193,196,194,196,194,193,193,197,194,196,196,193,194,196,192,193,195,205,193,199,193,195,192,192,195,197,195,193,193,196,194,193,192,195,192,198,193,195,195,194,191,194,196,193,193,195,193,192,195,193,191,194,194,195,194,195,196,197,195,196,193,196,193,193,193,196,193,193,194,194,194,194,194,195,193,194,195,194,193,196,196,194,193,195,194,194,193,194,194,195,195,195,194,195,192,193,194,196,193,194,193,195,194,195,194,194,195,196,194,196,194,195,195,194,192,196,195,196,193,193,195,193,195,197,194,195,195,193,194,196,193,196,195,196,193,194,193,193,194,196,192,198,194,194,194,195,193,196,195,196,194,197,195,194,194,194,192,197,195,196,193,195,194,193,193,192,195,196,192,194,195,197,192,194,194,195,194,195,196,194,195,194,196,195,194,194,194,195,195,196,195,196,195,193,194,194,195,198,192,195,194,196,195,195,193,196,193,196,195,195,193,195,193,196,194,195,196,195,194,194,194,194,194,194,195,196,192,197,194,192,195,195,194,196,195,196,195,195,193,194,194,197,194,197,193,195,195,196,191,195,195,195,195,196,195,195,195,196,194,198,195,193,191,195,193,195,195,196,192,195,194,195,194,195,194,197,196,194,194,195,193,196,195,194,195,195,193,194,194,197,193,197,192,196,193,195,194,197,193,196,194,194,193,195,194,198,192,197,194,196,194,194,193,196,194,196,194,195,192,196,193,197,192,196,194,195,193,197,193,196,194,196,195,197,194,193,194,196,194,198,195,197,193,196,196,195,195,197,193,195,194,195,195,198,192,195,193,198,193,197,194,196,197,197,195,197,194,196,195,197,194,195,194,195,193,196,193,196,191,198,192,194,194,194,194,198,191,197,193,197,193,197,195,197,191,194,191,197,194,195,194,197,192,195,193,194,195,196,193,196,192,196,195,196,196,194,195,199,194,196,193,194,193,196,192,196,194,195,191,196,195,195,194,198,193,197,195,198,193,199,193,197,194,195,194,196,192,195,195,195,192,197,195,194,194,194,191,196,195,196,193,195,193,197,194,197,194,197,194,196,193,194,193,197,194,196,192,197,195,196,192,195,192,198,195,195,193,196,195,198,194,196,195,194,194,195,192,196,190,196,194,195,192,197,194,194,194,195,191,198,192,195,194,197,193,197,193,196,193,196,193,194,192,197,191,196,195,193,192,197,193,197,193,196,193,198,194,196,193,195,196,194,195,196,195,197,194,197,192,195,190,195,195,193,194,197,195,196,194,194,196,193,192,196,193,196,194,197,192,197,194,195,193,196,195,195,192,196,194,194,192,194,194,194,193,196,195,197,193,198,193,193,195,196,193,194,193,196,194,196,196,195,193,196,195,196,192,196,194,197,193,196,193,195,193,196,195,195,192,196,195,195,195,194,193,196,194,196,192,195,195,194,192,196,195,196,191,196,193,196,193,197,191,195,194,195,193,198,194,197,192,195,194,195,193,193,194,197,194,198,194,195,195,194,194,195,193,195,193,195,194,193,194,194,193,196,195,195,192,197,194,193,192,194,194,195,192,197,194,195,191,195,194,194,193,193,193,197,193,196,193,193,193,195,194,196,193,196,193,195,194,196,193,195,191,196,194,195,193,194,196,196,193,195,192,195,195,196,195,196,193,192,194,197,194,195,194,194,193,195,195,195,194,195,195,197,193,196,192,193,195,193,195,196,192,196,194,197,194,196,193,193,196,195,193,195,194,195,194,198,193,195,194,196,192,196,192,195,194,195,193,195,195,193,193,197,192,196,194,196,193,196,193,194,192,195,194,193,191,194,194,197,192,195,195,195,194,195,195,196,192,194,194,193,192,194,195,194,192,194,195,194,193,195,194,195,193,195,194,194,192,194,194,195,192,197,193,194,193,195,197,193,195,195,195,195,196,194,194,195,191,196,196,195,195,194,192,195,196,196,195,194,194,192,195,195,192,195,192,195,193,194,194,197,195,195,194,193,194,193,194,193,194,194,194,195,194,195,195,194,194,195,194,193,193,194,194,195,194,194,193,192,194,195,194,195,194,195,193,192,193,195,194,197,192,195,193,195,195,198,195,194,195,192,193,193,194,193,194,192,191,194,194,195,192,196,194,195,196,194,194,194,195,193,192,197,195,196,194,194,193,193,195,193,194,193,193,194,193,195,193,195,193,193,195,194,192,193,194,194,193,195,194,193,194,194,193,196,191,193,195,195,194,195,193,193,195,198,192,193,192,195,192,194,192,195,194,194,193,197,194,196,194,195,193,193,193,195,196,196,192,195,193,196,192,193,193,195,193,194,195,194,193,196,194,196,192,194,195,195,193,194,193,195,194,195,193,196,194,195,193,196,194,194,194,194,195,195,193,193,193,197,195,196,194,195,194,196,194,195,194,196,193,196,193,195,194,196,193,196,195,192,195,193,194,193,192,193,195,195,192,195,195,194,194,193,193,193,193,198,193,195,194,194,193,195,194,193,194,192,194,195,194,195,192,194,194,195,194,195,192,195,194,195,195,196,192,193,195,196,192,197,193,195,193,193,194,195,194,194,194,197,192,196,192,195,193,198,192,194,194,197,194,195,192,194,194,195,193,195,193,194,194,195,193,196,195,198,192,197,195,194,195,195,193,194,194,195,195,197,195,194,193,196,192,195,194,195,193,194,192,194,196,194,194,197,193,196,194,194,192,193,193,196,194,195,194,195,194,195,193,197,194,197,193,195,194,195,194,195,196,198,196,197,194,194,197,196,195,195,194,195,195,195,195,197,194,196,196,195,194,197,195,196,192,196,194,195,195,196,193,196,194,199,191,195,195,195,194,195,194,198,193,197,194,197,193,196,195,192,194,196,195,195,194,196,195,196,193,196,194,196,195,196,195,197,195,195,196,193,195,195,195,199,192,193,196,196,196,195,196,195,194,197,194,197,193,197,195,197,192,199,195,195,194,195,194,196,193,196,194,196,193,196,193,198,196,196,195,197,196,197,193,197,195,195,194,196,194,198,194,195,194,196,193,197,192,196,195,197,194,196,195,193,194,199,193,196,193,193,193,197,195,193,195,198,195,197,193,195,196,197,191,198,196,194,194,196,194,194,195,196,195,196,193,195,193,197,195,195,194,197,193,195,195,195,192,197,192,194,196,197,193,197,196,195,194,197,194,195,194,196,195,193,194,197,195,197,193,197,194,196,194,195,195,197,196,196,193,197,193,196,195,195,195,196,194,198,195,197,194,196,194,195,192,195,195,195,194,195,192,195,193,198,193,196,194,196,195,197,194,199,192,196,193,195,195,197,196,197,192,196,195,197,195,195,193,195,193,196,193,196,194,197,191,196,195,196,193,196,192,195,194,198,194,198,194,196,192,195,192,197,191,195,194,197,193,197,193,196,195,197,194,195,193,197,193,195,195,197,194,196,194,197,193,193,193,199,193,195,194,196,193,197,194,197,194,198,196,197,193,197,192,193,193,193,194,198,192,196,195,195,193,195,194,198,194,197,193,194,195,194,195,199,192,194,193,197,193,194,194,194,194,197,194,194,195,193,195,197,193,197,195,195,194,195,192,197,195,193,193,195,193,195,191,197,193,198,193,194,194,193,194,197,193,196,193,196,195,195,193,196,194,195,194,195,194,199,193,195,193,195,194,195,192,192,194,197,191,197,193,195,193,195,194,195,193,197,195,194,195,195,194,197,192,196,194,195,195,195,193,197,195,196,191,195,194,192,193,197,192,195,195,193,194,198,193,197,194,195,193,196,196,195,196,196,194,197,191,193,194,195,192,194,193,194,193,198,195,193,193,196,194,195,194,195,193,194,194,197,194,197,193,196,191,195,194,197,194,196,195,196,194,195,194,195,193,197,193,195,195,194,192,197,191,194,192,195,192,197,194,194,195,195,194,195,193,195,194,194,194,195,194,196,195,191,194,196,193,196,195,193,194,195,194,195,195,196,194,194,193,194,194,196,193,195,194,196,194,191,194,196,194,195,194,196,194,196,195,193,195,195,194,194,193,194,193,197,195,195,192,193,194,193,194,194,194,192,194,194,194,195,193,197,193,193,192,194,193,196,195,196,193,197,194,198,192,194,194,196,192,196,194,195,192,197,192,195,196,196,194,194,194,194,195,197,194,197,194,196,193,196,192,195,194,195,191,196,194,196,195,195,193,194,194,195,194,197,193,194,193,195,194,193,191,195,194,196,191,194,193,196,195,196,194,195,195,196,194,194,194,194,195,196,192,194,192,196,193,194,194,193,194,197,193,195,194,193,195,195,192,196,194,195,194,193,195,193,192,196,194,195,194,193,194,193,194,196,193,195,193,196,193,196,194,196,192,197,192,194,195,196,193,194,194,195,193,197,192,195,194,193,194,194,194,193,194,197,192,195,193,197,192,196,191,197,191,196,192,194,192,193,194,196,191,195,193,195,191,195,192,196,192,197,193,193,193,195,193,196,193,193,194,196,194,195,194,197,194,197,193,197,193,192,194,197,193,195,192,193,193,195,197,194,193,194,195,195,194,194,194,196,191,196,192,196,193,195,193,193,193,196,194,195,194,195,195,195,194,196,193,193,194,196,195,197,193,196,194,196,195,192,194,196,193,195,193,193,193,193,193,195,194,195,195,196,194,196,196,193,193,195,193,194,194,196,192,193,194,196,193,196,194,193,195,194,192,196,192,194,194,195,193,194,194,195,195,195,192,193,195,196,194,193,194,196,193,195,195,193,192,194,194,197,195,193,196,197,193,197,193,195,193,193,194,193,195,196,193,195,193,195,194,197,193,200,193,192,193,196,192,193,192,196,195,196,194,193,192,196,192,191,192,194,192,197,194,193,194,193,194,193,194,193,193,195,193,196,192,196,195,194,194,197,193,193,194,192,193,195,195,197,193,198,194,196,194,194,196,193,196,195,193,195,194,194,195,195,194,195,193,195,195,197,195,193,193,196,192,192,193,195,196,198,192,195,194,196,192,194,194,196,193,194,196,195,194,196,193,195,192,193,194,197,193,195,193,194,196,195,194,193,195,193,195,194,193,198,192,194]

# Define array
trace_array = (c_uint16 * len(trace))(*trace)
            
# Define function prototype as used in dll
trace_Variables.argtypes = [c_uint16 * len(trace_array), c_int16, c_uint32, c_uint16, c_int16, POINTER(TVARIABLES)]
trace_Variables.restype = c_int32
            
# Run the DLL
dll_return = trace_Variables(trace_array, 25, len(trace), 25, 194, byref(blah))

# Show the output
print ("dll = ", dll_return)
print("height = ", blah.pulseHeight)
print("# pulses = ", blah.numberOfPeaks)
print("integral = ", blah.pulseIntegral)