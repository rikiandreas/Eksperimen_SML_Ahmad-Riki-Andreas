
import requests

data = {
    "dataframe_records": [
        {
            "sepal length (cm)": 5.1,
            "sepal width (cm)": 3.5,
            "petal length (cm)": 1.4,
            "petal width (cm)": 0.2
        }
    ]
}

r = requests.post(
    "http://127.0.0.1:5001/invocations",
    json=data
)

print(r.json())
