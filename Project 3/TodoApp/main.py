import uvicorn
from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos, admin, users

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# app.include_router(auth.router)
app.include_router(todos.router)
# app.include_router(admin.router)
# app.include_router(users.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
