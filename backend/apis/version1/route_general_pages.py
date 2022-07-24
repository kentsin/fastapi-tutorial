#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-07-24 10:44:12
# @Author  : kentsin (kentsin@gmail.com)
# @Link    : link
# @Version : 0.0.1

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()

@general_pages_router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("general_pages/homepage.html", {"request":request})

@general_pages_router.get("/about")
async def home(request: Request):
    return templates.TemplateResponse("general_pages/about.html", {"request":request})