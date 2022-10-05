# animations
# Канал - @modwini
from .. import loader
from asyncio import sleep


@loader.tds
class Animations(loader.Module):
    strings = {"name": "Animations by @modwini"}

    @loader.owner
    async def clowncmd(self, message):
        for _ in range(10):
            for clown in ["🤡", "👆"]:
                await message.edit(clown)
                await sleep(0.6)

    async def ftcmd(self, message):
        for _ in range(10):
            for ft in ["💨🙂", "😐💥", "😶📷", "😶📸", "🤨🖼️", "🤡"]:
                await message.edit(ft)
                await sleep(0.6)

    async def columncmd(self, message):
        for _ in range(10):
            for column in ["🔈", "🔉", "🔊"]:
                await message.edit(column)
                await sleep(0.3)

    async def kopcmd(self, message):
        for _ in range(10):
            for kop in ["🤡                   🙂", "🤡🔪              😐", "💨🤡🔪           😶", "👮‍♂️                  🤡🔪", "👮‍♂️              🔫🤡", "👜🤡             🚓💨", "🤡⛓️     👮‍♂️👮‍♂️"]:
                await message.edit(kop)
                await sleep(1.3)