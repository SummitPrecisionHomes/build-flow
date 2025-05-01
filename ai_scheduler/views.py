from django.shortcuts import render
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_schedule(request):
    # Dummy data: [weather_score, material_delay_days] -> completion_days
    X = np.array([[1, 0], [2, 1], [3, 2]])
    y = np.array([10, 12, 15])
    model = LinearRegression()
    model.fit(X, y)

    # Example prediction
    current_conditions = np.array([[2, 1]])
    predicted_days = model.predict(current_conditions)[0]

    return render(request, 'ai_scheduler/predict.html', {'days': predicted_days})