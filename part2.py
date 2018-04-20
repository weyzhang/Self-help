#!/bin/env python
#-*- coding: utf-8 -*-

from print_style import UseStyle

def queue():


    core_content = '可用队列查询'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * 查询命令： qload -w
    * q_sw_*** 表示国产计算平台队列
    * q_x86_*** 表示商用计算平台队列
    * CONFIG： 队列总节点个数； IDLE: 队列空闲节点个数；BUSY： 队列已占用节点个数；sleep: 队列休眠节点个数(可用)
    '''
    print '\t' + UseStyle(content)

    core_content = '测试队列注意事项'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * q_sw_expr  q_x86_expr 为测试队列
    * 测试队列中的程序只能运行 1 小时，超过 1 小时系统会自动杀题
    * q_sw_expr 只能使用 16 个节点，即 16*4 核心
    * q_x86_expr 只能使用 3 个节点，即 24*3 核心

    * 如需增加时长以及节点数，请联系商务购买正式计算队列
    '''
    print '\t' + UseStyle(content)
    core_content = 'sunway --help 获得更多帮助'
    print '\n' +  UseStyle(core_content,   mode='bold')

    others = '''
    (更为详细的介绍，请查阅无锡超算官网“上机指南”中相关文档)
    '''
    print UseStyle(others)


def bsub_x86():

    abstract = '前台作业提交:'
    print '\n' + UseStyle(abstract)

    core_content = '''
    bsub -I -q q_x86_expr -n 1 ./a.out para1 para2
    '''
    print '\t' + UseStyle(core_content,   mode='bold'),

    content = '''
    * -I 表示交互式提交，程序输出会打印到屏幕，屏幕关闭，作业会终止
    * -q 队列名。队列名可通过 "qload -w" 命令查看
    * -n 进程数
    * ./a.out 可执行程序
    * para1 para2 可执行程序所需的参数
    '''
    print '\t' + UseStyle(content)

    abstract = '后台作业提交:'
    print '\n' + UseStyle(abstract)

    core_content = '''
    bsub -q q_x86_expr -n 1 -o runlog ./a.out para1 para2
    '''
    print '\t' + UseStyle(core_content,   mode='bold'),

    content = '''
    * 去掉 -I 选项即提交到后台
    * -o 表示把程序输出打印到runlog文件中
    '''
    print '\t' + UseStyle(content)


    notes_title = '其他事项:'
    notes = '''
    * q_x86_expr 队列为测试队列，只能运行1小时,只能使用16个节点，其中1个节点24核心，因可以运行16*24个进程
    * 更多有关于bsub的使用说明，请查阅无锡超算官网->上机指南->"神威太湖之光系统快速使用指南"
    '''
    print '\n' + UseStyle(notes_title)
    print '\t' + UseStyle(notes)

    core_content = 'sunway --help 获得更多帮助'
    print '\n' +  UseStyle(core_content,   mode='bold')

    others = '''
    (更为详细的介绍，请查阅无锡超算官网“上机指南”中相关文档)
    '''
    print UseStyle(others)

