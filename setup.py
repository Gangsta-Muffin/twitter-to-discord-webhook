from setuptools import *

setup(
    name='Webhook',
    description='Twiter to discord webhook for Battlefield community',
    version='1.0',
    author='Gangsta Muffin',
    python_require='>=3.0',
    packages=find_packages(),
    install_package_data=True,
    install_requires=[
        'tweepy',
        'discord',
        'discord.embeds',
        'datetime',
        'requests',
        'typing',
    ]
)
