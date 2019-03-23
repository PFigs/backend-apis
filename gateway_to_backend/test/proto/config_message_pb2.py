# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import nanopb_pb2 as nanopb__pb2
import wp_global_pb2 as wp__global__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='config_message.proto',
  package='wirepas.proto.gateway_api',
  syntax='proto2',
  serialized_pb=_b('\n\x14\x63onfig_message.proto\x12\x19wirepas.proto.gateway_api\x1a\x0cnanopb.proto\x1a\x0fwp_global.proto\"\xe9\x01\n\x08NodeRole\x12:\n\x04role\x18\x01 \x02(\x0e\x32,.wirepas.proto.gateway_api.NodeRole.BaseRole\x12\x43\n\x05\x66lags\x18\x02 \x03(\x0e\x32-.wirepas.proto.gateway_api.NodeRole.RoleFlagsB\x05\x92?\x02\x10\x10\"0\n\x08\x42\x61seRole\x12\x08\n\x04SINK\x10\x01\x12\n\n\x06ROUTER\x10\x02\x12\x0e\n\nNON_ROUTER\x10\x03\"*\n\tRoleFlags\x12\x0f\n\x0bLOW_LATENCY\x10\x01\x12\x0c\n\x08\x41UTOROLE\x10\x02\"2\n\x10\x41\x63\x63\x65ssCycleRange\x12\x0e\n\x06min_ms\x18\x01 \x02(\r\x12\x0e\n\x06max_ms\x18\x02 \x02(\r\"8\n\x0c\x43hannelRange\x12\x13\n\x0bmin_channel\x18\x01 \x02(\r\x12\x13\n\x0bmax_channel\x18\x02 \x02(\r\"V\n\rAppConfigData\x12\x17\n\x0f\x64iag_interval_s\x18\x01 \x02(\r\x12\x1f\n\x0f\x61pp_config_data\x18\x02 \x02(\x0c\x42\x06\x92?\x03\x08\x80\x08\x12\x0b\n\x03seq\x18\x03 \x02(\r\"E\n\x0bNetworkKeys\x12\x16\n\x06\x63ipher\x18\x01 \x02(\x0c\x42\x06\x92?\x03\x08\x80\x08\x12\x1e\n\x0e\x61uthentication\x18\x02 \x02(\x0c\x42\x06\x92?\x03\x08\x80\x08\"\xb2\x05\n\x0eSinkReadConfig\x12\x17\n\x07sink_id\x18\x01 \x02(\tB\x06\x92?\x03\x08\x80\x01\x12\x36\n\tnode_role\x18\x02 \x01(\x0b\x32#.wirepas.proto.gateway_api.NodeRole\x12\x14\n\x0cnode_address\x18\x03 \x01(\r\x12\x17\n\x0fnetwork_address\x18\x04 \x01(\x04\x12\x17\n\x0fnetwork_channel\x18\x05 \x01(\r\x12<\n\napp_config\x18\x06 \x01(\x0b\x32(.wirepas.proto.gateway_api.AppConfigData\x12\x13\n\x0b\x63hannel_map\x18\x07 \x01(\r\x12\x14\n\x0c\x61re_keys_set\x18\x08 \x01(\x08\x12\x45\n\x10\x63urrent_ac_range\x18\t \x01(\x0b\x32+.wirepas.proto.gateway_api.AccessCycleRange\x12>\n\tac_limits\x18\n \x01(\x0b\x32+.wirepas.proto.gateway_api.AccessCycleRange\x12\x0f\n\x07max_mtu\x18\x0b \x01(\r\x12?\n\x0e\x63hannel_limits\x18\x0c \x01(\x0b\x32\'.wirepas.proto.gateway_api.ChannelRange\x12\x10\n\x08hw_magic\x18\r \x01(\r\x12\x15\n\rstack_profile\x18\x0e \x01(\r\x12\x1b\n\x13\x61pp_config_max_size\x18\x0f \x01(\r\x12\x44\n\x10\x66irmware_version\x18\x10 \x01(\x0b\x32*.wirepas.proto.gateway_api.FirmwareVersion\x12\x39\n\nsink_state\x18\x11 \x01(\x0e\x32%.wirepas.proto.gateway_api.OnOffState\"\xb3\x03\n\rSinkNewConfig\x12\x17\n\x07sink_id\x18\x01 \x02(\tB\x06\x92?\x03\x08\x80\x01\x12\x36\n\tnode_role\x18\x02 \x01(\x0b\x32#.wirepas.proto.gateway_api.NodeRole\x12\x14\n\x0cnode_address\x18\x03 \x01(\r\x12\x17\n\x0fnetwork_address\x18\x04 \x01(\x04\x12\x17\n\x0fnetwork_channel\x18\x05 \x01(\r\x12<\n\napp_config\x18\x06 \x01(\x0b\x32(.wirepas.proto.gateway_api.AppConfigData\x12\x13\n\x0b\x63hannel_map\x18\x07 \x01(\r\x12\x34\n\x04keys\x18\x08 \x01(\x0b\x32&.wirepas.proto.gateway_api.NetworkKeys\x12\x45\n\x10\x63urrent_ac_range\x18\t \x01(\x0b\x32+.wirepas.proto.gateway_api.AccessCycleRange\x12\x39\n\nsink_state\x18\n \x01(\x0e\x32%.wirepas.proto.gateway_api.OnOffState\"\x8c\x01\n\x0bStatusEvent\x12\x36\n\x06header\x18\x01 \x02(\x0b\x32&.wirepas.proto.gateway_api.EventHeader\x12\x0f\n\x07version\x18\x02 \x02(\r\x12\x34\n\x05state\x18\x03 \x02(\x0e\x32%.wirepas.proto.gateway_api.OnOffState\"I\n\rGetConfigsReq\x12\x38\n\x06header\x18\x01 \x02(\x0b\x32(.wirepas.proto.gateway_api.RequestHeader\"\x8e\x01\n\x0eGetConfigsResp\x12\x39\n\x06header\x18\x01 \x02(\x0b\x32).wirepas.proto.gateway_api.ResponseHeader\x12\x41\n\x07\x63onfigs\x18\x02 \x03(\x0b\x32).wirepas.proto.gateway_api.SinkReadConfigB\x05\x92?\x02\x10\x10\"\x82\x01\n\x0cSetConfigReq\x12\x38\n\x06header\x18\x01 \x02(\x0b\x32(.wirepas.proto.gateway_api.RequestHeader\x12\x38\n\x06\x63onfig\x18\x02 \x02(\x0b\x32(.wirepas.proto.gateway_api.SinkNewConfig\"\x85\x01\n\rSetConfigResp\x12\x39\n\x06header\x18\x01 \x02(\x0b\x32).wirepas.proto.gateway_api.ResponseHeader\x12\x39\n\x06\x63onfig\x18\x02 \x02(\x0b\x32).wirepas.proto.gateway_api.SinkReadConfig')
  ,
  dependencies=[nanopb__pb2.DESCRIPTOR,wp__global__pb2.DESCRIPTOR,])



