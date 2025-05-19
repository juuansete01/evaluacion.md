import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("users.csv")  # Asegúrate de que el nombre sea correcto

# Filtrar por países y edad
paises_deseados = ["Spain", "France", "Turkey"]
filtro = (df["pais"].isin(paises_deseados)) & (df["edad"] > 20)
usuarios_filtrados = df[filtro]

# Mostrar nombres de los usuarios filtrados
print("Nombres de usuarios mayores de 20 años de España, Francia o Turquía:")
print(usuarios_filtrados["nombre"])  # Cambia a "usuario" si esa es la columna

# Contar por género
conteo_genero = usuarios_filtrados["genero"].value_counts()

# Mostrar conteo
print("\nConteo por género:")
print(conteo_genero)

# Gráfico
conteo_genero.plot(kind='bar', color=['lightblue', 'pink'])
plt.title("Usuarios > 20 años de España, Francia y Turquía por género")
plt.xlabel("Género")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
