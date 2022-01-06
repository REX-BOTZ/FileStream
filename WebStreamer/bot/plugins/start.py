

from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, \nI can Convert a Telegram File to Stream Link Also Known as Direct Download Link. \nSend /help to Know More About Me. \n© @Rex_Botz',
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
    await m.reply(f'Hi {m.from_user.mention(style="md")}, \n✪ Send me a file to get an instant stream link. \n✪ I am Fastest Download Link Generator Bot. \n✪ I can Convert Telegram File to Link. \n\nJoin :- @Rex_Botz',
                 quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('ᴘᴏᴡᴇʀᴇᴅ ʙʏ', url='https://t.me/FluxPlay'),
                    InlineKeyboardButton('ɢʀᴏᴜᴘ', url='https://t.me/Rex_Bots_Support')
                ],
                [
                    InlineKeyboardButton('ᴅᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/Benwolf24'),
                    InlineKeyboardButton('ᴏᴛʜᴇʀ ʙᴏᴛs', url='https://t.me/Rex_Botz/94/')
                ]
            ]
        )
                 )
