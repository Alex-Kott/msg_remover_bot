import asyncio
import logging
import sys
from asyncio import sleep
from datetime import datetime

from telethon import TelegramClient

from config import APP_API_HASH, APP_API_ID, PHONE_NUMBER

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='log')

logger = logging.getLogger('msg_remover')

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


async def delete_read_messages(client: TelegramClient):
    dialogs = await client.get_dialogs()

    for dialog in dialogs:
        messages = await client.get_messages(dialog)

        for message in messages:
            # print(message.__dict__, end='\n\n')
            print(message)

        # message_ids = [message.id for message in messages if not message.media_unread]
        # await client.delete_messages(dialog, message_ids)


async def main(client: TelegramClient) -> None:
    await client.start()
    logger.info('Telegram client started')

    while True:
        current_time = datetime.now()
        # if current_time.hour == 4 and current_time.minute == 0 and current_time.second == 0:
        if True:
            logger.info("It's message removing time!")
            try:
                await delete_read_messages(client)
            except Exception as e:
                logger.exception('Exception during message removing has occurred')
        await sleep(0.6)


if __name__ == "__main__":
    telegram_client = TelegramClient(PHONE_NUMBER.strip('+'),
                                     APP_API_ID,
                                     APP_API_HASH)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(telegram_client))
    loop.close()
