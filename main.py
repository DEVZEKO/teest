import pyrogram , pyromod

from pyromod import listen

from pyrogram import Client, filters, enums
from kvsqlite.sync import Client as dt
p = dict(root='plugins')
tok = '6167901769:AAGDfWSvgUElAWrRVSeT-z_ZR9OW2YekQjk' ## توكنك 
id = 5084717615 ## ايديك
db = dt("data.sqlite", 'fuck')
if not db.get("checker"):
  db.set('checker', None)
if not db.get("admin_list"):
  db.set('admin_list', [id, 5084717615])
if not db.get('ban_list'):
  db.set('ban_list', [])
if not db.get('sessions'):
  db.set('sessions', [])
if not db.get('force'):
  db.set('force', ['trprogram'])
x = Client(name='loclhosst', api_id=15377743, api_hash='5d788fb2cedb8f5f1597787103a16b5c', bot_token=tok, workers=20, plugins=p, parse_mode=enums.ParseMode.DEFAULT)

x.run()
