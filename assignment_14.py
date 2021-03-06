# -*- coding: utf-8 -*-
"""Assignment-14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wDo2pQE6cZXF86aV6RFQhEQpSQxsC3uE
"""

import numpy


simlen = int(1e6)

die_output = numpy.random.randint(low = 1, high = 7, size = simlen)

mul_three_outputs = [elem for elem in die_output if elem%3==0]
even_outputs = [elem for elem in die_output if elem%2==0]
mul_three_given_even_outputs = [elem for elem in even_outputs if elem%3==0]


prob_E = numpy.size(mul_three_outputs)/simlen
prob_F = numpy.size(even_outputs)/simlen

prob_E_given_F = numpy.size(mul_three_given_even_outputs)/numpy.size(even_outputs)

print("E : Probability of getting a multiple of three is : ", prob_E)
print("F : Probability of getting a even number is : ", prob_F)
print("E|F : Probability of getting a multiple of three given an even number is : ", prob_E_given_F)