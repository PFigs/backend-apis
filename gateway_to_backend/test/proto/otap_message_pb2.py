# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: otap_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import wp_global_pb2 as wp__global__pb2
import nanopb_pb2 as nanopb__pb2
import error_pb2 as error__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='otap_message.proto',
  package='wirepas.proto.gateway_api',
  syntax='proto2',
  serialized_pb=_b('\n\x12otap_message.proto\x12\x19wirepas.proto.gateway_api\x1a\x0fwp_global.proto\x1a\x0cnanopb.proto\x1a\x0b\x65rror.proto\"7\n\x0eScratchpadInfo\x12\x0b\n\x03len\x18\x01 \x02(\r\x12\x0b\n\x03\x63rc\x18\x02 \x02(\r\x12\x0b\n\x03seq\x18\x03 \x02(\r\"R\n\x16GetScratchpadStatusReq\x12\x38\n\x06header\x18\x01 \x02(\x0b\x32(.wirepas.proto.gateway_api.RequestHeader\"\x81\x03\n\x17GetScratchpadStatusResp\x12\x39\n\x06header\x18\x01 \x02(\x0b\x32).wirepas.proto.gateway_api.ResponseHeader\x12\x44\n\x11stored_scratchpad\x18\x02 \x01(\x0b\x32).wirepas.proto.gateway_api.ScratchpadInfo\x12\x42\n\rstored_status\x18\x03 \x01(\x0e\x32+.wirepas.proto.gateway_api.ScratchpadStatus\x12>\n\x0bstored_type\x18\x04 \x01(\x0e\x32).wirepas.proto.gateway_api.ScratchpadType\x12G\n\x14processed_scratchpad\x18\x05 \x01(\x0b\x32).wirepas.proto.gateway_api.ScratchpadInfo\x12\x18\n\x10\x66irmware_area_id\x18\x06 \x01(\r\"p\n\x13UploadScratchpadReq\x12\x38\n\x06header\x18\x01 \x02(\x0b\x32(.wirepas.proto.gateway_api.RequestHeader\x12\x0b\n\x03seq\x18\x02 \x02(\r\x12\x12\n\nscratchpad\x18\x03 \x01(\x0c\"Q\n\x14UploadScratchpadResp\x12\x39\n\x06header\x18\x01 \x02(\x0b\x32).wirepas.proto.gateway_api.ResponseHeader\"P\n\x14ProcessScratchpadReq\x12\x38\n\x06header\x18\x01 \x02(\x0b\x32(.wirepas.proto.gateway_api.RequestHeader\"R\n\x15ProcessScratchpadResp\x12\x39\n\x06header\x18\x01 \x02(\x0b\x32).wirepas.proto.gateway_api.ResponseHeader*5\n\x0eScratchpadType\x12\t\n\x05\x42LANK\x10\x01\x12\x0b\n\x07PRESENT\x10\x02\x12\x0b\n\x07PROCESS\x10\x03*3\n\x10ScratchpadStatus\x12\x0b\n\x07SUCCESS\x10\x01\x12\x07\n\x03NEW\x10\x02\x12\t\n\x05\x45RROR\x10\x03')
  ,
  dependencies=[wp__global__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,error__pb2.DESCRIPTOR,])

_SCRATCHPADTYPE = _descriptor.EnumDescriptor(
  name='ScratchpadType',
  full_name='wirepas.proto.gateway_api.ScratchpadType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BLANK', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRESENT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROCESS', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=985,
  serialized_end=1038,
)
_sym_db.RegisterEnumDescriptor(_SCRATCHPADTYPE)

ScratchpadType = enum_type_wrapper.EnumTypeWrapper(_SCRATCHPADTYPE)
_SCRATCHPADSTATUS = _descriptor.EnumDescriptor(
  name='ScratchpadStatus',
  full_name='wirepas.proto.gateway_api.ScratchpadStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1040,
  serialized_end=1091,
)
_sym_db.RegisterEnumDescriptor(_SCRATCHPADSTATUS)

