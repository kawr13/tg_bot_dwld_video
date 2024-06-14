import asyncio


class AsyncQueue:
    def __init__(self):
        self.queue = asyncio.Queue()
        self.workers = []

    async def add_task(self, coro):
        await self.queue.put(coro)

    async def worker(self):
        while True:
            try:
                task_coro = await self.queue.get()
                await task_coro
            except Exception as e:
                print(e)
            finally:
                self.queue.task_done()

    def start_worker(self, num_workers=1):
        for _ in range(num_workers):
            worker = asyncio.create_task(self.worker())
            self.workers.append(worker)

    async def stop_workers(self):
        for worker in self.workers:
            worker.cancel()
        await asyncio.gather(*self.workers, return_exceptions=True)


queue = AsyncQueue()