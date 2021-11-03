import discord
import random
from keep_alive import keep_alive
from discord.ext import commands, tasks
from itertools import cycle
import asyncio

client = commands.Bot(command_prefix='.')
status = cycle(['pip install duality', 'github.com/dkundih', 'pypi.org/user/dkundih'])

@client.event
async def on_ready():
    change_status.start()
    print('Spreman.')

@tasks.loop(seconds= 5)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))

@client.command(aliases=['kamen', 'Kamen', 'Kamen.', 'kamen.'])
async def _kamen(ctx):
    responses = [
        'Kamen.', 'Škare.', 'Papir.'  
    ]
    odg = random.choice(responses)
    if odg == 'Kamen.':
     await ctx.send(f'{odg}\n\n=> Neriješeno!<= ')
    elif odg == 'Papir.':
      await ctx.send(f'{odg}\n\n=> Oprosti, gubiš. <=')
    elif odg == 'Škare.':
      await ctx.send(f'{odg}\n\n=> Ovaj put pobjeđuješ. <=')

@client.command(aliases=['Škare', 'škare', 'Skare', 'skare', 'Škare.', 'Skare.', 'skare.', 'škare.'])
async def _skare(ctx):
    responses = [
        'Kamen.', 'Škare.', 'Papir.'  
    ]
    odg = random.choice(responses)
    if odg == 'Škare.':
     await ctx.send(f'{odg}\n\n=> Neriješeno!<= ')
    elif odg == 'Kamen.':
      await ctx.send(f'{odg}\n\n=> Oprosti, gubiš. <=')
    elif odg == 'Papir.':
      await ctx.send(f'{odg}\n\n=> Ovaj put pobjeđuješ. <=')

@client.command(aliases=['Papir', 'papir', 'Papir.', 'papir.'])
async def _papir(ctx):
    responses = [
        'Kamen.', 'Škare.', 'Papir.'  
    ]
    odg = random.choice(responses)
    if odg == 'Papir.':
     await ctx.send(f'{odg}\n\n=> Neriješeno!<= ')
    elif odg == 'Kamen.':
      await ctx.send(f'{odg}\n\n=> Ovaj put pobjeđuješ. <=')
    elif odg == 'Škare.':
      await ctx.send(f'{odg}\n\n=> Oprosti, gubiš. <=')

@client.command(aliases=['duality', 'Duality'])
async def _alunari(ctx):
    await ctx.send('GITHUB: https://github.com/dkundih/duality\nPYPI: https://pypi.org/user/dkundih/')

@client.command(aliases=['cooldown', 'Cooldown'])
async def _cooldown(ctx, seconds, *, msg):
    secondint = int(seconds) 
    secondint += 1
    message = await ctx.send(f'Pokrenut je cooldown za {msg}, do kraja je preostalo još: {seconds} sekundi.')
    while True:
      secondint -= 1
      if secondint == 0:
          await message.edit(content='Brojač isključen!') 
          break
      await message.edit(content=f'Pokrenut je cooldown za {msg}, do kraja je preostalo još: {secondint} sekundi.')
      await asyncio.sleep(1)
    await ctx.send(f'{ctx.author.mention}, Cooldown događaja {msg} je završio.') 

@client.command(aliases=['countdownS', 'CountdownS'])
async def _countdownS(ctx, seconds, *, msg):
    secondint = int(seconds) 
    secondint += 1
    message = await ctx.send(f'Do događaja {msg} je preostalo još: {seconds} sekundi.')
    while True:
      secondint -= 1
      if secondint == 0:
          await message.edit(content='Brojač isključen!') 
          break
      await message.edit(content=f'Do događaja {msg} je preostalo još: {secondint} sekundi.')
      await asyncio.sleep(1)
    await ctx.send(f'{ctx.author.mention}, Događaj {msg} je započeo.') 

@client.command(aliases=['countdownM', 'CountdownM'])
async def _countdownM(ctx, seconds, *, msg):
    secondint = int(seconds) 
    secondint += 1
    message = await ctx.send(f'Do događaja {msg} je preostalo još: {seconds} minuta.')
    while True:
      secondint -= 1
      if secondint == 0:
          await message.edit(content='Brojač isključen!') 
          break
      await message.edit(content=f'Do događaja {msg} je preostalo još: {secondint} minuta.')
      await asyncio.sleep(60)
    await ctx.send(f'{ctx.author.mention}, Događaj {msg} je započeo.') 

@client.command(aliases=['countdownH', 'CountdownH'])
async def _countdownH(ctx, seconds, *, msg):
    secondint = int(seconds) 
    secondint += 1
    message = await ctx.send(f'Do događaja {msg} je preostalo još: {seconds} sati.')
    while True:
      secondint -= 1
      if secondint == 0:
          await message.edit(content='Brojač isključen!') 
          break
      await message.edit(content=f'Do događaja {msg} je preostalo još: {secondint} sati.')
      await asyncio.sleep(3600)
    await ctx.send(f'{ctx.author.mention}, Događaj {msg} je započeo.') 

@client.command(aliases=['countdownD', 'CountdownD'])
async def _countdownD(ctx, seconds, *, msg):
    secondint = int(seconds) 
    secondint += 1
    message = await ctx.send(f'Do događaja {msg} je preostalo još: {seconds} dana.')
    while True:
      secondint -= 1
      if secondint == 0:
          await message.edit(content='Brojač isključen!') 
          break
      await message.edit(content=f'Do događaja {msg} je preostalo još: {secondint} dana.')
      await asyncio.sleep(86400)
    await ctx.send(f'{ctx.author.mention}, Događaj {msg} je započeo.') 

keep_alive()
client.run('CENSORED') #Instead of 'CENSORED' paste 'Token-Code'.
