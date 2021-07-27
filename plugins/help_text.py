import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from translation import Translation

from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["help"]))
async def help_user(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕️ JOIN OUR CHANNEL ⭕️", url="https://t.me/bryll_education")]]),
   )

@Client.on_message(filters.command(["upgrade"]))
async def upgrade(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )

@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕️ CHANNEL ⭕️", url="https://t.me/bryll_education")], [InlineKeyboardButton(text="😇 SUPPORT", url="https://t.me/brylledu"),
                                                    InlineKeyboardButton(text="Donate ♐️", url="https://t.me/bryll_helpdesk_bot")]]),
    )

@Client.on_message(filters.command(["join"]))
async def join(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.JOIN_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="✅ OFFICIAL CHANNEL ✅", url="https://t.me/joinchat/pYITM96MQSs3OTRl")], [InlineKeyboardButton(text="🏹 ARJUNA NEET BATCH CHANNEL 🏹", url="https://t.me/joinchat/Byy3UEQiOGFmYzdl")],
                                                    [InlineKeyboardButton(text="🎯 LAKSHYA NEET BATCH CHANNEL 🎯", url="https://t.me/joinchat/LgoxoX9xbJg3OGE9")], [InlineKeyboardButton(text="🚀 UDAAN RELOADED CHANNEL 🚀", url="https://t.me/joinchat/2sNWupJ4FiMwMmQ1")], [InlineKeyboardButton(text="🙂🙂 YAKEEN BATCH 2022 CHANNEL 🙂🙂", url="https://t.me/joinchat/OV3uy8mueUxmYjM1")], [InlineKeyboardButton(text="🔥 LAKSHYA NEET BATCH 2.0 CHANNEL 🔥", url="https://t.me/joinchat/KUEo0gfLBvwzZjU1")], [InlineKeyboardButton(text="💵💵 EARN FROM TELEGRAM 💵💵", url="https://t.me/bryll_adnetwork_bot")]]),
    )
@Client.on_message(filters.command(["donate"]))
async def donate(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.DONATE_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="💬 OUR HELPDESK 💬", url="https://t.me/bryll_helpdesk_bot")]]),
   )

    @Client.on_message(filters.command(["upload"]))
async def upload(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPLOAD_START,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="✅ OFFICIAL CHANNEL ✅", url="https://t.me/joinchat/pYITM96MQSs3OTRl")], [InlineKeyboardButton(text="🏹 ARJUNA NEET BATCH CHANNEL 🏹", url="https://t.me/joinchat/Byy3UEQiOGFmYzdl")],
                                                    [InlineKeyboardButton(text="🎯 LAKSHYA NEET BATCH CHANNEL 🎯", url="https://t.me/joinchat/LgoxoX9xbJg3OGE9")], [InlineKeyboardButton(text="🚀 UDAAN RELOADED CHANNEL 🚀", url="https://t.me/joinchat/2sNWupJ4FiMwMmQ1")], [InlineKeyboardButton(text="🙂🙂 YAKEEN BATCH 2022 CHANNEL 🙂🙂", url="https://t.me/joinchat/OV3uy8mueUxmYjM1")], [InlineKeyboardButton(text="🔥 LAKSHYA NEET BATCH 2.0 CHANNEL 🔥", url="https://t.me/joinchat/KUEo0gfLBvwzZjU1")], [InlineKeyboardButton(text="💵💵 EARN FROM TELEGRAM 💵💵", url="https://t.me/bryll_adnetwork_bot")]]),
    )
    
@Client.on_message(filters.command(["about"]))
def about(bot, update):
    
    bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True   
    ) 
        
