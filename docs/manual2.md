## winspider的使用1

* 启动winspider
	打开cmd，在cmd中输入`winspider`并回车，如下图所示：
    
    ![](https://box.kancloud.cn/6151617ddda72989bfd128808f11621e_677x442.png)
    
	使用浏览器打开`http://127.0.0.1:5000/winspider`，您将会进入WinSpider的页面，如下图所示：
	
    ![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/docs/images/20180701154720.png)
    
* 使用爬虫
    
    点击`写入pyspider`，然后点击`返回pyspider`，你将来到**pyspider的管理界面**，如图：
    
    ![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/docs/images/20180701154923.png)
   
    ![](https://box.kancloud.cn/88f9bef53c273b12d2e33215d9e3e094_1439x313.png)
    
* 运行爬虫

	现在您已经有了一个可以运行的爬虫了，只需要把它运行起来就可以了。
    
    首先，你需要更改爬虫的状态，如图，将**status**更改为`running`。
    
    ![](https://box.kancloud.cn/c4c9e8d80042bb426757e850fc66fb80_685x179.png)
    
    然后，点击`run`，如图：
    
    ![](https://box.kancloud.cn/6270743a33bfd7a929b0392ce732abf0_219x103.png)
    
   这时，我们会得到一个警告，提示“知乎已退出登录”。
    
    ![](https://box.kancloud.cn/392df523fc1b762bb6f11e430d0fb1c5_317x185.png)
    
  那是因为我们还没有用Chrome浏览器登录知乎。
  先关闭警告框，使用Chrome登录[知乎](https://www.zhihu.com)。然后，重新点击`run`。稍等一会，接着点击`result`，我们就可以看到采集的结果了，如图。
    
    ![](https://box.kancloud.cn/a8ce60c8ab3990c76446dd157ca2a5c4_215x105.png)
    
    ![](https://box.kancloud.cn/49aedd720537af138094a00159d2ce60_1438x308.png)
    
   **在结果页面的右上角，您可以把采集结果导出。**
   
   
    
    
    
    