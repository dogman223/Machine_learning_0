import pandas as pd

# 1.Pobieramy zbiór danych o cenach nieruchomości w Kalifornii i zapisujemy jako tabelę
housing = fetch_california_housing(as_frame = true);
df = housing.frame

print("---PIERWSZE 5 WIERSZY---");
print(df.head());

# 2. Przygotowanie danych
