import os, random, discord
from urllib import request
from inflect import engine
from discord.ext import commands
print("Loading...")
intents = discord.Intents.default()
intents.members = True
#You need to enable intents in the bot settings in the panel or else some cmds might not work
token = "token here(for your bot)"
bot = commands.Bot(command_prefix="?", help_command=None, intents=intents)
prefix = "?"
color = 0x1f8b4c
sucess="<a:CheckAnimated:881988824929013771>"
#Add a check animated emoji in your server of choice and replace sucess with the emoji id(the bot needs to be in that server)
error="Couldn't dm that member with a message"

@bot.command()
async def funfact(ctx, amount: int = 1):
    user = ctx.author.id
    author = await bot.fetch_user(user)
    response = request.urlopen('https://raw.githubusercontent.com/assaf/dailyhi/master/facts.txt')
    funfacts = response.readlines()
    if amount <= 5:
        for r in range(amount):
            fact = random.choice(funfacts)
            embed = discord.Embed(title="Random fact/Fun fact", description=f"""Random fact: {fact}                                            
Does reading this make you smarter? <:smoothbrain:882413835611439154>""", color=color)
            embed.set_footer(text=f"""Facts from: https://github.com/assaf/dailyhi/blob/master/facts.txt. Funfact: there are exactly 3090 funfacts in this |
Command by {author}. Tip: You can get multiple funfacts by doing {prefix}funfact (amount) max is 5""")
            await ctx.send(embed=embed)
    else:
        await ctx.send("Amount needs to be 5 or lower")


@bot.command()
async def ping(ctx):
    await ctx.send(f"{int(bot.latency)}ms")


@bot.command()
async def serverinfo(ctx):
    id = ctx.message.guild.id
    name = ctx.message.guild.name
    owner = ctx.guild.owner
    oid = ctx.guild.owner_id
    creation = ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S")
    members = len(ctx.guild.members)
    bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
    people = len(list(filter(lambda m: not m.bot, ctx.guild.members)))
    bmembers = len(await ctx.guild.bans())
    tchannels = len(ctx.guild.text_channels)
    vchannels = len(ctx.guild.voice_channels)
    roles = len(ctx.guild.roles)
    c = len(ctx.guild.categories)
    picture = ctx.guild.icon_url
    embed = discord.Embed(title=f"Server Info for {name} ({id})", description=f"""**Server Name:** {name}                                  
**Server ID:** {id}                                                                                                                        
**Owner:** {owner} ({oid})                                                                                                                 
**Creation date:**  {creation}                                                                                                             
**Total Members:** {members}                                                                                                               
**Bots:** {bots}                                                                                                                           
**People:** {people}                                                                                                                       
**Bans:** {bmembers}                                                                                                                       
**Text Channels:** {tchannels}                                                                                                             
**Voice Channels:** {vchannels}                                                                                                            
**Roles:** {roles}                                                                                                                         
**Categories:** {c}                                                                                                                        
**Server Icon:** {picture}                                                                                                                 
""", color=color)
    embed.set_footer(text=f"Showing information for the server: {name}")
    embed.set_thumbnail(url=picture)
    await ctx.send(embed=embed)


# ^from carberra turtorials youtube

@bot.command()
async def rps(ctx, choice=None):
    embed = discord.Embed(title=f"{prefix}rps [Buggy] command", description="""**Description:** The bot plays rock paper scissors with you 
               **Usage:** rps (rock, paper, scissors) """, color=color)
    embed.set_footer(text="This might be buggy")
    if choice is None:
        await ctx.send(embed=embed)
    else:
        rock = str("rock")
        paper = str("paper")
        scissors = str("scissors")
        choices = rock, paper, scissors
        x = random.choice(choices)

        if choice is None:
            await ctx.send(embed)
        else:
            if choice not in choices:
                await ctx.send("Invalid option")
                await ctx.send(embed=embed)
            else:
                message = await ctx.send("Starting game...")
                author = ctx.author.id
                user = await bot.fetch_user(author)
                if choice == paper:
                    choice = ":newspaper:"
                if x == paper:
                    x = ":newspaper:"
                newembed = discord.Embed(title="Rock Paper Scissors [Buggy]",
                                         description=f"""**You | {user}:** :{choice}:                                                      
                 **Me | {bot.user}:** :{x}:                                                                                                
""", color=color)
                newembed.set_footer(text=f"Command by {user}")
                await message.edit(embed=newembed)


