from flask import Flask

# 'app' should match file name
app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

# 'flask run' to start app
@app.get("/store") # http://127.0.0.1:5000/store
def get_stores():
    return {"stores": stores}
