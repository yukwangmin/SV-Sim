import time
import cirq
import numpy as np
from functools import reduce
q = [cirq.NamedQubit('q' + str(i)) for i in range(11)]
circuit = cirq.Circuit(
    cirq.H(q[1]),
    cirq.H(q[2]),
    cirq.H(q[3]),
    cirq.H(q[4]),
    cirq.X(q[5]),
    cirq.X(q[6]),
    cirq.X(q[7]),
    cirq.X(q[8]),
    cirq.X(q[4]),
    cirq.CCX(q[1], q[2], q[9]),
    cirq.CCX(q[3], q[9], q[10]),
    cirq.CCX(q[4], q[10], q[5]),
    cirq.CCX(q[3], q[9], q[10]),
    cirq.CCX(q[1], q[2], q[9]),
    cirq.X(q[2]),
    cirq.X(q[3]),
    cirq.X(q[4]),
    cirq.CCX(q[1], q[2], q[9]),
    cirq.CCX(q[3], q[9], q[10]),
    cirq.CCX(q[4], q[10], q[6]),
    cirq.CCX(q[3], q[9], q[10]),
    cirq.CCX(q[1], q[2], q[9]),
    cirq.X(q[1]),
    cirq.X(q[2]),
    cirq.CCX(q[1], q[2], q[9]),
    cirq.CCX(q[3], q[9], q[10]),
    cirq.CCX(q[4], q[10], q[7]),
    cirq.CCX(q[3], q[9], q[10]),
    cirq.CCX(q[1], q[2], q[9]),
    cirq.X(q[1]),
    cirq.X(q[2]),
    cirq.CCX(q[2], q[3], q[8]),
    cirq.X(q[2]),
    cirq.X(q[3]),
    cirq.CCX(q[5], q[6], q[9]),
    cirq.CCX(q[7], q[9], q[10]),
    cirq.CCX(q[8], q[10], q[0]),
    cirq.X(q[0]),
    cirq.X(q[1]),
    cirq.X(q[2]),
    cirq.X(q[3]),
    cirq.CCX(q[7], q[9], q[10]),
    cirq.H(q[0]),
    cirq.CCX(q[5], q[6], q[9]),
    cirq.CCX(q[2], q[3], q[8]),
    cirq.X(q[2]),
    cirq.CCX(q[1], q[2], q[9]),
    cirq.CCX(q[3], q[9], q[10]),
    cirq.CCX(q[4], q[10], q[7]),
    cirq.CCX(q[3], q[9], q[10]),
    cirq.CCX(q[1], q[2], q[9]),
    cirq.X(q[1]),
    cirq.X(q[2]),
    cirq.CCX(q[1], q[2], q[9]),
    cirq.CCX(q[3], q[9], q[10]),
    cirq.CCX(q[4], q[10], q[6]),
    cirq.CCX(q[3], q[9], q[10]),
    cirq.CCX(q[1], q[2], q[9]),
    cirq.X(q[2]),
    cirq.X(q[3]),
    cirq.X(q[4]),
    cirq.CCX(q[1], q[2], q[9]),
    cirq.CCX(q[3], q[9], q[10]),
    cirq.CCX(q[4], q[10], q[5]),
    cirq.CCX(q[3], q[9], q[10]),
    cirq.CCX(q[1], q[2], q[9]),
    cirq.H(q[1]),
    cirq.H(q[2]),
    cirq.H(q[3]),
    cirq.X(q[4]),
    cirq.X(q[1]),
    cirq.X(q[2]),
    cirq.X(q[3]),
    cirq.H(q[4]),
    cirq.X(q[4]),
    cirq.CCX(q[1], q[2], q[9]),
    cirq.CCX(q[3], q[9], q[10]),
    cirq.CCX(q[4], q[10], q[0]),
    cirq.H(q[0]),
    cirq.CCX(q[3], q[9], q[10]),
    cirq.X(q[0]),
    cirq.CCX(q[1], q[2], q[9]),
    cirq.H(q[0]),
    cirq.X(q[1]),
    cirq.X(q[2]),
    cirq.X(q[3]),
    cirq.X(q[4]),
    cirq.H(q[1]),
    cirq.H(q[2]),
    cirq.H(q[3]),
    cirq.H(q[4]),
    cirq.measure(q[1], key='m0'),
    cirq.measure(q[2], key='m1'),
    cirq.measure(q[3], key='m2'),
    cirq.measure(q[4], key='m3')
)

start = time.time()
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1)
result_dict = dict(result.multi_measurement_histogram(keys=['m0', 'm1', 'm2', 'm3', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
#print(counts)
end = time.time()
print("sat_n11 simulate on Cirq:" + str(end-start))