def bsub_sw():

    abstract = '前台作业提交:'
    print '\n' + UseStyle(abstract)

    core_content = '''
    bsub -I -b -q q_sw_expr -n 1 -cgsp 64 -share_size 4096 -host_stack 128 ./a.out para1 para2
    '''
    print '\t' + UseStyle(core_content,   mode='bold'),

    content = '''
    * -I 表示交互式提交，程序输出会打印到屏幕，屏幕关闭，作业会终止
    * -b 表示从核函数栈变量放在从核局部存储上，该选项为获取加速性能必须的提交选项
    * -q 队列名，队列名可通过 "qload -w" 命令查看
    * -n 进程数，使用主核数
    * -cgsp 使用从核个数
    * -share_size 指定核组共享空间大小，一般最大可以用到 7600MB
    * -host_stack 指定主核栈空间大小，默认为 8M，一般设置为 128MB 以上
    * ./a.out 可执行程序
    * para1 para2 可执行程序所需的参数
    '''
    print '\t' + UseStyle(content)

    abstract = '后台作业提交:'
    print '\n' + UseStyle(abstract)

    core_content = '''
    bsub -b -q q_sw_expr -n 1 -o runlog -cgsp 64 -share_size 4096 -host_stack 128 ./a.out para1 para2
    '''
    print '\t' + UseStyle(core_content,   mode='bold'),

    content = '''
    * 去掉 -I 选项即提交到后台
    * -o 表示把程序输出打印到runlog文件中
    * 其他选项与上述相同
    '''
    print '\t' + UseStyle(content)


    others = '''
    (更多有关于bsub的使用说明，请参考无锡超算官网->上机指南->"神威太湖之光系统快速使用指南)"
    '''
    print UseStyle(others)

    core_content = 'sunway --help 获得更多帮助'
    print '\n' +  UseStyle(core_content,   mode='bold')

    others = '''
    (更为详细的介绍，请查阅无锡超算官网“上机指南”中相关文档)
    '''
    print UseStyle(others)

def compiler_sw():

    core_content = '基础编译器'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * c语言编译器：

            主核: sw5cc -host
            从核: sw5cc -slave
            混合链接: sw5cc -hybrid

    * c++编译器：

            主核: sw5CC -host
            从核: 不支持
            混合链接: sw5CC -hybrid

    * Fortran:

            主核: sw5f90 -host
            从核: sw5f90 -slave
            混合链接: sw5f90 -hybrid

    * 使用示例：

            sw5cc -host -c master.c
            sw5cc -slave -c slave.c (纯主核程序可省略该步骤)
            sw5cc -hybrid master.o slave.o -o test

    '''
    print '\t' + UseStyle(content)

    core_content = '并行编译器'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * C语言编译器: mpicc
    * C++编译器: mpiCC
    * Fortran编译器: mpif90
    '''
    print '\t' + UseStyle(content)

    core_content = 'OpenACC编译器'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * C语言编译器: swacc
    * Fortran编译器: swafort
    '''
    print '\t' + UseStyle(content)

    core_content = '常用编译选择'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * -OPT:IEEE_arith=2  浮点异常
    '''
    print '\t' + UseStyle(content)

    core_content = 'sunway --help 获得更多帮助'
    print '\n' +  UseStyle(core_content,   mode='bold')

    others = '''
    (更为详细的介绍，请查阅无锡超算官网“上机指南”中相关文档)
    '''
    print UseStyle(others)

def compiler_x86():

    core_content = 'Intel基础编译器'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * Fortran: ifort
    * C语言: icc
    * C++： icpc
    '''
    print '\t' + UseStyle(content)

    core_content = 'Intel并行编译器'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * Fortran: mpiifort
    * C语言: mpiicc
    * C++： mpiicpc
    '''
    print '\t' + UseStyle(content)
    core_content = 'sunway --help 获得更多帮助'
    print '\n' +  UseStyle(core_content,   mode='bold')

    others = '''
    (更为详细的介绍，请查阅无锡超算官网“上机指南”中相关文档)
    '''
    print UseStyle(others)

def job():

    core_content = 'bjobs -- 作业状态查询'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * 执行 bjobs 可以查询作业号以及运行状态
    * bjobs -l 作业号 可查询更多详细信息
    '''
    print '\t' + UseStyle(content)

    core_content = 'bkill + 作业号 -- 杀作业 '
    print '\n' +  UseStyle(core_content,   mode='bold')

    core_content = 'cnload -- 节点状态查询 '
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * cnload -c 节点号，如：cnload -c 1,2-10,20
    * cnload -c 节点号 -l（小写L）
    * bjobs回车，查看jobid占用的节点，复制cpuid，通过cnload -c jobid查看节点CPU，内存，负载状态
    * 节点处于softft/hartft/down/boot为异常状态
    * 节点处于N/A|BUSY|SBUSY|sleep|sleeping为正常状态
    '''

    print '\t' + UseStyle(content)
    core_content = 'sunway --help 获得更多帮助'
    print '\n' +  UseStyle(core_content,   mode='bold')

    others = '''
    (更为详细的介绍，请查阅无锡超算官网“上机指南”中相关文档)
    '''
    print UseStyle(others)

