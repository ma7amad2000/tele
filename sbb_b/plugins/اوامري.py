import re

from telethon import Button, events
from telethon.events import CallbackQuery

from sbb_b import sbb_b
from razan.CMD.aomari import *

from ..Config import Config
from ..core import check_owner

ROE = """** اهلا بك عزيزي المستخدم في قائمة اوامر حياه 
من هنا يمكنك تصفح جميع الاوامر المتاحة **"""

ROZADM = "من هنا يمكنك ايجاد جميع"
RAZAN = Config.TG_BOT_USERNAME

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await sbb_b.get_me()
        if query.startswith("اوامري") and event.query.user_id == sbb_b.uid:
            buttons = [
                [Button.inline("معلومات حياه ", data="AOMRDB")],
                [
                    Button.inline("البوت", data="BOTCMD4"),
                    Button.inline("الكروب", data="admincmd_s"),
                ],
                [
                    Button.inline("التسلية", data="TASLIACMD"),
                    Button.inline("الاداوات", data="toolsed1"),
                ],
                [
                    Button.inline("التحميل", data="DOWMANLODE4"),
                    Button.inline("الصيد/وعد", data="CEHKUSERNAME"),
                ],
                [
                    Button.inline("الاكسترا", data="EXTRACMD"),
                    Button.inline(" الفارات", data="VARJMTHON"),
                ],
            ]
            result = builder.article(
                title="sbb_b",
                text=ROE,
                buttons=buttons,
                link_preview=False,
            )
        await event.answer([result] if result else None)


@sbb_b.ar_cmd(pattern="اوامري")
async def repo(event):
    start = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await sbb_b.inline_query(start, "اوامري")
    await response[0].click(event.chat_id)
    await event.delete()


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"MAIN")))
@check_owner
async def _(event):
    butze = [
        [Button.inline("معلومات سبايدر", data="AOMRDB")],
        [
            Button.inline("البوت", data="BOTCMD4"),
            Button.inline("الكروب", data="admincmd_s"),
        ],
        [
            Button.inline("التسلية", data="TASLIACMD"),
            Button.inline("الاداوات", data="toolsed1"),
        ],
        [
            Button.inline("التحميل", data="DOWMANLODE4"),
            Button.inline("الصيد/وعد", data="CEHKUSERNAME"),
        ],
        [
            Button.inline("الاكسترا", data="EXTRACMD"),
            Button.inline(" الفارات", data="VARJMTHON"),
        ],
    ]
    await event.edit(ROE, buttons=butze)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"CEHKUSERNAME")))
async def varssett(event):
    await event.edit(
        "من هنا يمكنك عرض شروحات اوامر الصيد وبوت وعد:",
        buttons=[
            [
                Button.inline("اوامر الصيد", data="chekuserq"),
                Button.inline("بوت وعد", data="waadcmdbot"),
            ],
            [Button.inline("القائمة الرئيسية", data="MAIN")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"waadcmdbot")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="CEHKUSERNAME")]]
    await event.edit(waadcmdbot, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"chekuserq")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="CEHKUSERNAME")]]
    await event.edit(chekusername, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"VARJMTHON")))
async def varssett(event):
    await event.edit(
        "من هنا يمكنك عرض شروحات الفارات:",
        buttons=[
            [
                Button.inline("فارات الفحص", data="alivevar"),
                Button.inline("فارات الحماية", data="pmvars"),
            ],
            [Button.inline("فارات البروفايل", data="namevar")],
            [Button.inline("القائمة الرئيسية", data="MAIN")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"namevar")))
