

from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, Send me a file to get an instant stream link.',
         disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="help_data"),
                    InlineKeyboardButton("sᴛᴀʀᴛ", callback_data="start_data"),
                ],
                [
                    InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Benwolf24")
                ]
            ]
        ),
        reply_to_message_id=message.message_id       
                  )

@StreamBot.on_message(filters.command(['help']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, Send me a file to get an instant stream link. \nI am Fastest Download Link Generator Bot. \nJoin :- @Rex_Botz',
                  )
