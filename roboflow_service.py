import requests

API_KEY = "YOUR_API_KEY"

MODEL_ENDPOINT = (
    "https://serverless.roboflow.com"
)

def detect_image(image_path):

    with open(
        image_path,
        "rb"
    ) as image:

        response = requests.post(
            f"{MODEL_ENDPOINT}?api_key={API_KEY}",
            data=image.read()
        )

    return response.json()