from discord.ext import commands
import os
import traceback
import discord
import random  # おみくじで使用

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()


@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return

    if message.content == "SOS":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear {message.author.mention}　\n What's wrong? HELP sent. Please check DM✉.\n どうしましたか？HELP送信しました。DM✉を確認して下さい。")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "sos":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear {message.author.mention}　\n What's wrong? HELP sent. Please check DM✉.\n どうしましたか？HELP送信しました。DM✉を確認して下さい。")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "help":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear {message.author.mention}　\n HELP sent. Please check DM✉.\n HELP送信しました。DM✉を確認して下さい。")  # f文字列（フォーマット済み文字列リテラル）  
        
    if message.content == "HELP":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear {message.author.mention}　\n HELP sent. Please check DM✉.\n HELP送信しました。DM✉を確認して下さい。")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "DM":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear {message.author.mention}　\n HELP sent. Please check DM✉.\n HELP送信しました。DM✉を確認して下さい。")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "dm":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear {message.author.mention}　\n HELP sent. Please check DM✉.\n HELP送信しました。DM✉を確認して下さい。")  # f文字列（フォーマット済み文字列リテラル）

    elif message.content == "b/jpxzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send("/info jpx ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記  
   
    elif message.content == "b/link":
        # リアクションアイコンを付けたい
        q = await message.channel.send("/link ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "b/language":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /language EN ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記
              
    elif message.content == "b/accept":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /accept ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記

    elif message.content == "b/benzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info ben ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
        
    elif message.content == "b/jpynzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info jpyn ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記      
        
    elif message.content == "b/bgptzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info bgpt ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
    
    elif message.content == "b/kenjzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info kenj ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
             
    elif message.content == "b/sprtszan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info sprts ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 
        
    elif message.content == "b/29zan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info 29coin ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記  
     
    
    elif message.content == "x/rain":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain BGPT 60 ActiveUserOnly  <:BGPT02:698471366004965406><:good01:699581068285706301>🌈☔It Rains")
        [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '🌈')]  # for文の内包表記
         
            
    elif message.content == "x/Rain":
        # リアクションアイコンを付けたい
        q = await message.channel.send("  /rain BEN 30 ActiveUserOnly  <:benkeicoinsl:698471387064696833>🌈☔It Rains<:jhlo:700932650944299098>")
        [await q.add_reaction(i) for i in ('<:BENKEICOIN04:698471407650209832>', '<:benkeicoinsl:698471387064696833>')]  # for文の内包表記

        
    elif message.content == "x/RAIN":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain JPNY 50 ActiveUserOnly  <:JPYNdisco:698471276498649168>🌈☔It Rains<:jhlo:700932650944299098>")
        [await q.add_reaction(i) for i in ('<:JPYNdisco:698471276498649168>', '🌈')]  # for文の内包表記
        
   
    elif message.content == "x/RAin":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain KENJ 100 ActiveUserOnly  <:kenj:700136543003607101> 🌈☔It Rains<:jhlo:700932650944299098>")
        [await q.add_reaction(i) for i in ('<:kenj:700136543003607101>', '<:sangras01:699579409220370514>')]  # for文の内包表記
      
    
    elif message.content == "x/RAIn":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain SPRTS 1000 ActiveUserOnly  <:sprts:699076413931782146> 🌈☔It Rains🌱")
        [await q.add_reaction(i) for i in ('<:sprts:699076413931782146>', '🌱')]  # for文の内包表記
        
        
   
    elif message.content == "x/throw":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BGPT 200 4 EquallyDistributed  <:good01:699581068285706301><:BGPT02:698471366004965406>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:good:699580636448423936>')]  # for文の内包表記

        
    elif message.content == "x/THROW":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BEN 80 4 EquallyDistributed  <:benkeicoinsl:698471387064696833>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:BENKEICOIN04:698471407650209832>', '<:good:699580636448423936>')]  # for文の内包表記

        
    elif message.content == "x/THrow":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw JPYN 100 4 EquallyDistributed  <:good01:699581068285706301><:JPYNdisco:698471276498649168>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:JPYNdisco:698471276498649168>', '<:good01:699581068285706301>')]  # for文の内包表記

        
    elif message.content == "x/THRow":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw KENJ 400 4 EquallyDistributed  <:kenj:700136543003607101>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:kenj:700136543003607101>', '<:good01:699581068285706301>')]  # for文の内包表記


    elif message.content == "x/THROw":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BGPT 300 5 EquallyDistributed  <:good01:699581068285706301><:BGPT02:698471366004965406><:BGPT02:698471366004965406>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:good:699580636448423936>')]  # for文の内包表記


    elif message.content == "x/thunder":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /thunder BGPT 300 ActiveUserOnly  <:good:699580636448423936><:BGPT02:698471366004965406>thunder")
        [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:BGPT02:698471366004965406>')]  # for文の内包表記

        
    elif message.content == "x/tHROW":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BGPT 500 4 AttenuationDistributed  <:BGPT02:698471366004965406><:good:699580636448423936>")
        [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:jhlo:700932650944299098>')]  # for文の内包表記
    
    
    elif message.content == "x/thROW":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BEN 100 4 AttenuationDistributed  <:benkeicoinsl:698471387064696833>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:BENKEICOIN04:698471407650209832>', '<:good:699580636448423936>')]  # for文の内包表記
 
    
    elif message.content == "x/thrOW":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw JPYN 100 4 AttenuationDistributed  <:JPYNdisco:698471276498649168>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:JPYNdisco:698471276498649168>', '<:good01:699581068285706301>')]  # for文の内包表記

        
    elif message.content == "x/THRow":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw KENJ 1000 4 AttenuationDistributed  <:kenj:700136543003607101>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:kenj:700136543003607101>', '<:good01:699581068285706301>')]  # for文の内包表記

        
    elif message.content == "しね":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 9314 "f"{message.author.mention}　💀🚫Prohibited terms💩💩")
        [await q.add_reaction(i) for i in ('💩', '🚫')]  # for文の内包表記


    elif message.content == "死ね":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 9314 "f"{message.author.mention}　💩🚫Prohibited terms💩💩")
        [await q.add_reaction(i) for i in ('💩', '🚫')]  # for文の内包表記


    elif message.content == "SEX":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 9314 "f"{message.author.mention}💩🚫Prohibited terms💩💩")
        [await q.add_reaction(i) for i in ('💩', '🚫')]  # for文の内包表記
      
    
    elif message.content == "sex":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 9314 "f"{message.author.mention}💩🚫Prohibited terms💩💩")
        [await q.add_reaction(i) for i in ('💩', '🚫')]  # for文の内包表記

        
        

    elif message.content == "kuji":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[今日の運勢YourFortune] ",
                        value=random.choice(('☆☆彡超最高☆彡☆【何してもVeryGood!☆勝負に強い日です】','☆最高☆【チームに恵まれた日です。チャレンジしたら幸運を招きます☆彡】','やったね☆彡！【納得出来る日でしょう。金運は余り期待出来ないです。】','利益が出る☆彡！【法廷通貨の金運は余り期待出来ないですが！暗号通貨（仮想通貨）において、思わぬ利益が見込めるね☆】'
                                             ,'大吉【☆☆☆自信もって取り組めば必ず好成果となって返ってきます。♡♡♡恋愛運は超ベリグっ】', '中吉【☆☆好チャンス！攻めて成果あり。♡♡とりあえず問題なしかな！？】', '小吉【☆☆通常のセオリーを変化させたら好成果となる。♡♡現状から変化ない】'
                                             ,  '末吉【☆☆参加型オンラインゲームで好成果あり♡ゲームばかりじゃダメ。出会いを求めて外にでたら吉あり】', '吉【☆現状変化なし♡特に変化なし。そのままやっとけ！】', 'ちょい吉【☆と。り。あ。え。ず。って感じ。意味はとりあえずチャレンジしたら吉！】', '吉【☆まぁ！適当に！こんなもんよ】'
                                             , 'ごく普通やね【何それ！？と思うだろうがごく普通だ！棚から牡丹餅はない】', '凶【▲儲けようと企んだ事が、やっぱり裏目に出る日だね～。深く考えずに前向きに進もう！これしかないね】'
                                             , '凶【▲残念！好機はないね。負けも勝ちの内かと思え！ファイト】', '大凶【▲▲吐き気するわ！駄目だこりゃ】', '大大凶【▲▲▲寝るしかない！行動すれば余計に悪化。まず寝る事！】')), inline=False)
        await message.channel.send(embed=embed)



    elif message.content == "sos":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"Dear {message.author.mention}\n\n🔸 Please feel free to ask questions to the officials around you if there is an emergency. \n Please check the SNS mentioned in .\n\n🔸緊急なら周りの役職者に気軽に質問して下さい。\n記載のSNSにて連絡付きますので確認して下さい。\n   👍 \n ✉ Thank you DM. \n\n ✅ Please check each JPX information here for your requirements. You can contact them through SNS. \n 🔶Discord (JPX Main Communication) https://discord.gg/y7erbdw \n 🔷Discord (JPX information) https://discord.gg/czK9Z2s \n 🔷JPX Web! https://jpxcoin.theblog.me/ \n 🔷JPX Reddit https://www.reddit.com/user/jpxcoin  \n 🔷JPX Twitter https://twitter.com/jpxcoin \n 🔷 JPYN (JPX) Twitter https://twitter.com/JPYNCOIN \n 🔷 JPX Telegram http://t.me/jpxcoins \n 🔷 JPYN (JPX) Telegram https://t.me/JPYNCOIN \n Exciting Now ⚡ \n Copyright © 2020 Japan Excitement Coin (JPX) & JPYN \n\n ✉ DMありがとうございます。\n ✅ ご用件はこちらのそれぞれのJPX informationで確認して下さい。その中でSNSにて連絡を取る事が出来ます。\n🔶Discord(JPX Maord(JPX ord(JPX ord(JPX in Communication）https://discord.gg/y7erbdw　\n 🔷Discord(JPX information) https://discord.gg/czK9Z2s \n 🔷JPX Web! https://jpxcoin.theblog.me/ \n 🔷JPX Reddit https://www.reddit.com/user/jpxcoin \n 🔷JPX Twitter https://twitter.com/jpxcoin \n 🔷 JPYN(JPX)Twitter https://twitter.com/JPYNCOIN \n 🔷 JPX Telegram http://t.me/jpxcoins \n 🔷JPYN(JPX)Telegram https://t.me/JPYNCOIN \n  Exciting Now⚡　\n Copyright © 2020 Japan Excitement Coin (JPX) & JPYN ")




    elif message.content == "SOS":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"Dear {message.author.mention}\n\n🔸 Please feel free to ask questions to the officials around you if there is an emergency. \n Please check the SNS mentioned in .\n\n🔸緊急なら周りの役職者に気軽に質問して下さい。\n記載のSNSにて連絡付きますので確認して下さい。\n\n   👍 \n ✉ Thank you DM. \n\n ✅ Please check each JPX information here for your requirements. You can contact them through SNS. \n 🔶Discord (JPX Main Communication) https://discord.gg/y7erbdw \n 🔷Discord (JPX information) https://discord.gg/czK9Z2s \n 🔷JPX Web! https://jpxcoin.theblog.me/ \n 🔷JPX Reddit https://www.reddit.com/user/jpxcoin  \n 🔷JPX Twitter https://twitter.com/jpxcoin \n 🔷 JPYN (JPX) Twitter https://twitter.com/JPYNCOIN \n 🔷 JPX Telegram http://t.me/jpxcoins \n 🔷 JPYN (JPX) Telegram https://t.me/JPYNCOIN \n Exciting Now ⚡ \n Copyright © 2020 Japan Excitement Coin (JPX) & JPYN \n\n ✉ DMありがとうございます。\n ✅ ご用件はこちらのそれぞれのJPX informationで確認して下さい。その中でSNSにて連絡を取る事が出来ます。\n🔶Discord(JPX Maord(JPX ord(JPX ord(JPX in Communication）https://discord.gg/y7erbdw　\n 🔷Discord(JPX information) https://discord.gg/czK9Z2s \n 🔷JPX Web! https://jpxcoin.theblog.me/ \n 🔷JPX Reddit https://www.reddit.com/user/jpxcoin \n 🔷JPX Twitter https://twitter.com/jpxcoin \n 🔷 JPYN(JPX)Twitter https://twitter.com/JPYNCOIN \n 🔷 JPX Telegram http://t.me/jpxcoins \n 🔷JPYN(JPX)Telegram https://t.me/JPYNCOIN \n  Exciting Now⚡　\n Copyright © 2020 Japan Excitement Coin (JPX) & JPYN ")




    elif message.content == "help":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"Dear {message.author.mention} 👍 \n ✉ Thank you DM. \n\n ✅ Please check each JPX information here for your requirements. You can contact them through SNS. \n 🔶Discord (JPX Main Communication) https://discord.gg/y7erbdw \n 🔷Discord (JPX information) https://discord.gg/czK9Z2s \n 🔷JPX Web! https://jpxcoin.theblog.me/ \n 🔷JPX Reddit https://www.reddit.com/user/jpxcoin  \n 🔷JPX Twitter https://twitter.com/jpxcoin \n 🔷 JPYN (JPX) Twitter https://twitter.com/JPYNCOIN \n 🔷 JPX Telegram http://t.me/jpxcoins \n 🔷 JPYN (JPX) Telegram https://t.me/JPYNCOIN \n Exciting Now ⚡ \n Copyright © 2020 Japan Excitement Coin (JPX) & JPYN \n\n ✉ DMありがとうございます。\n ✅ ご用件はこちらのそれぞれのJPX informationで確認して下さい。その中でSNSにて連絡を取る事が出来ます。\n🔶Discord(JPX Maord(JPX ord(JPX ord(JPX in Communication）https://discord.gg/y7erbdw　\n 🔷Discord(JPX information) https://discord.gg/czK9Z2s \n 🔷JPX Web! https://jpxcoin.theblog.me/ \n 🔷JPX Reddit https://www.reddit.com/user/jpxcoin \n 🔷JPX Twitter https://twitter.com/jpxcoin \n 🔷 JPYN(JPX)Twitter https://twitter.com/JPYNCOIN \n 🔷 JPX Telegram http://t.me/jpxcoins \n 🔷JPYN(JPX)Telegram https://t.me/JPYNCOIN \n  Exciting Now⚡　\n Copyright © 2020 Japan Excitement Coin (JPX) & JPYN ")




    elif message.content == "dm":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"Dear {message.author.mention} 👍 \n ✉ Thank you DM. \n\n ✅ Please check each JPX information here for your requirements. You can contact them through SNS. \n 🔶Discord (JPX Main Communication) https://discord.gg/y7erbdw \n 🔷Discord (JPX information) https://discord.gg/czK9Z2s \n 🔷JPX Web! https://jpxcoin.theblog.me/ \n 🔷JPX Reddit https://www.reddit.com/user/jpxcoin  \n 🔷JPX Twitter https://twitter.com/jpxcoin \n 🔷 JPYN (JPX) Twitter https://twitter.com/JPYNCOIN \n 🔷 JPX Telegram http://t.me/jpxcoins \n 🔷 JPYN (JPX) Telegram https://t.me/JPYNCOIN \n Exciting Now ⚡ \n Copyright © 2020 Japan Excitement Coin (JPX) & JPYN \n\n ✉ DMありがとうございます。\n ✅ ご用件はこちらのそれぞれのJPX informationで確認して下さい。その中でSNSにて連絡を取る事が出来ます。\n🔶Discord(JPX Maord(JPX ord(JPX ord(JPX in Communication）https://discord.gg/y7erbdw　\n 🔷Discord(JPX information) https://discord.gg/czK9Z2s \n 🔷JPX Web! https://jpxcoin.theblog.me/ \n 🔷JPX Reddit https://www.reddit.com/user/jpxcoin \n 🔷JPX Twitter https://twitter.com/jpxcoin \n 🔷 JPYN(JPX)Twitter https://twitter.com/JPYNCOIN \n 🔷 JPX Telegram http://t.me/jpxcoins \n 🔷JPYN(JPX)Telegram https://t.me/JPYNCOIN \n  Exciting Now⚡　\n Copyright © 2020 Japan Excitement Coin (JPX) & JPYN ")




    elif message.content == "HELP":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"Dear {message.author.mention} 👍 \n ✉ Thank you DM. \n\n ✅ Please check each JPX information here for your requirements. You can contact them through SNS. \n 🔶Discord (JPX Main Communication) https://discord.gg/y7erbdw \n 🔷Discord (JPX information) https://discord.gg/czK9Z2s \n 🔷JPX Web! https://jpxcoin.theblog.me/ \n 🔷JPX Reddit https://www.reddit.com/user/jpxcoin  \n 🔷JPX Twitter https://twitter.com/jpxcoin \n 🔷 JPYN (JPX) Twitter https://twitter.com/JPYNCOIN \n 🔷 JPX Telegram http://t.me/jpxcoins \n 🔷 JPYN (JPX) Telegram https://t.me/JPYNCOIN \n Exciting Now ⚡ \n Copyright © 2020 Japan Excitement Coin (JPX) & JPYN \n\n ✉ DMありがとうございます。\n ✅ ご用件はこちらのそれぞれのJPX informationで確認して下さい。その中でSNSにて連絡を取る事が出来ます。\n🔶Discord(JPX Maord(JPX ord(JPX ord(JPX in Communication）https://discord.gg/y7erbdw　\n 🔷Discord(JPX information) https://discord.gg/czK9Z2s \n 🔷JPX Web! https://jpxcoin.theblog.me/ \n 🔷JPX Reddit https://www.reddit.com/user/jpxcoin \n 🔷JPX Twitter https://twitter.com/jpxcoin \n 🔷 JPYN(JPX)Twitter https://twitter.com/JPYNCOIN \n 🔷 JPX Telegram http://t.me/jpxcoins \n 🔷JPYN(JPX)Telegram https://t.me/JPYNCOIN \n  Exciting Now⚡　\n Copyright © 2020 Japan Excitement Coin (JPX) & JPYN ")




    elif message.content == "DM":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"Dear {message.author.mention} 👍 \n ✉ Thank you DM. \n\n ✅ Please check each JPX information here for your requirements. You can contact them through SNS. \n 🔶Discord (JPX Main Communication) https://discord.gg/y7erbdw \n 🔷Discord (JPX information) https://discord.gg/czK9Z2s \n 🔷JPX Web! https://jpxcoin.theblog.me/ \n 🔷JPX Reddit https://www.reddit.com/user/jpxcoin  \n 🔷JPX Twitter https://twitter.com/jpxcoin \n 🔷 JPYN (JPX) Twitter https://twitter.com/JPYNCOIN \n 🔷 JPX Telegram http://t.me/jpxcoins \n 🔷 JPYN (JPX) Telegram https://t.me/JPYNCOIN \n Exciting Now ⚡ \n Copyright © 2020 Japan Excitement Coin (JPX) & JPYN \n\n ✉ DMありがとうございます。\n ✅ ご用件はこちらのそれぞれのJPX informationで確認して下さい。その中でSNSにて連絡を取る事が出来ます。\n🔶Discord(JPX Maord(JPX ord(JPX ord(JPX in Communication）https://discord.gg/y7erbdw　\n 🔷Discord(JPX information) https://discord.gg/czK9Z2s \n 🔷JPX Web! https://jpxcoin.theblog.me/ \n 🔷JPX Reddit https://www.reddit.com/user/jpxcoin \n 🔷JPX Twitter https://twitter.com/jpxcoin \n 🔷 JPYN(JPX)Twitter https://twitter.com/JPYNCOIN \n 🔷 JPX Telegram http://t.me/jpxcoins \n 🔷JPYN(JPX)Telegram https://t.me/JPYNCOIN \n  Exciting Now⚡　\n Copyright © 2020 Japan Excitement Coin (JPX) & JPYN ")


client.run(token)

