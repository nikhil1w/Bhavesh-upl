from pyrogram import Client as bot, filters
from pyrogram.types import Message
import asyncio, os, sys
from config import Config
import database.db as db
from datetime import datetime, timedelta
import pytz
from main import LOGGER
IST = pytz.timezone('Asia/Kolkata')  
import constant.msg as msg
@bot.on_message(filters.command("start") & filters.private)
async def start(bot, m: Message):
    user_id = int(m.chat.id)
    user = await bot.get_users(user_id)
    await db.db_instance.save_subscriber(user_id)
    start_message = await bot.send_message(
        m.chat.id,
        f"Welcome {user.first_name}!"
    )
    await asyncio.sleep(0.1)
    await start_message.edit_text(
        "Initializing Uploader bot... 🤖\n\n"
        "Progress: [⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️] 0%\n\n"
    )
    await asyncio.sleep(0.1)
    await start_message.edit_text(
        "Loading features... ⏳\n\n"
        "Progress: [🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️] 25%\n\n"
    )
    await asyncio.sleep(0.1)
    await start_message.edit_text(
        "This may take a moment, sit back and relax! 😊\n\n"
        "Progress: [🟧🟧🟧🟧🟧⬜️⬜️⬜️⬜️⬜️] 50%\n\n"
    )
    await asyncio.sleep(0.1)
    await start_message.edit_text(
        "Checking subscription status... 🔍\n\n"
        "Progress: [🟨🟨🟨🟨🟨🟨🟨🟨⬜️⬜️] 75%\n\n"
    )
    await asyncio.sleep(0.1)
    user_id = m.from_user.id
    is_admin = user_id == Config.ADMIN_ID
    is_premium = await db.db_instance.is_premium(user_id)
    if is_admin or is_premium:
        await start_message.edit_text(
            "<b>Great! You are a premium member! Use Command : /drm to get started🌟</b>\n\n"
            "<blockquote><b><i>⚠️ If you face any problems, contact the Bot Admin.</i></b></blockquote>"
        )
    else:
        await asyncio.sleep(2)
        await start_message.edit_text(msg.planMessage)



