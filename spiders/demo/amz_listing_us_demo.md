### 详细说明

**采集字段**：

| 字段 | 描述 |
| ------------ | ------------ |
| title  | 商品标题  |
| star  |  商品评分 |
| reviews_count | 评论个数 |
| questions_count | question个数  |

**触发频率**：3分钟触发一次

**任务(采集结果)有效期**：半小时

**截图**：

![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/docs/images/cffd49b16c29a143bd6084689c39995e_s.png)

### 注意事项

- 本爬虫需要Chrome的支持，请事先安装Chrome

### 操作帮助

***本爬虫需要自己配置采集文件***

请在爬虫的配置文件夹中任意新建一个`txt文件`，将`asin列表`填入其中，如下图所示。**程序解析完该txt文件后，会删除文件，不会保留**。如需再次采集，请重新配置采集文件。

![](https://raw.githubusercontent.com/zebra-cl/winspider-spiders/master/docs/images/d62823848f654a645833268d6cc42f0a.png)

### 相关爬虫
无
