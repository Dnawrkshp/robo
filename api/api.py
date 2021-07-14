import threading
import os
import logging
from aiohttp import web
import asyncio
from time import sleep
import json


class Api():
	def __init__(self, monolith, ip: str, port: int, sync_rate: int):
		self._logger = logging.getLogger(f"robo.api")
		formatter = logging.Formatter('%(asctime)s API | %(levelname)s | %(message)s')
		filehandler = logging.FileHandler(os.path.join('logs','api.log'), mode='w')
		filehandler.setLevel(logging.DEBUG)
		filehandler.setFormatter(formatter)
		self._logger.addHandler(filehandler)

		self._players = "[]"
		self._games = "[]"

		self._monolith = monolith
		self._ip = ip
		self._port = port
		self._sync_rate = sync_rate
		self._thread = threading.Thread(target = self.start)
		self._thread.setDaemon(True)
		self._thread.start()

	async def monolith_sync(self):
		while True:
			self._logger.info("Syncing to monolith ...")

			# Sync player list
			players = self._monolith.api_req_players()
			self._players = str(players)

			# Sync game list
			games = self._monolith.api_req_games()
			self._games = str(games)

			await asyncio.sleep(self._sync_rate)

	async def players(self, request):
		return web.Response(text=self._players)

	async def games(self, request):
		return web.Response(text=self._games)

	async def main(self):
		# add stuff to the loop, e.g. using asyncio.create_task()

		app = web.Application()
		app.router.add_get('/players', self.players)
		app.router.add_get('/games', self.games)

		runner = web.AppRunner(app)
		await runner.setup()
		site = web.TCPSite(runner, self._ip, self._port)    
		await site.start()

		self._logger.info(f"Serving on ('{self._ip}', {self._port}) ...")

		# Add monolith sync to event loop
		asyncio.create_task(self.monolith_sync())
	
   	 	# wait forever
		await asyncio.Event().wait()

	def start(self):
		asyncio.run(self.main())

if __name__ == '__main__':
	a = Api()
	while True:
		sleep(100)
