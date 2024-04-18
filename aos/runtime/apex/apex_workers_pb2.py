# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aos/runtime/apex/apex_workers.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#aos/runtime/apex/apex_workers.proto\".\n\x19WorkerRegistrationRequest\x12\x11\n\tworker_id\x18\x01 \x01(\t\",\n\x1aWorkerRegistrationResponse\x12\x0e\n\x06ticket\x18\x01 \x01(\t\"\xb1\x01\n\x0eWorkerManifest\x12\x11\n\tworker_id\x18\x01 \x01(\t\x12\x37\n\x0c\x63\x61pabilities\x18\n \x03(\x0b\x32!.WorkerManifest.CapabilitiesEntry\x12\x1e\n\x0e\x63urrent_agents\x18\x14 \x03(\x0b\x32\x06.Agent\x1a\x33\n\x11\x43\x61pabilitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa8\x01\n\x05\x41gent\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x0c\x12\x11\n\tagent_did\x18\x02 \x01(\t\x12\x15\n\rstore_address\x18\x03 \x01(\t\x12.\n\x0c\x63\x61pabilities\x18\n \x03(\x0b\x32\x18.Agent.CapabilitiesEntry\x1a\x33\n\x11\x43\x61pabilitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x0f\x41gentAssignment\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x0c\x12\x1a\n\x05\x61gent\x18\x02 \x01(\x0b\x32\x06.AgentH\x00\x88\x01\x01\x42\x08\n\x06_agent\"\xb1\x01\n\x13\x41pexToWorkerMessage\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .ApexToWorkerMessage.MessageType\x12&\n\nassignment\x18\x0b \x01(\x0b\x32\x10.AgentAssignmentH\x00\"7\n\x0bMessageType\x12\x08\n\x04PING\x10\x00\x12\x0e\n\nGIVE_AGENT\x10\n\x12\x0e\n\nYANK_AGENT\x10\x0b\x42\t\n\x07payload\"\xf6\x01\n\x13WorkerToApexMessage\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .WorkerToApexMessage.MessageType\x12\x11\n\tworker_id\x18\x02 \x01(\t\x12\x0e\n\x06ticket\x18\x03 \x01(\t\x12#\n\x08manifest\x18\n \x01(\x0b\x32\x0f.WorkerManifestH\x00\x12&\n\nassignment\x18\x0b \x01(\x0b\x32\x10.AgentAssignmentH\x00\"4\n\x0bMessageType\x12\x08\n\x04PING\x10\x00\x12\t\n\x05READY\x10\x01\x12\x10\n\x0cRETURN_AGENT\x10\x0b\x42\t\n\x07payload2\x9d\x01\n\x0b\x41pexWorkers\x12K\n\x0eRegisterWorker\x12\x1a.WorkerRegistrationRequest\x1a\x1b.WorkerRegistrationResponse\"\x00\x12\x41\n\rConnectWorker\x12\x14.WorkerToApexMessage\x1a\x14.ApexToWorkerMessage\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aos.runtime.apex.apex_workers_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_WORKERMANIFEST_CAPABILITIESENTRY']._options = None
  _globals['_WORKERMANIFEST_CAPABILITIESENTRY']._serialized_options = b'8\001'
  _globals['_AGENT_CAPABILITIESENTRY']._options = None
  _globals['_AGENT_CAPABILITIESENTRY']._serialized_options = b'8\001'
  _globals['_WORKERREGISTRATIONREQUEST']._serialized_start=39
  _globals['_WORKERREGISTRATIONREQUEST']._serialized_end=85
  _globals['_WORKERREGISTRATIONRESPONSE']._serialized_start=87
  _globals['_WORKERREGISTRATIONRESPONSE']._serialized_end=131
  _globals['_WORKERMANIFEST']._serialized_start=134
  _globals['_WORKERMANIFEST']._serialized_end=311
  _globals['_WORKERMANIFEST_CAPABILITIESENTRY']._serialized_start=260
  _globals['_WORKERMANIFEST_CAPABILITIESENTRY']._serialized_end=311
  _globals['_AGENT']._serialized_start=314
  _globals['_AGENT']._serialized_end=482
  _globals['_AGENT_CAPABILITIESENTRY']._serialized_start=260
  _globals['_AGENT_CAPABILITIESENTRY']._serialized_end=311
  _globals['_AGENTASSIGNMENT']._serialized_start=484
  _globals['_AGENTASSIGNMENT']._serialized_end=557
  _globals['_APEXTOWORKERMESSAGE']._serialized_start=560
  _globals['_APEXTOWORKERMESSAGE']._serialized_end=737
  _globals['_APEXTOWORKERMESSAGE_MESSAGETYPE']._serialized_start=671
  _globals['_APEXTOWORKERMESSAGE_MESSAGETYPE']._serialized_end=726
  _globals['_WORKERTOAPEXMESSAGE']._serialized_start=740
  _globals['_WORKERTOAPEXMESSAGE']._serialized_end=986
  _globals['_WORKERTOAPEXMESSAGE_MESSAGETYPE']._serialized_start=923
  _globals['_WORKERTOAPEXMESSAGE_MESSAGETYPE']._serialized_end=975
  _globals['_APEXWORKERS']._serialized_start=989
  _globals['_APEXWORKERS']._serialized_end=1146
# @@protoc_insertion_point(module_scope)
