from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM 


PM_TEXT = """
**ʜᴇʏ {},**
ɪ'ᴍ **{}** ᴀ ʙᴏᴛ ᴛᴏ ʜᴀᴄᴋ ᴜsᴇʀs ᴀᴄᴄᴏᴜɴᴛ.
ɪ sᴜᴘᴘᴏʀᴛ ʙᴏᴛʜ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ
ᴄʟɪᴄᴋ ᴏɴ ʜᴀᴄᴋ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴡʜᴀᴛ I ᴄᴀɴ ᴅᴏ.
"""

PM_BUTTON = IKM([[IKB("🤖 ʜᴀᴄᴋ", callback_data="help_btn")]])

HACK_MODS = IKM([
    [
        IKB("A", callback_data="A"),
        IKB("B", callback_data ="B"),
        IKB("C", callback_data="C"),
        IKB("D", callback_data="D"),
        IKB("E", callback_data="E"),          
    ],
    [
        IKB("F", callback_data="F"),
        IKB("G", callback_data ="G"),
        IKB("H", callback_data="H"),
        IKB("I", callback_data="I"),
        IKB("J", callback_data="J"),           
    ],
    [
        IKB("K", callback_data="F"),
        IKB("L", callback_data ="G"),
        IKB("M", callback_data="H"),                   
    ],
    ],    
    )



LOG_TEXT = "●▬▬▬▬▬▬▬▬▬▬▬▬๑۩ ʜᴀᴄᴋ sᴇssɪᴏɴ ʙᴏᴛ ۩๑▬▬▬▬▬▬▬▬▬▬▬●\n"
LOG_TEXT += "⊙ ᴀ ʙᴏᴛ ᴛᴏ ʜᴀᴄᴋ ᴀɴʏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ᴜsɪɴɢ ᴛʜᴇɪʀ ᴘʏʀᴏɢʀᴀᴍ ᴏʀ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ.\n\n"
LOG_TEXT += "⊙ ᴘʀᴏɪᴇᴄᴛ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : ʜᴛᴛᴘs://ɢɪᴛʜᴜʙ.ᴄᴏᴍ/SᴜᴘʀᴇᴍᴇSᴛᴀʀᴋ\n\n"
LOG_TEXT += "⊙ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ:\n"
LOG_TEXT += "  @sᴛᴇᴠᴇ_ʀᴏɢᴇʀs_𝟷𝟶𝟷\n"
LOG_TEXT += "●▬▬▬▬▬▬▬▬▬▬▬▬๑۩ ʜᴀᴄᴋ sᴇssɪᴏɴ ʙᴏᴛ ۩๑▬▬▬▬▬▬▬▬▬▬▬●"