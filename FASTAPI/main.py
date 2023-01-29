# uvicorn main:app --reload
# Execute in the same directory
# --reload -> reloads when there is a change in the code 

import typing
import fastapi as fast
import pydantic # Shema validation, creates models

app = fast.FastAPI()

class Post(pydantic.BaseModel):
    title: str
    content: str
    published: bool = True # Set a default value for a field
    rating: typing.Optional[int] = None # Make a field optional, it will not exist if none provided

my_posts = {
    1: {
        'title': 'title of post 1',
        'content': 'content of the post 1'
    },
    2: {
        'title': 'title of post 2',
        'content': 'content of the post 2',
    }
}

@app.get('/')
async def root():
    return {'message': 'Hello World!'}

@app.get('/posts')
async def review():
    return {'data': my_posts}

@app.get('/posts/{id}') # {ID} -> Path Parameter
async def get_post(id: int): # Check
    return {
        'message': 'Successful',
        'post': my_posts[id]
        }

@app.post('/posts')
async def post(post: Post):
    post_dict = post.dict()
    my_posts[len(my_posts) + 1] = post_dict
    return {
        'message': 'Successful!'
        }  

