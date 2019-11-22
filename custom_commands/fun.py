import discord
from discord.ext import commands

import random
import sys
import traceback
import asyncio
import datetime
import json

from common_vars import *

# Commands in this file:
# blush, pat, kiss, hug, cuddle, slap, howgay, 
# howlesbian, thotrate, 8ball,  rate, roast, penis, ship, coinflip

@bot.command()
async def pat(ctx, *, user: discord.Member):
    embed = discord.Embed(title="{} pats {}. Cute!".format(ctx.message.author, user), color=0x000000)
    result = random.choice(pat_gifs["results"])
    chosen_media = result["media"][0]
    url = chosen_media["gif"]["url"]
    embed.set_image(url=url)
    await ctx.send(embed=embed)
    
    @pat.error
async def pat_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(title="I couldn't find this member, so I'll pat you instead.", color=0x000000)
        result = random.choice(pat_gifs["results"])
        chosen_media = result["media"][0]
        url = chosen_media["gif"]["url"]
        embed.set_image(url=url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Hey! Don't feel down. Here, take a pat from me. <3", color=0x000000)
        result = random.choice(pat_gifs["results"])
        chosen_media = result["media"][0]
        url = chosen_media["gif"]["url"]
        embed.set_image(url=url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
        @bot.command()
async def kiss(ctx, *, user: discord.Member):
    embed = discord.Embed(title="{} kisses {}.".format(ctx.message.author, user), color=0x000000)
    result = random.choice(kiss_gifs["results"])
    chosen_media = result["media"][0]
    url = chosen_media["gif"]["url"]
    embed.set_image(url=url)
    await ctx.send(embed=embed)
    
    @bot.command()
async def kiss(ctx, *, user: discord.Member):
    embed = discord.Embed(title="{} kisses {}.".format(ctx.message.author, user), color=0x000000)
    result = random.choice(kiss_gifs["results"])
    chosen_media = result["media"][0]
    url = chosen_media["gif"]["url"]
    embed.set_image(url=url)
    await ctx.send(embed=embed)
    
    @kiss.error
async def kiss_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(title="I couldn't find this member, so I'll kiss you instead.", color=0x000000)
        result = random.choice(kiss_gifs["results"])
        chosen_media = result["media"][0]
        url = chosen_media["gif"]["url"]
        embed.set_image(url=url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Aww, looks like you're lonely, I'll kiss you.", color=0x000000)
        result = random.choice(kiss_gifs["results"])
        chosen_media = result["media"][0]
        url = chosen_media["gif"]["url"]
        embed.set_image(url=url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
        @bot.command()
async def hug(ctx, *, user: discord.Member):
    embed = discord.Embed(title="{} hugs {}.".format(ctx.message.author, user), color=0x000000)
    result = random.choice(hug_gifs["results"])
    chosen_media = result["media"][0]
    url = chosen_media["gif"]["url"]
    embed.set_image(url=url)
    await ctx.send(embed=embed)

    @hug.error
async def hug_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(title="I couldn't find this member, so I'll hug you instead.", color=0x000000)
        result = random.choice(hug_gifs["results"])
        chosen_media = result["media"][0]
        url = chosen_media["gif"]["url"]
        embed.set_image(url=url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Aww, looks like you're lonely, I'll hug you.", color=0x000000)
        result = random.choice(hug_gifs["results"])
        chosen_media = result["media"][0]
        url = chosen_media["gif"]["url"]
        embed.set_image(url=url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

        @bot.command()
async def slap(ctx, *, user: discord.Member):
    embed = discord.Embed(title="{} slaps {}.".format(ctx.message.author, user), color=0x000000)
    result = random.choice(slap_gifs["results"])
    chosen_media = result["media"][0]
    url = chosen_media["gif"]["url"]
    embed.set_image(url=url)
    await ctx.send(embed=embed)

    @slap.error
async def slap_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(title="I couldn't find this member, so I'll slap you instead.", color=0x000000)
        result = random.choice(slap_gifs["results"])
        chosen_media = result["media"][0]
        url = chosen_media["gif"]["url"]
        embed.set_image(url=url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Aww, looks like you're too weak to slap someone, so I'll slap you.",
                              color=0x000000)
        result = random.choice(slap_gifs["results"])
        chosen_media = result["media"][0]
        url = chosen_media["gif"]["url"]
        embed.set_image(url=url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
        @bot.command()
async def cuddle(ctx, *, user: discord.Member):
    embed = discord.Embed(title="{} cuddles {}.".format(ctx.message.author, user), color=0x000000)
    result = random.choice(cuddle_gifs["results"])
    chosen_media = result["media"][0]
    url = chosen_media["gif"]["url"]
    embed.set_image(url=url)
    await ctx.send(embed=embed)
    
    @cuddle.error
async def cuddle_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(title="I couldn't find this member, so I'll cuddle you instead.", color=0x000000)
        result = random.choice(cuddle_gifs["results"])
        chosen_media = result["media"][0]
        url = chosen_media["gif"]["url"]
        embed.set_image(url=url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Aww, looks like you're lonely, I'll cuddle you.", color=0x000000)
        result = random.choice(cuddle_gifs["results"])
        chosen_media = result["media"][0]
        url = chosen_media["gif"]["url"]
        embed.set_image(url=url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
        @bot.command()
async def blush(ctx):
    embed = discord.Embed(title="{} blushes.".format(ctx.message.author), color=0x000000)
    result = random.choice(blush_gifs["results"])
    chosen_media = result["media"][0]
    url = chosen_media["gif"]["url"]
    embed.set_image(url=url)
    await ctx.send(embed=embed)
    
    @bot.command()
async def penis(ctx, *, user: discord.Member):
    sizes = ["8D", "8=D", "8==D", "8===D", "8====D", "8=====D", "8======D", "8=======D", "8========D", "8=========D",
             "8==========D", "8===========D", "8============D", "8=============D", "8==============D",
             "8===============D"]
    if user.id == 237938976999079948:
        size = "sorry bro, my dick so big this message can't fit it, for more info ask your mom, ily"
    else:
        size = random.choice(sizes)
    embed = discord.Embed(description=f"{user}'s pee pee size \n\n{size}", color=0x000000)
    embed.set_author(name=f"{ctx.message.author}", icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)
    
    @penis.error
async def penis_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="How did this error get raised to begin with?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        sizes = ["8D", "8=D", "8==D", "8===D", "8====D", "8=====D", "8======D", "8=======D", "8========D",
                 "8=========D", "8==========D", "8===========D", "8============D", "8=============D",
                 "8==============D", "8===============D"]
        size = random.choice(sizes)
        embed = discord.Embed(description=f"{ctx.message.author}'s pee pee size \n\n{size}", color=0x000000)
        embed.set_author(name=f"{ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

        @bot.command()
async def thotrate(ctx, *, user: discord.Member):
    les = random.randint(0, 100)
    embed = discord.Embed(
        description="{} is a **{}**% thot. <:shiki_is_cool:612767957570945024>".format(user.mention, str(les)),
        color=0xef42f5)
    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)
    
    @thotrate.error
async def thotrate_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member.", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        les = random.randint(0, 100)
        embed = discord.Embed(
            description="{} is a **{}**% thot. <:shiki_is_cool:612767957570945024>".format(ctx.message.author.mention,
                                                                                           str(les)),
            color=0xef42f5)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
        @bot.command()
async def howlesbian(ctx, *, user: discord.Member):
    les = random.randint(0, 101)
    embed = discord.Embed(
        description="{} is **{}**% lesbian. <:lesbian22:612745721883656203>".format(user.mention, str(les)),
        color=0xef42f5)
    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)
    
    @howlesbian.error
async def howlesbian_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        les = random.randint(0, 101)
        embed = discord.Embed(
            description="{} is **{}**% lesbian. <:lesbian22:612745721883656203>".format(ctx.message.author.mention,
                                                                                        str(les)),
            color=0xef42f5)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
        @bot.command(name="8ball")
async def ball(ctx, *, message: str):
    if len(message) > 0:
        responds = ["yes duh", "no wtf", "ig?", "naw", "pew pew", "ur mom a hoe", "u retarded fuck, its obv yes",
                    "ew, no", "ur pp smol", "ye", "no u", "as i see it nigga, yes", "without a fucking doubt",
                    "tbh most likely", "sorry to inform that its a yes", "i doubt that fr", "ofc its a fucking no",
                    "sorry nigga, but its a no", "what the fuck"]
        choice = random.choice(responds)
        embed1 = discord.Embed(description="__8Ball__\n\n...", color=0xffffff)
        embed1.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        msg = await ctx.send(embed=embed1)
        await asyncio.sleep(1)
        embed2 = discord.Embed(description="__8Ball__\n\n**{}**".format(choice), color=0xf252e8)
        embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await msg.edit(embed=embed2)
    else:
        embed1 = discord.Embed(description="__8Ball__\n\nI couldn't answer you because you didn't give me a question.",
                               color=0x000000)
        embed1.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed1)
        
        @ball.error
async def ball_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="How did this error get raised to begin with?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="__8Ball__\n\nI couldn't answer you because you didn't give me a question.",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
        @bot.command()
async def roast(ctx, *, user: discord.Member):
    responds = ["are you sure youre not mentally retarded?", "that's gay..", "can't roast him, he doesn't have parents",
                "this is why no one likes you", "just stfu retard", "they got no balls dawg", "can u speak chong bong?",
                "what u want pussy?", "!!", "couldn't roast"]
    choice = random.choice(responds)
    embed2 = discord.Embed(description="{}".format(choice), color=0xf252e8)
    embed2.set_author(name="{}".format(user), icon_url=user.avatar_url)
    embed2.set_footer(text="Roasted by {}".format(ctx.message.author))
    await ctx.send(embed=embed2)
    
    @roast.error
async def roast_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member. No roasing.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="Give me a member to roast.", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
        @bot.command()
async def ship(ctx, user: discord.Member, user2: discord.Member):
    percent = random.randint(0, 100)
    strr = " "
    if percent >= 0 and percent <= 10:
        strr = "horrible"
    if percent >= 11 and percent <= 20:
        strr = "very bad"
    if percent >= 21 and percent <= 30:
        strr = "bad"
    if percent >= 31 and percent <= 40:
        strr = "worse than avarage"
    if percent >= 41 and percent <= 50:
        strr = "avarage"
    if percent >= 51 and percent <= 60:
        strr = "better than avarage"
    if percent == 69:
        strr = ":wink:"
    if percent >= 61 and percent <= 68:
        strr = "good"
    if percent == 70:
        strr = "good"
    if percent >= 71 and percent <= 80:
        strr = "very good"
    if percent >= 81 and percent <= 90:
        strr = "almost perfect"
    if percent >= 91 and percent <= 100:
        strr = "amazing"
    embed = discord.Embed(title=":two_hearts:  MATCHMAKING: :two_hearts: ",
                          description="**{}** :heart: **{}**\n\n**{}%**! That's **{}**.".format(user.name, user2.name,
                                                                                                str(percent), strr),
                          color=0x000000)
    await ctx.send(embed=embed)
    
    @ship.error
async def ship_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="You didn't give me 1 or 2 correct users.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        percent = random.randint(0, 100)
        strr = " "
        if percent >= 0 and percent <= 10:
            strr = "horrible"
        if percent >= 11 and percent <= 20:
            strr = "very bad"
        if percent >= 21 and percent <= 30:
            strr = "bad"
        if percent >= 31 and percent <= 40:
            strr = "worse than avarage"
        if percent >= 41 and percent <= 50:
            strr = "avarage"
        if percent >= 51 and percent <= 60:
            strr = "better than avarage"
        if percent == 69:
            strr = ":wink:"
        if percent >= 61 and percent <= 68:
            strr = "good"
        if percent == 70:
            strr = "good"
        if percent >= 71 and percent <= 80:
            strr = "very good"
        if percent >= 81 and percent <= 90:
            strr = "almost perfect"
        if percent >= 91 and percent <= 100:
            strr = "amazing"
        user = ctx.message.content[6:]
        user = discord.Member
        embed = discord.Embed(title=":two_hearts:  MATCHMAKING: :two_hearts: ",
                              description="**{}** :heart: **{}**\n\n**{}%**! That's **{}**.".format(ctx.message.author.name, user.name,
                                                                                                    str(percent), strr),
                              color=0x000000)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
        @bot.command()
async def rate(ctx, who, *, user: discord.Member):
    if who == "dy":
        cool = random.randint(0, 10)
        embed = discord.Embed(title="👀", description="{} is a **{}**/10.".format(user.mention, str(cool)),
                              color=0xffffff)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        #    embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text="Rated by Dy")
        await ctx.send(embed=embed)
        return
    if who == "shiki":
        cool = random.randint(0, 10)
        embed = discord.Embed(title="<:thonk:611367036282732574>",
                              description="{} is a **{}**/10. <a:smileg:611367087201320991>".format(user.mention,
                                                                                                    str(cool)),
                              color=0x4287f5)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        #    embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text="Rated by Shiki")
        await ctx.send(embed=embed)
        return
    else:
        embed = discord.Embed(
            description="You didn't provide a valid argument, ``rate`` accepts only **dy** and **shiki**.",
            color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
        return
      
      @rate.error
async def rate_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="You actually have to give me a member to rate.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
        @bot.command()
async def howgay(ctx, *, user: discord.Member):
    gay = random.randint(0, 101)
    embed = discord.Embed(description="{} is **{}**% gay. :gay_pride_flag:".format(user.mention, str(gay)),
                          color=0xef42f5)
    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)
    
    @howgay.error
async def howgay_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        gay = random.randint(0, 101)
        embed = discord.Embed(description="{} is **{}**% gay. :gay_pride_flag:".format(ctx.message.author.mention, str(gay)),
                              color=0xef42f5)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
        @bot.command()
async def howhot(ctx, *, user: discord.Member):
    gay = random.randint(0, 101)
    embed = discord.Embed(description="{} is **{}**% hot. :sweat_drops:".format(user.mention, str(gay)), color=0xef42f5)
    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)
    
    @howthot.error
async def howhot_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        gay = random.randint(0, 101)
        embed = discord.Embed(description="{} is **{}**% hot. :sweat_drops:".format(ctx.message.author.mention, str(gay)), color=0xef42f5)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
        @bot.command(aliases=["cf"])
async def coinflip(ctx):
    embed1 = discord.Embed(description="Flipping... \n\nResults:", color=0xffffff)
    embed1.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    msg = await ctx.send(embed=embed1)
    await asyncio.sleep(5)
    rn = random.randint(0, 100)
    results = " "
    if rn < 51:
        results = "HEADS"
    if rn > 50:
        results = "TAILS"
    embed2 = discord.Embed(description="Flipped. \n\nResults: **{}**.".format(results), color=0xe9f542)
    embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    await msg.edit(embed=embed2)
    
    
