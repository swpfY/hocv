#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@IDE            : PyCharm
@Time           : 2022/1/13 2:17 PM
@Author         : JQS
@File           : main.py
@Introduction   : 主函数
"""

import gradio as gr
import img_operate as img


def main():
    gr.Interface(fn=[img.lblur, img.get_gray, img.pixelated], inputs='image', outputs='image').launch()
