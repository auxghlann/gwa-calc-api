from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def root():
    return {
        "Hello": "World",
        "About": {
            "description": "This is an API for my GWA Calculator project",
            "author": "Allan Mesa",
            "other_names": [
                "Quokka",
                "auxghlann"
            ],
            "email": "khestermesa@gmail.com"
        }
    }