@bot.command()
async def commands(ctx, amount: int = 1):
    if amount == 1 or None:
            embed = discord.Embed(title="Commands", description="""Features:                                                                   
    `userinfo`: Gets information on a user
`rolldice`: Gets a random number from 1-10
`cointoss`: Simulates flipping a coin
`antilink/antiadvertise` (ill add a scanner using vtapi soon): Automatically deletes links starting with https:// http:// and discord.gg
`ban`: Bans a member
`purge`: Deletes a certain amount of messages in a channel
`unban`: Unbans a member
`softban`: Bans then unbans a member to delete all their messages (They get dmed with an invite back to the server)
`kick`: Kicks a member
`addrole`: Gives a role to a member
`removerole`: Removes a role from a member
`mute`: Mutes a member so they can't talk
`prefix`: Gets the bot's prefix                                                                                                         
    """, color=color)
            embed.set_footer(
                text=f"Your current prefix is {prefix} | Page 1 of 3 (do {prefix}commands (page) to navigate to a different page)")
            await ctx.send(embed=embed)
    elif amount == 2:
        embed2 = discord.Embed(title="Commands", description="""Features:                                                                  
`unmute`: Unmutes a member
`pfp`: Gets the profile picture of a user
`slowmode`: Adds slowmode to a channel
`lock`(some error checking isnt complete): Locks a channel so regular members can't talk in it
`unlock`(some error checking isnt complete): Unlocks a channel
`autorole`: Automatically gives new members a role when they join 
`autowelcome`: Automatically welcomes new members
`help`: Shows the help page
`commands`: Shows this page
`ping`: Gets the bot's ping
`serverinfo`: Gets information on the server
`funfact`: Gets a random funfact
`rps`: The bot plays rock paper scissors with you (buggy)                                                                                                     
                """, color=color)
        embed2.set_footer(text=f"Your current prefix is {prefix} | Page 2 of 3")
        await ctx.send(embed=embed2)
    elif amount == 3:
        embed3=discord.Embed(title="Commands",description="""Features:
            `delchannel`: Deletes a channel
            `createchannel`: Creates a channel
            `gamble`: Starts a gambling game
            `randomnumber`: Generates a random number for you
            `ver`: Starts a verification
            I forgot to list some things check the code for all the features""")
        embed3.set_footer(text=f"Your current prefix is {prefix} | Page 3 of 3")
        await ctx.send(embed=embed3)


@bot.command()
async def changelog(ctx):
    author = ctx.author.id
    user = await bot.fetch_user(author)
    embed=discord.Embed(title="Changelog 7/21/2022", description=f"""
`[+]` Gamble
`[+]` Random number
`[+]`Verification
""", color=color)
    embed.set_footer(text=f"Update 7/21/2022 by iforgotmypassword#4647 | Requested by {user}")
    await ctx.send(embed=embed)


@bot.command()
async def gamble(ctx):
    id=ctx.author.id
    user=await bot.fetch_user(id)
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    final=dice2+dice1
    dice3 = random.randint(1, 6)
    dice4 = random.randint(1, 6)
    final2=dice3+dice4
    if final > final2:
        result="Won"
    else:
        result="Lost"

    embed=discord.Embed(title=f"{user.name}'s gambling game", description=f'''Result: {result}
{user.name}(you) rolled: `{final}`
Bot rolled: `{final2}`''')
    await ctx.send(embed=embed)



@bot.command()
async def randomnumber(ctx, user: discord.User = None):
    num = random.randint(0, 100)
    embed = discord.Embed(title="Random number", description=f"{num}")
    await ctx.send(embed=embed)


@bot.command()
async def help(ctx):
    author = ctx.author.id
    user = await bot.fetch_user(author)
    embed=discord.Embed(title="Help", description="""modbot.
    The bot is written in python using discord.py(https://github.com/Rapptz/discord.py)
    The bot is equipped with most essential moderation commands, more will be added in the future
    Notable mentions: Stackoverflow, iforgotmypassword#4647""", color=color)
    embed.set_footer(text=f"Your current prefix is {prefix} | Requested by {user}")
    await ctx.send(embed=embed)


