import pandas as pd
from sklearn.datasets import fetch_california_housing

# 1.Pobieramy zbiór danych o cenach nieruchomości w Kalifornii i zapisujemy jako tabelę
housing = fetch_california_housing(as_frame = true);
df = housing.frame

print("---PIERWSZE 5 WIERSZY---");
print(df.head());

# 2. Przygotowanie danych
# Podział tabeli na dwie: 
# x - przechowanie danych o domu (wiek domu, mediana lokalnego przychodu, liczba pokoi, liczba sypialni)
# y - mediana przewidzianej ceny domu

X = df[["HouseAge", "Rooms", "MedIncome", "Bedrooms"]];
Y = df["MedHouseValue"];