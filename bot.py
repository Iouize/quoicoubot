import discord
import random
import string
from secret_token import TOKEN

DISCORD_TOKEN = TOKEN
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
nombres = ["un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf", "vingt"]
emojis = ["!!!", "x)", "xD", "^^", "O.o", "uwu", ":P", ";D", "°_°", ":3", "X.X", "hehe", ":O"]

quoi_answer = ['coubeh', 'feur']
toi_answer = ['lette', 'ture']
moi_answer = ['ssonneuse batteuse', 'gnon']

@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')

@client.event
async def on_message(message):
    msg = message.content.lower().translate(str.maketrans('', '', string.punctuation))
    response = ""

    if message.author == client.user:
        return

    if msg.endswith('quoi'):
        response += random.choice(quoi_answer)

    if msg.endswith('de'):
        response += 'trois'

    if msg.endswith('hein'):
        response += 'deux'

    if msg.endswith('qui'):
        response += 'quette'

    if msg.endswith('toi'):
        response += random.choice(toi_answer)

    if msg.endswith('moi'):
        response += random.choice(moi_answer)

    if msg.endswith('mais'):
        response += 'juin'

    if msg.endswith('thé'):
        response += 'té'

    if msg.endswith('cul'):
        response += 'curbitacée'

    if msg.endswith('puceau'):
        response += 'puceau moi ? serieusement ^^ haha on me l avait pas sortie celle la depuis loooongtemps :) demande a mes potes si je suis puceau tu vas voir les reponses que tu vas te prendre XD rien que la semaine passee j ai niquer donc chuuuuut ferme la puceau de merde car oui toi tu m as tout l air d un bon puceau de merde car souvent vous etes frustrer de ne pas BAISER :) ses agreable de se faire un missionnaire ou un amazone avec une meuf hein? tu peux pas repondre car tu ne sais pas ce que c ou alors tu le sais mais tu as du taper dans ta barre de recherche "missionnaire sexe" ou "amazone sexe" pour comprendre ce que c etait mdddrrr !! c est grave quoiquil en soit.... pour revenir a moi, je pense que je suis le mec le moins puceau de ma bande de 11 meilleurs amis pas psk j ai eu le plus de rapport intime mais psk j ai eu les plus jolie femme que mes amis :D ses pas moi qui le dit, ses eux qui commente sous mes photos insta "trop belle la fille que tu as coucher avec hier en boite notamment!" donc apres si tu veux que sa parte plus loi sa peut partir vraiment loi j habite dans la banlieue de niort sa te parle steven sanchez ? ses juste un cousin donc OKLM hahaha on verra si tu parles encore le puceau de merde mdddrrr pk insulter qd on est soi meme puceau tu me feras toujour marrer!!'

    quoi_nb = list(filter(msg.endswith, nombres))

    if quoi_nb != []:
        response += nombres[nombres.index(quoi_nb[0])+1]

    if response != "":
        await message.channel.send(f'{response} {random.choice(emojis)}')


client.run(DISCORD_TOKEN)