@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    if member is None:
        embed = discord.Embed(title=f"{prefix}userinfo command", description=f"""**Description:** Get the user info of a user on discord   
        **Usage:** {prefix}userinfo (member)""", color=color)
        await ctx.send(embed=embed)
    else:
        user = member.id
        creationdate = member.created_at.strftime("%a, %b %d, %Y %I:%M:%S %p")
        joindate = member.joined_at.strftime("%a, %b %d, %Y %I:%M:%S %p")
        a = await bot.fetch_user(user)
        embed = discord.Embed(title=f"Userinfo for {member}", description=f"""Creation date: {creationdate} UTC                            
Joined at: {joindate} UTC                                                                                                                  
Avatar: {member.avatar_url}""", color=color)
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)


@bot.command()
async def rolldice(ctx, amount: int = 1):
    for r in range(amount):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        dice = random.choice(numbers)
        b = engine()
        numberword = b.number_to_words(dice)
        message = await ctx.send("Rolling dice...")
        if numberword == "ten":
            ten = discord.Embed(title="Finished rolling dice <a:diceroll:882286593900183553>",
                                description=f"You rolled the number :keycap_ten:!", color=color)
            await message.delete()
            await ctx.send(embed=ten)
        else:
            other = discord.Embed(title="Finished rolling dice <a:diceroll:882286593900183553>",
                                  description=f"You rolled the number :{numberword}:!", color=color)
            await message.delete()
            await ctx.send(embed=other)


@bot.command()
async def cointoss(ctx, amount: int = 1):
    for r in range(amount):
        message = await ctx.send("Throwing coin :coin:")
        options = "Heads", "Tails"
        result = random.choice(options)
        embed = discord.Embed(title = "Finished coin toss :coin:", description = f"You got {result}", color=color)
        await message.delete()
        await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    id = message.author.id
    if "discord.gg/" in message.content.lower():
        await message.delete()
        await message.channel.send("You can't send links <@%s>" % id, delete_after=3)
    elif "https://" in message.content.lower():
        await message.delete()
        await message.channel.send("You can't send links <@%s>" % id, delete_after=3)
    elif "http://" in message.content.lower():
        await message.delete()
        await message.channel.send("You can't send links <@%s>" % id, delete_after=3)
    if bot.user.mentioned_in(message):
        if message.mention_everyone:
            pass
        else:
            await message.channel.send(f"Hi im modbot, nice to meet you <@{message.author.id}>! :wave:")
    await bot.process_commands(message)


@bot.command()
async def ban(ctx, member: discord.User = None, reason=None):
    if not ctx.author.guild_permissions.ban_members:
        await ctx.send("You don't have permission to use that command")
    else:
        if member is None:
            embed = discord.Embed(title=f"{prefix}ban command", description=f"""**Usage**: {prefix}ban (member) (reason)                   
**Description**: Bans a member""", color=color)
            embed.set_footer(text="Using 0.01% of my power")
            await ctx.send(embed=embed)
        elif member == ctx.message.author:
            ctx.send("You can't ban yourself")
            return
        else:
            author = ctx.author.id
            user = await bot.fetch_user(author)
            if reason is None:
                reason = "Not specified"
            message = f"You were banned from {ctx.guild.name} by {user} ({author}). **Reason**: {reason}"
            try:
                await ctx.guild.ban(member, reason=reason)
                await member.send(message)
                embed = discord.Embed(title="", description=f"{sucess} **{member} was banned**", color=color)
                await ctx.send(embed=embed)
            except Exception as e:
                await ctx.send(error)
                print(e)


@bot.command()
async def purge(ctx, channel: discord.TextChannel = None, amount: int = 0):
        if not ctx.author.guild_permissions.manage_channels:
            await ctx.send("You don't have permission to use that command")
        else:
            if channel is None:
                embed=discord.Embed(title=f"{prefix}purge command", description=f"""**Usage:** {prefix}purge (channel) (amount of messages)
**Description:** Deletes a certain amount of messages from the last 14 days from a certain channel""", color=color)
                await ctx.send(embed=embed)
            else:
                count = 0
                async for _ in channel.history(limit=None):
                    count += 1
                if count == 1:
                    await ctx.send("There aren't any messages to purge")
                else:
                    try:
                        await channel.purge(limit=amount)
                        embed=discord.Embed(title="", description=f"{sucess} **Purged {amount} messages from {channel.name}**", color=color)
                        await ctx.send(embed=embed, delete_after=5)
                    except:
                        await ctx.send("I can't delete messages that are more then 14 days old")


