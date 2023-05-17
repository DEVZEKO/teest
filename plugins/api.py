import pyrogram,asyncio,random
from pyrogram.raw import functions
from pyrogram import Client, filters
from kvsqlite.sync import Client as rp

db = rp("data.sqlite", 'fuck')

async def vote(session,channel, msg_id, pi):
    ap = Client(name=session[10:], api_id=15102119, api_hash='3dfdcee3e3bedad4738f81287268180f', session_string=session, workers=2, no_updates=True)
    await ap.start()
    if db.exists(f"voted_{msg_id}_{channel}_{session[:14]}"):
        return "v"
    try:
        await ap.vote_poll(channel, msg_id, [pi])
        await ap.stop()
        db.set(f"voted_{msg_id}_{channel}_{session[:14]}", True)
        return True
    except:
        await ap.stop()
        return False
async def view(session, channel, msg_id):
    ap = Client(name=session[10:], api_id=15102119, api_hash='3dfdcee3e3bedad4738f81287268180f', session_string=session, workers=2, no_updates=True)
    if db.exists(f"viewd_{msg_id}_{channel}_{session[:14]}"):
        return 'v'
    await ap.start()
    try:
        z = await ap.invoke(functions.messages.GetMessagesViews(
                    peer= (await ap.resolve_peer(channel)),
                    id=[int(msg_id)],
                    increment=True
        ))
        await ap.stop()
        db.set(f"viewd_{msg_id}_{channel}_{session[:14]}", True)
        return True
    except Exception as x:
        print(x)
        await ap.stop()
        return False
async def sendmsg(session, username, text, type):
    ap = Client(name=session[10:], api_id=15102119, api_hash='3dfdcee3e3bedad4738f81287268180f', session_string=session, workers=2, no_updates=True)
    await ap.start()
    try:
        if type == 'private':
            await ap.send_message(username, text)
            await ap.stop()
            return True
        if type == 'bot':
            n = await ap.get_chat(username)
            id = n.id
            await ap.send_message(chat_id=id, text=text)
            return True
        else:
            await ap.join_chat(username)
            await ap.send_message(username, text)
            await ap.leave_chat(username)
            await ap.stop()
            return True
    except:
        return False 
async def reaction(session, channel, msg_id, rs: list):
    ap = Client(name=session[10:], api_id=15102119, api_hash='3dfdcee3e3bedad4738f81287268180f', session_string=session, workers=2, no_updates=True)
    if db.exists(f"reacted_{msg_id}_{channel}_{session[:14]}"):
        return 'v'
    await ap.start()
    try:
        await ap.send_reaction(channel, msg_id, random.choice(rs))
        await ap.stop()
        db.set(f"reacted_{msg_id}_{channel}_{session[:14]}", True)
        return True
    except:
        await ap.stop()
        return False
async def members(session, channel):
    ap = Client(name=session[10:], api_id=15102119, api_hash='3dfdcee3e3bedad4738f81287268180f', session_string=session, workers=2, no_updates=True)
    if db.exists(f"joined_{channel}_{session[:14]}"):
        return 'v'
    await ap.start()
    try:
        await ap.join_chat(channel)
        await ap.stop()
        db.set(f"joined_{channel}_{session[:14]}", True)
        return True
    except:
        await ap.stop()
        return False
async def click(session, channel, msg_id):
    ap = Client(name=session[10:], api_id=15102119, api_hash='3dfdcee3e3bedad4738f81287268180f', session_string=session, workers=2, no_updates=True)
    if db.exists(f"clicked_{msg_id}_{channel}_{session[:14]}"):
        return 'v'
    try:
        await ap.start()
        
        try:
            await ap.join_chat(channel)
        except Exception as e:
            print(f"{e} = lol")
            pass
            
        g = await ap.get_messages(channel, msg_id)
        if g.reply_markup:
            x = g.reply_markup.inline_keyboard[0][0].text
            
            await g.click(x)
            
            await ap.stop()
            db.set(f"clicked_{msg_id}_{channel}_{session[:14]}", True)
            return True
    except:
        return False
async def leave(session, channel):
    ap = Client(name=session[10:], api_id=15102119, api_hash='3dfdcee3e3bedad4738f81287268180f', session_string=session, workers=2, no_updates=True)
    if db.exists(f"leaved_{channel}_{session[:14]}"):
        return 'v'
    await ap.start()
    try:
        await ap.leave_chat(channel)
        await ap.stop()
        db.set(f"leaved_{channel}_{session[:14]}", True)
        return True
    except:
        await ap.stop()
        return False