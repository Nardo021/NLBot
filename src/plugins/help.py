from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot

help_text = "NLBot 帮助菜单\nhelp: 获取帮助\n命令前缀: /"

help = on_command("help", priority=0)

@help.handle()
async def _(bot:Bot):
    await help.finish(help_text)