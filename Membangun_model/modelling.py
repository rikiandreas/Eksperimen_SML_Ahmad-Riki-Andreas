
import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ✅ WAJIB INI (INI YANG KAMU KURANG)
mlflow.set_tracking_uri("http://127.0.0.1:5000/")
mlflow.set_experiment("Iris Classification")

# load data
df = pd.read_csv("Membangun_model/iris_preprocessing.csv")

X = df.drop("target", axis=1)
y = df["target"]

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# autolog
mlflow.sklearn.autolog()

with mlflow.start_run():

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print("Accuracy:", accuracy)
