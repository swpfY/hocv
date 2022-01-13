#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@IDE            : PyCharm
@Time           : 2022/1/13 2:18 PM
@Author         : JQS
@File           : img_operate.py
@Introduction   : 图像处理操作
"""

import cv2
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


def lblur(src):
    """
    均值模糊
    :param src: 输入图片
    """
    ksize = int(config['blur']['ksize'])
    return cv2.blur(src, (ksize, ksize))


def get_gray(src):
    """
    提取灰度图
    :param src: 输入图片
    """
    return cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)


def pixelated(src):
    """
    像素化
    :param src: 输入图片
    """
    height, width = src.shape[:2]
    size = int(config['pixel']['size'])
    w, h = (size, size)
    temp = cv2.resize(src, (w, h), interpolation=cv2.INTER_LINEAR)
    return cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)


if __name__ == '__main__':
    input = cv2.imread('./test/input/1.png')
    output = lblur(input)
    cv2.imshow('output' ,output)
    cv2.waitKey(0)