_NODEROLE_BASEROLE = _descriptor.EnumDescriptor(
  name='BaseRole',
  full_name='wirepas.proto.gateway_api.NodeRole.BaseRole',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SINK', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTER', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NON_ROUTER', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=224,
  serialized_end=272,
)
_sym_db.RegisterEnumDescriptor(_NODEROLE_BASEROLE)

_NODEROLE_ROLEFLAGS = _descriptor.EnumDescriptor(
  name='RoleFlags',
  full_name='wirepas.proto.gateway_api.NodeRole.RoleFlags',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LOW_LATENCY', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTOROLE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=274,
  serialized_end=316,
)
_sym_db.RegisterEnumDescriptor(_NODEROLE_ROLEFLAGS)


_NODEROLE = _descriptor.Descriptor(
  name='NodeRole',
  full_name='wirepas.proto.gateway_api.NodeRole',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='wirepas.proto.gateway_api.NodeRole.role', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flags', full_name='wirepas.proto.gateway_api.NodeRole.flags', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\020\020')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NODEROLE_BASEROLE,
    _NODEROLE_ROLEFLAGS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=316,
)


_ACCESSCYCLERANGE = _descriptor.Descriptor(
  name='AccessCycleRange',
  full_name='wirepas.proto.gateway_api.AccessCycleRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_ms', full_name='wirepas.proto.gateway_api.AccessCycleRange.min_ms', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_ms', full_name='wirepas.proto.gateway_api.AccessCycleRange.max_ms', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=318,
  serialized_end=368,
)


