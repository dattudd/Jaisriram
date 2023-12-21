from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"𝖢𝗅𝗈𝗌𝖾"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝖠𝖽𝗆𝗂𝗇",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="𝖠𝗎𝗍𝗁",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="𝖡𝖫-𝖴𝗌𝖾𝗋𝗌",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝖡𝗋𝗈𝖺𝖽𝖼𝖺𝗌𝗍",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="𝖦-𝖡𝖺𝗇",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="𝖫𝗒𝗋𝗂𝖼𝗌",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝖯𝗂𝗇𝗀",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="𝖯𝗅𝖺𝗒",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="𝖯𝗅𝖺𝗒𝗅𝗂𝗌𝗍",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝖵𝖢-𝖢𝗁𝖺𝗍𝗌",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="𝖲𝗍𝖺𝗋𝗍",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="𝖲𝗎𝖽𝗈",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝖧𝖾𝗅𝗉 𝖠𝗇𝖽 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
