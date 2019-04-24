#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
class VectorOp(object):
    '''
    实现向量计算操作
    '''
    @staticmethod
    def dot(x, y):
        '''
        计算两个向量x和y的内积
        '''
        # 首先把x[x1,x2,x3...]和y[y1,y2,y3...]按元素相乘
        # 变成[x1*y1, x2*y2, x3*y3...]
        # 然后利用reduce求和
        return reduce(lambda a,b : a+b, VectorOp.element_multiply(x, y), 0.0)

    @staticmethod
    def element_multiply(x, y):
        '''
        将两个向量x和y按元素相乘
        '''
        # 首先把x[x1,x2,x3...]和y[y1,y2,y3...]打包在一起
        # 变成[(x1,y1), (x2,y2), (x3,y3)...]
        # 然后利用map函数计算[x1*y1, x2*y2, x3*y3]
        return list(map(lambda (a,b): a*b, zip(x,y)))

    @staticmethod
    def element_add(x, y):
        '''
        将两个向量x和y按元素相加
        '''
        # 首先把x[x1,x2,x3...]和y[y1,y2,y3...]打包在一起
        # 变成[(x1,y1), (x2,y2), (x3,y3)...]
        # 然后利用map函数计算[x1+y1, x2+y2, x3+y3]
        return list(map(lambda (a,b): a+b, zip(x,y)))

    @staticmethod
    def scala_multiply(v, s):
        '''
        将向量v中的每个元素和标量s相乘
        '''
        return map(lambda e: e*s, v)

if __name__ == '__main__':
    x= [1,2,3]
    y= [1,2,4]
    s= 2
    print VectorOp.dot(x,y)
    print VectorOp.element_multiply(x,y)
    print VectorOp.element_add(x,y)
    print VectorOp.scala_multiply(x,s)