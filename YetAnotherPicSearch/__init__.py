from nonebot.plugin import PluginMetadata, inherit_supported_adapters, require

require("nonebot_plugin_waiter")
require("nonebot_plugin_alconna")

from . import __main__ as __main__
from .config import ConfigModel, config
from .data_source import load_search_func

load_search_func()

__version__ = "2.0.10"
__plugin_meta__ = PluginMetadata(
    name="图片搜索",
    description="YetAnotherPicSearch",
    usage="""
*   **群聊：**
    *   发送“搜图”指令及参数时附带或回复图片（推荐）
    *   发送“搜图”指令及参数进入搜图模式
*   可以在同一条消息中包含多张图片，会自动批量搜索
*   搜索图片时可以在消息内包含以下参数：
    *   `--purge` - 无视缓存进行搜图，并更新缓存
    *   指定搜索范围 (以下参数仅可选一个)：
        *   `--all` - 全库搜索 (默认)
        *   `--pixiv` - 从 Pixiv 中搜索
        *   `--danbooru` - 从 Danbooru 中搜索
        *   `--doujin` - 搜索本子
        *   `--anime` - 搜索番剧
        *   `--a2d` - 使用 Ascii2D 进行搜索 (优势搜索局部图能力较强)
        *   `--baidu` - 使用 Baidu 进行搜索
        *   `--ex` - 使用 ExHentai (E-Hentai) 进行搜索
        *   `--google` - 使用 Google 进行搜索
        *   `--iqdb` - 使用 Iqdb 进行搜索
        *   `--yandex` - 使用 Yandex 进行搜索
*   **对于 SauceNAO：**
    *   如果得到的结果相似度低于 60% (可配置)，会自动使用 Ascii2D 进行搜索 (可配置)
    *   如果额度耗尽，会自动使用 Ascii2D 进行搜索
    *   如果搜索到本子，会自动在 ExHentai (E-Hentai) 中搜索并返回链接 (如果有汉化本会优先返回汉化本链接)
    *   如果搜到番剧，会自动使用 WhatAnime 搜索番剧详细信息：
        *   AnimeDB 与 WhatAnime 的结果可能会不一致，是正常现象，毕竟这是两个不同的搜索引擎
        *   同时展示这两个搜索的目的是为了尽力得到你可能想要的识别结果
*   **对于 ExHentai：**
    *   如果没有配置 `EXHENTAI_COOKIES`，会自动回退到 E-Hentai 搜索
    *   不支持单色图片的搜索，例如黑白漫画，只推荐用于搜索 CG、画集、图集、彩色漫画、彩色封面等
    *   如果没有配置 `SUPERUSERS`，不会显示搜索结果的收藏状态
*   **关于消息发送失败的情况：**
    *   在某些国内平台如 QQ 上，这可能是因为消息中包含的链接被列入黑名单，成了所谓的 红链。
    *   需确定哪个网站的域名被封禁了，然后配置 `TO_CONFUSE_URLS` 配置项来规避。
    """,
    type="application",
    homepage="https://github.com/lgc-NB2Dev/YetAnotherPicSearch",
    config=ConfigModel,
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_waiter",
        "nonebot_plugin_alconna",
    ),
    extra={},
)
