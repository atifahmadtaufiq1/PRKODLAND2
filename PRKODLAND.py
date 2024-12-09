import discord
from discord.ext import commands
import os, random
import requests
from get_model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def classify(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            nama_file = file.filename
            url_file = file.url
            await file.save(nama_file)
            await ctx.send(f'file telah disimpan dengan nama {nama_file}')
            await ctx.send(f'alamat cloud discord untuk file {url_file}')

            kelas, skor = get_class(image=nama_file, model='keras_model.h5', label='labels.txt')

            if kelas == 'bebek' and skor >= 0.65:
                await ctx.send(f'Anda mengirimkan gambar Bebek')
                await ctx.send(f'Persentase kemiripan yaitu {skor}')
                await ctx.send(f'Bebek adalah unggas yang dikenal dengan kaki berselaput untuk berenang, paruh datar untuk menyaring makanan dari air, dan kemampuan terbang meski tidak semua jenis bebek terbang jauh. Mereka memiliki penglihatan yang sangat baik, hampir 360 derajat, dan hidup secara sosial dalam kelompok. Bebek adalah omnivora, memakan tanaman, biji, serangga, dan krustasea kecil. Selain hidup di air, mereka juga dapat hidup di darat, seperti bebek domestik yang ditemukan di peternakan. Anak bebek belajar berenang dan mencari makanan segera setelah menetas, dengan induknya melindungi mereka. Ada banyak spesies bebek, masing-masing dengan ciri khasnya.')
            elif kelas == 'angsa' and skor >= 0.65:
                await ctx.send(f'Anda mengirimkan gambar Angsa')
                await ctx.send(f'Persentase kemiripan yaitu {skor}')
                await ctx.send(f'Angsa adalah burung besar yang sering ditemukan di danau dan sungai, dikenal dengan migrasi jarak jauh dan leher panjang yang memudahkan mereka mencari makan di perairan dangkal. Mereka hidup dalam kelompok atau kawanan, bersifat teritorial, dan berpasangan seumur hidup. Sebagai herbivora, angsa memakan rumput dan tanaman air. Mereka mahir berenang menggunakan kaki berselaput dan terbang dalam formasi V saat migrasi. Angsa juga sangat melindungi anak-anak mereka dan berperan penting dalam ekosistem dengan mengendalikan pertumbuhan tanaman air berlebih.')
            else:
                await ctx.send(f'HMM, Ini gambar apa ya?')

    
    else:
        await ctx.send(f'kamu tidak mengirim apa apa!!!')
