#Código para crear Dataset Simulada


import pandas as pd
import numpy as np

# Generar un dataset simulado
np.random.seed(42)
num_samples = 1000

data = {
    'day_of_week': np.random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], num_samples),
    'hour_of_day': np.random.randint(0, 24, num_samples),
    'temperature': np.random.uniform(15, 35, num_samples),
    'precipitation': np.random.uniform(0, 50, num_samples),
    'event': np.random.choice(['None', 'Sports', 'Concert', 'Holiday'], num_samples),
    'traffic_density': np.random.uniform(0, 1, num_samples),
    'population_density': np.random.uniform(1000, 10000, num_samples),
    'public_transport_capacity': np.random.uniform(50, 100, num_samples),
    'demand': np.random.randint(50, 500, num_samples)  # Variable objetivo
}

df = pd.DataFrame(data)

# Mostrar las primeras filas del dataset
print(df.head())

# Guardar el dataset en un archivo CSV
df.to_csv('C:/INGENIERIA CIENCIA DE DATOS/ACTIVIDAD 3/simulated_transport_demand.csv', index=False)
