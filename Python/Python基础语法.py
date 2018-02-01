#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：Python基础语法


# # 行和缩进 
# 学习python与其他语言最大区别就是，python的代码块不使用代码块{}控制类，函数，以及其他逻辑判断，python最具特色的就是用缩进来写模块。
# # 缩进的空白数量是可变的，但是多有代码块语句必须包含相同的缩进空白数量，这个必须严格执行，如下：
# if False:
#    print "Answer"
#    print "True"
# else:
# 	print "Answer2"
# 	print "False"


# # 多行语句 
# Python语句中一般以新行作为语句的结束符。但是可以使用 斜杠（\）将一行的语句分为多行显示，如：
# total = "item_one" + \
# "item_two" +  \
# "item_three"
# print(total);

# # 语句中包含[],{},()就不需要使用多行连接符
# days = ["Mon" + "Tus" + 
# "Wed" + "Thu"]
# print (days);


# python引号 
# python可以使用引号（'），双引号(")，三引号('''或"")，引号的开始与结束必须是相同类型，其中三引号可以由多行组成，编写多行文本的快捷语法，常用语文档字符串，在文件的特定地点，被当做注释。
# word = 'word'
# sentence = "这是一个句子"
# paragragp = """这是一个段落"""
# print word,sentence,paragragp


# python注释
# python中单行注释采用#开头
"""python多行注释采用三个单引号或
三个双引号"""


# python空行


# 等待用户输入
# raw_input ("按下 enter 退出，其他任意键显示... \n")


# 同一行显示多条语句 用；隔开
import sys; x = 'runoob11'; sys.stdout.write(x + '\n')
print sys.argv




















