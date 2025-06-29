import os
import faiss
import json
import numpy as np
import discord
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("faiss_patch.index")
with open("contexts.json", "r", encoding="utf-8") as f:
    contexts = json.load(f)

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f"✅ Bot đã online: {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!patch"):
        query = message.content[6:].strip()
        q_emb = model.encode(query).astype('float32')
        D, I = index.search(np.array([q_emb]), 1)
        context = contexts[I[0][0]]
        await message.channel.send(f"🔎 Nội dung liên quan: {context[:1800]}")

client.run(os.getenv("DISCORD_TOKEN"))