@bot.command()
async def unban(ctx, member: discord.User = None):
    if not ctx.author.guild_permissions.ban_members:
        await ctx.send("You don't have permission to use that command")
    else:
        if member is None:
            embed = discord.Embed(title=f"{prefix}unban command", description=f"""**Usage**: {prefix}unban (member)                        
**Description**: unbans a member (If they're banned)""", color=color)
            await ctx.send(embed=embed)
        elif member == ctx.message.author:
            ctx.send("You can't unban yourself")
            return
        else:
            try:
                await ctx.guild.unban(member)
                embed = discord.Embed(title="", description=f"{sucess} **{member} was unbanned**", color=color)
                await ctx.send(embed=embed)
            except Exception as e:
                await ctx.send("Are you sure that user is banned?")
                print(e)


@bot.command()
async def softban(ctx, member: discord.User = None):
    if not ctx.author.guild_permissions.ban_members:
        await ctx.send("You don't have permission to use that command")
    else:
        if member is None:
            embed = discord.Embed(title=f"{prefix}softban command", description=f"""**Usage**: {prefix}softban (member)                    
**Description**: bans a member then unbans them to delete their messages (If they're in the server)""", color=color)
            await ctx.send(embed=embed)
        elif member == ctx.message.author:
            ctx.send("You can't softban yourself")
            return
        else:
            author = ctx.author.id
            user = await bot.fetch_user(author)
            invite = await ctx.channel.create_invite(max_uses=1)
            try:
                await ctx.guild.ban(member)
                await ctx.guild.unban(member)
                await member.send(
                    f"You were softbanned from {ctx.guild.name} b {user} ({author}), (This means that you were banned then unbanned to delete all your messages). Here is an invite to the server {invite}")
                embed = discord.Embed(title="", description=f"{sucess} **{member} was softbanned**", color=color)
                await ctx.send(embed=embed)
            except Exception as e:
                await ctx.send("Are you sure that user is in the server?")
                print(e)


@bot.command()
async def kick(ctx, member: discord.User = None, *, reason=None):
    if not ctx.author.guild_permissions.kick_members:
        await ctx.send("You don't have permission to use that command")
    else:
        if member is None:
            embed = discord.Embed(title=f"{prefix}kick command", description=f"""**Usage**: {prefix}kick (member) (reason)                 
                                    **Description**: kicks a member""", color=color)
            await ctx.send(embed=embed)
        elif member == ctx.message.author:
            await ctx.channel.send("You can't' kick yourself")
            return
        else:
            author = ctx.author.id
            user = await bot.fetch_user(author)
            if reason is None:
                reason = "Not specified"
            message = f"You were kicked from {ctx.guild.name} by {user} ({author}). **Reason:** {reason}"
            try:
                await ctx.guild.kick(member, reason=reason)
                await member.send(message)
            except Exception as e:
                await ctx.send("Couldn't kick that member")
                print(e)
            embed = discord.Embed(title="", description=f"{sucess}**{member} was kicked**", color=color)
            await ctx.send(embed=embed)


@bot.command()
async def addrole(ctx, member: discord.Member = None, role: discord.Role = None):
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.send("You don't have permission to use that command")
    else:
        if member is None:
            embed = discord.Embed(title = f"{prefix}addrole command", description = f"""**Description:** Gives a member a specific role
            **Usage:** {prefix}addrole (member) (role)
""", color=color)
            await ctx.send(embed=embed)
        elif member == bot.user:
            await ctx.send("I already have admin why would I need that role lol")
        else:
            embed=discord.Embed(tile="",description=f"{sucess} **Added role <@{role.id}> to {member.name}**", color=color)
            await member.add_roles(role)
            await ctx.send(embed=embed)


