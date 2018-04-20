#!/bin/env python
#-*- coding: utf-8 -*-

from print_style import UseStyle


def hardware():

    core_content = '国产计算平台'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * 峰值计算性能： 125PetaFlops， 适合有源代码的科学与工程计算
    * 申威 26010 处理器个数： 40960（每个处理器 260 核,每个处理器含 4 个核组）
    * 申威 26010 处理器核组数： 163840
    * 一般情况下，一个核组可以运行 1 个进程和 64 个线程
    * 1 个核组 = 1 个主核 + 64 个从核（基本收费单位）
    '''
    print '\t' + UseStyle(content)

    core_content = '商用计算平台'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * 980 个普通计算节点：2路12核心 E5-2680V3 处理器,每个节点 128GB DDR4 内存
    * 32 个胖计算节点：每个节点包含 8 路 16 核 E7-8860V3 处理器，主频 2.2GHz,每个节点 1024GB DDR4 内存
    * GPU 节点,每个节点包含 2 路 8 核心 E5-2630V3 处理器（ 128GB DDR4 内存）,每个节点一块 K40 计算加速卡（ 具有 2880 个流处理器， 显存 12GB）
    '''
    print '\t' + UseStyle(content)

    core_content = 'sunway --help 获得更多帮助'
    print '\n' +  UseStyle(core_content,   mode='bold')

    others = '''
    (更为详细的介绍，请查阅无锡超算官网“上机指南”中相关文档)
    '''
    print UseStyle(others)

def software():


    core_content ='软件列表查询及使用方法'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * 已安装软件列表请查询官网  http://www.nsccwx.cn/soft.php?word=soft&&i=47
    * 部分软件使用方法请查询官网 http://www.nsccwx.cn/detail.php?word=process&&i=55&id=335
    * 更多软件的使用方法请联系技术支持
    '''
    print '\t' + UseStyle(content)

    core_content = '软件移植'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * 请先自行尝试移植所需软件，如遇到问题，可再与技术支持人员讨论交流
    '''
    print '\t' + UseStyle(content)

    core_content = 'sunway --help 获得更多帮助'
    print '\n' +  UseStyle(core_content,   mode='bold')

    others = '''
    (更为详细的介绍，请查阅无锡超算官网“上机指南”中相关文档)
    '''
    print UseStyle(others)

def access():


    core_content = 'VPN登录'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * VPN登录遇到异常，请先检查电脑外网连接是否正常
    * VPN有共有人数上限，如需提高上限，请联系技术支持
    '''
    print '\t' + UseStyle(content)

    core_content = '主机登录'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * 超算平台有登录节点、计算节点之分；程序、数据等文件要放在 online1 或者 GPFS 目录，计算节点才能访问到

    * 登录节点为用户提供一个登陆系统的平台，用户可以通过internet网络登录VPN，然后通过ssh终端登录到登陆节点上
    * 登录节点用户可以进行软件编译与调试、环境变量配置作业提交、文件编辑、结果查看等操作
    * 登录节点禁止用户直接运行计算程序
    * 登录节点有三个 psn002 psn004 psn010，一般情况下重复登录三次可切换到另外一个登录节点

    * 计算节点本身没有本地硬盘，挂载共享存储，具备软件运行所需的运行环境
    * 用户程序、数据等文件要放在 online1 或者 GPFS 目录，计算节点才能访问到
    * 计算程序需通过bsub作业管理系统提交到计算节点运行

    '''
    print '\t' + UseStyle(content)

    core_content = 'sunway --help 获得更多帮助'
    print '\n' +  UseStyle(core_content,   mode='bold')

    others = '''
    (更为详细的介绍，请查阅无锡超算官网“上机指南”中相关文档)
    '''
    print UseStyle(others)

def contact():


    core_content = '微信联系'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * 微信号： nsccwx_tech / 180 1235 0507
    '''
    print '\t' + UseStyle(content)

    core_content = '超算官网及论坛'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * http://www.nsccwx.cn
    '''
    print '\t' + UseStyle(content)
    core_content = 'sunway --help 获得更多帮助'
    print '\n' +  UseStyle(core_content,   mode='bold')

    others = '''
    (更为详细的介绍，请查阅无锡超算官网“上机指南”中相关文档)
    '''
    print UseStyle(others)
