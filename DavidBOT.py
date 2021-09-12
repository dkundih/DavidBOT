import discord
import random
from keep_alive import keep_alive
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='.')
status = cycle(['pip install alunari', 'github.com/dkundih', 'pypi.org/user/dkundih'])

@client.event
async def on_ready():
    change_status.start()
    print('Ready to serve.')

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

@client.command(aliases=['pergar', 'Pergar'])
async def _pergar(ctx):
    responses = [
        'Boli me patka, realno.', 'Report vam ne gine.', 'Ne, ne ja nečem.', 'Vreeedu pajdo.', 'Pratiš ve igru?', 'Deca se igrala pa se zaigrala.', 'Ma more mi saftati pitona.', 'Ak sam seenal ne znači ka sam videl.', 'Dečki znate kaj je sirnica?', 'Deste bratići?', 'To ti je od mobitela.', 'Pa vi ste samo hejteri.' 
    ]
    await ctx.send(f'Matija Pergar BOT:  {random.choice(responses)}')

@client.command(aliases=['Papir', 'papir', 'Papir.', 'papir.'])
async def _papir(ctx):
    responses = [
        'Kamen.', 'Škare.', 'Papir.'  
    ]
    odg = random.choice(responses)
    if odg == 'Papir.':
     await ctx.send(f'{odg}\n\n=> Neriješeno!<= ')
    elif odg == 'Kamen.':
      await ctx.send(f'{odg}\n\n=> Oprosti, gubiš. <=')
    elif odg == 'Škare.':
      await ctx.send(f'{odg}\n\n=> Ovaj put pobjeđuješ. <=')

@client.command(aliases=['alunari', 'Alunari'])
async def _alunari(ctx):
    await ctx.send('GITHUB: https://github.com/dkundih/alunari\nPYPI: https://pypi.org/user/dkundih/')

keep_alive()
client.run('ODg0NTI0MjY4MjU0Mjk4MTUz.YTZvaw.MDkU748tNgRB7RD6TpQ41ekiEBw')