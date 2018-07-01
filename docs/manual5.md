## 保存Chrome的UserAgent

**User Agent**中文名为用户代理，简称 UA，它是一个特殊字符串头，使得服务器能够识别客户使用的操作系统及版本、CPU 类型、浏览器及版本、浏览器渲染引擎、浏览器语言、浏览器插件等。

在数据采集的过程中，有些网站会根据UserAgent判断用户的登录状态，或者判断网页请求是不是来自爬虫。因此，UserAgent在数据采集时很重要。有些爬虫会在**注意事项**中标明需要提前保存UserAgent，如下图。

![](https://box.kancloud.cn/fb25bf295255e939c71a38f8a88011e1_470x126.png)

* 如何保存Chrome的UserAgent

	使用cmd打开winspider，然后使用Chrome（**一定是Chrome**）访问 http://127.0.0.1:5000/winspider ，接着点击`保存Chrome的UserAgent`。
    
    ![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/docs/images/20180701162729.png)
    
## 调节爬虫的采集速度（rate/burst）

在数据采集过程中，过快的访问速度会给服务器带来很大的压力，甚至会让服务器奔溃。因此，基本上所有网站都不大欢迎爬虫，会用各种办法限制爬虫的访问，例如跳出验证码、封锁IP地址。

winspider虽然会共享爬虫，只是希望能方便大家收集数据，却不希望给其他网站带来访问上的压力。因此，**我们倡议用户在采集过程中尽量放慢采集的速度**。

* 如何调节爬虫的访问速度

	首先需要了解两个名词的含义，rate与burst。
    
    **rate**：每秒执行多少个请求，其倒数（1/rate）为多少秒发送一个请求，*建议小于1*。
	**burst**：并发数，*建议为1*。
    **栗子**：rate/burst = 0.1/3，意思是爬虫10秒爬一个页面。但是开始时前三个任务会同时时行，不会等10秒，第四个任务爬取前会等10秒． 
    
   如图，直接访问pyspider的管理界面 http://127.0.0.1:5000 ，然后点击爬虫的`rate/burst`，直接在文本框里修改即可。
   
   ![](https://box.kancloud.cn/0cccda8f748ba7d8e2de339e7a5d81a4_491x53.png)
    
## pyspider控制台的使用说明
可参考[该网站](http://www.pyspider.cn/article/12.html)。



