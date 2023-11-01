from flask import Flask, request

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

# GET STORE


@app.get('/store')
def get_stores():
    return {"stores": stores}


@app.post('/store')
def create_store():
    request_data = request.get_json()
    new_store = {'name': request_data['name'], 'items': []}
    stores.append(new_store)
    return new_store, 201
