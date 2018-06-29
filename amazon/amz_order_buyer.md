### 详细说明

本爬虫匹配了亚马逊(美国)卖家中心的顾客和订单，匹配方法可参考[该链接](https://jingyan.baidu.com/article/f0e83a2561f5e922e5910126.html "该链接")。

**采集字段**：

| 字段  | 描述  |
| ------------ | ------------ |
|  order_id | 订单id  |
|  buyer_id | 卖家id  |

**触发频率**：每3分钟触发一次

**任务(采集结果)有效期**：24个小时

**截图**：

![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/images/c709ee11850d822642386b680259e32d_s.jpg)

![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/images/8e5a3e61a2271dda9529aea69c719135_s.jpg)


### 注意事项

- 本爬虫需要Chrome的支持，请事先安装Chrome
- 使用过程中请确保亚马逊(美国)卖家中心处于登录状态
- 本爬虫需要您提前保存Chrome的UserAgent

`爬虫的运行环境为电脑本地，不会造成店铺关联，请放心使用`

### 操作帮助

***本爬虫需要自己配置采集文件***

请在爬虫的配置文件夹中任意新建一个`txt文件`，将`订单id(orderid)`列表填入其中，如下图所示。**程序解析完该txt文件后，会删除文件，不会保留。如需再次采集，请重新配置采集文件**。

![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/images/0ad1a8daf65cc8b9e041335a946940ac.png)

### 相关爬虫
无