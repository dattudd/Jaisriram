from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="❄️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ❄️",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="♡ Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ ♡",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✨ sᴇᴛᴛɪɴɢs ✨", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="❄️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ❄️",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="♡ Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ ♡", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="☃˹ꜱᴜᴘᴘᴏʀᴛ˼☃", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="♪˹ᴜᴘᴅᴀᴛᴇꜱ˼♪", url=f"https://t.me/its_dev_telegram",
            )
        ],
        [
            InlineKeyboardButton(
                 text="☠Sᴏᴜʀᴄᴇ☠", url="https://telegra.ph/file/b1f8ff56996c3d952fa48.mp4"
            )
         ]
     ]
    return buttons
