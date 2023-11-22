# Lesson 1、Linux环境与CMake

## $\color{red}{以下红色内容为验收内容}$

>  **Linux**是一套免费使用和自由传播的类Unix操作系统，是一个多用户、多任务、支持多线程和多CPU的操作系统。它能运行主要的UNIX工具软件、应用程序和网络协议。它支持32位和64位硬件。Linux继承了Unix以网络为核心的设计思想，是一个性能稳定的多用户网络操作系统。

尽管为大家提供了这些资料，但是大家仍要具有查阅资料的能力，希望大家实践过程中遇到问题，多多查阅资料，查阅资料也是一种能力。



## 任务一：linux系统

> 如果已经拥有linux系统（双系统或者wsl），可以跳过此任务，如果未使用过linux或者采用的是虚拟机，则仍需要完成此任务！

操作系统*（英语：Operating System，缩写：OS）*是一组主管并控制计算机操作、运用和运行硬件、软件资源和提供公共服务来组织用户交互的相互关联的系统软件程序。根据运行的环境，操作系统可以分为桌面操作系统，手机操作系统，服务器操作系统，嵌入式操作系统等。

**推荐双系统，也可以使用WSL2**

**双系统**：一台机器上同时存在两个操作系统，启用之后只有一个系统在工作，能够最大限度的发挥硬件性能，并且对于外设支持十分友好。

**WSL**：WSL 是 Windows Subsystem for Linux 的缩写，意思是 linux 版的 window 子系统。顾名思义，本身实在windows上的运行linux子系统。

[Windows安装Ubuntu双系统（Win11+最新Ubuntu22.04.1LTS）-CSDN博客](https://blog.csdn.net/syluxhch/article/details/128071404?ops_request_misc=%7B%22request%5Fid%22%3A%22169701668116800180684883%22%2C%22scm%22%3A%2220140713.130102334.pc%5Fall.%22%7D&request_id=169701668116800180684883&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~times_rank-4-128071404-null-null.142^v96^pc_search_result_base2&utm_term=安装双系统&spm=1018.2226.3001.4187)

[如何在Windows11上安装WSL2的Ubuntu22.04（包括换源）_wsl2换源_syqkali的博客-CSDN博客](https://blog.csdn.net/syqkali/article/details/131524540?ops_request_misc=%7B%22request%5Fid%22%3A%22169701672416800186513365%22%2C%22scm%22%3A%2220140713.130102334.pc%5Fall.%22%7D&request_id=169701672416800186513365&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~times_rank-1-131524540-null-null.142^v96^pc_search_result_base2&utm_term=安装WSL2&spm=1018.2226.3001.4187)

**$\color{red}{任务要求：可以参考上述资料，在自己的机器上配置双系统或者使用WSL2，拥有自己的linux系统}$**



## 任务二：了解linux文件系统

阅读下面这一页笔记：

[Linux 系统目录结构 | 菜鸟教程 (runoob.com)](https://www.runoob.com/linux/linux-system-contents.html)



## 任务三：linux命令

回答最常用的命令位于哪个目录下（参考任务二）

[史上最牛的Linux视频教程—兄弟连_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1mW411i7Qf/?spm_id_from=333.337.search-card.all.click&vd_source=d3e5165825082cd17457aab2378b8f54)

[Linux命令大全(手册) – 真正好用的Linux命令在线查询网站 (linuxcool.com)](https://www.linuxcool.com/)

**$\color{red}{任务要求：参考上述内容，使用命令行在 主目录 也就是 ~ 下，使用mkdir新建一个任务文件夹，使用cd进入该文件夹，使用touch新建cpp代码文件，编写helloword代码，使用gcc编译，执行可执行文件，能够正确输出。（能够自己查阅不熟悉的命令）}$**



## 任务四：CMake简单实践

`cmake` 是一个强大的自动化配置工具，它是开源的，跨平台的，它通过读取脚本文件——`CMakeLists.txt` 中的规则来构建编译系统。

简单入门阅读：

[cmake：入门 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/87283287)

在任务三中的文件夹中新建一个build文件夹以及CMakeLists.txt文件，新建README.md

该任务对应的目录结构如下：

```
|-CMakeLists.txt
|-helloworld.cpp
|-helloworld			# 任务三中使用gcc编译的生成的helloworld可执行文件
|-build
|-README.md				# 存放工程的说明文档
```

**该任务的目录结构要特别注意，如果不在build文件里编译，则会显得杂乱**

**熟悉该任务，后续各种安装环境，例如opencv等，以及调试过程中经常用到**

**$\color{red}{任务要求：参考上述资料，使用CMake编译任务三中的helloworld代码，然后cd进入build目录，使用cmake .. 命令，然后使用make命令生成执行文件}$**



## 任务五：使用编译安装OpenCV

OpenCV(开源的计算机视觉库)，可以安装4.5.0 -> 最新4.8.1（随意选择一个版本即可）

[ubuntu22.04 OpenCV4.6.0(c++)环境配置_ubuntu22.04安装opencv4.6.0_路飞DoD的博客-CSDN博客](https://blog.csdn.net/qq_51022848/article/details/128095476)

1. 锻炼大家安装第三方库的能力（c++大多数第三方库都会采用类似的方法进行安装）
2. 为任务六准备环境



## 任务六：CMake实践

下载群文件的segment.zip

填空，完成segment文件下的CMakeLists.txt文件

在build文件夹下成功cmake ..，make，成功生成可执行文件

**$\color{red}{任务要求：查阅CMake资料，能够在build文件夹下成功编译并运行可执行文件，不报错}$**



