from math import pi
import math
import sys
import random as rdm 
from enum import Enum
import kansas

from rps7 import rock_paper_scissors

# gunakan from jika hanya spesifik modul yang akan dipakai
# jika butuh banyak modul gunakan import

#jika menggunakan from
print(pi)

# jika menggunakan import
print(math.pi)

#show inside modoule
# for item in dir(rdm):
#     print(item)

print(kansas.bird)
kansas.randomfunfact()

print(__name__)
print(kansas.__name__)

rock_paper_scissors()