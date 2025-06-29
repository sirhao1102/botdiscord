import discord
import json
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Load JSON patch data
with open("patch_data.json", "r", encoding="utf-8") as f:
    patch_data = json.load(f)

def search_patch(query):
    query_lower = query.lower()
    results = []
    for item in patch_data:
        if query_lower in (item["title"] + " " + item["content"]).lower():
            results.append(item)
    return results

@client.event
async def on_ready():
    print(f"✅ Bot đã online: {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("!patch"):
        query = message.content[len("!patch"):].strip()
        await message.channel.send("⏳ Đang tìm thông tin...")
        results = search_patch(query)
        if results:
            reply = "\n\n".join([f"📌 **{r['title']}**\n{r['content']}" for r in results[:3]])
        else:
            reply = "❌ Không tìm thấy thông tin liên quan trong patch notes."
        await message.channel.send(reply)

client.run(TOKEN)
