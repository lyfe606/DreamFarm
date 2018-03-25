import discord
import asyncio
import requests
import json
import os
import logging
from dreamfarm.bot.log import logger

class EmbedBuilder:
    api_host = os.environ.get('API_HOST')

    async def get_plot_image_url(self, user_id):
        params = {
            'user_id': user_id
        }
        response = requests.post(EmbedBuilder.api_host + '/plot-img-url', data=json.dumps(params))

        if (response.status_code == 200):
            return response.text
        else:
            logger.warn('ERROR: get_plot_image_url; user %s; %s %s', user_id, response.status_code, response.reason)
            return ''

    async def build(self, title, description, user_id, fields):
        embed = discord.Embed(title=title, description=description, color=0x4c9265)

        url = await self.get_plot_image_url(user_id)
        embed.set_image(url=url)

        for field in fields:
            embed.add_field(name=field.name, value=field.value, inline=False)

        return embed