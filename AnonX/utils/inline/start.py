from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝖠𝖽𝖽 𝖬𝖾 𝖨𝗇 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝖧𝖾𝗅𝗉 𝖠𝗇𝖽 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="Settings", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝖠𝖽𝖽 𝖬𝖾 𝖨𝗇 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝖧𝖾𝗅𝗉 𝖠𝗇𝖽 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝖴𝗉𝖽𝖺𝗍𝖾𝗌 📢", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋", url=f"https://t.me/its_dev_telegram",
            )
        ],
        [
            InlineKeyboardButton(
                 text="𝖲𝗈𝗎𝗋𝖼𝖾 𝖢𝗈𝖽𝖾", url="https://telegra.ph/file/b1f8ff56996c3d952fa48.mp4"
            )
         ]
     ]
    return buttons
