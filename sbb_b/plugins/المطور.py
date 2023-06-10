from telethon import Button, events

from sbb_b import sbb_b 

from ..Config import Config

ROZ_PIC = "https://telegra.ph/file/89e5316364eeb1e17e554.jpg"
RAZAN = Config.TG_BOT_USERNAME
ROZ_T = (
    f"**مطور سورس حياه **\n"
  
)

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("المطور") and event.query.user_id == bot.uid:
            buttons = [
                [
                    Button.url("𓏺᭙ɦᎥ᥉ƙᥱᥡ", "https://t.me/bp_bp"),
                    Button.url("𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼", "https://t.me/HL_BG"),
                    
                ]
            ]
            
            if ROZ_PIC and ROZ_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    ROZ_PIC, text=ROZ_T, buttons=buttons, link_preview=False
                )
            elif ROZ_PIC:
                result = builder.document(
                    ROZ_PIC,
                    title="JMTHON - sbb_b",
                    text=ROZ_T,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="JMTHON - sbb_b",
                    text=ROZ_T,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@sbb_b.ar_cmd(pattern="المطور")
async def repo(event):
    RR7PP = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(RR7PP, "المطور")
    await response[0].click(event.chat_id)
    await event.delete()


# edit by ~ @sbb_b
