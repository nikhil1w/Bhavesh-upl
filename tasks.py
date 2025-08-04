from pyrogram import Client as bot, filters
from main import LOGGER
import database.db as db
from master import helper

active_tasks = {}

@bot.on_message(filters.command("stop") & filters.private)
async def stop_task(bot, m):
    user_id = m.chat.id
    is_premium = await db.db_instance.is_premium(user_id)
    if not is_premium:
        await m.reply_text(
            "╭━━━━━━ ERROR ━━━━━━➣\n"
            "┣⪼ ⚠️ **Access Denied**\n"
            "┣⪼ 🔒 Premium users only\n"
            "╰━━━━━━━━━━━━━━━━➣"
        )
        return
    if user_id not in active_tasks:
        await m.reply_text(
            "╭━━━━━━ ERROR ━━━━━━➣\n"
            "┣⪼ ❌ **No Active Tasks**\n"
            "╰━━━━━━━━━━━━━━━━➣"
        )
        return
    reply_markup = await helper.create_task_buttons(bot, active_tasks[user_id])
    await m.reply_text(
        "╭━━━━━━ SELECT TASK ━━━━━━➣\n"
        "┣⪼ 🛑 **Select a task to stop**\n"
        "╰━━━━━━━━━━━━━━━━➣",
        reply_markup=reply_markup
    )

@bot.on_callback_query(filters.regex(r"^stop_"))
async def stop_selected_task(bot, query):
    user_id = query.message.chat.id
    channel_id = int(query.data.split("_")[1])
    if user_id in active_tasks:
        task_to_remove = None
        for task_info in active_tasks[user_id]:
            if task_info['channel_id'] == channel_id:
                try:
                    task_info['task'].cancel()
                    task_to_remove = task_info
                    await query.message.edit_text(
                        "╭━━━━━━ SUCCESS ━━━━━━➣\n"
                        "┣⪼ 🛑 **Task Stopped**\n"
                        "┣⪼ ✅ Download cancelled\n"
                        "╰━━━━━━━━━━━━━━━━➣"
                    )
                    break
                except Exception as e:
                    LOGGER.error(f"Error stopping task: {e}")
                    await query.message.edit_text(
                        "╭━━━━━━ ERROR ━━━━━━➣\n"
                        "┣⪼ ❌ **Failed to Stop**\n"
                        f"┣⪼ 💭 Error: {str(e)}\n"
                        "╰━━━━━━━━━━━━━━━━➣"
                    )
                    return
        
        if task_to_remove:
            active_tasks[user_id].remove(task_to_remove)
            if not active_tasks[user_id]:
                del active_tasks[user_id]
        else:
            await query.message.edit_text(
                "╭━━━━━━ ERROR ━━━━━━➣\n"
                "┣⪼ ❌ **Task Not Found**\n"
                "┣⪼ 💭 Task may have finished\n"
                "╰━━━━━━━━━━━━━━━━➣"
            )
    else:
        await query.message.edit_text(
            "╭━━━━━━ ERROR ━━━━━━➣\n"
            "┣⪼ ❌ **No Active Tasks**\n"
            "┣⪼ 💭 All tasks completed\n"
            "╰━━━━━━━━━━━━━━━━➣"
        )
