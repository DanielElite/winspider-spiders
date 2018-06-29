### 详细说明

**采集字段**：

| 字段  | 描述  |
| ------------ | ------------ |
| rating  | 评分  |
| title  | 评论标题  |
|  url | 评论的链接  |
| author  | 评论人昵称  |
| asin | ASIN  |
|  child_asin |  子ASIN |
|  review_date | 评论日期  |
| color  | 商品颜色  |
| verified_purchase  |  是否认证购买 |
| review_text  | 评论内容  |
| w_comments  |  回复个数 |
| review_votes  |  投票个数 |
| review_id  |  评论id |


**触发频率**：每3分钟触发一次

**任务(采集结果)有效期**：半小时

**截图**：

![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/docs/images/adca687b32be2b5a6cb2d44401441b37_s.png)

### 注意事项

- 本爬虫需要Chrome的支持，请事先安装Chrome

### 操作帮助

***本爬虫需要自己配置采集文件***

请在爬虫的配置文件夹中任意新建一个`txt文件`，将`asin列表`填入其中，如下图所示。**程序解析完该txt文件后，不会删除文件，而会重复采集您配置的文件**。

![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/docs/images/d62823848f654a645833268d6cc42f0a.png)

### 相关爬虫
无