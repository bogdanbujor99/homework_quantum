#ex1
#a)
import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
from math import gcd
from numpy.random import randint
import pandas as pd
from fractions import Fraction
import math


'''
N = 15
a = 2

xvals = np.arange(100)
yvals = [np.mod(a**x, N) for x in xvals]

fig, ax = plt.subplots()
ax.plot(xvals, yvals, linewidth=1, linestyle='dashed', marker='.')

plt.show()'''

#b)
'''
#Idee preluata de pe qiskit.

a = 2
N = 15
n_count = int(2 * math.log(N*N, 2))

#blackbox-ul:

def c_amod15(a, power):
    """Controlled multiplication by a mod 15"""
    if a not in [2,7,8,11,13]:
        raise ValueError("'a' must be 2,7,8,11 or 13")
    U = QuantumCircuit(4)
    for iteration in range(power):
        if a in [2,13]:
            U.swap(0,1)
            U.swap(1,2)
            U.swap(2,3)
        if a in [7,8]:
            U.swap(2,3)
            U.swap(1,2)
            U.swap(0,1)
        if a == 11:
            U.swap(1,3)
            U.swap(0,2)
        if a in [7,11,13]:
            for q in range(4):
                U.x(q)
    U = U.to_gate()
    U.name = "%i^%i mod 15" % (a, power)
    c_U = U.control()
    return c_U

#poarta QTF dagger:

def qft_dagger(n):
    qc = QuantumCircuit(n)
    # Don't forget the Swaps!
    for qubit in range(n//2):
        qc.swap(qubit, n-qubit-1)
    for j in range(n):
        for m in range(j):
            qc.cp(-math.pi/float(2**(j-m)), m, j)
        qc.h(j)
    qc.name = "QFT†"
    return qc


#Construim circuitul

qc = QuantumCircuit(n_count + 4, n_count)

for q in range(n_count): #punem hadamard pe primii n qubiti
    qc.h(q)

qc.x(3 + n_count) #punem not pe ultimul qubit 

for q in range(n_count):
    qc.append(c_amod15(a, 2 ** q), [q] + [i + n_count for i in range(4)]) #punem control pe primul primul element din vector si poarta pe ultimele elemente din vector 
                                                                          #q=0 [0,n_count,n_count+1,n_count+2,n_count+3] q=1 [1,n_count,n_count+2,n_count+3] 

qc.append(qft_dagger(n_count), range(n_count)) #pune qft pe primii n qubiti

qc.measure(range(n_count), range(n_count)) #masoara primii n qubiti

#Afisam circuitul

print(qc.draw('text'))

simulator = Aer.get_backend('qasm_simulator')

result = execute(qc, simulator, shots=100).result()

counts = result.get_counts()

#Afisam rezultatele

print(counts)
plot_histogram(counts, color='midnightblue', title="New Histogram").savefig('T2.1.png')


#calculam r-ul

rows, measured_phases = [], []
for output in counts:
    decimal = int(output, 2)
    phase = decimal/(2**n_count)
    measured_phases.append(phase)

for phase in measured_phases:
    frac = Fraction(phase).limit_denominator(15)
    rows.append([phase, "%i/%i" % (frac.numerator, frac.denominator), frac.denominator])

#afisam r-ul

headers=["Phase", "Fraction", "Guess for r"]
df = pd.DataFrame(rows, columns=headers)
print(df)'''

#ex2
simulator=Aer.get_backend('qasm_simulator')
qc = QuantumCircuit(4,4)

qc.x(3)
qc.y(3)
qc.x(3)
qc.h(0)
qc.h(1)
qc.h(2)

j = 0.000

theta = 4*math.pi * j

qc.cry(theta,0,3)

qc.cry(theta,1,3)
qc.cry(theta,1,3)

qc.cry(theta,2,3)
qc.cry(theta,2,3)
qc.cry(theta,2,3)
qc.cry(theta,2,3)

qc.h(0)
qc.h(1)
qc.h(2)

qc.crx(-(math.pi/4) ,2, 0)
qc.crx(-(math.pi/2) ,1, 0)
qc.crx(-(math.pi/2) ,2, 1)

qc.measure(0,0)
qc.measure(1,1)
qc.measure(2,2)

print(qc)

backend = Aer.get_backend('qasm_simulator')
results = execute(qc, backend, shots=2048).result()
counts = results.get_counts()
print(counts)