ScratchpadStatus = enum_type_wrapper.EnumTypeWrapper(_SCRATCHPADSTATUS)
BLANK = 1
PRESENT = 2
PROCESS = 3
SUCCESS = 1
NEW = 2
ERROR = 3



_SCRATCHPADINFO = _descriptor.Descriptor(
  name='ScratchpadInfo',
  full_name='wirepas.proto.gateway_api.ScratchpadInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='len', full_name='wirepas.proto.gateway_api.ScratchpadInfo.len', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='crc', full_name='wirepas.proto.gateway_api.ScratchpadInfo.crc', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq', full_name='wirepas.proto.gateway_api.ScratchpadInfo.seq', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=148,
)


_GETSCRATCHPADSTATUSREQ = _descriptor.Descriptor(
  name='GetScratchpadStatusReq',
  full_name='wirepas.proto.gateway_api.GetScratchpadStatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wirepas.proto.gateway_api.GetScratchpadStatusReq.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=232,
)


_GETSCRATCHPADSTATUSRESP = _descriptor.Descriptor(
  name='GetScratchpadStatusResp',
  full_name='wirepas.proto.gateway_api.GetScratchpadStatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wirepas.proto.gateway_api.GetScratchpadStatusResp.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stored_scratchpad', full_name='wirepas.proto.gateway_api.GetScratchpadStatusResp.stored_scratchpad', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stored_status', full_name='wirepas.proto.gateway_api.GetScratchpadStatusResp.stored_status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stored_type', full_name='wirepas.proto.gateway_api.GetScratchpadStatusResp.stored_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processed_scratchpad', full_name='wirepas.proto.gateway_api.GetScratchpadStatusResp.processed_scratchpad', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='firmware_area_id', full_name='wirepas.proto.gateway_api.GetScratchpadStatusResp.firmware_area_id', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=235,
  serialized_end=620,
)


_UPLOADSCRATCHPADREQ = _descriptor.Descriptor(
  name='UploadScratchpadReq',
  full_name='wirepas.proto.gateway_api.UploadScratchpadReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wirepas.proto.gateway_api.UploadScratchpadReq.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq', full_name='wirepas.proto.gateway_api.UploadScratchpadReq.seq', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scratchpad', full_name='wirepas.proto.gateway_api.UploadScratchpadReq.scratchpad', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=622,
  serialized_end=734,
)


_UPLOADSCRATCHPADRESP = _descriptor.Descriptor(
  name='UploadScratchpadResp',
  full_name='wirepas.proto.gateway_api.UploadScratchpadResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wirepas.proto.gateway_api.UploadScratchpadResp.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=736,
  serialized_end=817,
)


_PROCESSSCRATCHPADREQ = _descriptor.Descriptor(
  name='ProcessScratchpadReq',
  full_name='wirepas.proto.gateway_api.ProcessScratchpadReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wirepas.proto.gateway_api.ProcessScratchpadReq.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=819,
  serialized_end=899,
)


_PROCESSSCRATCHPADRESP = _descriptor.Descriptor(
  name='ProcessScratchpadResp',
  full_name='wirepas.proto.gateway_api.ProcessScratchpadResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wirepas.proto.gateway_api.ProcessScratchpadResp.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=901,
  serialized_end=983,
)

