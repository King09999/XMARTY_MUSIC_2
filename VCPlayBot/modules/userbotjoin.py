
from pyrogram import Client
from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from VCPlayBot.helpers.decorators import authorized_users_only
from VCPlayBot.helpers.decorators import errors
from VCPlayBot.services.callsmusic import client as USER
from VCPlayBot.config import SUDO_USERS

@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>𝐀𝐝𝐝 𝐦𝐞 𝐚𝐬 𝐚𝐝𝐦𝐢𝐧 𝐨𝐟 𝐲𝐨𝐫 𝐠𝐫𝐨𝐮𝐩 𝐟𝐢𝐫𝐬𝐭</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "XmartyBot"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "𝐈 𝐣𝐨𝐢𝐧𝐞𝐝 𝐡𝐞𝐫𝐞 𝐚𝐬 𝐲𝐨𝐮 𝐫𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>𝐡𝐞𝐥𝐩𝐞𝐫 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐢𝐧 𝐲𝐨𝐮𝐫 𝐜𝐡𝐚𝐭</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 𝐅𝐥𝐨𝐨𝐝 𝐖𝐚𝐢𝐭 𝐄𝐫𝐫𝐨𝐫 🛑 \n User {user.first_name} 𝐜𝐨𝐮𝐥𝐝𝐧'𝐭 𝐣𝐨𝐢𝐧 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩 𝐝𝐮𝐞 𝐭𝐨 𝐡𝐞𝐚𝐯𝐲 𝐣𝐨𝐢𝐧 𝐫𝐞𝐪𝐮𝐞𝐬𝐭𝐬 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫𝐛𝐨𝐭! 𝐌𝐚𝐤𝐞 𝐬𝐮𝐫𝐞 𝐮𝐬𝐞𝐫 𝐢𝐬 𝐧𝐨𝐭 𝐛𝐚𝐧𝐧𝐞𝐝 𝐢𝐧 𝐠𝐫𝐨𝐮𝐩."
            "\n\nOr 𝐦𝐚𝐧𝐮𝐚𝐥𝐥𝐲 𝐚𝐝𝐝 @𝐗 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐚𝐧𝐝 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧</b>",
        )
        return
    await message.reply_text(
        "<b>𝐗𝐦𝐚𝐫𝐭𝐲 𝐡𝐞𝐥𝐩𝐞𝐫 𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐣𝐨𝐢𝐧𝐞𝐝 𝐲𝐨𝐮𝐫 𝐜𝐡𝐚𝐭</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>User couldn't leave your group! May be floodwaits."
            "\n\nOr manually kick me from to your Group</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("Assistant Leaving all chats")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
    
    
@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is chat even linked")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Add me as admin of yor channel first</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "VCPlayBot"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>helper already in your channel</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} couldn't join your channel due to heavy join requests for userbot! Make sure user is not banned in channel."
            "\n\nOr manually add @VCPlayAssistant to your Group and try again</b>",
        )
        return
    await message.reply_text(
        "<b>helper userbot joined your channel</b>",
    )
    
