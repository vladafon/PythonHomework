from fastapi import FastAPI
from fastapi.responses import JSONResponse
import faker

import logging

logger = logging.getLogger(__name__)

app = FastAPI()

faker.Faker.seed()
_faker = faker.Faker()

@app.route('/')
async def handler(*args):

    logger.error((args))
    return JSONResponse({
        'data':_faker.address()
    })