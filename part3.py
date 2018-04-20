#!/bin/env python
#-*- coding: utf-8 -*-

from print_style import UseStyle

def bsub_error():


    core_content = '1. current cwd is "/home/export/base/xxx/yyy", canot submit job on fs base, job not submitted'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * 家目录无法提交作业，切换至全局文件系统(online1,online2,GPFS)的工作目录提交
    '''
    print '\t' + UseStyle(content)

    core_content = '2. Disk quota exceeded'
    print '\n' +  UseStyle(core_content,   mode='bold')
    content = '''
    * 家目录因存放大量文件导致磁盘限额超出1G出错
    * 删除家目录下的文件【注：不要删除online1,online2,GPFS软链接】
    * 清空隐藏目录.rmsbatch下的文件
    '''
    print '\t' + UseStyle(content)

    core_content = '3. Job submit failed, Access/permission denied'
    print '\n' +  UseStyle(core_content,   mode='bold')
    content = '''
    * 因无队列权限提交失败
    * qload -w 查看具有权限的队列
    * 查看提交命令中的队列名是否正确
    '''
    print '\t' + UseStyle(content)

    core_content = '4. job submit failed, ret = -19, reason: No enough compute nodes'
    print '\n' +  UseStyle(core_content,   mode='bold')
    content = '''
    * 查看是否将使用国产编译器编译的程序提交到q_x86_xxx，即x86架构处理的平台,或者反之
    '''
    print '\t' + UseStyle(content)

    core_content = '5. job submit failed, ret = -40, reason: Exceed user avail resource quota.'
    print '\n' +  UseStyle(core_content,   mode='bold')
    content = '''
    * 因超出队列资源限制提交失败
    * 使用qlimit -l（小写L） 队列名 | grep 用户名 查看用户在该队列的资源限制
    * 调整核心数，重新提交
    '''
    print '\t' + UseStyle(content)

    core_content = '6. 交互式提交后长时间PEND或dispatch.'
    print '\n' +  UseStyle(core_content,   mode='bold')
    content = '''
    * 超出队列可使用资源限制。执行bjobs -l jobid 查看原因为Pend reason<RMS_USER_QUOTA_ERROR>
    * bjobs -l jobid 查看其他原因
    * 用户查看队列可使用资源，见第5点
    '''
    print '\t' + UseStyle(content)

    core_content = 'sunway --help 获得更多帮助'
    print '\n' +  UseStyle(core_content,   mode='bold')

    others = '''
    (更为详细的介绍，请查阅无锡超算官网“上机指南”中相关文档)
    '''
    print UseStyle(others)

def run_error():


    core_content = '1. plugin_load_from_file:dlopen(/usr/sw-slurm/slurm-16.05.3/lib/slurm/auth_munge.so):libmunge.so.2:cannont open shared object file: No such file or directory'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * 用户需要重新提交作业；联系管理员确认；需向管理员提供jobid，便于定位问题原因
    '''
    print '\t' + UseStyle(content)

    core_content = '2. Transport endpoint is not connectd'
    print '\n' +  UseStyle(core_content,   mode='bold')
    content = '''
    * 该节点文件系统传输断开，联系管理员确认
    '''
    print '\t' + UseStyle(content)

    core_content = '3. ......'
    print '\n' +  UseStyle(core_content,   mode='bold')
    content = '''
    * ......
    '''
    print '\t' + UseStyle(content)


    core_content = 'sunway --help 获得更多帮助'
    print '\n' +  UseStyle(core_content,   mode='bold')

    others = '''
    (更为详细的介绍，请查阅无锡超算官网“上机指南”中相关文档)
    '''
    print UseStyle(others)

def others_error():

    core_content = '1. 登陆节点卡顿排查'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * ......
    '''
    print '\t' + UseStyle(content)

    core_content = 'sunway --help 获得更多帮助'
    print '\n' +  UseStyle(core_content,   mode='bold')

    others = '''
    (更为详细的介绍，请查阅无锡超算官网“上机指南”中相关文档)
    '''
    print UseStyle(others)

def more():

    core_content = '无锡超算官网 \n\t\t\t   http://www.nsccwx.cn '
    print '\n\t\t\t\t' +  UseStyle(core_content,   mode='bold')

    content = '''\n * 官网上机指南中，有文档、视频、demo等多种形式的资料，建议使用前先查阅相关资料
    '''
    print UseStyle(content)
