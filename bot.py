import os
import time
import random
import string
import json
import base64
import re
from datetime import datetime, timedelta
from multiprocessing import Process
import threading
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import cloudscraper
import user_agent
import telebot
from telebot import types
from faker import Faker
from bs4 import BeautifulSoup
from gatet import *
from reg import reg
os.chdir(os.path.dirname(os.path.abspath(__file__)))
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


os.system("cls" if os.name == "nt" else "clear")


redo = ' /gift'
id = 5643656889
stopuser = {}
token = '8404535914:AAFRo09HY4ZsiPfhvvt4ie74049A1wwmwkM'

bot=telebot.TeleBot(token,parse_mode="HTML")
admin=5643656889
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}	
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate = ''
		name = message.from_user.first_name

		startbot = f'''<b>
مرحبا بك 👋
{name}
في بوت النخبة
هو بوت فحص بطاقات علي منصة تليجرام 🛂

</b>'''

		# قراءة ملف JSON
		try:
			with open('data.json', 'r', encoding="utf-8") as file:
				json_data = json.load(file)
		except:
			json_data = {}

		user_id = str(message.from_user.id)

		# إذا المستخدم غير موجود → أضفه
		if user_id not in json_data:
			json_data[user_id] = {
				"plan": "𝗙𝗥𝗘𝗘",
				"timer": "none"
			}

			with open('data.json', 'w', encoding="utf-8") as json_file:
				json.dump(json_data, json_file, ensure_ascii=False, indent=4)

		# قراءة الخطة بأمان
		BL = json_data.get(user_id, {}).get("plan", "𝗙𝗥𝗘𝗘")

		# إرسال رسالة البداية
		if BL == '𝗙𝗥𝗘𝗘':
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(
				text="✨ المالك  ✨",
				url="https://t.me/EbrahimEldsoky"
			)
			keyboard.add(contact_button)

			photo_url = 'https://t.me/fcdhtddc12/29435'

			bot.send_photo(
				chat_id=message.chat.id,
				photo=photo_url,
				caption=startbot,
				reply_markup=keyboard
			)
	
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ قناة البوت  ✨", url="https://t.me/")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		random_number = 3
		photo_url = f'https://t.me/fcdhtddc12/29435'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=startbot,reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start2(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"✨ المالك  ✨", url='https://t.me/EbrahimEldsoky')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text='''<b>
مرحبا بك في قائمة اوامر الفحص 🗂️

ملحوظة ✋
				  الحد الاقصي 350 بطاقة
استرايب اتشارج 1$
.stch
/stch
اوامر الملف
قم بارسالة وبعدها يظهر لك منفذ البوابات اختر ماتريد

فحص otp البطاقة
.otp
/otp
اوامر الملف
قم بارسالة وبعدها يظهر لك منفذ البوابات اختر ماتريد
	</b>''',reply_markup=keyboard)

@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ المالك  ✨", url="https://t.me/EbrahimEldsoky")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>{name}
عفوا لست مشترك مميز 🌟

لا يحق لك استعمال البوت بالميزات المدفوعة

للتواصل 
@EbrahimEldsoky</b>''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ المالك  ✨", url="https://t.me/EbrahimEldsoky")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>
مرحبا بك 👋
{name}
في بوت (❣️ CARDIOLOGIST )

هو بوت فحص بطاقات علي منصة تليجرام 🛂

