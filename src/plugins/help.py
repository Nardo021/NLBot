from nonebot import on_command

help_text = "NLBot Help Menu"

help = on_command("help", priority=0)

@help.handle()
async def handle_city():
    await help.finish(help_text)