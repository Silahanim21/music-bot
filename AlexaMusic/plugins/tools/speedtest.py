# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio
import speedtest
from pyrogram import filters
from strings import get_command
from AlexaMusic import app
from AlexaMusic.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("🙄 İndirme hızını kontrol ediyorum...")
        test.download()
        m = m.edit("🙄 Yükleme hızını kontrol ediyorum...")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("😴 Yükleme hız testi sonuçları yükleniyor...")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("💫 Yükleme ve indirme hızını kontrol etmeye çalışıyorum")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**Hız Testi Sonuçları**
    
<u>**ᴄʟɪᴇɴᴛ:**</u>
**__ɪsᴩ:__** {result['client']['isp']}
**__Ülke:__** {result['client']['country']}
  
<u>**sᴇʀᴠᴇʀ:**</u>
**__İsim:__** {result['server']['name']}
**__Ülke:__** {result['server']['country']}, {result['server']['cc']}
**__sᴩᴏɴsᴏʀ:__** {result['server']['sponsor']}
**__Gecikme:__** {result['server']['latency']}  
**__ᴩɪɴɢ:__** {result['ping']}"""
    msg = await app.send_message(
        chat_id=message.chat.id, photo=result["share"], text=output
    )
    await m.delete()
