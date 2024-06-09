import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Cargar el dataset
df = pd.read_csv('C:/INGENIERIA CIENCIA DE DATOS/ACTIVIDAD 3/simulated_transport_demand.csv')

# Preprocesamiento
df = pd.get_dummies(df, columns=['day_of_week', 'event'], drop_first=True)

# Separar características y variable objetivo
X = df.drop('demand', axis=1)
y = df['demand']

# Dividir el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predecir y evaluar el modelo
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

print(f'error absoluto promedio: {mae}')
