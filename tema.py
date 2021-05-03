#ex1
import  numpy as np
from qiskit import (QuantumCircuit,QuantumRegister,ClassicalRegister,execute,Aer)
from qiskit.tools.visualization import plot_histogram

'''simulator=Aer.get_backend('qasm_simulator')
circuit=QuantumCircuit(2,2)
circuit.x(0)
circuit.x(1)
circuit.cx(0,1)
circuit.cx(1,0)
circuit.cx(0,1)
for i in range(2):
    circuit.measure(i,i)
print(circuit.draw())
job=execute(circuit,simulator)
result=job.result()
count=result.get_counts(circuit)
print(count)
plot_histogram(count).savefig('circuit')'''

#ex2 hadamard jos, c not, hadamard jos
#a)
'''simulator=Aer.get_backend('')
circuit=QuantumCircuit(2,2)
circuit.x(0)
circuit.x(1)
circuit.h(1)
circuit.cx(0,1)
circuit.h(1)
for i in range(2):
    circuit.measure(i,i)
print(circuit.draw())
job=execute(circuit,simulator)
result=job.result()
count=result.get_counts(circuit)
print(count)'''


#b) 
simulator=Aer.get_backend('qasm_simulator')
def C_(qc,a,b):
    qc.h(b)
    qc.cx(a,b)
    qc.h(b)
    return qc

qc=QuantumCircuit(2,2)
qc.x(0)
qc.h(1)
C_(qc,0,1)
qc.h(1)

for i in range(2):
    qc.measure(i,i)

print(qc.draw())
job=execute(qc,simulator)
result=job.result()
count=result.get_counts(qc)
print(count)


