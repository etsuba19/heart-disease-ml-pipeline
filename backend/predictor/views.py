import os
import json
import joblib
import pandas as pd

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

logistic_model = joblib.load(
    os.path.join(BASE_DIR, "models_ml/logistic_heart_model.joblib")
)

dt_model = joblib.load(
    os.path.join(BASE_DIR, "models_ml/dt_heart_model.joblib")
)

from django.shortcuts import render

def home(request):
    return render(request, "predictor/index.html")


@csrf_exempt
def predict_logistic(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=405)

    try:
        data = json.loads(request.body)
        df = pd.DataFrame([data])

        prediction = logistic_model.predict(df)[0]
        probability = logistic_model.predict_proba(df)[0].tolist()

        return JsonResponse({
            "model": "Logistic Regression",
            "prediction": int(prediction),
            "probability": probability
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@csrf_exempt
def predict_tree(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=405)

    try:
        data = json.loads(request.body)
        df = pd.DataFrame([data])

        prediction = dt_model.predict(df)[0]

        return JsonResponse({
            "model": "Decision Tree",
            "prediction": int(prediction)
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)



from django.shortcuts import render

def home(request):
    return render(request, "predictor/index.html")