async def varssett(event):
    await event.edit(
        "من هنا يمكنك عرض شروحات فارات الاسم والبايو والخ:",
        buttons=[
            [
                Button.inline("اسم حسابك", data="nameprvr"),
                Button.inline("زخرفة الارقام", data="numlokvar"),
            ],
            [
                Button.inline("نبذة حسابك", data="biolokvar"),
                Button.inline("صورة حسابك", data="phovarlok"),
            ],
            [
                Button.inline("رمز الاسم", data="symnamvar"),
            ],
            [Button.inline("رجوع", data="VARJMTHON")],
            [Button.inline("القائمة الرئيسية", data="MAIN")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"symnamvar")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات البروفايل
الفار الحالي: فار الرمز

الامر:             `.وضع الرمز`

الشرح :  يقوم هذا الامر بوضع رمز بداية اسم حسابك عند تشغيل امر  .اسم وقتي
الاستخدام : تقوم بالرد على الرمز بالامر   `.وضع الرمز`

**ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة**| : 𖢿
اوامر فارات سورس حياه @HL_BG""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"phovarlok")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات البروفايل
الفار الحالي: فار الصورة

الامر:             `.وضع الصورة`

الشرح :  يقوم هذا الامر بوضع الصورة الخاصة بحسابك عند تشغيل امر الصورة الوقتية
الاستخدام : تقوم بالرد على رابط الصورة بالامر   `.وضع البايو`
*يمكنك استخدا الزخرفة او اللغة الانكليزية او العربية الخ..

* كيفية جلب رابط الصورة؟
-بالرد على الصورة المراد استخراج منها الرابط ب  `.تلكراف ميديا`
**ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة**| : 𖢿
اوامر فارات سورس حياه @HL_BG""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"AOMRDB")))
async def varssett(event):
    await event.edit(
        """اهلا بك في قائمة اوامر سورس حياه هذه بعض المعلومات عن حياه :

- سورس حياه يمتلك اكثر من 100 أمر 
- حياه ليس افضل سورس لان زدثون هوا افضل سورس ولكن يتميز بالحماية

قـنـاة الـسـورس : @HL_BG

مـطـور الـسـورس : @BP_BP""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"biolokvar")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات البروفايل
الفار الحالي: فار البايو

الامر:             `.وضع البايو`

الشرح :  يقوم هذا الامر بوضع النبذه او البايو عند تشغيل امر البايو الوقتي
الاستخدام : تقوم بالرد على البايو بالامر   `.وضع البايو`

*يمكنك استخدا الزخرفة او اللغة الانكليزية او العربية الخ..
**ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة**| : 𖢿
اوامر فارات سورس حياه @HL_BG""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"numlokvar")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات البروفايل
الفار الحالي: فار الزخرفة

`.زخرفة الوقت 1`| : 𖢿
`.زخرفة الوقت 2`| : 𖢿
.زخرفة الوقت 3`| : 𖢿
`.زخرفة الوقت 4`| : 𖢿
`.زخرفة الوقت 5`| : 𖢿
`.زخرفة الوقت 6`| : 𖢿
`.زخرفة الوقت 7`| : 𖢿
`.زخرفة الوقت 8`| : 𖢿
`.زخرفة الوقت 9`| : 𖢿

**ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة**| : 𖢿
اوامر فارات سورس حياه @HL_BG""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"nameprvr")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات البروفايل
الفار الحالي: فار الاسم| : 𖢿

الامر:             `.وضع الاسم`

الشرح :  يقوم هذا الامر بوضع اسم حسابك للعديد من الاوامر مثل الفحص والخ
الاستخدام : تقوم بالرد على اسمك بالامر   `.وضع الاسم`

*يمكنك استخدا الزخرفة او اللغة الانكليزية او العربية الخ..
**ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة**| : 𖢿
اوامر فارات سورس حياه @HL_BG""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"pmvars")))
async def varssett(event):
    await event.edit(
        "من هنا يمكنك عرض شروحات فارات الحماية:",
        buttons=[
            [
                Button.inline("صورة الحماية", data="picpmvar"),
                Button.inline("كليشة الحماية", data="pmvarkish"),
            ],
            [
                Button.inline("كليشة الحظر", data="banklish"),
                Button.inline("عدد التحذيرات", data="warnvars"),
            ],
            [Button.inline("رجوع", data="VARJMTHON")],
            [Button.inline("القائمة الرئيسية", data="MAIN")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"banklish")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات الحماية
الفار الحالي: فار كليشة الحظر

الامر:             `.وضع كليشة الحظر`

الشرح :  يقوم هذا الامر بتغيير الكليشة (الكلام) التي تظهر عندما تنتهي تحذيرات الشخص ويتم حظره
الاستخدام : تقوم بالرد على الكليشة التي تريد وضعها بالامر   `.وضع كليشة الحظر `

* يمكنك كتابة اي كليشة مثلا: عزيزي المستخدم تم حظرك 
****ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة**| : 𖢿**| : 𖢿
اوامر فارات سورس حياه @HL_BG""",|
        buttons=[
            [Button.inline("رجوع", data="pmvars")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"warnvars")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات الحماية
الفار الحالي: فار عدد التحذيرات

الامر:             `.وضع عدد التحذيرات`

الشرح :  يقوم هذا الامر بتغيير عدد التحذيرات التي يقوم السورس بتحذير المستخدم بها قبل حظره
الاستخدام : تقوم بالرد على عدد التحذيرات كرقم  بالامر   `.وضع عدد التحذيرات `

****ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة**| : 𖢿**| : 𖢿
اوامر فارات سورس حياه @HL_BG""",
        buttons=[
            [Button.inline("رجوع", data="pmvars")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"pmvarkish")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات الحماية
الفار الحالي: فار كليشة الحماية

الامر:             `.وضع كليشة الحماية`

الشرح :  يقوم هذا الامر بتغيير الكليشة (الكلام) التي تظهر عندما يكون امر الحماية شغال ويراسلك احد
الاستخدام : تقوم بالرد على الكليشة التي تريد وضعها بالامر   `.وضع كليشة الحماية `

* يمكنك الحصول على  كليشة جاهزة من هذه القناة @HL_BG
**ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة**| : 𖢿
اوامر فارات سورس حياه @HL_BG""",
        buttons=[
            [Button.inline("رجوع", data="pmvars")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"picpmvar")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات الحماية
الفار الحالي: فار صورة الحماية

الامر:             `.وضع صورة الحماية`

الشرح :  يقوم هذا الامر بتغيير او وضع الصورة التي تظهر عندما يكون امر الحماية  شغال ويراسلك احد
الاستخدام : تقوم بالرد على رابط الصورة التي تريد وضعها بالامر   `.وضع صورة الحماية` 

* كيفية جلب رابط الصورة؟
-بالرد على الصورة المراد استخراج منها الرابط ب  `.تلكراف ميديا`
ملاحظة : **يمكنك استخدام الاوامر في اي دردشة او محادثة**
اوامر فارات سورس حياه @HL_BG""",
        buttons=[
            [Button.inline("رجوع", data="pmvars")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"alivevar")))
async def varssett(event):
    await event.edit(
        "من هنا يمكنك عرض شروحات فارات الفحص:",
        buttons=[
            [
                Button.inline("صورة الفحص", data="picvars"),
                Button.inline("كليشة الفحص", data="kleshalive"),
            ],
            [Button.inline("رمز الفحص", data="rmzalive")],
            [Button.inline("رجوع", data="VARJMTHON")],
            [Button.inline("القائمة الرئيسية", data="MAIN")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"picvars")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات الفحص
الفار الحالي: فار صورة الفحص

الامر:             `.وضع صورة الفحص`
الشرح :  يقوم هذا الامر بتغيير او وضع الصورة التي تظهر عند ارسال  امر   `.فحص`
الاستخدام : تقوم بالرد على رابط الصورة التي تريد وضعها بالامر   `.وضع صورة الفحص` 

* كيفية جلب رابط الصورة؟
-بالرد على الصورة المراد استخراج منها الرابط ب  `.تلكراف ميديا`
ملاحظة : **يمكنك استخدام الاوامر في اي دردشة او محادثة**
اوامر فارات سورس حياه @HL_BG""",
        buttons=[
            [Button.inline("رجوع", data="alivevar")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"kleshalive")))
async def varssett(event):
    await event.edit(
        """ نوع الفار: فارات الفحص
الفار الحالي: فار كليشة الفحص
الامر:             `.وضع كليشة الفحص`

الشرح :  يقوم هذا الامر بتغيير الكليشة (الكلام) التي تظهر عند ارسال  امر  `.فحص`
الاستخدام : تقوم بالرد على الكليشة التي تريد وضعها بالامر   `.وضع كليشة الفحص `

* يمكنك الحصول على  كليشة جاهزة من هذه القناة @HL_BG
**ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة**| : 𖢿
اوامر فارات سورس حياه @HL_BG""",
        buttons=[
            [Button.inline("رجوع", data="alivevar")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"rmzalive")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات الفحص
الفار الحالي: فار رمز الفحص

الامر:             `.وضع رمز الفحص`

الشرح :  يقوم هذا الامر بتغيير الرمز  الذي يظهر عند ارسال  امر  `.فحص`
الاستخدام : تقوم بالرد على الرمز التي تريد وضعه بالامر   `.وضع رمز الفحص `

**ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة**| : 𖢿
اوامر فارات حياه @HL_BG""",
        buttons=[
            [Button.inline("رجوع", data="alivevar")],
        ],
    )


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"EXTRACMD")))
@check_owner
async def _(event):
    butze = [
        [
            Button.inline("الترجمة", data="ALIVETRG"),
            Button.inline("التوجيه", data="SAVETECXT"),
            Button.inline("حالتي", data="R7ALTIE"),
        ],
        [
            Button.inline("الحاسبة", data="CALCATERE"),
            Button.inline("كورونا", data="COROONA"),
            Button.inline("الارسال الوهمي", data="SACAMF"),
        ],
        [
            Button.inline("حماية الخاص", data="HEMAIREF"),
            Button.inline("الذاتية", data="DATECMD"),
            Button.inline("البروفيل", data="PROFUIECMD"),
        ],
        [
            Button.inline("الصلاة", data="SALACMD"),
            Button.inline("الكتابة", data="KTABAFE"),
            Button.inline("التاك و المنشن", data="TAGE4E"),
        ],
        [
            Button.inline("التالي", data="EXTRAC7"),
            Button.inline("رجوع", data="EXTRAC7"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=butze)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"HEMAIREF")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(HEMAIREF, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"KTABAFE")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(KTABAFE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"EXTRAC7")))
@check_owner
async def _(event):
    butze = [
        [
            Button.inline("ملصق متحرك", data="VASCHER"),
            Button.inline("تحويل صورة", data="STIKERPIC"),
        ],
        [
            Button.inline("تحويل متحركة", data="TOGIDEF"),
            Button.inline("تحويل لملف", data="ITESRAZAN"),
        ],
        [
            Button.inline("تحويل لكتابة", data="LTABAMEKF"),
            Button.inline("الملف لصورة", data="AJMTHOEF"),
        ],
        [
            Button.inline("تحويل ملصق", data="PICYEYS"),
            Button.inline("تحويل صوتي", data="JISORO"),
        ],
        [
            Button.inline("التالي", data="EXTRACMD"),
            Button.inline("رجوع", data="EXTRACMD"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=butze)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"DOWMANLODE4")))
@check_owner
async def _(event):
    butze = [
        [
            Button.inline("تحميل فيديو", data="YOUTUBECCMD"),
            Button.inline("تحميل صوتي", data="YOUTUBECMD"),
        ],
        [
            Button.inline("بحث", data="ALIVETSM"),
            Button.inline("فيديو", data="ALIVEFDO"),
        ],
        [
            Button.inline("انستا", data="INSTAGRAMCMD"),
            Button.inline("بينترست", data="BENTRSTCMD"),
        ],
        [
            Button.inline("نتائج بحث", data="YIOFDD"),
            Button.inline("تحميل صور", data="PICSERACJ"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=butze)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"INSTAGRAMCMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(INSTAGRAMCMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"YOUTUBECMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(YOUTUBECMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"YOUTUBECCMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(YOUTUBECCMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETSM")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(ALIVETSM, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEFDO")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(ALIVEFDO, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"BENTRSTCMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(BENTRSTCMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"YIOFDD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(YIOFDD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"PICSERACJ")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(PICSERACJ, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"PICYEYS")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(PICYEYS, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"AJMTHOEF")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(AJMTHOEF, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"JISORO")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(JISORO, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"LTABAMEKF")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(LTABAMEKF, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ITESRAZAN")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(ITESRAZAN, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TOGIDEF")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(TOGIDEF, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"STIKERPIC")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(STIKERPIC, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"VASCHER")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(VASCHER, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TAGE4E")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(TAGE4E, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"PROFUIECMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(PROFUIECMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"SACAMF")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(SACAMF, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"R7ALTIE")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(R7ALTIE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"SALACMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(SALACMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"DATECMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(DATECMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"COROONA")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(COROONA, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"SAVETECXT")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(SAVETECXT, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETRG")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(ALIVETRG, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"BOTCMD4")))
@check_owner
async def _(event):
    butze = [
        [
            Button.inline("الفحص", data="ALICES"),
            Button.inline("سليب ميديا", data="IMSLEEPF"),
        ],
        [
            Button.inline("البنك", data="PINGSMC"),
            Button.inline("السورس", data="ALICVEINLI"),
        ],
        [
            Button.inline("سرعة الانترنت", data="ALNTDOS"),
            Button.inline("اعادة تشغيل", data="ALIVEAUD"),
        ],
        [
            Button.inline("تحديث السورس", data="UPDATE4E"),
            Button.inline("السليب", data="ALIVESLB"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=butze)


#


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALICVEINLI")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCMD4")]]
    await event.edit(ALICVEINLI, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEAUD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCMD4")]]
    await event.edit(ALIVEAUD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVESLB")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCMD4")]]
    await event.edit(ALIVESLB, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"IMSLEEPF")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCMD4")]]
    await event.edit(IMSLEEPF, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"UPDATE4E")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCMD4")]]
    await event.edit(UPDATE4E, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALICES")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCMD4")]]
    await event.edit(ALICES, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALNTDOS")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCMD4")]]
    await event.edit(ALNTDOS, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"toolsed1")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("اذاعة للخاص", data="BROADEV1"),
            Button.inline("اذاعة للكروب", data="BRWAADV1"),
            Button.inline("اضافة اعضاء", data="ADDMEM7"),
        ],
        [
            Button.inline("الانتحال", data="CLIONEACMD"),
            Button.inline("الاعادة", data="ALIVEMEE"),
            Button.inline("الايدي", data="ALIVEDIII"),
        ],
        [
            Button.inline("ايدي", data="KSHFCMD"),
            Button.inline("التقليد", data="ADDTKLED"),
            Button.inline("ايقاف التقليد", data="STOPAZAG"),
        ],
        [
            Button.inline("التالي", data="TOOLCMD2"),
            Button.inline("رجوع", data="TOOLCM3"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEMEE")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(ALIVEMEE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ADDMEM7")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(ADDMEM7, buttons=buttons, link_preview=False)


#######################################################################


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TOOLCMD2")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("المقلدهم", data="ALMKD5D"),
            Button.inline("حذف المقلدهم", data="NOAZAJ4"),
            Button.inline("تلكراف ميديا", data="TELEHTMED"),
        ],
        [
            Button.inline("كرر", data="TKRAR3ADI"),
            Button.inline("بوت نشر (مكرر)", data="MKRRR5"),
            Button.inline("سبام", data="SPAM3AAH"),
        ],
        [
            Button.inline("ايقاف التكرار", data="STOPTKRARE"),
            Button.inline("وسبام", data="FGKHEF8"),
            Button.inline("حذف دردشة", data="Deltejm"),
        ],
        [
            Button.inline("التالي", data="TOOLCM3"),
            Button.inline("رجوع", data="toolsed1"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TOOLCM3")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("نوع المعرف", data="typeusername"),
            Button.inline("كروباتي", data="mygroups"),
            Button.inline("الحاظرهم", data="whoibanhim"),
        ],
        [
            Button.inline("تجميع", data="mlirabotcmd"),
            Button.inline("تقييد المحتوى", data="resscmdeq"),
        ],
        [
            Button.inline("التالي", data="toolsed1"),
            Button.inline("رجوع", data="TOOLCMD2"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"whoibanhim")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCM3")]]
    await event.edit(whoibanhim, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"resscmdeq")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCM3")]]
    await event.edit(resscmdeq, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"mlirabotcmd")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCM3")]]
    await event.edit(mlirabotcmd, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"mygroups")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCM3")]]
    await event.edit(mygroups, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"typeusername")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCM3")]]
    await event.edit(typeusername, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"Deltejm")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(Deltejm, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEDIII")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(ALIVEDIII, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALMKD5D")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(ALMKD5D, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"NOAZAJ4")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(NOAZAJ4, buttons=buttons, link_preview=False)


#
@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TELEHTMED")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(TELEHTMED, buttons=buttons, link_preview=False)


# TELEHTMED


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TKRAR3ADI")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(TKRAR3ADI, buttons=buttons, link_preview=False)


# ثثثث


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"MKRRR5")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(MKRRR5, buttons=buttons, link_preview=False)


# ويو جوا


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"FGKHEF8")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(FGKHEF8, buttons=buttons, link_preview=False)


# اي


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"SPAM3AAH")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(SPAM3AAH, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"STOPTKRARE")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(STOPTKRARE, buttons=buttons, link_preview=False)


######


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"BROADEV1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(BROADEV1, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"BRWAADV1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(BRWAADV1, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"CLIONEACMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(CLIONEACMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIBACK")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(ALIBACK, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"KSHFCMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(KSHFCMD, buttons=buttons, link_preview=False)


#
@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ADDTKLED")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(ADDTKLED, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"STOPAZAG")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(STOPAZAG, buttons=buttons, link_preview=False)


##


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TASLIACMD")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("الترفيه", data="TRFEHCMD"),
            Button.inline("التسلية", data="TSLEACMD"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TSLEACMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TASLIACMD")]]
    await event.edit(TSLEACMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TRFEHCMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TASLIACMD")]]
    await event.edit(TRFEHCMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"admincmd_s")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("حظر", data="bancmd"),
            Button.inline("الغاء حظر", data="unbancmd"),
            Button.inline("المحظورين", data="ALIVEMHA"),
        ],
        [
            Button.inline("كتم", data="ALIVEcatm"),
            Button.inline("الغاء كتم", data="unmutecmd"),
            Button.inline("طرد", data="KICKCMD"),
        ],
        [
            Button.inline("تثبيت", data="ALIVEbin"),
            Button.inline("الغاء التثبيت", data="ALIVEunbin"),
            Button.inline("رفع مشرف", data="ALIVEadmin"),
        ],
        [Button.inline("التالي", data="admin2"), Button.inline("رجوع", data="ADMSS4")],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"admin2")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("تنزيل مشرف", data="ALIVEtnadmin"),
            Button.inline("وضع صورة", data="ALIVEsod"),
            Button.inline("حذف الصورة", data="ALIVESOR"),
        ],
        [
            Button.inline("ارفع", data="ALIVErfe"),
            Button.inline("نزل", data="ALIVEnzl"),
            Button.inline("الاحداث", data="ALIVEADV"),
        ],
        [
            Button.inline("تفليش", data="ALIVETFL"),
            Button.inline("تنزيل الكل", data="ALIVEgma"),
            Button.inline("تحذير", data="ALIVETHR"),
        ],
        [
            Button.inline("التالي", data="admi3"),
            Button.inline("رجوع", data="admincmd_s"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETFL")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVETFL, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"admi3")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("حذف التحذيرات", data="ALIVEunTHR"),
            Button.inline("التحذيرات", data="ALIVETSV"),
            Button.inline("اضافة ترحيب", data="ALIVETRSB"),
        ],
        [
            Button.inline("ايقاف الترحيب", data="ALIVEundf"),
            Button.inline("الترحيبات", data="ALIVETRS"),
            Button.inline("منع كلمة", data="ALMN3CMD"),
        ],
        [
            Button.inline("الغاء منع", data="A3ALMN3"),
            Button.inline("قائمة المنع", data="LISTBLCK"),
            Button.inline("مسح المحظورين", data="UMBLCTR"),
        ],
        [Button.inline("التالي", data="ADMSS4"), Button.inline("رجوع", data="admin2")],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALMN3CMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(ALMN3CMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ADMSS4")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("اضافة رد", data="RDAJFDA"),
            Button.inline("ايقاف رد", data="RSTOPRD"),
            Button.inline("حذف الردود", data="ALLRDSTOP"),
        ],
        [
            Button.inline("الردود", data="ALLRD5"),
            Button.inline("احصائيات", data="ALMSHRFE1"),
            Button.inline("اطردني", data="MELICLW"),
        ],
        [
            Button.inline("المحذوفين", data="ACCD5SS"),
            Button.inline("ضع التكرار", data="ALTKRARCMD"),
            Button.inline("اشتراك اجباري", data="forcesub"),
        ],
        [
            Button.inline("التالي", data="admincmd_s"),
            Button.inline("رجوع", data="admi3"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"forcesub")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(forcesub, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALTKRARCMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ALTKRARCMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ACCD5SS")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ACCD5SS, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALMSHRFE1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ALMSHRFE1, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETRS")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ALIVETRS, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"MELICLW")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(MELICLW, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALLRD5")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ALLRD5, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALLRDSTOP")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ALLRDSTOP, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"RSTOPRD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(RSTOPRD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"RDAJFDA")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(RDAJFDA, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"UMBLCTR")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(UMBLCTR, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"LISTBLCK")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(LISTBLCK, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"A3ALMN3")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(A3ALMN3, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETRS")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(ALIVETRS, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEundf")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(ALIVEundf, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETRSB")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(ALIVETRSB, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETSV")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(ALIVETSV, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEunTHR")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(ALIVEunTHR, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETHR")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVETHR, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEgma")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVEgma, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEADV")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVEADV, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVErfe")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVErfe, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEnzl")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVEnzl, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVESOR")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVESOR, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEsod")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVEsod, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEtnadmin")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVEtnadmin, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEbin")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEbin, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEunbin")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEunbin, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEadmin")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEadmin, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"KICKCMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(KICKCMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEMHA")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEMHA, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"bancmd")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEBand, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"unbancmd")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEunban, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEcatm")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEcatm, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"unmutecmd")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEuncatm, buttons=buttons, link_preview=False)
