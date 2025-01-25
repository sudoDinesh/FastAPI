from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()



@app.get('/')
def test():
    return 'test'

 
@app.get('/blog')
def index(limit=10, published:bool=True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} blogs from db'}
    

@app.get('/blog/{id}')
def blog(id:int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': [1,2]}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data' : f'blog is created with {request.title}'}



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port=9000)