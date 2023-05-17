from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
import time
from kvsqlite.sync import Client

db = Client("data.sqlite", 'fuck')
def trend():
    k = db.keys("user_%")
    users = []
    for i in k:
        try:
             g = db.get(i[0])
             d = g["id"]
             users.append(g)
        except: continue
    data = users
    sorted_users = sorted(data, key=lambda x: len(x["users"]), reverse=True)
    result_string = "•<strong> المستخدمين الاكثر مشاركة لرابط الدعوى :</strong>\n"
    for user in sorted_users[:5]:
        result_string += f"🏅: ({len(user['users'])}) -> {user['id']} .\n"
    return(result_string)

@app.on_callback_query(filters.regex("^sharelink$"))
async def sharelinkk(app, query):
    user_id = query.from_user.id
    bot_username = None
    chats = db.get('force')
    from .force import check_channel_member
    for i in chats:
      if not await check_channel_member(app, i, user_id):
        k = f'''
همم، انت ممشترك بلقناة !! اشتراك وارجع ارسل ستارت !!
- @{i}
        '''
        return await query.edit_message_text(k, reply_markup=mk([[btn(f'- @{i} .', url=f't.me/{i}')]]))
    cq = 250 if not db.get("invite_price") else db.get("invite_price")
    try:
        c  = await app.get_me()
        bot_username = c.username
    except:
        await query.edit_message_text("حدث خطأ بالبوت ، حاول لاحقاً .")
        return
    keys = mk(
        [
            [btn(text='رجوع', callback_data='back_invite')],
        ]
    )
    link = f"https://t.me/{bot_username}?start={user_id}"
    t = trend()
    h = len(db.get(f"user_{user_id}")['users'])
    rk = f"""
انسخ الرابط ثم قم بمشاركته مع اصدقائك 📥 .

• كل شخص يقوم بالدخول ستحصل على 1 نقطه

- <strong>بإمكانك عمل اعلان خاص برابط الدعوة الخاص بك </strong>

~ رابط الدعوة : {link}

• مشاركتك للرابط : {h} 🌀

{t}
    """
    await query.edit_message_text(rk, reply_markup=keys)