# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='helloworld.proto',
  package='helloworld',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10helloworld.proto\x12\nhelloworld\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1f\n\x0cHelloReponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x9d\x05\n\tDTRequest\x12\x13\n\x0bint32_value\x18\x01 \x01(\x05\x12\x14\n\x0csint32_value\x18\x02 \x01(\x11\x12\x15\n\rfixed32_value\x18\x03 \x01(\x07\x12\x13\n\x0bint64_value\x18\x04 \x01(\x03\x12\x14\n\x0csint64_value\x18\x05 \x01(\x12\x12\x15\n\rfixed64_value\x18\x06 \x01(\x06\x12\x14\n\x0cuint32_value\x18\x07 \x01(\r\x12\x16\n\x0esfixed32_value\x18\x08 \x01(\x0f\x12\x16\n\x0esfixed64_value\x18\t \x01(\x10\x12\x12\n\nbool_value\x18\n \x01(\x08\x12\x13\n\x0b\x66loat_value\x18\x0b \x01(\x02\x12\x14\n\x0c\x64ouble_value\x18\x0c \x01(\x01\x12\x14\n\x0cstring_value\x18\r \x01(\t\x12\x13\n\x0b\x62ytes_value\x18\x0e \x01(\x0c\x12,\n\x06status\x18\x0f \x01(\x0e\x32\x1c.helloworld.DTRequest.Status\x12H\n\x13string_to_int32_map\x18\x10 \x03(\x0b\x32+.helloworld.DTRequest.StringToInt32MapEntry\x12H\n\x13int32_to_string_map\x18\x11 \x03(\x0b\x32+.helloworld.DTRequest.Int32ToStringMapEntry\x1a\x37\n\x15StringToInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x37\n\x15Int32ToStringMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"(\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02OK\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"\x1b\n\nDTResponse\x12\r\n\x05value\x18\x01 \x01(\x08*&\n\x08\x65numtype\x12\x05\n\x01\x41\x10\x00\x12\x05\n\x01\x42\x10\x01\x12\x05\n\x01\x43\x10\x02\x12\x05\n\x01\x44\x10\x03\x32\xfc\x02\n\x07Greeter\x12@\n\x08SayHello\x12\x18.helloworld.HelloRequest\x1a\x18.helloworld.HelloReponse\"\x00\x12P\n\x16SayHelloStreamResponse\x12\x18.helloworld.HelloRequest\x1a\x18.helloworld.HelloReponse\"\x00\x30\x01\x12O\n\x15SayHelloStreamRequest\x12\x18.helloworld.HelloRequest\x1a\x18.helloworld.HelloReponse\"\x00(\x01\x12N\n\x12SayHelloBidiStream\x12\x18.helloworld.HelloRequest\x1a\x18.helloworld.HelloReponse\"\x00(\x01\x30\x01\x12<\n\tDataTypes\x12\x15.helloworld.DTRequest\x1a\x16.helloworld.DTResponse\"\x00\x62\x06proto3'
)

_ENUMTYPE = _descriptor.EnumDescriptor(
  name='enumtype',
  full_name='helloworld.enumtype',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='A', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='B', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='C', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='D', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=796,
  serialized_end=834,
)
_sym_db.RegisterEnumDescriptor(_ENUMTYPE)

enumtype = enum_type_wrapper.EnumTypeWrapper(_ENUMTYPE)
A = 0
B = 1
C = 2
D = 3


_DTREQUEST_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='helloworld.DTRequest.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=725,
  serialized_end=765,
)
_sym_db.RegisterEnumDescriptor(_DTREQUEST_STATUS)


_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='helloworld.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='helloworld.HelloRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=60,
)


_HELLOREPONSE = _descriptor.Descriptor(
  name='HelloReponse',
  full_name='helloworld.HelloReponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='helloworld.HelloReponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=93,
)


_DTREQUEST_STRINGTOINT32MAPENTRY = _descriptor.Descriptor(
  name='StringToInt32MapEntry',
  full_name='helloworld.DTRequest.StringToInt32MapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='helloworld.DTRequest.StringToInt32MapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='helloworld.DTRequest.StringToInt32MapEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=611,
  serialized_end=666,
)

_DTREQUEST_INT32TOSTRINGMAPENTRY = _descriptor.Descriptor(
  name='Int32ToStringMapEntry',
  full_name='helloworld.DTRequest.Int32ToStringMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='helloworld.DTRequest.Int32ToStringMapEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='helloworld.DTRequest.Int32ToStringMapEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=668,
  serialized_end=723,
)

_DTREQUEST = _descriptor.Descriptor(
  name='DTRequest',
  full_name='helloworld.DTRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='int32_value', full_name='helloworld.DTRequest.int32_value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sint32_value', full_name='helloworld.DTRequest.sint32_value', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fixed32_value', full_name='helloworld.DTRequest.fixed32_value', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int64_value', full_name='helloworld.DTRequest.int64_value', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sint64_value', full_name='helloworld.DTRequest.sint64_value', index=4,
      number=5, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fixed64_value', full_name='helloworld.DTRequest.fixed64_value', index=5,
      number=6, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uint32_value', full_name='helloworld.DTRequest.uint32_value', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sfixed32_value', full_name='helloworld.DTRequest.sfixed32_value', index=7,
      number=8, type=15, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sfixed64_value', full_name='helloworld.DTRequest.sfixed64_value', index=8,
      number=9, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='helloworld.DTRequest.bool_value', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='helloworld.DTRequest.float_value', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='helloworld.DTRequest.double_value', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='helloworld.DTRequest.string_value', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bytes_value', full_name='helloworld.DTRequest.bytes_value', index=13,
      number=14, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='helloworld.DTRequest.status', index=14,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_to_int32_map', full_name='helloworld.DTRequest.string_to_int32_map', index=15,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int32_to_string_map', full_name='helloworld.DTRequest.int32_to_string_map', index=16,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DTREQUEST_STRINGTOINT32MAPENTRY, _DTREQUEST_INT32TOSTRINGMAPENTRY, ],
  enum_types=[
    _DTREQUEST_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=765,
)


_DTRESPONSE = _descriptor.Descriptor(
  name='DTResponse',
  full_name='helloworld.DTResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='helloworld.DTResponse.value', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=767,
  serialized_end=794,
)

_DTREQUEST_STRINGTOINT32MAPENTRY.containing_type = _DTREQUEST
_DTREQUEST_INT32TOSTRINGMAPENTRY.containing_type = _DTREQUEST
_DTREQUEST.fields_by_name['status'].enum_type = _DTREQUEST_STATUS
_DTREQUEST.fields_by_name['string_to_int32_map'].message_type = _DTREQUEST_STRINGTOINT32MAPENTRY
_DTREQUEST.fields_by_name['int32_to_string_map'].message_type = _DTREQUEST_INT32TOSTRINGMAPENTRY
_DTREQUEST_STATUS.containing_type = _DTREQUEST
DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReponse'] = _HELLOREPONSE
DESCRIPTOR.message_types_by_name['DTRequest'] = _DTREQUEST
DESCRIPTOR.message_types_by_name['DTResponse'] = _DTRESPONSE
DESCRIPTOR.enum_types_by_name['enumtype'] = _ENUMTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReponse = _reflection.GeneratedProtocolMessageType('HelloReponse', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPONSE,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloReponse)
  })
_sym_db.RegisterMessage(HelloReponse)

DTRequest = _reflection.GeneratedProtocolMessageType('DTRequest', (_message.Message,), {

  'StringToInt32MapEntry' : _reflection.GeneratedProtocolMessageType('StringToInt32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _DTREQUEST_STRINGTOINT32MAPENTRY,
    '__module__' : 'helloworld_pb2'
    # @@protoc_insertion_point(class_scope:helloworld.DTRequest.StringToInt32MapEntry)
    })
  ,

  'Int32ToStringMapEntry' : _reflection.GeneratedProtocolMessageType('Int32ToStringMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _DTREQUEST_INT32TOSTRINGMAPENTRY,
    '__module__' : 'helloworld_pb2'
    # @@protoc_insertion_point(class_scope:helloworld.DTRequest.Int32ToStringMapEntry)
    })
  ,
  'DESCRIPTOR' : _DTREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.DTRequest)
  })
_sym_db.RegisterMessage(DTRequest)
_sym_db.RegisterMessage(DTRequest.StringToInt32MapEntry)
_sym_db.RegisterMessage(DTRequest.Int32ToStringMapEntry)

DTResponse = _reflection.GeneratedProtocolMessageType('DTResponse', (_message.Message,), {
  'DESCRIPTOR' : _DTRESPONSE,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.DTResponse)
  })
_sym_db.RegisterMessage(DTResponse)


_DTREQUEST_STRINGTOINT32MAPENTRY._options = None
_DTREQUEST_INT32TOSTRINGMAPENTRY._options = None

_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='helloworld.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=837,
  serialized_end=1217,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='helloworld.Greeter.SayHello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SayHelloStreamResponse',
    full_name='helloworld.Greeter.SayHelloStreamResponse',
    index=1,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SayHelloStreamRequest',
    full_name='helloworld.Greeter.SayHelloStreamRequest',
    index=2,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SayHelloBidiStream',
    full_name='helloworld.Greeter.SayHelloBidiStream',
    index=3,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DataTypes',
    full_name='helloworld.Greeter.DataTypes',
    index=4,
    containing_service=None,
    input_type=_DTREQUEST,
    output_type=_DTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