_CHANNELRANGE = _descriptor.Descriptor(
  name='ChannelRange',
  full_name='wirepas.proto.gateway_api.ChannelRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_channel', full_name='wirepas.proto.gateway_api.ChannelRange.min_channel', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_channel', full_name='wirepas.proto.gateway_api.ChannelRange.max_channel', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=370,
  serialized_end=426,
)


_APPCONFIGDATA = _descriptor.Descriptor(
  name='AppConfigData',
  full_name='wirepas.proto.gateway_api.AppConfigData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='diag_interval_s', full_name='wirepas.proto.gateway_api.AppConfigData.diag_interval_s', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_config_data', full_name='wirepas.proto.gateway_api.AppConfigData.app_config_data', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\003\010\200\010')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq', full_name='wirepas.proto.gateway_api.AppConfigData.seq', index=2,
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
  serialized_start=428,
  serialized_end=514,
)


_NETWORKKEYS = _descriptor.Descriptor(
  name='NetworkKeys',
  full_name='wirepas.proto.gateway_api.NetworkKeys',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cipher', full_name='wirepas.proto.gateway_api.NetworkKeys.cipher', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\003\010\200\010')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authentication', full_name='wirepas.proto.gateway_api.NetworkKeys.authentication', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\003\010\200\010')), file=DESCRIPTOR),
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
  serialized_start=516,
  serialized_end=585,
)


_SINKREADCONFIG = _descriptor.Descriptor(
  name='SinkReadConfig',
  full_name='wirepas.proto.gateway_api.SinkReadConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sink_id', full_name='wirepas.proto.gateway_api.SinkReadConfig.sink_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\003\010\200\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_role', full_name='wirepas.proto.gateway_api.SinkReadConfig.node_role', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_address', full_name='wirepas.proto.gateway_api.SinkReadConfig.node_address', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_address', full_name='wirepas.proto.gateway_api.SinkReadConfig.network_address', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_channel', full_name='wirepas.proto.gateway_api.SinkReadConfig.network_channel', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_config', full_name='wirepas.proto.gateway_api.SinkReadConfig.app_config', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_map', full_name='wirepas.proto.gateway_api.SinkReadConfig.channel_map', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='are_keys_set', full_name='wirepas.proto.gateway_api.SinkReadConfig.are_keys_set', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_ac_range', full_name='wirepas.proto.gateway_api.SinkReadConfig.current_ac_range', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ac_limits', full_name='wirepas.proto.gateway_api.SinkReadConfig.ac_limits', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_mtu', full_name='wirepas.proto.gateway_api.SinkReadConfig.max_mtu', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_limits', full_name='wirepas.proto.gateway_api.SinkReadConfig.channel_limits', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hw_magic', full_name='wirepas.proto.gateway_api.SinkReadConfig.hw_magic', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stack_profile', full_name='wirepas.proto.gateway_api.SinkReadConfig.stack_profile', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_config_max_size', full_name='wirepas.proto.gateway_api.SinkReadConfig.app_config_max_size', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='firmware_version', full_name='wirepas.proto.gateway_api.SinkReadConfig.firmware_version', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sink_state', full_name='wirepas.proto.gateway_api.SinkReadConfig.sink_state', index=16,
      number=17, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  serialized_start=588,
  serialized_end=1278,
)


