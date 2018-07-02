### 详细说明

**采集字段**：

| 字段  | 描述  |
| ------------ | ------------ |
| url  | 当前页面的链接 |
| category  | 当前榜单的类目名称  |
|  asin | ASIN  |
| img  | 商品的图片链接  |
| ranking | 商品的排名  |
|  review_count |  商品的评论个数 |
|  review_rating | 商品的评分  |
| price  | 商品的价格  |
| title  |  商品的标题 |
| percent_change  |  商品排名上升百分比 |
| sales_movement  |  商品排名变动 |


**触发频率**：每3分钟触发一次

**任务(采集结果)有效期**：60分钟

**截图**：

![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/docs/images/20180702085357.png)

### 注意事项

- 本爬虫需要Chrome的支持，请事先安装Chrome

### 操作帮助

***本爬虫需要自己配置采集文件***

请在爬虫的配置文件夹中任意新建一个`txt文件`，将需要采集的`bestseller链接`填入其中，如下图所示。**程序解析完该txt文件后，不会删除文件，而会重复采集该文件**。

![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/docs/images/20180702085328.png)

### 相关爬虫
无