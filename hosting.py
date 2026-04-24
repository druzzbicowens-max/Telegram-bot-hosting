import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8773050881:AAHQ5n0860l1OMZOJ6teK0U02OAIH4qcPHU"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ================= MENU =================
def main_menu():
    keyboard = [
        [InlineKeyboardButton("🎁 Refer & Earn", callback_data="refer"),
         InlineKeyboardButton("💎 My Balance", callback_data="balance")],
        
        [InlineKeyboardButton("🏆 Leaderboard", callback_data="leaderboard"),
         InlineKeyboardButton("💳 Paid Panel", callback_data="paid")],
        
        [InlineKeyboardButton("🚀 Create Panel", callback_data="create"),
         InlineKeyboardButton("🗄 My Panels", callback_data="mypanels")],
        
        [InlineKeyboardButton("👤 My Profile", callback_data="profile"),
         InlineKeyboardButton("💬 Support", callback_data="support")]
    ]
    return InlineKeyboardMarkup(keyboard)

# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name

    text = f"""
🌟 *WELCOME TO HOSTING BOT 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗯𝘆 𝗗𝗥𝗨𝗭𝗭 𝗗𝗘𝗩 !*

👋 Hey *{user}*!
Welcome to Panel Bot!

Get your free hosting panel here.

⬇️ Choose an option from the menu below:
"""

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=main_menu()
    )

# ================= BUTTON HANDLER =================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "create":
        await create_panel(query)

    elif data == "balance":
        await query.edit_message_text("💎 Your balance: 0.00$")

    elif data == "refer":
        await query.edit_message_text("🎁 Invite friends and earn rewards!")

    elif data == "leaderboard":
        await query.edit_message_text("🏆 Leaderboard coming soon...")

    elif data == "paid":
        await query.edit_message_text("💳 Paid panels available soon.")

    elif data == "mypanels":
        await query.edit_message_text("🗄 You don't have any panels yet.")

    elif data == "profile":
        user = query.from_user
        await query.edit_message_text(
            f"👤 Profile\n\nName: {user.first_name}\nID: {user.id}"
        )

    elif data == "support":
        await query.edit_message_text("💬 Contact support: @Druzz_Dev")

# ================= CREATE PANEL =================
async def create_panel(query):
    # ⚠️ THIS IS MOCK — replace with real API call
    await query.edit_message_text(
        "🚀 Creating your server...\n\n⏳ Please wait..."
    )

    # simulate creation
    import asyncio
    await asyncio.sleep(2)

    await query.edit_message_text(
        "✅ Panel Created Successfully!\n\n"
        "🌐 URL: https://wispbyte.com\n"
        "👤 Username: your name\n"
        "🔑 Password: your password\n\n"
        "⚠️ Login your email and finish."
    )

# ================= MAIN =================
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