def download():

    core_content = '数据上传下载'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * 支持采用ftp，rsync，scp等主流文件传输协议
    * 协议地址为登陆地址，端口22，用户自己的账号密码认证。命令使用方式自行检索
    * 上传数据的路径为用户根目录下的软链接online1/2或GPFS
    * 用户需要将数据传输到账号根目录下的online1,online2或GPFS目录内，否则会因家目录大小限制而上传异常
    '''
    print '\t' + UseStyle(content)

    core_content = '大量数据上传下载'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * 用户有大量数据上传下载时，可快递硬盘至无锡超算进行内网传输，内网传输速率为 100MB/s-120MB/s

    * 快递地址：江苏省无锡市滨湖区吟白路1号。收件人和联系方式在技术支持群索取。无锡超算将数据寄回时均为【到付】

    * 建议使用USB3.0移动硬盘，SATA接口硬盘，各类USB接口存储设备
    * 移动硬盘或存储设备的文件系统可为Linux主流文件系统或NTFS文件系统，不支持ios文件系统

    * 用户需要便签说明数据上传或者下载的【账号】和【路径】
    '''
    print '\t' + UseStyle(content)

    core_content = '用户与用户之间数据传输与共享'
    print '\n' +  UseStyle(core_content,   mode='bold')
    content = '''
    * 用户修改自己的目录为755，即可共享自己的目录或文件于他人
    * 用户可使用scp实现账号之间的数据拷贝

    * scp axx@psn002:~/online1/a.txt  ./  从axx账号拷贝文件到当前目录, psn002为登录节点名称，请根据实际登录情况选择相应登录节点

    * 用户可通过创建软链接的形式实现数据共享
    '''
    print '\t' + UseStyle(content)

    core_content = 'sunway --help 获得更多帮助'
    print '\n' +  UseStyle(core_content,   mode='bold')

    others = '''
    (更为详细的介绍，请查阅无锡超算官网“上机指南”中相关文档)
    '''
    print UseStyle(others)

def memory():

    core_content = 'online1 存储查询'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * lfs quota -h -u username /home/export/online1【查看用户的online1存储使用】
    * lfs quota -h -g groupname /home/export/online1 【查看组的online1存储使用】
    '''
    print '\t' + UseStyle(content)


    core_content = 'GPFS 存储查询'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * mmlsquota -u username【查看用户存储使用情况】
    * mmlsquota -g groupname【查看组存储使用情况】
    '''
    print '\t' + UseStyle(content)

    core_content = '查看家目录大小'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * 输入cd命令，回车，回到家目录
    * 输入du -sh命令，回车，统计家目录大小
    '''
    print '\t' + UseStyle(content)

    core_content = '注意事项'
    print '\n' +  UseStyle(core_content,   mode='bold')

    content = '''
    * 测试账号磁盘限额为 1T
    * 存储资源不仅包括磁盘限额（Block Limits），也包括文件数目（File Limits）
    * 存储磁盘限额超额，必定会影响【文件操作】和【作业提交和运行】
    * 超额之后，请删除废弃数据和旧数据，或联系商务洽谈存储收费扩容
    '''
    print '\t' + UseStyle(content)


    core_content = 'sunway --help 获得更多帮助'
    print '\n' +  UseStyle(core_content,   mode='bold')

    others = '''
    (更为详细的介绍，请查阅无锡超算官网“上机指南”中相关文档)
    '''
    print UseStyle(others)
