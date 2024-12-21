import discord
import random
import time
import os  
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("メインシステム、戦闘モード起動！")
    await client.change_presence(activity=discord.Game(name="傭兵支援システムALL MIND"))

@client.event
async def on_member_join(member):
    guild = client.get_guild(1111111111111)   #サーバID
    channel = guild.get_channel(111111111111111) #チャンネルID
    time.sleep(2)
    await channel.send(f"登録番号Rb23\n識別名{member.name}による認証を確認\n")
    time.sleep(2)
    await channel.send("安否不明状態を解除\n")
    time.sleep(2)
    await channel.send("ユーザー権限を復旧します\n")
    time.sleep(3)
    await channel.send("傭兵支援システム「オールマインド」へようこそ\n")
    time.sleep(2)
    await channel.send(f"{member.name}貴方の帰還を歓迎します")


@client.event
async def on_message(message: discord.Message):
    
    if message.author.bot:
        return
    # メッセージの送信者がbotだった場合は無視する

    if message.content.startswith('/AM'):
        await message.channel.send('オールマインドは、全ての傭兵の為にあります')
   
    if message.content.startswith("!music"):
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            return
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("hoge.m4a"), volume=0.05)
        message.guild.voice_client.play(source)
        await message.channel.send("再生します。")

    if message.content.startswith("!stop"):
        discord.VoiceClient.pause


    if message.content.startswith('ケイトちゃんかわいいね'):
        file_names = ["am2.png","am3.png","am4.png","am5.png","am6.png","am7.png"]
        file_name = random.choice(file_names)
        # スクリプトからの相対パスで画像ディレクトリを指定
        img_path = os.path.join(os.path.dirname(__file__), '..', 'img', file_name)
        file_obj = discord.File(img_path)
        m="よくわかってますね" + message.author.name + "さん。オールマインド特性ステッカーあげちゃいます!!!"
        await message.channel.send(m,file=file_obj)
    # ランダムな画像データを返信する    
    
    
    if message.content == "!start":
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            return
        
        await message.author.voice.channel.connect()  #ボイスチャンネルに接続する
        audio_path = os.path.join(os.path.dirname(__file__), '..', 'audio', 'start.mp3')
        start = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(audio_path), volume=0.5)
        await message.channel.send("メインシステム、戦闘モード起動！"),message.guild.voice_client.play(start)
        

    elif message.content == "!leave":
        if message.guild.voice_client is None:
            await message.channel.send("接続していません。")
            return

        audio_path = os.path.join(os.path.dirname(__file__), '..', 'audio', 'am.mp3')
        leave = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(audio_path), volume=0.25)
        # 切断する
        message.guild.voice_client.play(leave)
        time.sleep(7)
        await message.guild.voice_client.disconnect()
        await message.channel.send("任務完了。お疲れさまでした。")

       

@client.event
async def on_message_delete(message):
    channel = client.get_channel(111111111111111)#チャンネルID
    await channel.send(f"{message.author.name}さんのメッセージが削除されました\n私じゃなきゃ見逃しちゃいますね(*＾∀ﾟ)ъ```\n{message.content}\n```")
#誰がメッセージを削除したとき、任員のチャンネルにそのメッセージを公開する


client.run("----------------Please input your bot token----------------") #使用するBotのトークンを入力