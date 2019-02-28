import asyncio
import logging

from telethon import TelegramClient

from config import APP_API_HASH, APP_API_ID, PHONE_NUMBER


async def main(client: TelegramClient) -> None:
    await client.start()
    await client.run_until_disconnected()


if __name__ == "__main__":
    telegram_client = TelegramClient(PHONE_NUMBER.strip('+'),
                            APP_API_ID,
                            APP_API_HASH)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(telegram_client))
    loop.close()
