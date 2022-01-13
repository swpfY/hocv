#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@IDE            : PyCharm
@Time           : 2022/1/13 6:58 PM
@Author         : JQS
@File           : __init__.py.py
@Introduction   : __init__
"""

import gradio as gr
import hocv.img_operate as img


def index():
    gr.Interface(fn=[img.lblur, img.get_gray, img.pixelated], inputs='image', outputs='image').launch()
