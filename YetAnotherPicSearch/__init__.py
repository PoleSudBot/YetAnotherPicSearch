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
    *   发送“搜图”指令及参数时附带或回复图片（推荐）
    *   发送“搜图”指令及参数进入搜图模式
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
