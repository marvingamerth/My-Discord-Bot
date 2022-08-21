import discord
import os
import dotenv

client = discord.Client()

@client.event
async def on_ready():
    print(f'Successfully logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content == '!hello':
        await message.channel.send('Hello! ' + str(message.author))
    elif message.content == '!logout':
        await client.logout()
    elif message.content == '!role':
        await message.channel.send('1.ห้ามส่งสื่อ18+\n2.ห้ามสแปมข้อความ\n3.ห้ามบูสต์ไมค์\n4.ห้ามทะเลาะกัน\n5.ห้ามพูดคำหยาบ(นิดหน่อยได้)\
            \n6.ห้ามส่งอะไรที่เกี่ยวกับการhack(ยกเว้นเห็นคนhackแล้วส่งรูปหรือวีดีโอมาให้ดู)\n7.ห้ามขายของ\n8.ห้ามดูถูกคนอื่น\
            \n9.เข้ามาแล้วต้องกดอีโมจิรับยศและแนะนำตัว')
    elif message.content == '!report':
        await message.channel.send('หากต้องการรายงานคนในเซิร์ฟเวอร์ กรุณาแจ้งรายละเอียดพร้อมแท็กชื่อผู้ที่ต้องการรายงาน')

token = os.getenv('TOKEN')
client.run(token)