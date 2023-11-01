from flask import Flask

app = Flask(__name__)

# A SAMPLE PYTHON DATA SET
stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "my item",
                "price": 15.99
            }
        ]
    }
]


@app.get('/store')
def get_stores():
    return {"stores": stores}
