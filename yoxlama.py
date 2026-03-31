import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import selenium
import openpyxl

print("Kitabxanalar yoxlanılır...")

# Kiçik bir data yaradaq (Pandas və Numpy testi)
data = {'Ay': ['Yanvar', 'Fevral', 'Mart'], 'Gelir': [2500, 3200, 2800]}
df = pd.DataFrame(data)

print("\n--- Maliyyə Cədvəli Testi ---")
print(df)

print("\n--- Sistem Yoxlanışı ---")
print(f"Pandas versiyası: {pd.__version__}")
print(f"Numpy versiyası: {np.__version__}")
print("\nBütün kitabxanalar uğurla işləyir! Təbriklər!")