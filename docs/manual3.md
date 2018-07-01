## winspider的使用2

* 写入一个新爬虫

	如图，将`amz_listing_us_demo`写入pyspider。
    
    ![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/docs/images/20180701155944.png)
    
* 打开爬虫的配置文件夹路径

    如图，点击爬虫名称后的小图标。
    
    ![](https://box.kancloud.cn/5f12d827316b556b4ec10e0a90b78b00_652x92.png)
    
    打开**资源管理器（我的电脑）**，在地址栏中按下粘贴快捷键（`Ctrl + V`），然后回车。资源管理器提示*找不到该文件路径*。
    
    ![](https://box.kancloud.cn/e135a578772c59fd072bb5b80ca73fdd_897x339.png)
    
    回到pyspider的管理页面，更改爬虫的状态，并点击`run`。
    
    ![](https://box.kancloud.cn/9dab13d17c0bb0dbea83dc5d3970b33f_1212x213.png)
    
    ![](https://box.kancloud.cn/8a419d2382c4da05549b94dabf86da4d_1440x216.png)
    
    接着重新在**资源管理器**的地址栏中粘贴刚才复制的路径，然后回车，我们成功的进入了这个爬虫的配置文件夹。
    
    ![](https://box.kancloud.cn/0e08a070a17f1673d419f84cbc15b5ec_904x244.png)
    
    第一次进入配置文件夹失败是因为爬虫需要在首次运行时创建文件夹。因此，在进入文件夹前需提前运行爬虫。  
    
* 添加配置文件
    
    点击`amz_listing_us_demo`的标题链接，可以打开操作帮助。按照操作帮助的提示，我们需要添加配置文件。
    
    ![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/docs/images/20180701160521.png)
    
    ![](https://box.kancloud.cn/63a8f927ad1333c1c569f8e9123aa781_1142x337.png)
    
    ![](https://box.kancloud.cn/6f785a9b4239fc1ca757ce435f44fbcd_523x157.png)
    
	按照操作帮助的说明添加配置文件后，点击`Run`，程序会自动运行您添加的配置文件。然后点击`Result`，来到结果页，我们就可以看到采集结果了。
    
    ![](https://box.kancloud.cn/c0b4e69a01c8712b5e98bd6980308401_1436x197.png)
    
    回到爬虫的配置文件夹，我们发现我们的配置文件不见了，多了一个`recycle`文件夹。在`recycle`文件夹，我们可以看到我们刚才配置的文件。
    
    ![](https://box.kancloud.cn/288145e5f8e59716d1f3ab941b8c8579_776x268.png)
    
    这是因为该爬虫只运行一次配置文件。运行完后，会把它放置到`recycle`文件夹（类似回收站）。如果您需要重新运行爬虫，您可以再添加一次配置文件。
    
    
    
    
    