import os
import asyncio
from concurrent import futures
import logging
import grpc
from grpc import Server
from aos.runtime.store import grit_store_pb2, grit_store_pb2_grpc
from aos.runtime.store import agent_store_pb2, agent_store_pb2_grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from .lmdb_backend import LmdbBackend

class GritStore(grit_store_pb2_grpc.GritStoreServicer):
    def __init__(self, backend:LmdbBackend) -> None:
        super().__init__()
        self._backend = backend

    def Store(self, request: grit_store_pb2.StoreRequest, context):
        self._backend.store(request)
        return google_dot_protobuf_dot_empty__pb2.Empty()

    def Load(self, request: grit_store_pb2.LoadRequest, context):
        return self._backend.load(request)
    
    def SetRef(self, request: grit_store_pb2.SetRefRequest, context):
        self._backend.set_ref(request)
        return google_dot_protobuf_dot_empty__pb2.Empty()

    def GetRef(self, request: grit_store_pb2.GetRefRequest, context):
        return self._backend.get_ref(request)
    
    def GetRefs(self, request: grit_store_pb2.GetRefsRequest, context):
        return self._backend.get_refs(request)
    

class AgentStore(agent_store_pb2_grpc.AgentStoreServicer):
    def __init__(self, backend:LmdbBackend) -> None:
        super().__init__()
        self._backend = backend

    def GetAgent(self, request, context):
        return self._backend.get_agent(request)
    
    def GetAgents(self, request, context):
        return self._backend.get_agents()
    
    def CreateAgent(self, request, context):
        return self._backend.create_agent(request)
    
    def DeleteAgent(self, request, context):
        return self._backend.delete_agent(request)
    
    
    def SetVar(self, request: agent_store_pb2.SetVarRequest, context):
        self._backend.set_var(request)
        return google_dot_protobuf_dot_empty__pb2.Empty()

    def GetVar(self, request: agent_store_pb2.GetVarRequest, context):
        return self._backend.get_var(request)
    
    def GetVars(self, request: agent_store_pb2.GetVarsRequest, context):
        return self._backend.get_vars(request)
    
    def DeleteVar(self, request: agent_store_pb2.DeleteVarRequest, context):
        self._backend.delete_var(request)
        return google_dot_protobuf_dot_empty__pb2.Empty()
    

async def start_server(grit_dir:str, port:str="50051") -> Server:
    lmdb_backend = LmdbBackend(grit_dir, writemap=True)
    #kind of a hack to switch from asyc to sync lmdb handling (which is mostly sync)
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    grit_store_pb2_grpc.add_GritStoreServicer_to_server(GritStore(lmdb_backend), server)
    agent_store_pb2_grpc.add_AgentStoreServicer_to_server(AgentStore(lmdb_backend), server)
    server.add_insecure_port("[::]:" + port)
    await server.start()
    print("Server started, listening on " + port)
    return server

def start_server_sync(grit_dir:str, port:str="50051") -> Server:
    lmdb_backend = LmdbBackend(grit_dir, writemap=True)
    #kind of a hack to switch from asyc to sync lmdb handling (which is mostly sync)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grit_store_pb2_grpc.add_GritStoreServicer_to_server(GritStore(lmdb_backend), server)
    agent_store_pb2_grpc.add_AgentStoreServicer_to_server(AgentStore(lmdb_backend), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    return server

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # async def arun():
    #     server = await start_server("/tmp/grit_store")
    #     await server.wait_for_termination()
    # asyncio.run(arun())
    
    #IMPORTANT: since we are not using asycn storage (lmdb is sync), it is about 30% faster to use the sync server 

    #delete the dir if it exists
    if os.path.exists("/tmp/aos_store"):
        print("deleting /tmp/aos_store")
        os.system("rm -rf /tmp/aos_store")
    server = start_server_sync("/tmp/aos_store")
    server.wait_for_termination()