_SINKNEWCONFIG = _descriptor.Descriptor(
  name='SinkNewConfig',
  full_name='wirepas.proto.gateway_api.SinkNewConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sink_id', full_name='wirepas.proto.gateway_api.SinkNewConfig.sink_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\003\010\200\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_role', full_name='wirepas.proto.gateway_api.SinkNewConfig.node_role', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_address', full_name='wirepas.proto.gateway_api.SinkNewConfig.node_address', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_address', full_name='wirepas.proto.gateway_api.SinkNewConfig.network_address', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_channel', full_name='wirepas.proto.gateway_api.SinkNewConfig.network_channel', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_config', full_name='wirepas.proto.gateway_api.SinkNewConfig.app_config', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_map', full_name='wirepas.proto.gateway_api.SinkNewConfig.channel_map', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keys', full_name='wirepas.proto.gateway_api.SinkNewConfig.keys', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_ac_range', full_name='wirepas.proto.gateway_api.SinkNewConfig.current_ac_range', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sink_state', full_name='wirepas.proto.gateway_api.SinkNewConfig.sink_state', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  serialized_start=1281,
  serialized_end=1716,
)


_STATUSEVENT = _descriptor.Descriptor(
  name='StatusEvent',
  full_name='wirepas.proto.gateway_api.StatusEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wirepas.proto.gateway_api.StatusEvent.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='wirepas.proto.gateway_api.StatusEvent.version', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='wirepas.proto.gateway_api.StatusEvent.state', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
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
  serialized_start=1719,
  serialized_end=1859,
)


_GETCONFIGSREQ = _descriptor.Descriptor(
  name='GetConfigsReq',
  full_name='wirepas.proto.gateway_api.GetConfigsReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wirepas.proto.gateway_api.GetConfigsReq.header', index=0,
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
  serialized_start=1861,
  serialized_end=1934,
)


_GETCONFIGSRESP = _descriptor.Descriptor(
  name='GetConfigsResp',
  full_name='wirepas.proto.gateway_api.GetConfigsResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wirepas.proto.gateway_api.GetConfigsResp.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configs', full_name='wirepas.proto.gateway_api.GetConfigsResp.configs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\020\020')), file=DESCRIPTOR),
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
  serialized_start=1937,
  serialized_end=2079,
)


_SETCONFIGREQ = _descriptor.Descriptor(
  name='SetConfigReq',
  full_name='wirepas.proto.gateway_api.SetConfigReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wirepas.proto.gateway_api.SetConfigReq.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='wirepas.proto.gateway_api.SetConfigReq.config', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  serialized_start=2082,
  serialized_end=2212,
)


_SETCONFIGRESP = _descriptor.Descriptor(
  name='SetConfigResp',
  full_name='wirepas.proto.gateway_api.SetConfigResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wirepas.proto.gateway_api.SetConfigResp.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='wirepas.proto.gateway_api.SetConfigResp.config', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  serialized_start=2215,
  serialized_end=2348,
)

