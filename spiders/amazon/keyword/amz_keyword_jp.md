### 详细说明

**采集字段**：

| 字段  | 描述  |
| ------------ | ------------ |
| keyword  | 搜索关键词  |
| page  | 搜索关键词页面的第几页  |
|  serial | 当前商品在页面中的序号  |
| img  | 当前商品图片链接  |
| asin | ASIN  |
|  review_count |  当前商品的评论个数 |
|  review_rating | 当前商品的评分  |
| price  | 当前商品的价格  |
| title  |  当前商品的标题 |
| brand  | 当前商品的品牌  |
| is_ad  |  是否为广告 |
| is_bestseller  |  是否为Bestseller |


**触发频率**：每3分钟触发一次

**任务(采集结果)有效期**：10分钟

**截图**：

![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/docs/images/20180701215807.png)

### 注意事项

- 本爬虫需要Chrome的支持，请事先安装Chrome
- 本爬虫只采集搜索关键词页面的前10页

### 操作帮助

***本爬虫需要自己配置采集文件***

请在爬虫的配置文件夹中任意新建一个`txt文件`，将`keyword`填入其中，如下图所示。**程序解析完该txt文件后，不会删除文件，而会重复采集该文件**。

![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/docs/images/20180701215913.png)

### 相关爬虫
无