import os, sys, random, asyncio, discord

TOKEN = os.getenv("TOKEN") or os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")
DELAY = os.getenv("DELAY")
VANITY_FILE = os.getenv("VANITY_FILE")

if not TOKEN or not GUILD_ID or not DELAY or not VANITY_FILE:
    print("Missing required environment variables: TOKEN, GUILD_ID, DELAY, VANITY_FILE")
    sys.exit(1)

try:
    GUILD_ID = int(GUILD_ID)
    DELAY = float(DELAY)
except Exception as e:
    print("GUILD_ID must be an integer and DELAY must be a number.")
    sys.exit(1)

try:
    with open(VANITY_FILE, "r", encoding="utf-8") as f:
        vanities = [line.strip() for line in f if line.strip()]
except Exception as e:
    print("Failed to read vanity file:", e)
    sys.exit(1)

if not vanities:
    print("No vanity entries found in file.")
    sys.exit(1)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def _rotate():
    await client.wait_until_ready()
    guild = client.get_guild(GUILD_ID)
    if guild is None:
        print("Guild not found. Check GUILD_ID and bot membership.")
        await client.close()
        return
    last = None
    while True:
        choice = random.choice(vanities)
        if len(vanities) > 1:
            while choice == last:
                choice = random.choice(vanities)
        try:
            await guild.edit(vanity_code=choice)
            print("Vanity changed to:", choice)
            last = choice
        except discord.Forbidden:
            print("Forbidden: missing permissions to change vanity.")
        except discord.HTTPException as e:
            print("HTTP error:", e)
        except Exception as e:
            print("Unexpected error:", e)
        await asyncio.sleep(DELAY)

client.loop.create_task(_rotate())
client.run(TOKEN, bot=False)
