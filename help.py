#!/bin/env python
#-*- coding: utf-8 -*-

from print_style import UseStyle


def sunway_help():

    abstract = '欢迎使用无锡超算平台自助问答系统'
    print '\n\t\t\t' + UseStyle(abstract)

    abstract = '使用方法：'
    print  '\n' + UseStyle(abstract)
    abstract = 'sunway [选项]; 例如: sunway access'
    print  '\n\t' + UseStyle(abstract,mode='bold')
    abstract = '选项说明：'
    print  '\n' + UseStyle(abstract)
    abstract = '01. hardware -- 无锡超算平台硬件资源介绍'
    print  '\n\t' + UseStyle(abstract),
    abstract = '02. software -- 无锡超算平台软件资源介绍'
    print  '\t' + UseStyle(abstract)
    abstract = '03. access -- 登录及基本使用方式'
    print  '\t' + UseStyle(abstract),
    abstract = '04. contact -- 技术联系与反馈'
    print  '\t\t' + UseStyle(abstract)

    abstract = '05. queue -- 计算队列查询与注意事项'
    print  '\n\t' + UseStyle(abstract),
    abstract = '06. bsub_sw -- 提交作业到国产平台'
    print  '\t\t' + UseStyle(abstract,fore='red')
    abstract = '07. bsub_x86 -- 提交作业到商用平台'
    print  '\t' + UseStyle(abstract,fore='red'),
    abstract = '08. compiler_sw -- 国产平台编译器信息'
    print  '\t\t' + UseStyle(abstract)
    abstract = '09. compiler_x86 -- 商用平台编译器信息'
    print  '\t' + UseStyle(abstract),
    abstract = '10. job -- 作业状态查询与管理、节点状态查询'
    print  '\t\t' + UseStyle(abstract)
    abstract = '11. download -- 数据传输与下载'
    print  '\t' + UseStyle(abstract),
    abstract = '12. memory -- 存储查询'
    print  '\t\t\t' + UseStyle(abstract)

    abstract = '13. bsub_error -- 作业提交时常见问题及解决方法'
    print  '\n\t' + UseStyle(abstract),
    abstract = '14. run_error -- 程序运行时常见问题及解决方法'
    print  '\t' + UseStyle(abstract)
    abstract = '15. others_error -- 其他问题及解决方法'
    print  '\t' + UseStyle(abstract),
    abstract = '16. more  -- 更多资料获取途径'
    print  '\t\t' + UseStyle(abstract)

#    core_content = '''
#    bsub -I -q q_x86_expr -n 1 ./a.out para1 para2
#    '''
#    print '\t' + UseStyle(core_content,   mode='bold'),
#
#    content = '''
#    * -I 表示交互式提交，程序输出会打印到屏幕，屏幕关闭，作业会终止
#    * -q 队列名。队列名可通过 "qload -w" 命令查看
#    * -n 进程数
#    * ./a.out 可执行程序
#    * para1 para2 可执行程序所需的参数
#    '''
#    print '\t' + UseStyle(content)
#
#    abstract = '后台作业提交:'
#    print '\n' + UseStyle(abstract)
#
#    core_content = '''
#    bsub -q q_x86_expr -n 1 -o runlog ./a.out para1 para2
#    '''
#    print '\t' + UseStyle(core_content,   mode='bold'),
#
#    content = '''
#    * 去掉 -I 选项即提交到后台
#    * -o 表示把程序输出打印到runlog文件中
#    '''
#    print '\t' + UseStyle(content)
#
#
#    notes_title = '其他事项:'
#    notes = '''
#    * q_x86_expr 队列为测试队列，只能运行1小时,只能使用16个节点，其中1个节点24核心，因可以运行16*24个进程
#    * 更多有关于bsub的使用说明，请查阅无锡超算官网->上机指南->"神威太湖之光系统快速使用指南"
#    '''
#    print '\n' + UseStyle(notes_title)
#    print '\t' + UseStyle(notes)