_NODEROLE.fields_by_name['role'].enum_type = _NODEROLE_BASEROLE
_NODEROLE.fields_by_name['flags'].enum_type = _NODEROLE_ROLEFLAGS
_NODEROLE_BASEROLE.containing_type = _NODEROLE
_NODEROLE_ROLEFLAGS.containing_type = _NODEROLE
_SINKREADCONFIG.fields_by_name['node_role'].message_type = _NODEROLE
_SINKREADCONFIG.fields_by_name['app_config'].message_type = _APPCONFIGDATA
_SINKREADCONFIG.fields_by_name['current_ac_range'].message_type = _ACCESSCYCLERANGE
_SINKREADCONFIG.fields_by_name['ac_limits'].message_type = _ACCESSCYCLERANGE
_SINKREADCONFIG.fields_by_name['channel_limits'].message_type = _CHANNELRANGE
_SINKREADCONFIG.fields_by_name['firmware_version'].message_type = wp__global__pb2._FIRMWAREVERSION
_SINKREADCONFIG.fields_by_name['sink_state'].enum_type = wp__global__pb2._ONOFFSTATE
_SINKNEWCONFIG.fields_by_name['node_role'].message_type = _NODEROLE
_SINKNEWCONFIG.fields_by_name['app_config'].message_type = _APPCONFIGDATA
_SINKNEWCONFIG.fields_by_name['keys'].message_type = _NETWORKKEYS
_SINKNEWCONFIG.fields_by_name['current_ac_range'].message_type = _ACCESSCYCLERANGE
_SINKNEWCONFIG.fields_by_name['sink_state'].enum_type = wp__global__pb2._ONOFFSTATE
_STATUSEVENT.fields_by_name['header'].message_type = wp__global__pb2._EVENTHEADER
_STATUSEVENT.fields_by_name['state'].enum_type = wp__global__pb2._ONOFFSTATE
_GETCONFIGSREQ.fields_by_name['header'].message_type = wp__global__pb2._REQUESTHEADER
_GETCONFIGSRESP.fields_by_name['header'].message_type = wp__global__pb2._RESPONSEHEADER
_GETCONFIGSRESP.fields_by_name['configs'].message_type = _SINKREADCONFIG
_SETCONFIGREQ.fields_by_name['header'].message_type = wp__global__pb2._REQUESTHEADER
_SETCONFIGREQ.fields_by_name['config'].message_type = _SINKNEWCONFIG
_SETCONFIGRESP.fields_by_name['header'].message_type = wp__global__pb2._RESPONSEHEADER
_SETCONFIGRESP.fields_by_name['config'].message_type = _SINKREADCONFIG
DESCRIPTOR.message_types_by_name['NodeRole'] = _NODEROLE
DESCRIPTOR.message_types_by_name['AccessCycleRange'] = _ACCESSCYCLERANGE
DESCRIPTOR.message_types_by_name['ChannelRange'] = _CHANNELRANGE
DESCRIPTOR.message_types_by_name['AppConfigData'] = _APPCONFIGDATA
DESCRIPTOR.message_types_by_name['NetworkKeys'] = _NETWORKKEYS
DESCRIPTOR.message_types_by_name['SinkReadConfig'] = _SINKREADCONFIG
DESCRIPTOR.message_types_by_name['SinkNewConfig'] = _SINKNEWCONFIG
DESCRIPTOR.message_types_by_name['StatusEvent'] = _STATUSEVENT
DESCRIPTOR.message_types_by_name['GetConfigsReq'] = _GETCONFIGSREQ
DESCRIPTOR.message_types_by_name['GetConfigsResp'] = _GETCONFIGSRESP
DESCRIPTOR.message_types_by_name['SetConfigReq'] = _SETCONFIGREQ
DESCRIPTOR.message_types_by_name['SetConfigResp'] = _SETCONFIGRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeRole = _reflection.GeneratedProtocolMessageType('NodeRole', (_message.Message,), dict(
  DESCRIPTOR = _NODEROLE,
  __module__ = 'config_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.NodeRole)
  ))
_sym_db.RegisterMessage(NodeRole)

AccessCycleRange = _reflection.GeneratedProtocolMessageType('AccessCycleRange', (_message.Message,), dict(
  DESCRIPTOR = _ACCESSCYCLERANGE,
  __module__ = 'config_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.AccessCycleRange)
  ))
_sym_db.RegisterMessage(AccessCycleRange)

ChannelRange = _reflection.GeneratedProtocolMessageType('ChannelRange', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELRANGE,
  __module__ = 'config_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.ChannelRange)
  ))
