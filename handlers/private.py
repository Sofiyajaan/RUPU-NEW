
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**Hᴇʏ ɪᴛs {bn}** \n
**I ᴀᴍ ʟᴀᴢʏ Aʙᴏᴜᴛ ᴛʏᴘɪɴɢ sᴏᴍᴇᴛʜɪɴɢ ɴᴇᴡ..ɪᴛᴢ ᴀ ʙᴏᴛ ᴍᴀᴅᴇ ғᴏʀ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ Vᴄ.😈❣️
Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ : [ʟ•4•ʟᴜᴄᴋʏ](https://t.me/cute_boy701)**.
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💞 ᴏᴡɴᴇʀ ", url="https://t.me/cute_boy701")
                  ],[
                    InlineKeyboardButton(
                        "🔥Aɴʏ Pʀᴏʙʟᴇᴍ ", url="https://t.me/maxopeditz"
                    ),
                    InlineKeyboardButton(
                        "🐬 Gʀᴏᴜᴘ ", url="https://t.me/terayaarhoomai"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Aᴅᴅ ᴍʏ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴅᴀʀʟɪɴɢ🤭", url=f"https://t.me/luckyybbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("alive") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""Bᴏᴛ ᴏɴ Fᴏʀᴍ ʙᴀʙʏ 😈""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😎 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/terayaarhoomai")
                ]
            ]
        )
   )
