import discord

class KDbot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):

        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('```pong```')
            print("(Console) ping")

        if message.content == 'help':
            await message.channel.send('```Команды бота: gen1-100, gen1-10, genx (генерирует число), больше нету надеюсь карпен через 100 тысячилетий меня научит```')
            print("(Console) help")

        if message.content == 'gen1-100':
            import random
            rand_num = random.randint(1, 100)
            await message.channel.send(rand_num)

            print("(Console) gen1-100")


        if message.content == 'gen1-10':
            import random
            rand_num2 = random.randint(1, 10)
            await message.channel.send(rand_num2)

            print("(Console) gen1-10")


        if message.content == 'genxx':
            one = input("(Console) Plese write one radient >>> ")
            tu = input("(Console) Plase write two radient >>> ")
            import random
            rand_numx = random.randint(one, tu)
            await message.channel.send(rand_numx)

            print("(Console) Genx")

intents = discord.Intents.default()
intents.message_content = True
client = KDbot(intents=intents)
client.run('Plase write your token')