import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("users.csv")  # Cambia el nombre si es necesario

# Filtrar usuarios entre 45 y 60 años
usuarios_45_60 = df[(df["edad"] >= 45) & (df["edad"] <= 60)]

# Mostrar los usuarios filtrados (opcional)
print("Usuarios entre 45 y 60 años:")
print(usuarios_45_60[["nombre", "edad", "genero"]])  # Asegúrate de usar los nombres correctos de las columnas

# Conteo por género
conteo_genero = usuarios_45_60["genero"].value_counts()

# Mostrar conteo
print("\nConteo por género:")
print(conteo_genero)

# Gráfico
conteo_genero.plot(kind='bar', color=['lightblue', 'pink'])
plt.title("Usuarios entre 45 y 60 años por género")
plt.xlabel("Género")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()