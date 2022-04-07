"""A Markov chain generator that can tweet random messages."""

import sys, os, discord, pyjokes
from random import choice

client = discord.Client()

@client.event
async def on_ready():
    print(f'Successfully connected! Logged in as {client.user}.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    def open_and_read_file(file_path):
        """Take file path as string; return text as string.
        Takes a string that is a file path, opens the file, and turns
        the file's contents as one string of text.
        """

        input_string = open(file_path).read()
        
        return input_string


    def make_chains(text_string):
        """Take input text as string; return dictionary of Markov chains.
        A chain will be a key that consists of a tuple of (word1, word2)
        and the value would be a list of the word(s) that follow those two
        words in the input text.
        For example:
            >>> chains = make_chains('hi there mary hi there juanita')
        Each bigram (except the last) will be a key in chains:
            >>> sorted(chains.keys())
            [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]
        Each item in chains is a list of all possible following words:
            >>> chains[('hi', 'there')]
            ['mary', 'juanita']
            >>> chains[('there','juanita')]
            [None]
        """

        chains = {}
        words = text_string.split()

        for i in range(len(words)-2):
            key = (words[i], words[i+1])

            if i < len(words) - 2:
                value = words[i+2]

            if key not in chains:
                chains[key] = [value]
            else:
                chains[key].append(value)

        return chains


    def make_text(chains):
        """Return text from chains."""
        
        words = []
        key = choice(list(chains.keys()))

        while True:
            value = choice(chains[key])
            words.append(value)
            key = (key[1], choice(chains[key]))

            if key not in chains:
                break

        return ' '.join(words)


    input_path = 'green-eggs.txt'

    # Open the file and turn it into one long string
    input_text = open_and_read_file(input_path)

    # Get a Markov chain
    chains = make_chains(input_text)

    # Produce random text
    random_text = make_text(chains)

    print ('received message: ', message)
    joke_triggers = ["joke", "funny", "lol", "haha"]
    greeting_triggers = ["hello", "hello!", "hi", "greetings", "hey"]
    marco = ["marco"]

    if any(element in message.content for element in greeting_triggers):
        await message.channel.send(f"Hi {message.author.name}!  You're awesome!")
    elif message.content.startswith("marco"):
        await message.channel.send(f"Polo!")
    elif message.content.startswith('markov'):
        await message.channel.send(random_text)
    elif any(trigger in message.content for trigger in joke_triggers):
        joke = pyjokes.get_joke(language="en",category="neutral")        
        await message.channel.send(f"Hey {message.author.name}! Have you heard the one about: {joke}")
    else:
        print ("failed")

client.run(os.environ['DISCORD_TOKEN'])