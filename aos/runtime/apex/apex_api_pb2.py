# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aos/runtime/apex/apex_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x61os/runtime/apex/apex_api.proto\"%\n\x11StartAgentRequest\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x0c\"\x14\n\x12StartAgentResponse\"$\n\x10StopAgentRequest\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x0c\"\x13\n\x11StopAgentResponse\"\x19\n\x17GetRunningAgentsRequest\"6\n\x18GetRunningAgentsResponse\x12\x1a\n\x06\x61gents\x18\n \x03(\x0b\x32\n.AgentInfo\"\xb0\x01\n\tAgentInfo\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x0c\x12\x11\n\tagent_did\x18\x02 \x01(\t\x12\x15\n\rstore_address\x18\x03 \x01(\t\x12\x32\n\x0c\x63\x61pabilities\x18\x04 \x03(\x0b\x32\x1c.AgentInfo.CapabilitiesEntry\x1a\x33\n\x11\x43\x61pabilitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x16\n\x14GetApexStatusRequest\"\xdf\x01\n\x15GetApexStatusResponse\x12\x31\n\x06status\x18\x01 \x01(\x0e\x32!.GetApexStatusResponse.ApexStatus\x12\x0f\n\x07node_id\x18\x02 \x01(\t\x12\x15\n\rstore_address\x18\x03 \x01(\t\x12\x1c\n\x07workers\x18\n \x03(\x0b\x32\x0b.WorkerInfo\"M\n\nApexStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08STARTING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0c\n\x08STOPPING\x10\x03\x12\t\n\x05\x45RROR\x10\n\"\xa1\x01\n\nWorkerInfo\x12\x11\n\tworker_id\x18\x01 \x01(\t\x12\x33\n\x0c\x63\x61pabilities\x18\x02 \x03(\x0b\x32\x1d.WorkerInfo.CapabilitiesEntry\x12\x16\n\x0e\x63urrent_agents\x18\x03 \x03(\x0c\x1a\x33\n\x11\x43\x61pabilitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xef\x01\n\x14InjectMessageRequest\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x0c\x12\x14\n\x0crecipient_id\x18\x02 \x01(\x0c\x12\x33\n\x07headers\x18\x03 \x03(\x0b\x32\".InjectMessageRequest.HeadersEntry\x12\x11\n\tis_signal\x18\x04 \x01(\x08\x12\x14\n\ncontent_id\x18\x05 \x01(\x0cH\x00\x12\x16\n\x0c\x63ontent_blob\x18\x06 \x01(\x0cH\x00\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\t\n\x07\x63ontent\"=\n\x15InjectMessageResponse\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x0c\x12\x12\n\nmessage_id\x18\x02 \x01(\x0c\"k\n\x0fRunQueryRequest\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x0c\x12\x10\n\x08\x61\x63tor_id\x18\x02 \x01(\x0c\x12\x12\n\nquery_name\x18\x04 \x01(\t\x12\x14\n\x07\x63ontext\x18\x05 \x01(\x0cH\x00\x88\x01\x01\x42\n\n\x08_context\"c\n\x10RunQueryResponse\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x0c\x12\x10\n\x08\x61\x63tor_id\x18\x02 \x01(\x0c\x12\x11\n\x07tree_id\x18\n \x01(\x0cH\x00\x12\x0e\n\x04\x62lob\x18\x0b \x01(\x0cH\x00\x42\x08\n\x06result2\xc7\x02\n\x07\x41pexApi\x12@\n\rGetApexStatus\x12\x15.GetApexStatusRequest\x1a\x16.GetApexStatusResponse\"\x00\x12I\n\x10GetRunningAgents\x12\x18.GetRunningAgentsRequest\x1a\x19.GetRunningAgentsResponse\"\x00\x12\x37\n\nStartAgent\x12\x12.StartAgentRequest\x1a\x13.StartAgentResponse\"\x00\x12\x34\n\tStopAgent\x12\x11.StopAgentRequest\x1a\x12.StopAgentResponse\"\x00\x12@\n\rInjectMessage\x12\x15.InjectMessageRequest\x1a\x16.InjectMessageResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aos.runtime.apex.apex_api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_AGENTINFO_CAPABILITIESENTRY']._options = None
  _globals['_AGENTINFO_CAPABILITIESENTRY']._serialized_options = b'8\001'
  _globals['_WORKERINFO_CAPABILITIESENTRY']._options = None
  _globals['_WORKERINFO_CAPABILITIESENTRY']._serialized_options = b'8\001'
  _globals['_INJECTMESSAGEREQUEST_HEADERSENTRY']._options = None
  _globals['_INJECTMESSAGEREQUEST_HEADERSENTRY']._serialized_options = b'8\001'
  _globals['_STARTAGENTREQUEST']._serialized_start=35
  _globals['_STARTAGENTREQUEST']._serialized_end=72
  _globals['_STARTAGENTRESPONSE']._serialized_start=74
  _globals['_STARTAGENTRESPONSE']._serialized_end=94
  _globals['_STOPAGENTREQUEST']._serialized_start=96
  _globals['_STOPAGENTREQUEST']._serialized_end=132
  _globals['_STOPAGENTRESPONSE']._serialized_start=134
  _globals['_STOPAGENTRESPONSE']._serialized_end=153
  _globals['_GETRUNNINGAGENTSREQUEST']._serialized_start=155
  _globals['_GETRUNNINGAGENTSREQUEST']._serialized_end=180
  _globals['_GETRUNNINGAGENTSRESPONSE']._serialized_start=182
  _globals['_GETRUNNINGAGENTSRESPONSE']._serialized_end=236
  _globals['_AGENTINFO']._serialized_start=239
  _globals['_AGENTINFO']._serialized_end=415
  _globals['_AGENTINFO_CAPABILITIESENTRY']._serialized_start=364
  _globals['_AGENTINFO_CAPABILITIESENTRY']._serialized_end=415
  _globals['_GETAPEXSTATUSREQUEST']._serialized_start=417
  _globals['_GETAPEXSTATUSREQUEST']._serialized_end=439
  _globals['_GETAPEXSTATUSRESPONSE']._serialized_start=442
  _globals['_GETAPEXSTATUSRESPONSE']._serialized_end=665
  _globals['_GETAPEXSTATUSRESPONSE_APEXSTATUS']._serialized_start=588
  _globals['_GETAPEXSTATUSRESPONSE_APEXSTATUS']._serialized_end=665
  _globals['_WORKERINFO']._serialized_start=668
  _globals['_WORKERINFO']._serialized_end=829
  _globals['_WORKERINFO_CAPABILITIESENTRY']._serialized_start=364
  _globals['_WORKERINFO_CAPABILITIESENTRY']._serialized_end=415
  _globals['_INJECTMESSAGEREQUEST']._serialized_start=832
  _globals['_INJECTMESSAGEREQUEST']._serialized_end=1071
  _globals['_INJECTMESSAGEREQUEST_HEADERSENTRY']._serialized_start=1014
  _globals['_INJECTMESSAGEREQUEST_HEADERSENTRY']._serialized_end=1060
  _globals['_INJECTMESSAGERESPONSE']._serialized_start=1073
  _globals['_INJECTMESSAGERESPONSE']._serialized_end=1134
  _globals['_RUNQUERYREQUEST']._serialized_start=1136
  _globals['_RUNQUERYREQUEST']._serialized_end=1243
  _globals['_RUNQUERYRESPONSE']._serialized_start=1245
  _globals['_RUNQUERYRESPONSE']._serialized_end=1344
  _globals['_APEXAPI']._serialized_start=1347
  _globals['_APEXAPI']._serialized_end=1674
# @@protoc_insertion_point(module_scope)
