import discord
from discord.ext.commands import Bot

from config import BAD_WORDS_FILENAME, ENABLE_CHANNELS
from helpers.book_scraping_helper import BookAPI
from helpers.csv_helper import insert_word, validate_word
from helpers.embed import EmbedHelper


def init(bot: Bot):
    @bot.event
    async def on_ready():
        print('LOG: Bot Started ...')

    @bot.event
    async def on_member_join(member):
        print(member.guild.system_channel)
        if channel := member.guild.system_channel:
            fields = [{
                "name": ":loudspeaker: Fique atento!",
                "value":"Temos Diversas Salas, fique a vontade e faça novas amizades. Obrigado por entrar no nosso servidor",
                "inline": False
            }]
            ebd = EmbedHelper(
                f"{member.nick} | Bem-vindo(a)!.",
                discord.Color.green(),
                description=f"Olá! {member.mention}! Você acabou de entrar no servidor {member.guild}, aqui você poderá interagir e fazer diversas amizades!",
                thumb=member.avatar_url,
                fields=fields,
                image='https://media.discordapp.net/attachments/728741178186399839/840963544907907092/bem-vindo_ao_study_community_br.gif?width=1092&height=614'
            )
            ebd.generate_embed()
            await channel.send(embed=ebd.embed)

    @bot.event
    async def on_message(message):
        current_message, channel = message.content.lower(), message.channel
        splited_message = str(current_message).split(' ')

        """
        fiz esse bloco if: pra conseguir capturar o conteúdo completo da mensagem, visto que, caso coverta em um
         command ele pegara sempre a primeira palavra da frase, sendo que o intuito da funcionalidade é analizar
         a frase digitada pelo usuário, sendo ela unica ou composta, e incluir no repositorio de palavras proibidas.
        """
        if splited_message[0] == '--append_bad_word':
            insert_word(BAD_WORDS_FILENAME, 'bad_words', ' '.join(splited_message[1:]))

            await channel.send('Nova palavra adicionada a lista de bloqueio')
            await bot.process_commands(message)

            return

        if splited_message[0] == '--search_book':
            book_name = ' '.join(splited_message[1:])

            if result := BookAPI().fetch_book_api(book_name):
                for book in result.get("items")[:3]:
                    author = {}
                    try:
                        book.get('volumeInfo').get('imageLinks')
                        book.get('volumeInfo').get('imageLinks').get('thumbnail')

                    except (AttributeError, KeyError):
                        book['volumeInfo']['imageLinks'] = {}
                        book['volumeInfo']['imageLinks']['thumbnail'] = "https://books.google.com.br/googlebooks/images/no_cover_thumb.gif"
                        book['volumeInfo']['imageLinks']['smallThumbnail'] = "https://books.google.com.br/googlebooks/images/no_cover_thumb.gif"

                    author = {
                        'name': " ".join(book.get('volumeInfo').get('authors') or []),
                        'url': book.get('volumeInfo').get('imageLinks').get('smallThumbnail')
                    }

                    ebd = EmbedHelper(
                        title=book.get('volumeInfo').get('title'),
                        color=discord.Color.green(),
                        url=book.get('volumeInfo').get('infoLink'),
                        author=author,
                        description=book.get('volumeInfo').get('description'),
                        image=book.get('volumeInfo').get('imageLinks').get('thumbnail')
                    )
                    ebd.generate_embed()

                    await channel.send(embed=ebd.embed)

                await bot.process_commands(message)

                return

            await channel.send('Não localizamos resultado para a busca realizada.')
            return

        try:
            if message.author == bot.user:
                return

            await validate_messager(current_message, channel)

            valid, err_message = validate_word(BAD_WORDS_FILENAME, current_message)

            if valid:
                await message.delete()
                await channel.send(f"{message.author.mention}, {err_message}")

                return

        except:
            await channel.send('Tivemos um erro ao tentar processar sua solicitação, por favor, tente novamente!.')

        finally:
            await bot.process_commands(message)


async def validate_messager(current_message, channel):

    valid_message = [
        word for word in ENABLE_CHANNELS.get('all_words')
        if current_message.lower().startswith(word)
    ]

    if not valid_message:
        return

    if c_message := ENABLE_CHANNELS.get(valid_message[0]):
        if c_message.get('ids') == 'all' or str(channel.id) in c_message.get('ids'):
            await channel.send(c_message.get('message'))