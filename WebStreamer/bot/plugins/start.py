

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
                    InlineKeyboardButton('📌  Support Group', url='https://t.me/InFoTelGroup'),
                    InlineKeyboardButton('🔖  Projects Channel', url='https://t.me/TGBotsZ')
                ],
                [
                    InlineKeyboardButton('💡  Source Code', url='https://github.com/TGExplore/Screenshot-Bot'),
                    InlineKeyboardButton('👨  Master', url='https://t.me/odbots')
                ]
            ]
        )
                  )

@StreamBot.on_message(filters.command(['help']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, Send me a file to get an instant stream link. \nI am Fastest Download Link Generator Bot. \nJoin :- @Rex_Botz',
                  )
