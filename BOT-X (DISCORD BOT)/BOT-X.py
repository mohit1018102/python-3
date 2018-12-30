
import discord
import nltk
with open("token.txt") as file:
    token=file.read()

client=discord.Client()

@client.event
async def on_ready():
    print(f"we have logged in as {client.user}")

@client.event
async def on_message(message):  # event that happens per any message.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if str(message.author) !="BOT-X#2596" and "!table" in message.content.lower():
        await client.send_message(message.channel,content ='''POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent\'s
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when''')
        
        
    elif str(message.author) !="BOT-X#2596" and "!pos" in message.content.lower():
        words=nltk.word_tokenize( message.content.lower()[4:])
        tagged=nltk.pos_tag(words)
        a_msg=""
        for t,p in tagged:
            a_msg=a_msg+"word : "+t+"\tpos : "+p+"\n"
        print(a_msg)
        await client.send_message(message.channel,content ="WORD : PART OF SPEECH : \n"+a_msg)
        
client.run(token)



