import os
import asyncio
from concurrent import futures
from typing import AsyncIterable
import grpc
from grpc import Server
from aos.runtime.worker import worker_api_pb2, worker_api_pb2_grpc
from .worker_core_loop import WorkerCoreLoop

import logging
logger = logging.getLogger(__name__)

class WorkerApi(worker_api_pb2_grpc.WorkerApiServicer):
    def __init__(self, core_loop:WorkerCoreLoop):
        self.core_loop = core_loop

    async def InjectMessage(self, request: worker_api_pb2.InjectMessageRequest, context) -> worker_api_pb2.InjectMessageResponse:
        result = await self.core_loop.inject_message(request)
        if result is None:
            raise Exception("Failed to inject message")
        return result
    
    async def RunQuery(self, request: worker_api_pb2.RunQueryRequest, context) -> worker_api_pb2.RunQueryResponse:
        result = await self.core_loop.run_query(request)
        if result is None:
            raise Exception("Failed to run query.")
        return result
    
async def start_server(
        port:str="50053", 
        apex_address:str="localhost:50052",
        worker_id:str|None=None,
        ) -> Server:
    
    #start core loop
    core_loop = WorkerCoreLoop(apex_address, worker_id)
    core_loop_task = asyncio.create_task(core_loop.start())
    await core_loop.wait_until_running()

    #start server
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=5)) #not many workers needed, as the server is entirely async
    worker_api_pb2_grpc.add_WorkerApiServicer_to_server(WorkerApi(core_loop), server)
    server.add_insecure_port("[::]:" + port)
    await server.start()
    server_task = asyncio.create_task(server.wait_for_termination())
    logger.info("Worker Server started, listening on " + port)
    await asyncio.wait([core_loop_task, server_task], return_when=asyncio.FIRST_COMPLETED)
    core_loop.stop()
    await asyncio.wait_for(core_loop_task, 0.5)
    await server.stop(0.5)
    await server_task
    logger.info("Worker Server stopped.")


# how to do graceful shutdown 

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    async def arun():
        await start_server()
    asyncio.run(arun())