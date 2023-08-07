import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # To access message content

bot = commands.Bot(command_prefix='>', intents=intents) #ginamit ko ay > for bot commands

# Dictionary to store manga recommendations
manga_recommendations = {}
# Dictionary to store games recommendations
games_recommendations = {}
# Dictionary to store movies recommendations
movies_recommendations = {}
# Dictionary to store songs recommendations
songs_recommendations = {}
# Dictionary to store anime recommendations
anime_recommendations = {}

bot.remove_command('help') #inaalis nya yung help command dahil nagiinterfere siya sa help command ni discord
#for manga
@bot.command()
async def manga(ctx, *, title: str):
    if title:
        if 'Manga' not in manga_recommendations:
            manga_recommendations['Manga'] = []
        manga_recommendations['Manga'].append(title)
        await ctx.send(f"Added '{title}' to manga recommendations.")
    else:
        await ctx.send("Please provide the title of the manga.")

@bot.command()
async def mangaclear(ctx):
    manga_recommendations.clear()
    await ctx.send("Cleared all manga recommendations.")

@bot.command()
async def mangaremove(ctx, *, title: str):
    removed = False
    for category, titles in manga_recommendations.items():
        if title in titles:
            titles.remove(title)
            await ctx.send(f"Removed '{title}' from manga recommendations.")
            removed = True
            break
    if not removed:
        await ctx.send(f"'{title}' not found in manga recommendations.")

@bot.command()
async def mangasummary(ctx):
    summary = []
    for category, titles in manga_recommendations.items():
        summary.append(f"{category}:\n" + '\n'.join(titles))
    if summary:
        await ctx.send('\n\n'.join(summary))
    else:
        await ctx.send("No manga recommendations available yet.")

#for Games
@bot.command()
async def games(ctx, *, title: str):
    if title:
        if 'Games' not in games_recommendations:
            games_recommendations['Games'] = []
        games_recommendations['Games'].append(title)
        await ctx.send(f"Added '{title}' to games recommendations.")
    else:
        await ctx.send("Please provide the title of the game.")

@bot.command()
async def gamesclear(ctx):
    games_recommendations.clear()
    await ctx.send("Cleared all games recommendations.")

@bot.command()
async def gamesremove(ctx, *, title: str):
    removed = False
    for category, titles in games_recommendations.items():
        if title in titles:
            titles.remove(title)
            await ctx.send(f"Removed '{title}' from games recommendations.")
            removed = True
            break
    if not removed:
        await ctx.send(f"'{title}' not found in games recommendations.")

@bot.command()
async def gamessummary(ctx):
    summary = []
    for category, titles in games_recommendations.items():
        summary.append(f"{category}:\n" + '\n'.join(titles))
    if summary:
        await ctx.send('\n\n'.join(summary))
    else:
        await ctx.send("No games recommendations available yet.")

#for movies
@bot.command()
async def movies(ctx, *, title: str):
    if title:
        if 'Movies' not in movies_recommendations:
            movies_recommendations['Movies'] = []
        movies_recommendations['Movies'].append(title)
        await ctx.send(f"Added '{title}' to movies recommendations.")
    else:
        await ctx.send("Please provide the title of the movie.")

@bot.command()
async def moviesclear(ctx):
    movies_recommendations.clear()
    await ctx.send("Cleared all movies recommendations.")

@bot.command()
async def moviesremove(ctx, *, title: str):
    removed = False
    for category, titles in movies_recommendations.items():
        if title in titles:
            titles.remove(title)
            await ctx.send(f"Removed '{title}' from movies recommendations.")
            removed = True
            break
    if not removed:
        await ctx.send(f"'{title}' not found in movies recommendations.")

@bot.command()
async def moviessummary(ctx):
    summary = []
    for category, titles in movies_recommendations.items():
        summary.append(f"{category}:\n" + '\n'.join(titles))
    if summary:
        await ctx.send('\n\n'.join(summary))
    else:
        await ctx.send("No movies recommendations available yet.")
#for songs
@bot.command()
async def songs(ctx, *, title: str):
    if title:
        if 'Songs' not in songs_recommendations:
            songs_recommendations['Songs'] = []
        songs_recommendations['Songs'].append(title)
        await ctx.send(f"Added '{title}' to songs recommendations.")
    else:
        await ctx.send("Please provide the title of the song.")

@bot.command()
async def songsclear(ctx):
    songs_recommendations.clear()
    await ctx.send("Cleared all songs recommendations.")

@bot.command()
async def songsremove(ctx, *, title: str):
    removed = False
    for category, titles in songs_recommendations.items():
        if title in titles:
            titles.remove(title)
            await ctx.send(f"Removed '{title}' from songs recommendations.")
            removed = True
            break
    if not removed:
        await ctx.send(f"'{title}' not found in songs recommendations.")

@bot.command()
async def songssummary(ctx):
    summary = []
    for category, titles in songs_recommendations.items():
        summary.append(f"{category}:\n" + '\n'.join(titles))
    if summary:
        await ctx.send('\n\n'.join(summary))
    else:
        await ctx.send("No songs recommendations available yet.")
#for anime
@bot.command()
async def anime(ctx, *, title: str):
    if title:
        if 'Anime' not in anime_recommendations:
            anime_recommendations['Anime'] = []
        anime_recommendations['Anime'].append(title)
        await ctx.send(f"Added '{title}' to anime recommendations.")
    else:
        await ctx.send("Please provide the title of the anime.")

@bot.command()
async def animeclear(ctx):
    anime_recommendations.clear()
    await ctx.send("Cleared all anime recommendations.")

@bot.command()
async def animeremove(ctx, *, title: str):
    removed = False
    for category, titles in anime_recommendations.items():
        if title in titles:
            titles.remove(title)
            await ctx.send(f"Removed '{title}' from anime recommendations.")
            removed = True
            break
    if not removed:
        await ctx.send(f"'{title}' not found in anime recommendations.")

@bot.command()
async def animesummary(ctx):
    summary = []
    for category, titles in anime_recommendations.items():
        summary.append(f"{category}:\n" + '\n'.join(titles))
    if summary:
        await ctx.send('\n\n'.join(summary))
    else:
        await ctx.send("No anime recommendations available yet.")

@bot.command()
async def help(ctx):
    help_message = (
        "Here are the available commands:\n\n"
        ">manga [title] - Add a manga recommendation\n"
        ">mangaclear - Clear all manga recommendations\n"
        ">mangaremove [title] - Remove a specific manga recommendation\n"
        ">mangasummary - Show a summary of manga recommendations\n\n"

        ">games [title] - Add a games recommendation\n"
        ">gamesclear - Clear all games recommendations\n"
        ">gamesremove [title] - Remove a specific game recommendation\n"
        ">gamessummary - Show a summary of games recommendations\n\n"

        ">movies [title] - Add a movies recommendation\n"
        ">moviesclear - Clear all movies recommendations\n"
        ">moviesremove [title] - Remove a specific movie recommendation\n"
        ">moviessummary - Show a summary of movies recommendations\n\n"

        ">songs [title] - Add a songs recommendation\n"
        ">songsclear - Clear all songs recommendations\n"
        ">songsremove [title] - Remove a specific song recommendation\n"
        ">songssummary - Show a summary of songs recommendations\n\n"

        ">anime [title] - Add an anime recommendation\n"
        ">animeclear - Clear all anime recommendations\n"
        ">animeremove [title] - Remove a specific anime recommendation\n"
        ">animesummary - Show a summary of anime recommendations\n\n"
    )
    await ctx.send(help_message)


# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('Your Bot_Token')
