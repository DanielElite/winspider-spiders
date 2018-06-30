## 安装Python

安装winspider前，首先要安装python。WinSpider的运行环境为python3，推荐python3.5及以上环境。这里给出[python3.5.3的安装包](https://www.python.org/ftp/python/3.5.3/python-3.5.3.exe)，方便大家下载。

> 注意：安装过程中一定要选择`Add Python 3.5 to PATH`，其他地方使用默认设置即可。

如图所示：

![](https://box.kancloud.cn/1d6e5a046403871266aab6a0c6e51ba2_480x295.png)

> python3.5的系统最低要求为Windows 7 Service Pack 1。如果您的电脑安装不上python3.5，您可以选择python3.5的以下版本。

### python3.5以下版本的安装

这里推荐的Python版本为[Python3.4.3(点击下载)](https://www.python.org/ftp/python/3.4.3/python-3.4.3.msi)。

安装截图如下图所示，其他地方使用默认设置即可。

![](https://box.kancloud.cn/7b0bdcc60682a9378cefacaa78b1120c_499x429.png)

![](https://box.kancloud.cn/a8ff03ffba84121c8cbd00aed64ab29f_499x429.png)

> 在最后的一个步骤里，一定要把`Add python.exe to Path`选中

![](https://box.kancloud.cn/b6d95d7a89e25503de361c33e276a526_557x411.jpg)

安装完python3.4后，还需要安装一个python的扩展包[pywin32(点击下载)](https://www.winspider.cn/static/ext/pywin32-221.win32-py3.4.zip)，安装过程中使用默认设置即可。**python3.5不需要安装这个扩展包**。

### 验证安装是否成功

* 打开cmd
	按下`WIN+R`组合键，弹出**运行窗口**，在输入栏中输入`cmd`，然后点击回车，如下图所示。
    
    ![](https://box.kancloud.cn/9dee3c7d93e2276853fc0b4ad20941fe_402x229.png)
    
    ![](https://box.kancloud.cn/b46d0d11e1024b2d40176425404926e5_812x443.png)
   	
	**请记住cmd的打开方法，因为在您使用winspider的过程中会经常和cmd打交道**
   
* 检测pip命令是否生效
 	在cmd中输入如下命令
	~~~
	pip list
	~~~
	如下图所示，您会在屏幕上看到以下提示。如果您安装的是python3.4且安装了pywin32，那么您会在提示中会看到`pywin32`。
    
    ![](https://box.kancloud.cn/a2b39da267016a0317610434e0d66b82_619x114.png)

* 如果您使用的是python3.4，您还需要操作以下两个步骤，python3.5可以跳过

    1. 升级pip
		在cmd中输入如下命令
        ~~~
        python -m pip install -U pip
        ~~~
    2. 安装pycurl
    	在cmd中输入如下命令
        ~~~
       	pip install https://files.pythonhosted.org/packages/14/cd/0be81b9eaa7bce0d13b981fda7a33c3537e862119258d08f58c636b51475/pycurl-7.43.0-cp34-none-win32.whl
        ~~~
 
 成功完成以上操作后，Python的安装就完成了。

## 安装winspider

打开cmd，输入如下命令即可完成安装。

~~~
pip install winspider
~~~




