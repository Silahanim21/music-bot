# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="🙄 ᴩᴀᴜsᴇ 🙄",
            description=f"Şu anda çalan akışı duraklat.",
            thumb_url="https://envs.sh/SoF.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="😋 ʀᴇsᴜᴍᴇ 😋",
            description=f"Duraklatılmış akışı devam ettir.",
            thumb_url="https://envs.sh/SoF.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="🙂 sᴋɪᴩ 🙂",
            description=f"Şu anda çalan akışı atla ve bir sonraki akışa geç.",
            thumb_url="https://envs.sh/SoF.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="🥺 ᴇɴᴅ 🥺",
            description="Şu anda çalan akışı sonlandır.",
            thumb_url="https://envs.sh/SoF.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="🥴 sʜᴜғғʟᴇ 🥴",
            description="Oynatma listesinde sıradaki şarkıları karıştır.",
            thumb_url="https://envs.sh/SoF.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="🥱 ʟᴏᴏᴩ 🥱",
            description="Şu anda çalan parçayı döngüye al.",
            thumb_url="https://envs.sh/SoF.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
