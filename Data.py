from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
𝑯𝒆𝒚 {}

𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 {}

𝒀𝒐𝒖 𝒄𝒂𝒏 𝒖𝒔𝒆 𝒕𝒉𝒊𝒔 𝒃𝒐𝒕 𝒕𝒐 𝒄𝒐𝒏𝒗𝒆𝒓𝒕
1) 𝑺𝒕𝒊𝒄𝒌𝒆𝒓 𝒕𝒐 𝑰𝒎𝒂𝒈𝒆
2) 𝑰𝒎𝒂𝒈𝒆 𝒕𝒐 𝑺𝒕𝒊𝒄𝒌𝒆𝒓

𝑺𝒆𝒏𝒅 𝑴𝒖𝒍𝒕𝒊𝒑𝒍𝒆 𝒊𝒎𝒂𝒈𝒆𝒔 𝒐𝒓 𝒔𝒕𝒊𝒄𝒌𝒆𝒓𝒔 𝒂𝒏𝒅 𝒊𝒕 𝒘𝒊𝒍𝒍 𝒘𝒐𝒓𝒌 𝒕𝒉𝒆 𝒔𝒂𝒎𝒆

❤️✨
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("📣 Channel", url="https://t.me/Tg_Galaxy")],
        [InlineKeyboardButton(text="🏠 Return Home", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("📣 Channel", url="https://t.me/Galaxy_bots")
        ],
        [
            InlineKeyboardButton("💢 Help", callback_data="help"),
            InlineKeyboardButton("🆘 About", callback_data="about")
        ],
        [InlineKeyboardButton("👥 Group",url="https://t.me/Stdjdjdjkdjjbot")],
        
                              
    ]

    # Help Message
    HELP = """
You Really Need Help ?!?!?!?!

1) Send Sticker to get Image
2) Send Image to get Sticker

Note : You can send any amount of images or stickers or both together at once and it will work with same speed and accuracy.

More features in development. Keep track tar.
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @bots

Source Code : [Click Here](https://github.com/Srooyadustries/StickkolsBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Thanks for using me ☺️
    """