@bot.command()
async def removerole(ctx, member: discord.Member = None, role: discord.Role = None):
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.send("You don't have permission to use that command")
    else:
        if member is None:
            embed = discord.Embed(title = f"{prefix}removerole command", description = f"""**Description:** Removes a specific role from a member
            **Usage:** {prefix}removerole (member) (role)
""", color=color)
            await ctx.send(embed=embed)
        elif member == bot.user:
            await ctx.send("You can't remove roles from me")
        else:
            await member.remove_roles(role)
            embed = discord.Embed(title = "", description = f"{sucess} **Removed the role {role} from {member}**", color=color)
            await ctx.send(embed=embed)


@bot.command()
async def unmute(ctx, member: discord.Member = None):
    if not ctx.author.guild_permissions.ban_members:
        await ctx.send("You don't have permission to use that command")
    else:
        if member == ctx.message.author:
            await ctx.send("You can't unmute yourself")
        elif member == bot.user:
            await ctx.send("You cant unmute me im a bot")
        else:
            if member is None:
                embed = discord.Embed(title=f"{prefix}unmute command", description=f"""**Usage**: {prefix}unmute (member) (reason)                 
                    **Description:** Unmutes a member""", color=color)
                await ctx.send(embed=embed)
            else:
                author = ctx.author.id
                user = await bot.fetch_user(author)
                role = discord.utils.get(ctx.guild.roles, name="Muted")
                if role not in member.roles:
                    await ctx.send(f"{member} isn't muted")
                else:
                    muted = discord.Permissions(send_messages=False, speak=False)
                    if discord.utils.get(ctx.guild.roles, name="Muted"):
                        pass
                    else:
                        await ctx.guild.create_role(name="Muted", permissions=muted, color=0x979c9f)
                    for channel in ctx.guild.text_channels:
                        perms = channel.overwrites_for(role)
                        perms.send_messages = False
                        await channel.set_permissions(role, overwrite=perms)
                    await member.remove_roles(role)
                    embed = discord.Embed(title="",
                                          description=f"{sucess} **{member} was unmuted**", color=color)
                    await ctx.send(embed=embed)
                    await member.send(f"You were unmuted in {ctx.guild.name} by {user} ({author}).")


@bot.command()
async def mute(ctx, member: discord.Member = None, reason = None):
    if not ctx.author.guild_permissions.ban_members:
        await ctx.send("You don't have permission to use that command")
    else:
        if member == ctx.message.author:
            await ctx.send("You can't mute yourself")
        elif member == bot.user:
            await ctx.send("You cant mute me im a bot")
        else:
            if member is None:
                embed = discord.Embed(title=f"{prefix}mute command", description=f"""**Usage**: {prefix}unmute (member) (reason)                 
                    **Description:** Mutes a member""", color=color)
                await ctx.send(embed=embed)
            else:
                author = ctx.author.id
                user = await bot.fetch_user(author)
                role = discord.utils.get(ctx.guild.roles, name="Muted")
                if role in member.roles:
                    await ctx.send(f"{member} is already muted")
                else:
                    if reason is None:
                        reason = "Not specified"
                    muted = discord.Permissions(send_messages=False, speak=False)
                    if discord.utils.get(ctx.guild.roles, name="Muted"):
                        for channel in ctx.guild.text_channels:
                            perms = channel.overwrites_for(role)
                            perms.send_messages = False
                            await channel.set_permissions(role, overwrite=perms)
                        await member.add_roles(role)
                        embed = discord.Embed(title="", description=f"{sucess} **{member} was muted**", color=color)
                        await ctx.send(embed=embed)
                        await member.send(f"You were muted in {ctx.guild.name} by {user} ({author}). **Reason:** {reason}")
                    else:
                        await ctx.guild.create_role(name="Muted", permissions=muted, color=0x979c9f)
                        role = discord.utils.get(ctx.guild.roles, name="Muted")
                        for channel in ctx.guild.text_channels:
                            perms = channel.overwrites_for(role)
                            perms.send_messages = False
                            await channel.set_permissions(role, overwrite=perms)
                        await member.add_roles(role)
                        embed = discord.Embed(title="", description=f"{sucess} **{member} was muted**", color=color)
                        await ctx.send(embed=embed)


@bot.command()
async def pfp(ctx, member: discord.User = None):
    if member is None:
        embed = discord.Embed(title=f"{prefix}pfp command", description=f"""                                                               
**Description**: Gets the pfp of a user                                                                                                    
**Usage**: {prefix}pfp (member) """)
        await ctx.send(embed=embed)
    else:
        try:
            target = member.id
            user = await bot.fetch_user(target)
            embed = discord.Embed(title=f"{user}'s avatar")
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)
        except Exception as e:
            pass
            print(e)


@bot.command()
async def slowmode(ctx, channel: discord.TextChannel = None, seconds: int = 5):
    if not ctx.author.guild_permissions.manage_channels:
        await ctx.send("You don't have permission to use that command")
    else:
        if channel is None:
            embed = discord.Embed(title=f"{prefix}slowmode command", description = f"""**Description:** Sets slowmode on a given channel
**Usage:** {prefix}slowmode (channel) (delay)""", color=color)
            embed.set_footer(text = "Default slowmode is 5. Set delay to 0 if you want to remove slowmode")
            await ctx.send(embed=embed)
        else:
            if seconds > 21600:
                await ctx.send("Max slowmode is 21600 (6h) why would you want to do this lol")
            else:
                await ctx.channel.edit(slowmode_delay=seconds)
                embed = discord.Embed(title="",
                                  description=f"{sucess} **Set a slowmode of {seconds} seconds in the channel #{channel}**", color=color)
                await ctx.send(embed=embed)


@bot.command()
async def lock(ctx, channel: discord.TextChannel = None, reason = None):
    if not ctx.author.guild_permissions.manage_channels:
        await ctx.send("You don't have permission to use that command")
    else:
        if channel is None:
            embed = discord.Embed(title=f"{prefix}lock command", description=f"""**Description:** Locks a channel so no one can speak in it except for higher ranks
**Usage:** {prefix}lock (channel) (reason)""", color=color)
            await ctx.send(embed=embed)
        else:
            if reason is None:
                reason = "Not specified"
                await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
                embed = discord.Embed(title="", description=f"{sucess} **Locked channel {channel}** | Reason: {reason}", color=color)
                await ctx.send(embed=embed)


@bot.command()
async def unlock(ctx, channel: discord.TextChannel= None):
    if not ctx.author.guild_permissions.manage_channels:
        await ctx.send("You don't have permission to use that command")
    else:
        if channel is None:
            embed = discord.Embed(title=f"{prefix}unlock command", description=f"""**Description:** Unlocks a channel that was previously locked
**Usage:** {prefix}unlock (channel)""", color=color)
            await ctx.send(embed=embed)
        else:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
            embed = discord.Embed(title="", description=f"{sucess} **Unlocked channel #{channel}**", color=color)
            await ctx.send(embed=embed)


@bot.event
async def on_member_join(member):
    c = bot.get_channel("channel id") #the bot needs to be able to access this channel
    await c.send(f"<@{member.id}> just joined")


@bot.command()
async def delchannel(ctx,channel:discord.TextChannel=None):
    if not ctx.author.guild_permissions.manage_channels:
        await ctx.send("You don't have permission to use that command")
    else:
        if channel is None:
            embed=discord.Embed(title=f"{prefix}delchannel command", description=f"""**Description:** Deletes a channel
**Usage:** {prefix}delchannel (channel)""", color=color)
            await ctx.send(embed=embed)
        else:
            await channel.delete()
            embed=discord.Embed(title="", description=f"{sucess}Deleted channel {channel.name}", color=color)
            await ctx.send(embed=embed)


@bot.command()
async def nick(ctx, member: discord.Member = None, nick: str= None):
    if not ctx.author.guild_permissions.manage_nicknames:
        await ctx.send("You don't have permission to use that command")
    if member is None:
        embed=discord.Embed(title=f"{prefix}nick command", description=f"""**Description:** Changes a members nickname
        **Usage:** {prefix}nick (member) (nickname)""", color=color)
        embed.set_footer(text="Nick name needs to be 2-32 characters long")
        await ctx.send(embed=embed)
    else:
        await member.edit(nick=nick)
        embed=discord.Embed(title="", description=f"{sucess} **Set nickname {nick} for {member.name}**", color=color)
        await ctx.send(embed=embed)


@bot.command()
async def createchannel(ctx,channel: str = None):
    if not ctx.author.guild_permissions.manage_channels:
        await ctx.send("You don't have permission to use that command")
    else:
        if channel is None:
            embed=discord.Embed(title=f"{prefix}createchannel command", description=f"""**Description:** Creates a channel
**Usage:** {prefix}createchannel (channel)""", color=color)
            await ctx.send(embed=embed)
        else:
            await ctx.message.guild.create_text_channel(channel)
            embed=discord.Embed(title="", description=f"{sucess}Created channel {channel}", color=color)
            await ctx.send(embed=embed)

#verification by sending a message
@bot.event
async def on_member_join(member):
    guild=member.guild
    unverified=discord.utils.get(guild.roles, id="unverified role")#bot needs to be able to give the unverified role in order for verification to work
    await member.add_roles(unverified)


@bot.event
async def on_ready():
    print("Finished loading")
    os.system("cls")
    print(bot.user, 'is running')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{prefix}help"))


@bot.command()
async def eightball(ctx):
    id=ctx.author.id
    user=bot.get_user(id)
    replies = [
        'It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes - definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Do not count on it.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Very doubtful.'
    ]
    reply=random.choice(replies)
    def check(m):
        return (
            m.channel.id == ctx.channel.id
        )
    await ctx.send("message")
    msg = await bot.wait_for("message", check=check)
    embed = discord.Embed(title=f"{user.name} asked 8ball a question", description=f"""**Question**: {msg.content}
    **Answer**: {reply}""")
    await ctx.send(embed=embed)


@bot.command()
async def ver(ctx):
    id = ctx.author.id
    user1 = bot.get_user(id)
    role = discord.utils.get(ctx.guild.roles, name="unverified")
    valid_reactions = ["🇦","🇧","🇨","🇩","🇪"]
    verified=random.choice(valid_reactions)
    if ctx.message.channel.id == 975176691741761546 and role in ctx.author.roles: #the channel id is the verification channel
        verificationembed=discord.Embed(title="Are you a bot?", description=f"React to this message with the letter {verified}")
        verificationembed.set_footer(text="Verification will timeout after 30 seconds")
        message=await ctx.send(embed=verificationembed)
        for reaction in valid_reactions:
            await message.add_reaction(reaction)
        def check(reaction, user):

            return user == ctx.author and str(reaction.emoji) in valid_reactions

        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)

        if str(reaction.emoji) == verified:
            embed =  discord.Embed(description="Verification passed", color=0x2ecc71)
            embed.set_footer(text="Thank you for verifying")
            newembed = discord.Embed(description="Thank you for verifying")
            newembed.set_footer(text=f"Sent from {ctx.message.guild.name}")
            await user1.send(embed=newembed)
            await message.edit(embed=embed)
            await ctx.author.remove_roles(role)
        else:
            embedf = discord.Embed(description="Verification failed", color=0xe74c3c)
            await message.edit(embed=embedf)
            await user1.send(f"You were kicked from {ctx.message.guild.name} because you failed the verification")
            await ctx.author.kick()


    else:
        await ctx.send("you can't use this command")

@bot.command()
async def gaw(ctx):
    id=ctx.author.id
    await ctx.send("Are you sure you want to start a giveaway?(y/N)")
    def check(m):
        return (
            m.channel.id == ctx.channel.id
        )
    msg = await bot.wait_for("message", check=check)
    if msg.content == "N":
        await ctx.send("Aborted giveaway")
    elif msg.content == "y":
        await ctx.send("What do you want the prize to be?")
        prize = await bot.wait_for("message", check=check)
        await ctx.send("How long do you want the giveaway to last?")
        timeline = await bot.wait_for("message", check=check)
        await ctx.send("How many winners should there be")
        winners = await bot.wait_for("message", check=check)
        await ctx.send("Starting giveaway")
        embed=discord.Embed(title=prize, description=f"""Host: <@{id}>
Number of winners: {winners}
Duration: {timeline}""")
        await ctx.send(embed=embed)
    else:
        await ctx.send("Thats not a valid choice")
#in progress

bot.run(token)
