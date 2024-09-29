# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AlexaMusic.utils.database import is_on_off
from AlexaMusic import app


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Özel Sohbet"
        logger_text = f"""
**━━━━━━━━━━━━━━━**
**💞 {MUSIC_BOT_NAME} music logs **
**━━━━━━━━━━━━━━━**
**🌹️ Sohbet Adı : >** {message.chat.title} [`{message.chat.id}`]
**━━━━━━━━━━━━━━━**
**🥀 İsim : ›** {message.from_user.mention}
**━━━━━━━━━━━━━━━**
**🌸 Kullanıcı Adı : ›** @{message.from_user.username}
**━━━━━━━━━━━━━━━**
**🌷 𝐈𝐃  : ›** `{message.from_user.id}`
**━━━━━━━━━━━━━━━**
**🌿 Sohbet Bağlantısı: >** {chatusername}
**━━━━━━━━━━━━━━━**
**🌻 Aranan:** {message.text}
**━━━━━━━━━━━━━━━**
**💐 akış türü:** {streamtype}
**━━━━━━━━━━━━━━━**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
