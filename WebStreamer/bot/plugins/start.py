

from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, Send me a file to get an instant stream link.',
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('ᴄʜᴀɴɴᴇʟ', url='https://t.me/Rex_Botz'),
                    InlineKeyboardButton('ɢʀᴏᴜᴘ', url='https://t.me/Rex_Bots_Support')
                ],
                [
                    InlineKeyboardButton('ᴅᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/Benwolf24'),
                    InlineKeyboardButton('ᴏᴛʜᴇʀ ʙᴏᴛs', url='https://t.me/Rex_Botz/94/')
                ]
            ]
        )
                  )

@StreamBot.on_message(filters.command(['help']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, Send me a file to get an instant stream link. \nI am Fastest Download Link Generator Bot. \nJoin :- @Rex_Botz',
                  )
