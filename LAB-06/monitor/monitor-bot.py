import psutil
import logging
import time
import asyncio
from telegram import Bot

# Thay thế bằng mã truy cập API của bot bạn đã tạo
BOT_TOKEN = "7222161160:AAGKEK9Cu2SJ2yc0NU8YXZCCTB8xs2ZsoFQ"

# Thay thế bằng chat_id của cuộc trò chuyện bạn muốn gửi thông báo tới
CHAT_ID = "-4609468938"

# Cấu hình logging
logging.basicConfig(level=logging.INFO, filename="system_monitor_bot.log",
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Hàm ghi log
def log_info(category, message):
    logger.info(f"{category}: {message}")
    print(f"{category}: {message}")

# Hàm gửi tin nhắn qua Telegram
async def send_telegram_message(message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)

# Hàm giám sát CPU và bộ nhớ
def monitor_cpu_memory():
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()

    log_info("CPU", f"Usage: {cpu_percent}%")
    log_info("Memory", f"Usage: {memory_info.percent}%")

    # Gửi thông báo qua Telegram
    message = f"CPU Usage: {cpu_percent}%\nMemory Usage: {memory_info.percent}%"
    asyncio.run(send_telegram_message(message))

# Hàm thực hiện giám sát toàn bộ hệ thống
def monitor_system():
    log_info("System Monitor", "Starting system monitoring...")
    while True:
        monitor_cpu_memory()
        log_info("System Monitor", "---------------")
        time.sleep(60)

if __name__ == "__main__":
    monitor_system()