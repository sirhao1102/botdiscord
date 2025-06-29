import discord
from discord.ext import commands

# Tạo intents với quyền đọc nội dung tin nhắn
intents = discord.Intents.default()
intents.message_content = True

# Khởi tạo bot với prefix "!"
bot = commands.Bot(command_prefix="!", intents=intents)

# Khi bot online, in ra thông báo
@bot.event
async def on_ready():
    print(f"✅ Bot đã sẵn sàng: {bot.user}")

# Lệnh kiểm tra bot sống
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# Lệnh mẫu cho patch notes (anh có thể gắn xử lý context ở đây)
@bot.command()
async def patch(ctx, *, query: str):
    await ctx.send(f"🔍 Đang tìm thông tin cho: {query}")
    # Đây anh gắn code tìm context JSON / FAISS / gọi API vào
    # Ví dụ trả lời đơn giản
    await ctx.send(f"❌ Hiện tại chưa có thông tin cho: {query}")

# Chạy bot (token lấy từ ENV hoặc dán trực tiếp trong dev)
import os
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    TOKEN = "DÁN_TOKEN_VÀO_ĐÂY_NẾU_TEST_LOCAL"

bot.run(TOKEN)
