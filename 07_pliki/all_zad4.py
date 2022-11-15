# 4▹ Wyświetl 3 losowe cytaty

import random

filename = "cytat.txt"

with open(filename, 'r', encoding="utf-8") as f:
  content = f.readlines()

cytat1 = random.choice(content)
cytat2 = random.choice(content)
cytat3 = random.choice(content)

print(cytat1, cytat2, cytat3)

