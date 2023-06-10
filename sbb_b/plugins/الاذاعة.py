from sbb_b import sbb_b

GCAST_BLACKLIST = [
-1001904354189,
-1001904354189,
]

DEVS = [
    6275847466,
    56568,
]


@sbb_b.ar_cmd(pattern="للكروبات(?: |$)(.*)")
async def gcast(event):
    sbb_b = event.pattern_match.group(1)
    if sbb_b:
        msg = sbb_b
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await edit_or_reply(
            event, "**⌔𖢿 يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await edit_or_reply(event, "⌔𖢿 يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔𖢿  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )


@sbb_b.ar_cmd(pattern="للخاص(?: |$)(.*)")
async def gucast(event):
    sbb_b = event.pattern_match.group(1)
    if sbb_b:
        msg = sbb_b
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await edit_or_reply(
            event, "**⌔𖢿 يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await edit_or_reply(event, "⌔𖢿 يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔𖢿  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )
