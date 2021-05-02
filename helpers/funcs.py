import discord


def check(author, channel):
    def inner_check(message):
        return message.author == author and message.channel == channel
    return inner_check


def create_embed(title=None, description=None, author=None, fields=None, image=None, thumbnail=None, footer=None, color=discord.Color.teal()):
    if title:
        embed = discord.Embed(title=title, color=color)
    else:
        embed = discord.Embed(color=color)
    if description:
        embed.description = description
    if author:
        embed.set_author(name="For " + author.name, icon_url=author.avatar_url)
    if fields:
        for field in fields:
            embed.add_field(name=field[0], value=field[1], inline=field[2] if len(field) > 2 else False)
    if image:
        embed.set_image(url=image)
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    if footer:
        embed.set_footer(text=footer)
    return embed


async def get_reacts(context, client, message, emojis, timeout=None):
    for emoji in emojis:
        await message.add_reaction(emoji)
    try:
        def check(reaction, user):
            return user.id == context.author.id
        reaction, user = await client.wait_for("reaction_add", check=check, timeout=timeout)
        for emoji in emojis:
            if reaction.emoji == emoji:
                return reaction
    except:
        pass