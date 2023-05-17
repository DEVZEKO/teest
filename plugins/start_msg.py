from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
import time
import pyrogram.errors
from  pyrogram.enums import ChatMemberStatus
from kvsqlite.sync import Client
db = Client("data.sqlite", 'fuck')


@app.on_message(filters.private & filters.regex("^/start$"), group=1)
async def startm(app, msg):
    user_id = msg.from_user.id
    count = len(db.get("orders")) if db.get("orders") else 0
    if db.get("ban_list") is None:
        db.set('ban_list', [])
        pass
    if user_id in db.get("ban_list"):
        return
    chats = db.get('force')
    from .force import check_channel_member
    for i in chats:
      if not await check_channel_member(app, i, user_id):
        k = f'''
همم، انت ممشترك بلقناة !! اشتراك وارجع ارسل ستارت !!
- @{i}
        '''
        return await msg.reply(k, reply_markup=mk([[btn(f'- @{i} .', url=f't.me/{i}')]]))
    if db.exists(f"user_{user_id}"):
        coin = db.get(f'user_{user_id}')['coins']
        keys = mk(
        [
            [btn(text='فلوسك: {:,} USD'.format(coin), callback_data='lol')],
            [btn(text='🛒 الخدمات .', callback_data='service')],
            [btn(text='➕ تجميع الرصيد .', callback_data='invite'), btn(text='💳 شراء الرصيد', callback_data='buy')],
            [btn(text='🪪 معلومات حسابك .', callback_data='account'), btn(text='🏧 تحويل الرصيد .', callback_data='trans')],
            [btn(text=f'عدد الطلبات الكلي: {count}', callback_data='none')]
        ]
    )
        rk = f'''
- مرحبا بك،
+ حسابات البوت جميعها عربية حقيقية 
⌁︙البوت يمتاز بسرعة تنفيذ الطلب ✓ .
ال ID الخاص بك ↫ {msg.from_user.id}
⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯
        '''
        await app.send_message(msg.from_user.id,rk, reply_markup=keys)
    else:
        info = {'coins': 0 , 'id': user_id, 'premium': False, 'admin': False, "phone":[], "users":[], "date":str(time.time())}
        db.set(f'user_{user_id}', info)
        xxe = db.get("admin_list")
        sc = set(xxe)
        xxx = sorted(sc)
        for i in xxx:
            await app.send_message(i,f"عضو جديد فات للبوت!!\n{msg.from_user.mention} .\nايدي: {msg.from_user.id} .")
        
        coin = db.get(f'user_{user_id}')['coins']
        keys = mk(
        [
            [btn(text='فلوسك: {:,} USD'.format(coin), callback_data='lol')],
            [btn(text='🛒 الخدمات .', callback_data='service')],
            [btn(text='➕ تجميع الرصيد .', callback_data='invite'), btn(text='💳 شراء الرصيد', callback_data='buy')],
            [btn(text='🪪 معلومات حسابك .', callback_data='account'), btn(text='🏧 تحويل الرصيد .', callback_data='trans')],
            [btn(text=f'عدد الطلبات الكلي: {count}', callback_data='none')]
        ]
    )
        rk =f'''
- مرحبا بك،
+ حسابات البوت جميعها عربية حقيقية 
⌁︙البوت يمتاز بسرعة تنفيذ الطلب ✓ .
ال ID الخاص بك ↫ {msg.from_user.id}
⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯
        '''
        await app.send_message(msg.from_user.id,rk, reply_markup=keys)