</b>''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ المالك  ✨", url="https://t.me/EbrahimEldsoky")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>لا يمكنك استخدام الروبوت لأن اشتراكك قد انتهى</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		stchb = types.InlineKeyboardButton(text="STRIP CHARGE 1$🟢",callback_data='stchd')
		staub = types.InlineKeyboardButton(text="STRIP AUTH 🟢",callback_data='staud')

		keyboard.add(stchb)
		keyboard.add(staub)
		
		bot.reply_to(message, text=f'يمكنك الان اختيار بوابة الفحص بعد تحديد رغبة عملك ✓',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
			


###############################stch
@bot.callback_query_handler(func=lambda call: call.data == "stchd")
def stchd(call):
	def my_function():
		id=call.from_user.id
		gate='STRIRE CHARGE 1$'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "انتظر قليلا جاري التحقق...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='تم انهاء الفحص بنجاح ✅:::::: ')
						return					

					try:
						data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
					except:
						pass
					try:
						bank=(data['bank'])
					except:
						bank=('UNKNOWN')
					try:
						emj=(data['country_flag'])
					except:
						emj=('UNKNOWN')
					try:
						cn=(data['country_name'])
					except:
						cn=('UNKNOWN')
					try:
						dicr=(data['level'])
					except:
						dicr=('UNKNOWN')
					try:
						typ=(data['type'])
					except:
						typ=('UNKNOWN')
					try:
						url=(data['brand'])
						
					except:
						url=('UNKNOWN')
						
						
					if total >= 3000000:
						break
					start_time = time.time()
					try:
						last = str(stch(cc))
					except Exception as e:
						print(e)
						last = f"{gate} ERORR"
				
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"{last}", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f" {gate} ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm6 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,cm4,cm5,cm6, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''جيد يتم الان التحقق من البطاقات علي بوابة {gate}
برجاء انتظار النتائج ''', reply_markup=mes)
					
					msg=f'''<b>{gate} ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ Thank you, payment has been made
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {typ} - {url}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {cn} - {emj} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @EbrahimEldsoky</b>'''

					msgfund=f'''<b>insufficient funds ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {typ} - {url}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {cn} - {emj} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @EbrahimEldsoky</b>'''


					msgccn=f'''<b>{gate} CCN ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {typ} - {url}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {cn} - {emj} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @EbrahimEldsoky</b>'''
					if "successfully" in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif "Your card has insufficient funds." in last:
						live += 1
						bot.send_message(call.from_user.id, msgfund)
					elif "Your card's security code is incorrect." in last:
						ccnn += 1
						bot.send_message(call.from_user.id, msgccn)
					else:
						dd += 1
				
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''تم ايقاف الفحص بسبب انك اوقفتة او الملف اكبر من 300 بطاقة 🔒
عدد البطاقات التي في الملف {total}''')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()


###############################stch

@bot.message_handler(func=lambda message: message.text.lower().startswith('.sch') or message.text.lower().startswith('/sch'))
def stauuu(message):
	gate='STRIP CHARGE 1$'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ المالك  ✨", url="https://t.me/EbrahimEldsoky")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>{name}
عفو الخدمة غير متاحة للخطة المجانية ✋</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ المالك  ✨", url="https://t.me/EbrahimEldsoky")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>{name}
عفو الخدمة غير متاحة للخطة المجانية ✋</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ المالك  ✨", url="https://t.me/EbrahimEldsoky")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>لا يمكنك استخدام الروبوت لأن اشتراكك قد انتهى</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 0:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 خطأ !
 يرجى التأكد من إدخال تفاصيل البطاقة بالتنسيق الصحيح:
