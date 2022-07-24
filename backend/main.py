#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-07-24 10:29:55
# @Author  : kentsin (kentsin@gmail.com)
# @Link    : link
# @Version : 0.0.1

from fastapi import FastAPI
from core.config import settings
from apis.general_pages.route_homepage import general_pages_router

def include_router(app):
    app.include_router(general_pages_router)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    return app

app = start_application()

#@app.get("/")
#def hello_api():
#    return {"msg":"Hello API"}
