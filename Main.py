


import os
import asyncio
from highrise import BaseBot
from highrise.__main__ import main

API_KEY = os.environ.get("API_KEY", "2ed771548efc3430de8d3ff59d2da7f7c0a31fbce840c6c5064b19e5ac9d943c")
ROOM_ID = "68e5f2de20e333f74f37b067"
OWNER_USERNAME = "UR0N_505"

EMOTES = {
    "wave": "emote-wave", "hello": "emote-hello",
    "thumbsup": "emote-thumbsup", "shy": "emote-shy",
    "happy": "emote-happy", "sad": "emote-sad",
    "angry": "emote-angry", "confused": "emote-confused",
    "dance": "dance-tiktok8", "dance2": "dance-blackpink",
    "dance3": "dance-anime", "dance4": "dance-gangnam",
    "sit": "idle-sit", "float": "idle-floating",
    "pose": "emote-pose1", "kiss": "emote-kiss",
    "clap": "emote-clap", "laugh": "emote-laugh",
    "cry": "emote-cry", "bow": "emote-bow",
    "flex": "emote-flex", "heart": "emote-heart",
}

class EmoteBot(BaseBot):
    def is_owner(self, user):
        return user.username == OWNER_USERNAME

    async def on_start(self, session_metadata):
        print("Bot conectado!")
        await self.highrise.chat("Bot activo! Usa !emote [nombre] o !lista")

    async def on_chat(self, user, message):
        msg = message.strip().lower()

        if msg == "!lista":
            await self.highrise.chat("Emotes: " + " | ".join(EMOTES.keys()))

        elif msg.startswith("!emote "):
            nombre = msg.replace("!emote ", "").strip()
            emote_id = EMOTES.get(nombre)
            if emote_id:
                await self.highrise.send_emote(emote_id)
                await self.highrise.chat(f"Haciendo: {nombre}!")
            else:
                await self.highrise.chat(f"Emote '{nombre}' no existe. Usa !lista")

        elif msg == "!help":
            await self.highrise.chat("Comandos: !emote [nombre] | !lista | !help")

        elif msg == "!stop" and self.is_owner(user):
            await self.highrise.chat("Apagando bot... Hasta luego!")
            raise SystemExit

        elif msg.startswith("!decir ") and self.is_owner(user):
            texto = message[7:]
            await self.highrise.chat(texto)

        elif msg == "!stop" and not self.is_owner(user):
            await self.highrise.chat("No tenés permiso para eso.")

    async def on_user_join(self, user, position):
        await self.highrise.chat(f"Bienvenido/a {user.username}!")

if __name__ == "__main__":
    asyncio.run(main(EmoteBot(), ROOM_ID, API_KEY))