بطاقة: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(stch(cc))
	except Exception as e:
		last='Error'

	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>{gate} ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ Thank you, payment has been made
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @EbrahimEldsoky</b>'''


	msgccn=f'''<b>{gate} CCN ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @EbrahimEldsoky</b>'''


	msgno=f'''<b> insufficient funds✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @EbrahimEldsoky</b>'''

	msgd=f'''<b>{gate} ❌
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @EbrahimEldsoky</b>'''

	if "successfully" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	elif "Your card has insufficient funds" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgno)
	elif "Your card's security code is incorrect" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgccn)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)




###############################stau
@bot.callback_query_handler(func=lambda call: call.data == "staud")
def staud(call):
	def my_function():
		id=call.from_user.id
		gate='STRIRE AUTH'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "انتظر قليلا جاري التحقق...⌛")

		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='تم انهاء الفحص بنجاح ✅:::::: ')
						return					

					try:
						data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
					except:
						pass
					try:
						bank=(data['bank'])
					except:
						bank=('UNKNOWN')
					try:
						emj=(data['country_flag'])
					except:
						emj=('UNKNOWN')
					try:
						cn=(data['country_name'])
					except:
						cn=('UNKNOWN')
					try:
						dicr=(data['level'])
					except:
						dicr=('UNKNOWN')
					try:
						typ=(data['type'])
					except:
						typ=('UNKNOWN')
					try:
						url=(data['brand'])
						
					except:
						url=('UNKNOWN')
						
					if total >= 3000000:
						break
					start_time = time.time()
					try:
						last = str(stau(cc))
					except Exception as e:
						print(e)
						last = f"{gate} ERORR"
				
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f" {last} ", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f" {gate} ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm6 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,cm4,cm5,cm6, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''جيد يتم الان التحقق من البطاقات علي بوابة {gate} 
برجاء انتظار النتائج ''', reply_markup=mes)

					
					
					msg=f'''<b>{gate} ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {typ} - {url}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {cn} - {emj} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @EbrahimEldsoky</b>'''

					msgfund=f'''<b>{gate} ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {typ} - {url}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {cn} - {emj} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @EbrahimEldsoky</b>'''


					msgccn=f'''<b>{gate} CCN ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {typ} - {url}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {cn} - {emj} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @EbrahimEldsoky</b>'''
					if "Card saved successfully" in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif "Your card has insufficient funds." in last:
						live += 1
						bot.send_message(call.from_user.id, msgfund)
					elif "Your card's security code is incorrect." in last:
						ccnn += 1
						bot.send_message(call.from_user.id, msgccn)
					else:
						dd += 1
				
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''تم ايقاف الفحص بسبب انك اوقفتة او الملف اكبر من 300 بطاقة 🔒
عدد البطاقات التي في الملف {total}''')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()


###############################stau

@bot.message_handler(func=lambda message: message.text.lower().startswith('.sa') or message.text.lower().startswith('/sa'))
def stauuu2(message):
	gate='STRIP AUTH'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ المالك  ✨", url="https://t.me/EbrahimEldsoky")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>{name}
عفو الخدمة غير متاحة للخطة المجانية ✋</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ المالك  ✨", url="https://t.me/EbrahimEldsoky")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>{name}
عفو الخدمة غير متاحة للخطة المجانية ✋</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ المالك  ✨", url="https://t.me/EbrahimEldsoky")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>لا يمكنك استخدام الروبوت لأن اشتراكك قد انتهى</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 0:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 خطأ !
 يرجى التأكد من إدخال تفاصيل البطاقة بالتنسيق الصحيح:
بطاقة: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(stau(cc))
	except Exception as e:
		last='Error'

	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>{gate} ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @EbrahimEldsoky</b>'''


	msgccn=f'''<b>{gate} CCN ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @EbrahimEldsoky</b>'''


	msgno=f'''<b>insufficient funds ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @EbrahimEldsoky</b>'''

	msgd=f'''<b>{gate} ❌
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @EbrahimEldsoky</b>'''
	
	if "Card saved successfully" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	elif "Your card has insufficient funds" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgno)
	elif "Your card's security code is incorrect" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgccn)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)


#################################/code
@bot.message_handler(commands=["code"])
def code(message):
	def my_function():
		id = message.from_user.id

		if id != admin:
			return

		try:
			h = float(message.text.split(' ')[1])

			# قراءة JSON بترميز UTF-8
			with open('data.json', 'r', encoding="utf-8") as json_file:
				existing_data = json.load(json_file)

			characters = string.ascii_uppercase + string.digits
			pas = (
				"EBRAHIM-" +
				"".join(random.choices(characters, k=7)) + "-" +
				"".join(random.choices(characters, k=5)) + "-" +
				"".join(random.choices(characters, k=7))
			)

			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan = "𝗩𝗜𝗣"

			parts = str(ig).split(':')
			ig = ":".join(parts[:2])

			# تحديث البيانات
			new_data = {
				pas: {
					"plan": plan,
					"time": ig,
				}
			}

			existing_data.update(new_data)

			# كتابة JSON بترميز UTF-8
			with open('data.json', 'w', encoding="utf-8") as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

			# تصحيح مشكلة redo
			msg=f'''<b> تم انشاء كود مستخدم بنجاح 🟢 نوع المستخدم : مميز 🌟 وقت انتهاء الكود : {ig} الكود : <code>{redo} {pas}</code> قم بنسخ الفتاح وإرسال للبوت فقط .</b>'''

			bot.reply_to(message, msg, parse_mode="HTML")

		except Exception as e:
			import html
			safe = html.escape(str(e))
			print("ERROR :", e)
			bot.reply_to(message, safe)

	my_thread = threading.Thread(target=my_function)
	my_thread.start()
	

##############################/gift
@bot.message_handler(func=lambda message: message.text.lower().startswith('.gift') or message.text.lower().startswith('/gift'))
def gift(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>
			تم تفعيل الكود بنجاح ✅
مده انتهاء الكود 
{timer}
اصبحت مشترك مميز 🌟
 </b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR ID : ',e)
			bot.reply_to(message,'<b> عفوا كود غير صالح ❌ </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()



@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback4(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("BOT ONLAIN")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"حدث خطأ: {e}")
