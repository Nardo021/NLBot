from nonebot import on_command

menu_text = "NLBot 菜单\n——————————————————————\n指令前缀：“/”\n——————————————"



menu = on_command("菜单", priority=0)
menu2 = on_command("menu", priority=0)


@menu.handle()
async def handle_city():
    await menu.finish(menu_text)
    
@menu2.handle()
async def handle_city():
    await menu2.finish(menu_text)