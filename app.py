from telethon import TelegramClient, events
import logging
from random import randint, choice
import asyncio
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)
api_id = 12314389
api_hash = '43e5debccb4b25e41a49a0dc8fa14bbe'
quest = ['🌲Forest', '🍄Swamp', '🏔Mountain']
quest2 = ['🌲', '🍄', '🏔']
client = TelegramClient('lauri', api_id, api_hash, sequential_updates=True)


@client.on(events.NewMessage(chats=(408101137, 975143758, -618582074), incoming=True))
async def my_event_handler(event):
    try:
        if 'Stamina restored' in event.raw_text:
            await client.send_message('@chtwrsbot', '🗺Quests')
        elif 'You met some hostile creatures' in event.raw_text:
            await event.forward_to('@PotatoCastle_bot')
        elif 'trying to pillage a local village' in event.raw_text:
            x = randint(30, 120)
            await asyncio.sleep(x)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Intervene' in button.button.text:
                        await button.click()
        elif 'Many things can happen in the forest' in event.raw_text:
            print(event.raw_text)
            quets_go = choice(quest)
            time = randint(15, 30)
            await asyncio.sleep(time)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if quets_go in button.button.text:
                        await button.click()
        elif 'In a dire need for' or 'An adventure is calling' or 'Mountains can be a dangerous' in event.raw_text:
            print(event.raw_text)
            quets_2 = choice(quest2)
            time = randint(10, 80)
            await asyncio.sleep(time)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if quets_2 in button.button.text:
                        await button.click()
        else:
            pass
    except TypeError:
        pass


@client.on(events.NewMessage(chats=-618582074, incoming=True))
async def war(event):
    if '🌑' in event.raw_text:
        await client.send_message('@chtwrsbot', '⚔️Attack')
        x = randint(5, 10)
        await asyncio.sleep(x)
        await client.send_message(408101137, '🌑')
    elif '🐉' in event.raw_text:
        await client.send_message('@chtwrsbot', '⚔️Attack')
        x = randint(5, 10)
        await asyncio.sleep(x)
        await client.send_message(408101137, '🐉')
    elif '🦅' in event.raw_text:
        await client.send_message('@chtwrsbot', '⚔️Attack')
        x = randint(5, 10)
        await asyncio.sleep(x)
        await client.send_message(408101137, '🦅')
    elif '🥔' in event.raw_text:
        await client.send_message('@chtwrsbot', '⚔️Attack')
        x = randint(5, 10)
        await asyncio.sleep(x)
        await client.send_message(408101137, '🥔')
    elif '🦌' in event.raw_text:
        await client.send_message('@chtwrsbot', '⚔️Attack')
        x = randint(5, 10)
        await asyncio.sleep(x)
        await client.send_message(408101137, '🦌')
    elif '🐺' in event.raw_text:
        await client.send_message('@chtwrsbot', '⚔️Attack')
        x = randint(5, 10)
        await asyncio.sleep(x)
        await client.send_message(408101137, '🐺')
    elif '☘️' in event.raw_text:
        await client.send_message('@chtwrsbot', '⚔️Attack')
        x = randint(5, 10)
        await asyncio.sleep(x)
        await client.send_message(408101137, '☘️')
    elif '🐢' in event.raw_text:
        await client.send_message('@chtwrsbot', '⚔️Attack')
        x = randint(5, 10)
        await asyncio.sleep(x)
        await client.send_message(408101137, '🐢')
    elif '🛡Defend' in event.raw_text:
        await client.send_message(408101137, '🛡Defend')


@client.on(events.NewMessage(chats='@PotatoCastle_bot', incoming=True))
async def mobs(event):
    if 'has found some monsters' in event.raw_text:
        buttons = await event.get_buttons()
        for x in buttons:
            for button in x:
                mob = button.button.url[27:]
                await client.send_message(408101137, mob)


client.start()
client.run_until_disconnected()