_GETSCRATCHPADSTATUSREQ.fields_by_name['header'].message_type = wp__global__pb2._REQUESTHEADER
_GETSCRATCHPADSTATUSRESP.fields_by_name['header'].message_type = wp__global__pb2._RESPONSEHEADER
_GETSCRATCHPADSTATUSRESP.fields_by_name['stored_scratchpad'].message_type = _SCRATCHPADINFO
_GETSCRATCHPADSTATUSRESP.fields_by_name['stored_status'].enum_type = _SCRATCHPADSTATUS
_GETSCRATCHPADSTATUSRESP.fields_by_name['stored_type'].enum_type = _SCRATCHPADTYPE
_GETSCRATCHPADSTATUSRESP.fields_by_name['processed_scratchpad'].message_type = _SCRATCHPADINFO
_UPLOADSCRATCHPADREQ.fields_by_name['header'].message_type = wp__global__pb2._REQUESTHEADER
_UPLOADSCRATCHPADRESP.fields_by_name['header'].message_type = wp__global__pb2._RESPONSEHEADER
_PROCESSSCRATCHPADREQ.fields_by_name['header'].message_type = wp__global__pb2._REQUESTHEADER
_PROCESSSCRATCHPADRESP.fields_by_name['header'].message_type = wp__global__pb2._RESPONSEHEADER
DESCRIPTOR.message_types_by_name['ScratchpadInfo'] = _SCRATCHPADINFO
DESCRIPTOR.message_types_by_name['GetScratchpadStatusReq'] = _GETSCRATCHPADSTATUSREQ
DESCRIPTOR.message_types_by_name['GetScratchpadStatusResp'] = _GETSCRATCHPADSTATUSRESP
DESCRIPTOR.message_types_by_name['UploadScratchpadReq'] = _UPLOADSCRATCHPADREQ
DESCRIPTOR.message_types_by_name['UploadScratchpadResp'] = _UPLOADSCRATCHPADRESP
DESCRIPTOR.message_types_by_name['ProcessScratchpadReq'] = _PROCESSSCRATCHPADREQ
DESCRIPTOR.message_types_by_name['ProcessScratchpadResp'] = _PROCESSSCRATCHPADRESP
DESCRIPTOR.enum_types_by_name['ScratchpadType'] = _SCRATCHPADTYPE
DESCRIPTOR.enum_types_by_name['ScratchpadStatus'] = _SCRATCHPADSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScratchpadInfo = _reflection.GeneratedProtocolMessageType('ScratchpadInfo', (_message.Message,), dict(
  DESCRIPTOR = _SCRATCHPADINFO,
  __module__ = 'otap_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.ScratchpadInfo)
  ))
_sym_db.RegisterMessage(ScratchpadInfo)

GetScratchpadStatusReq = _reflection.GeneratedProtocolMessageType('GetScratchpadStatusReq', (_message.Message,), dict(
  DESCRIPTOR = _GETSCRATCHPADSTATUSREQ,
  __module__ = 'otap_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.GetScratchpadStatusReq)
  ))
_sym_db.RegisterMessage(GetScratchpadStatusReq)

GetScratchpadStatusResp = _reflection.GeneratedProtocolMessageType('GetScratchpadStatusResp', (_message.Message,), dict(
  DESCRIPTOR = _GETSCRATCHPADSTATUSRESP,
  __module__ = 'otap_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.GetScratchpadStatusResp)
  ))
_sym_db.RegisterMessage(GetScratchpadStatusResp)

UploadScratchpadReq = _reflection.GeneratedProtocolMessageType('UploadScratchpadReq', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADSCRATCHPADREQ,
  __module__ = 'otap_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.UploadScratchpadReq)
  ))
_sym_db.RegisterMessage(UploadScratchpadReq)

UploadScratchpadResp = _reflection.GeneratedProtocolMessageType('UploadScratchpadResp', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADSCRATCHPADRESP,
  __module__ = 'otap_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.UploadScratchpadResp)
  ))
_sym_db.RegisterMessage(UploadScratchpadResp)

ProcessScratchpadReq = _reflection.GeneratedProtocolMessageType('ProcessScratchpadReq', (_message.Message,), dict(
  DESCRIPTOR = _PROCESSSCRATCHPADREQ,
  __module__ = 'otap_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.ProcessScratchpadReq)
  ))
_sym_db.RegisterMessage(ProcessScratchpadReq)

ProcessScratchpadResp = _reflection.GeneratedProtocolMessageType('ProcessScratchpadResp', (_message.Message,), dict(
  DESCRIPTOR = _PROCESSSCRATCHPADRESP,
  __module__ = 'otap_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.ProcessScratchpadResp)
  ))
_sym_db.RegisterMessage(ProcessScratchpadResp)


# @@protoc_insertion_point(module_scope)
