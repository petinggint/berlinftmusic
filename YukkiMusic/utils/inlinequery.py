#
# Copyright (C) 2024-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="ᴘᴀᴜsᴇ sᴛʀᴇᴀᴍ",
            description=f"ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ.",
            thumb_url="https://files.catbox.moe/ditwxi.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="ʀᴇsᴜᴍᴇ sᴛʀᴇᴀᴍ",
            description=f"ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴘᴀᴜsᴇᴅ sᴏɴɢ ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ.",
            thumb_url="https://files.catbox.moe/ditwxi.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="ᴍᴜᴛᴇ sᴛʀᴇᴀᴍ",
            description=f"ᴍᴜᴛᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴏɴɢ ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ",
            thumb_url="https://files.catbox.moe/ditwxi.jpg",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="ᴜɴᴍᴜᴛᴇ sᴛʀᴇᴀᴍ",
            description=f"ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴏɴɢ ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ",
            thumb_url="https://files.catbox.moe/ditwxi.jpg",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="sᴋɪᴘ sᴛʀᴇᴀᴍ",
            description=f"sᴋɪᴘ ᴛᴏ ɴᴇxᴛ ᴛʀᴀᴄᴋ. | sᴋɪᴘ ᴛᴏ ɴᴇxᴛ ᴛʀᴀᴄᴋ. | ғᴏʀ sᴘᴇᴄɪғɪᴄ ᴛʀᴀᴄᴋ ɴᴜᴍʙᴇʀ: /skip [number] ",
            thumb_url="https://files.catbox.moe/ditwxi.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="ᴇɴᴅ sᴛʀᴇᴀᴍ",
            description="sᴛᴏᴘ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴏɴɢ ᴏɴ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇᴄʜᴀᴛ.",
            thumb_url="https://files.catbox.moe/ditwxi.jpg",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="sʜᴜғғʟᴇ sᴛʀᴇᴀᴍ",
            description="sʜᴜғғʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ʟɪsᴛ.",
            thumb_url="https://files.catbox.moe/ditwxi.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="sᴇᴇᴋ sᴛʀᴇᴀᴍ",
            description="sᴇᴇᴋ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ ᴛᴏ ᴀ sᴘᴇᴄɪғɪᴄ ᴅᴜʀᴀᴛɪᴏɴ.",
            thumb_url="https://files.catbox.moe/ditwxi.jpg",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="ʟᴏᴏᴘ sᴛʀᴇᴀᴍ",
            description="ʟᴏᴏᴘ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ. ᴜsᴀsɢᴇ: /loop [enable|disable]",
            thumb_url="https://files.catbox.moe/ditwxi.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