@bot.on_message(filters.command("restart") & filters.private)
async def restart_handler(bot, m):
    user_id = m.from_user.id
    if user_id != Config.ADMIN_ID:
        return await m.reply_text("You are not authorized to use this command.")
    await m.reply_text("🚦RESTARTING🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command("auth") & filters.private)
async def add_premium_command(bot, m):
    if m.chat.id != Config.ADMIN_ID:
        return await m.reply_text("You are not authorized to use this command.")
    parts = m.text.split()
    if len(parts) < 2:
        return await m.reply_text("Usage: /auth __user_id__ __days__")
    user_id = int(parts[1])
    days = int(parts[2])
    try:
        user = await bot.get_users(user_id)
        first_name = user.first_name if user.first_name else "User"
        await db.db_instance.add_premium(user_id, days)
        message = (
            f"🎉 <b>Congrats {first_name} on Joining the Non-DRM Bot Family!</b> 🎉\n\n"
            f"<b><i>You now have access to download all Non-DRM+AES Encrypted URLs 🔐 including:</b></i>\n\n"
            f"<blockquote>"
            f"   • 📚 <b>Appx Zip+Encrypted Url</b>\n"
            f"   • 🎓 <b>Classplus DRM+ NDRM</b>\n"
            f"   • 🧑‍🏫 <b>PhysicsWallah DRM</b>\n"
            f"   • 📚 <b>CareerWill + PDF</b>\n"
            f"   • 🎓 <b>Khan GS</b>\n"
            f"   • 🎓 <b>Study Iq DRM</b>\n"
            f"   • 🚀 <b>APPX + APPX Enc PDF</b>\n"
            f"   • 🎓 <b>Vimeo DRM (Allen)</b>\n"
            f"   • 🎓 <b>M3u8 URLs that use cookies (e.g., Shreedhar)</b>\n"
            f"   • 🎓 <b>MPD URLs if the key is known (e.g., Mpd_url?key=--key XX:XX)</b>\n"
            f"</blockquote>\n\n"
            f"🚀Enjoy your access for <b>{days} days!</b>\n\n"
            f"<b><i><blockquote>🤩You can also use a text overlay on the thumbnail. Just send your name in a simple font when the bot asks for the thumbnail URL</b></i></blockquote>"
            f"<b><i>If you need any assistance, feel free to contact the Bot Admin.</b></i>"
        )
        await bot.send_message(user_id, message) 
        await m.reply_text(f"Premium status added for user {user_id}.")
    except Exception as e:
        await m.reply_text(f"Error adding premium status: {e}")


@bot.on_message(filters.command("remove") & filters.private)
async def remove_command(bot, m):
    if m.chat.id != Config.ADMIN_ID:
        return await m.reply_text("You are not authorized to use this command.")
    parts = m.text.split()
    if len(parts) != 2:
        return await m.reply_text("Usage: /remove __user_id__")
    user_id = int(parts[1])
    try:
        await db.db_instance.remove_user_from_premium(user_id)
        await bot.send_message(user_id, "<blockquote><b><i>Your account has been removed from Premium User<blockquote></b></i>.")
        await m.reply_text(f"User {user_id} has been removed.")
    except Exception as e:
        await m.reply_text(f"Error removing user: {e}")


@bot.on_message(filters.command("id"))
async def get_chat_id(_, m):
    await m.reply_text(f"<blockquote><b>The ID of this chat id is:</b></blockquote> `{m.chat.id}`")


@bot.on_message(filters.command("authlist") & filters.private)
async def authlist_handler(bot, m):
    if m.chat.id != Config.ADMIN_ID:
        await m.reply_text("You are not authorized to use this command.")
        return
    premium_users_cursor = await db.db_instance.get_premium_collection()
    auth_list = []
    async for user in premium_users_cursor:
        user_id = int(user['_id'])
        first_name = ''
        try:
            user_info = await bot.get_users(user_id)
            first_name = user_info.first_name
        except:
            LOGGER.info(f"User not Found {user_id}")
        start_at = user.get('start_at')
        expires_at = user.get('expires_at')
        auth_list.append(f"User: {first_name} ({user_id})\nStart: {start_at}\nExpires: {expires_at}\n")
    if not auth_list:
        await m.reply_text("No authorized users.")
    else:
        await m.reply_text("\n".join(auth_list))

@bot.on_message(filters.command("myplan") & filters.private)
async def myplan_handler(_, m):
    user_id = m.from_user.id
    user_data = await db.db_instance.get_premium_user(user_id)
    if user_data:
        start_at = user_data.get('start_at')
        expires_at = user_data.get('expires_at')
        if start_at.tzinfo is None:
            start_at = IST.localize(start_at)
        if expires_at.tzinfo is None:
            expires_at = IST.localize(expires_at)
        now_ist = datetime.now(IST)
        plan_duration = expires_at - start_at if start_at and expires_at else timedelta(0)
        time_left = expires_at - now_ist if expires_at else timedelta(0)
        response = (
            "<blockquote><b>🌟 Premium Plan Details 🌟</b></blockquote>\n\n"
            f"<b>Join Date:</b> <i>{start_at}</i>\n"
            f"<b>Expiry Date:</b> <i>{expires_at}</i>\n"
            f"<b>Plan Duration:</b> <i>{plan_duration}</i>\n"
            f"<b>Time Remaining:</b> <i>{time_left} ⏳</i>\n\n"
            "<blockquote><b>Enjoy exclusive benefits and features! 🎉🚀</b></blockquote>"
        ).format(
            start_at=start_at.strftime('%Y-%m-%d %H:%M:%S'),
            expires_at=expires_at.strftime('%Y-%m-%d %H:%M:%S'),
            plan_duration=plan_duration,
            time_left=time_left
        )
        await m.reply_text(response)
    else:
        await m.reply_text(msg.planMessage)

@bot.on_message(filters.command("status") & filters.private)
async def status_command(_, m):
    if m.chat.id != Config.ADMIN_ID:
        await m.reply_text("You are not authorized to use this command.")
        return
    subscriber_count = await db.db_instance.get_subscription_count()
    await m.reply_text(f"Number of subscribers: {subscriber_count}")

@bot.on_message(filters.command("broadcast") & filters.private)
async def broadcast(bot, m):
    if m.chat.id != Config.ADMIN_ID: 
        return await m.reply_text("You are not authorized to use this command.")
    parts = m.text.split(maxsplit=1)
    if len(parts) < 2:
        return await m.reply_text("Usage: /broadcast <message> or /broadcast -v for video broadcast")
    if parts[1] == "-v":
        await m.reply_text("Please send the video or photo with a caption that you want to broadcast.")
        media_message = await bot.listen(chat_id=m.chat.id)  
        media_file_id = None
        caption = media_message.caption or ""
        if media_message.video:
            media_file_id = media_message.video.file_id
            media_type = "video"
        elif media_message.photo:
            media_file_id = media_message.photo.file_id
            media_type = "photo"
        if media_file_id:
            subscribers = await db.db_instance.get_subscribers_collections()
            async for subscriber in subscribers:
                try:
                    if media_type == "video":
                        await bot.send_video(subscriber['_id'], media_file_id, caption=caption)
                    elif media_type == "photo":
                        await bot.send_photo(subscriber['_id'], media_file_id, caption=caption)
                except Exception as e:
                    print(f"Failed to send {media_type} to user {subscriber['_id']}: {e}")
            return await m.reply_text(f"{media_type.capitalize()} broadcast completed.")
        else:
            return await m.reply_text("No video or photo found. Please try again.")
    message = parts[1]
    subscribers = await db.db_instance.get_subscribers_collections()
    async for subscriber in subscribers:
        try:
            await bot.send_message(subscriber['_id'], message)
        except Exception as e:
            LOGGER.error(f"Failed to send message to user {subscriber['_id']}: {e}")
    await m.reply_text("Broadcast completed.")