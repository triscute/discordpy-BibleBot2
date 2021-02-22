import discord
import time

token = open("token")
ascii_art = open("BibleBotAsciiArt", 'r').read()

msgcount = 0
current_lines = 0
total_lines = 0

class MyClient(discord.Client):
    async def on_ready(self):
        print(ascii_art)
        print("╰ Bible Bot 2: Electric Boogaloo")
        print("╰ Current User: {0}".format(self.user))
        print("╰ Guilds: " + str(len(client.guilds)))
        print("╰ Users: " + str(len(client.users)))
        print("╰ Messages: "+str(msgcount))
        print("╰ Hidden Channels: " + str(len(client.private_channels)))
        print("╰────────────────────────────────────────────────────────────────")
        print("╰ Line " + str(current_lines) + " out of " + str(total_lines))

    async def on_message(self, message):
        global msgcount
        global current_lines
        global total_lines

        msgcount = msgcount + 1
        print("\n"*40)
        print(ascii_art)
        print("╰ Bible Bot 2: Electric Boogaloo")
        print("╰ Current User: {0}".format(self.user))
        print("╰ Guilds: " + str(len(client.guilds)))
        print("╰ Users: " + str(len(client.users)))
        print("╰ Messages: " + str(msgcount))
        print("╰ Hidden Channels: " + str(len(client.private_channels)))
        print("╰────────────────────────────────────────────────────────────────")
        print("╰ Line " + str(current_lines) + " out of " + str(total_lines))

        if "'start" in message.content and "token" not in message.content:
            a = open(message.content.replace("'start ", '', 1), 'r')
            for lines_in_file in a:
                if lines_in_file != "\n":
                    total_lines = total_lines + 1
            msg = ""
            lines = 0
            a = open(message.content.replace("'start ", '', 1), 'r') # !?!? it wouldnt work unless I did this and it was simple aight
            for word in a:
                if word != "\n":
                    msg = msg + word
                    lines = lines + 1
                    current_lines = current_lines + 1
                    if lines == 25:
                        lines = 0
                        await message.channel.send(msg)
                        msg = ""
                        time.sleep(0.5)
            await message.channel.send(msg)
            total_lines = 0
            current_lines = 0


client = MyClient()
client.run(token.read())
