import html
import os
import base64

from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import MessageEntityMentionName

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest

from sbb_b import sbb_b
from sbb_b.core.logger import logging

from sbb_b.Config import Config
from sbb_b.core.managers import edit_or_reply, edit_delete
from sbb_b.helpers import reply_id
from sbb_b.sql_helper.globals import gvarstatus
from sbb_b.plugins import spamwatch
ZED_TEXT = gvarstatus("CUSTOM_ALIVE_TEXT") or "•𖢿• مـعلومـات المسـتخـدم مـن بـوت حيـــاه | : 𖢿"
ZEDM = gvarstatus("CUSTOM_ALIVE_EMOJI") or "𖢿 "
ZEDF = gvarstatus("CUSTOM_ALIVE_FONT") or "𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼"
zed_dev = (6275847466, 6275847466)
zel_dev = (6119417529, 6195765774)
zelzal = (6275847466, 6275847466)
LOGS = logging.getLogger(__name__)

async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_object = await event.client.get_entity(previous_message.sender_id)
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        if isinstance(user, int) or user.startswith("@"):
            user_obj = await event.client.get_entity(user)
            return user_obj
        try:
            user_object = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_object


async def fetch_info(replied_user, event):
    
    FullUser = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(user_id=replied_user.id, offset=42, max_id=0, limit=80)
    )
    replied_user_profile_photos_count = "⌔𖢿 هذا المستخدم لم يضع اي صورة"
    dc_id = "Can't get dc id"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
        dc_id = replied_user.photo.dc_id
    except AttributeError:
        pass
    user_id = replied_user.id
    first_name = replied_user.first_name
    full_name = FullUser.private_forward_name
    common_chat = FullUser.common_chats_count
    username = replied_user.username
    user_bio = FullUser.about
    is_bot = replied_user.bot
    restricted = replied_user.restricted
    verified = replied_user.verified
    photo = await event.client.download_profile_photo(
        user_id,
        Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",
        download_big=True,
    )
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("هذا المستخدم ليس لديه اسم اول")
    )
    full_name = full_name or first_name
    username = "@{}".format(username) if username else ("⌔𖢿 هذا المستخدم ليس لديه معرف")
    user_bio = "⌔𖢿 هذا المستخدم ليس لديه اي نبذة" if not user_bio else user_bio
    if user_id in zelzal: 
        rotbat = "「 🔱 مبــࢪمـج آلُِسورس  | : 𖢿 」" 
    elif user_id in zel_dev:
        rotbat = "「🔱  مطـ،ـوࢪ أســأّسـي  | : 𖢿" 
    elif user_id == (await event.client.get_me()).id and user_id not in zed_dev:
        rotbat = "⌁ مـالك الحساب | : 𖢿" 
    else:
        rotbat = "⌁ العضـو | : 𖢿"
    caption = " 𖢿╮مـعلومات الـشخص مـن بـوت حيــاه \n"
    caption += f"\n"
    caption = f"<b> {ZED_TEXT} </b>\n"
    caption += f"ٴ<b>{ZEDF}</b>\n"
    caption += f"<b>{ZEDM}الاسـم    ⇠ </b> "
    caption += f'<a href="tg://user?id={user_id}">{full_name}</a>'
    caption += f"\n<b>{ZEDM}المعـرف  ⇠  {username}</b>"
    caption += f"\n<b>{ZEDM}الايـدي   ⇠ </b> <code>{user_id}</code>\n"
    caption += f"<b>{ZEDM}الرتبـــه   ⇠ {rotbat} </b>\n"
    if zilzal == True or user_id in zelzal: # code by t.me/zzzzl1l
    caption += f"<b>{ZEDM}الحسـاب ⇠  بـريميـوم 🌟</b>\n"
    caption += f"<b>{ZEDM}الصـور    ⇠ </b> {replied_user_profile_photos_count}\n"
    if user_id != (await event.client.get_me()).id: # code by t.me/zzzzl1l
    caption += f"<b>{ZEDM}الـمجموعات المشتـركة ⇠ </b> {common_chat} \n"
    caption += f"<b>{ZEDM}البايـو     ⇠  {user_bio}</b> \n"
    caption += f"ٴ<b>{ZEDF}</b>"
    return photo, caption

@sbb_b.ar_cmd(pattern="ايدي(?: |$)(.*)")
async def who(event):
    roz = await edit_or_reply(event, "**اصـبر شـوي😄🤍**")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return await edit_or_reply(roz,  "**⌔𖢿 لم يتم العثور على معلومات لهذا المستخدم **")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await roz.delete()
    except TypeError:
        await roz.edit(caption, parse_mode="html")


@sbb_b.ar_cmd(pattern="رابط الحساب(?:\s|$)([\s\S]*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"⪼  [{tag}](tg://user?id={user.id})  𓆰. ")