_sym_db.RegisterMessage(ChannelRange)

AppConfigData = _reflection.GeneratedProtocolMessageType('AppConfigData', (_message.Message,), dict(
  DESCRIPTOR = _APPCONFIGDATA,
  __module__ = 'config_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.AppConfigData)
  ))
_sym_db.RegisterMessage(AppConfigData)

NetworkKeys = _reflection.GeneratedProtocolMessageType('NetworkKeys', (_message.Message,), dict(
  DESCRIPTOR = _NETWORKKEYS,
  __module__ = 'config_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.NetworkKeys)
  ))
_sym_db.RegisterMessage(NetworkKeys)

SinkReadConfig = _reflection.GeneratedProtocolMessageType('SinkReadConfig', (_message.Message,), dict(
  DESCRIPTOR = _SINKREADCONFIG,
  __module__ = 'config_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.SinkReadConfig)
  ))
_sym_db.RegisterMessage(SinkReadConfig)

SinkNewConfig = _reflection.GeneratedProtocolMessageType('SinkNewConfig', (_message.Message,), dict(
  DESCRIPTOR = _SINKNEWCONFIG,
  __module__ = 'config_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.SinkNewConfig)
  ))
_sym_db.RegisterMessage(SinkNewConfig)

StatusEvent = _reflection.GeneratedProtocolMessageType('StatusEvent', (_message.Message,), dict(
  DESCRIPTOR = _STATUSEVENT,
  __module__ = 'config_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.StatusEvent)
  ))
_sym_db.RegisterMessage(StatusEvent)

GetConfigsReq = _reflection.GeneratedProtocolMessageType('GetConfigsReq', (_message.Message,), dict(
  DESCRIPTOR = _GETCONFIGSREQ,
  __module__ = 'config_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.GetConfigsReq)
  ))
_sym_db.RegisterMessage(GetConfigsReq)

GetConfigsResp = _reflection.GeneratedProtocolMessageType('GetConfigsResp', (_message.Message,), dict(
  DESCRIPTOR = _GETCONFIGSRESP,
  __module__ = 'config_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.GetConfigsResp)
  ))
_sym_db.RegisterMessage(GetConfigsResp)

SetConfigReq = _reflection.GeneratedProtocolMessageType('SetConfigReq', (_message.Message,), dict(
  DESCRIPTOR = _SETCONFIGREQ,
  __module__ = 'config_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.SetConfigReq)
  ))
_sym_db.RegisterMessage(SetConfigReq)

SetConfigResp = _reflection.GeneratedProtocolMessageType('SetConfigResp', (_message.Message,), dict(
  DESCRIPTOR = _SETCONFIGRESP,
  __module__ = 'config_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.SetConfigResp)
  ))
_sym_db.RegisterMessage(SetConfigResp)


_NODEROLE.fields_by_name['flags'].has_options = True
_NODEROLE.fields_by_name['flags']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\020\020'))
_APPCONFIGDATA.fields_by_name['app_config_data'].has_options = True
_APPCONFIGDATA.fields_by_name['app_config_data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\003\010\200\010'))
_NETWORKKEYS.fields_by_name['cipher'].has_options = True
_NETWORKKEYS.fields_by_name['cipher']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\003\010\200\010'))
_NETWORKKEYS.fields_by_name['authentication'].has_options = True
_NETWORKKEYS.fields_by_name['authentication']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\003\010\200\010'))
_SINKREADCONFIG.fields_by_name['sink_id'].has_options = True
_SINKREADCONFIG.fields_by_name['sink_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\003\010\200\001'))
_SINKNEWCONFIG.fields_by_name['sink_id'].has_options = True
_SINKNEWCONFIG.fields_by_name['sink_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\003\010\200\001'))
_GETCONFIGSRESP.fields_by_name['configs'].has_options = True
_GETCONFIGSRESP.fields_by_name['configs']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\020\020'))
# @@protoc_insertion_point(module_scope)
