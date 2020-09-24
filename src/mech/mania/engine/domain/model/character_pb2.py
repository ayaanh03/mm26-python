# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: character.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from . import item_pb2 as item__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='character.proto',
  package='character',
  syntax='proto3',
  serialized_options=b'\n\036mech.mania.engine.domain.modelB\017CharacterProtos\252\002\016MM26.IO.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x63haracter.proto\x12\tcharacter\x1a\nitem.proto\"\xe9\x04\n\tCharacter\x12\x16\n\x0e\x63urrent_health\x18\x01 \x01(\x05\x12\x17\n\x0f\x62\x61se_max_health\x18\x02 \x01(\x05\x12\x12\n\nexperience\x18\x03 \x01(\x05\x12\r\n\x05level\x18\x04 \x01(\x05\x12\x12\n\nbase_speed\x18\x05 \x01(\x05\x12%\n\x08position\x18\x06 \x01(\x0b\x32\x13.character.Position\x12(\n\x0bspawn_point\x18\x07 \x01(\x0b\x32\x13.character.Position\x12\x1c\n\x06weapon\x18\x08 \x01(\x0b\x32\x0c.item.Weapon\x12\x45\n#active_effects_temp_status_modifier\x18\t \x03(\x0b\x32\x18.item.TempStatusModifier\x12\x1d\n\x15\x61\x63tive_effects_source\x18\n \x03(\t\x12 \n\x18\x61\x63tive_effects_is_player\x18\x0b \x03(\x08\x12L\n\x15tagged_players_damage\x18\x0c \x03(\x0b\x32-.character.Character.TaggedPlayersDamageEntry\x12\x0f\n\x07is_dead\x18\r \x01(\x08\x12\x19\n\x11ticks_since_death\x18\x0e \x01(\x05\x12\x0c\n\x04name\x18\x0f \x01(\t\x12\x13\n\x0b\x62\x61se_attack\x18\x10 \x01(\x05\x12\x14\n\x0c\x62\x61se_defense\x18\x11 \x01(\x05\x12\x0e\n\x06sprite\x18\x12 \x01(\t\x1a:\n\x18TaggedPlayersDamageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"b\n\x07Monster\x12\'\n\tcharacter\x18\x01 \x01(\x0b\x32\x14.character.Character\x12\x19\n\x05\x64rops\x18\x02 \x03(\x0b\x32\n.item.Item\x12\x13\n\x0b\x61ggro_range\x18\x03 \x01(\x05\"\xa4\x01\n\x06Player\x12\'\n\tcharacter\x18\x01 \x01(\x0b\x32\x14.character.Character\x12\x16\n\x03hat\x18\x02 \x01(\x0b\x32\t.item.Hat\x12\x1e\n\x07\x63lothes\x18\x03 \x01(\x0b\x32\r.item.Clothes\x12\x1a\n\x05shoes\x18\x04 \x01(\x0b\x32\x0b.item.Shoes\x12\x1d\n\tinventory\x18\x05 \x03(\x0b\x32\n.item.Item\"\xc6\x01\n\x0bPlayerStats\x12\r\n\x05level\x18\x01 \x01(\x05\x12\x12\n\nexperience\x18\x02 \x01(\x05\x12\x16\n\x0emonsters_slain\x18\x03 \x01(\x05\x12\x0e\n\x06\x61ttack\x18\x04 \x01(\x05\x12\x0f\n\x07\x64\x65\x66\x65nse\x18\x05 \x01(\x05\x12\x16\n\x0e\x63urrent_health\x18\x06 \x01(\x05\x12\x12\n\nmax_health\x18\x07 \x01(\x05\x12\x13\n\x0b\x64\x65\x61th_count\x18\x08 \x01(\x05\x12\x1a\n\x12turns_since_joined\x18\t \x01(\x05\"\x91\x01\n\x11PlayerStatsBundle\x12\x36\n\x05stats\x18\x01 \x03(\x0b\x32\'.character.PlayerStatsBundle.StatsEntry\x1a\x44\n\nStatsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.character.PlayerStats:\x02\x38\x01\"2\n\x08Position\x12\x10\n\x08\x62oard_id\x18\x01 \x01(\t\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05\"\x80\x01\n\x11\x43haracterDecision\x12.\n\rdecision_type\x18\x01 \x01(\x0e\x32\x17.character.DecisionType\x12,\n\x0ftarget_position\x18\x02 \x01(\x0b\x32\x13.character.Position\x12\r\n\x05index\x18\x03 \x01(\x05*[\n\x0c\x44\x65\x63isionType\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04MOVE\x10\x01\x12\n\n\x06\x41TTACK\x10\x02\x12\n\n\x06PORTAL\x10\x03\x12\x08\n\x04\x44ROP\x10\x04\x12\t\n\x05\x45QUIP\x10\x05\x12\n\n\x06PICKUP\x10\x06\x42\x42\n\x1emech.mania.engine.domain.modelB\x0f\x43haracterProtos\xaa\x02\x0eMM26.IO.Modelsb\x06proto3'
  ,
  dependencies=[item__pb2.DESCRIPTOR, ])

_DECISIONTYPE = _descriptor.EnumDescriptor(
  name='DecisionType',
  full_name='character.DecisionType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MOVE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ATTACK', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PORTAL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DROP', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EQUIP', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PICKUP', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1461,
  serialized_end=1552,
)
_sym_db.RegisterEnumDescriptor(_DECISIONTYPE)

DecisionType = enum_type_wrapper.EnumTypeWrapper(_DECISIONTYPE)
NONE = 0
MOVE = 1
ATTACK = 2
PORTAL = 3
DROP = 4
EQUIP = 5
PICKUP = 6



_CHARACTER_TAGGEDPLAYERSDAMAGEENTRY = _descriptor.Descriptor(
  name='TaggedPlayersDamageEntry',
  full_name='character.Character.TaggedPlayersDamageEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='character.Character.TaggedPlayersDamageEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='character.Character.TaggedPlayersDamageEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
  serialized_start=602,
  serialized_end=660,
)

_CHARACTER = _descriptor.Descriptor(
  name='Character',
  full_name='character.Character',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_health', full_name='character.Character.current_health', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_max_health', full_name='character.Character.base_max_health', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='experience', full_name='character.Character.experience', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='character.Character.level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_speed', full_name='character.Character.base_speed', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='position', full_name='character.Character.position', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spawn_point', full_name='character.Character.spawn_point', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='weapon', full_name='character.Character.weapon', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active_effects_temp_status_modifier', full_name='character.Character.active_effects_temp_status_modifier',
      index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active_effects_source', full_name='character.Character.active_effects_source', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active_effects_is_player', full_name='character.Character.active_effects_is_player', index=10,
      number=11, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tagged_players_damage', full_name='character.Character.tagged_players_damage', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_dead', full_name='character.Character.is_dead', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ticks_since_death', full_name='character.Character.ticks_since_death', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='character.Character.name', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_attack', full_name='character.Character.base_attack', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_defense', full_name='character.Character.base_defense', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sprite', full_name='character.Character.sprite', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CHARACTER_TAGGEDPLAYERSDAMAGEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=660,
)


_MONSTER = _descriptor.Descriptor(
  name='Monster',
  full_name='character.Monster',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='character', full_name='character.Monster.character', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='drops', full_name='character.Monster.drops', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aggro_range', full_name='character.Monster.aggro_range', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
  serialized_start=662,
  serialized_end=760,
)


_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='character.Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='character', full_name='character.Player.character', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hat', full_name='character.Player.hat', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clothes', full_name='character.Player.clothes', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shoes', full_name='character.Player.shoes', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inventory', full_name='character.Player.inventory', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
  serialized_start=763,
  serialized_end=927,
)


_PLAYERSTATS = _descriptor.Descriptor(
  name='PlayerStats',
  full_name='character.PlayerStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='character.PlayerStats.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='experience', full_name='character.PlayerStats.experience', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='monsters_slain', full_name='character.PlayerStats.monsters_slain', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attack', full_name='character.PlayerStats.attack', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='defense', full_name='character.PlayerStats.defense', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current_health', full_name='character.PlayerStats.current_health', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_health', full_name='character.PlayerStats.max_health', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='death_count', full_name='character.PlayerStats.death_count', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='turns_since_joined', full_name='character.PlayerStats.turns_since_joined', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
  serialized_start=930,
  serialized_end=1128,
)


_PLAYERSTATSBUNDLE_STATSENTRY = _descriptor.Descriptor(
  name='StatsEntry',
  full_name='character.PlayerStatsBundle.StatsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='character.PlayerStatsBundle.StatsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='character.PlayerStatsBundle.StatsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
  serialized_start=1208,
  serialized_end=1276,
)

_PLAYERSTATSBUNDLE = _descriptor.Descriptor(
  name='PlayerStatsBundle',
  full_name='character.PlayerStatsBundle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stats', full_name='character.PlayerStatsBundle.stats', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PLAYERSTATSBUNDLE_STATSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1131,
  serialized_end=1276,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='character.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='board_id', full_name='character.Position.board_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='character.Position.x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='character.Position.y', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
  serialized_start=1278,
  serialized_end=1328,
)


_CHARACTERDECISION = _descriptor.Descriptor(
  name='CharacterDecision',
  full_name='character.CharacterDecision',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='decision_type', full_name='character.CharacterDecision.decision_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_position', full_name='character.CharacterDecision.target_position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index', full_name='character.CharacterDecision.index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
  serialized_start=1331,
  serialized_end=1459,
)

_CHARACTER_TAGGEDPLAYERSDAMAGEENTRY.containing_type = _CHARACTER
_CHARACTER.fields_by_name['position'].message_type = _POSITION
_CHARACTER.fields_by_name['spawn_point'].message_type = _POSITION
_CHARACTER.fields_by_name['weapon'].message_type = item__pb2._WEAPON
_CHARACTER.fields_by_name['active_effects_temp_status_modifier'].message_type = item__pb2._TEMPSTATUSMODIFIER
_CHARACTER.fields_by_name['tagged_players_damage'].message_type = _CHARACTER_TAGGEDPLAYERSDAMAGEENTRY
_MONSTER.fields_by_name['character'].message_type = _CHARACTER
_MONSTER.fields_by_name['drops'].message_type = item__pb2._ITEM
_PLAYER.fields_by_name['character'].message_type = _CHARACTER
_PLAYER.fields_by_name['hat'].message_type = item__pb2._HAT
_PLAYER.fields_by_name['clothes'].message_type = item__pb2._CLOTHES
_PLAYER.fields_by_name['shoes'].message_type = item__pb2._SHOES
_PLAYER.fields_by_name['inventory'].message_type = item__pb2._ITEM
_PLAYERSTATSBUNDLE_STATSENTRY.fields_by_name['value'].message_type = _PLAYERSTATS
_PLAYERSTATSBUNDLE_STATSENTRY.containing_type = _PLAYERSTATSBUNDLE
_PLAYERSTATSBUNDLE.fields_by_name['stats'].message_type = _PLAYERSTATSBUNDLE_STATSENTRY
_CHARACTERDECISION.fields_by_name['decision_type'].enum_type = _DECISIONTYPE
_CHARACTERDECISION.fields_by_name['target_position'].message_type = _POSITION
DESCRIPTOR.message_types_by_name['Character'] = _CHARACTER
DESCRIPTOR.message_types_by_name['Monster'] = _MONSTER
DESCRIPTOR.message_types_by_name['Player'] = _PLAYER
DESCRIPTOR.message_types_by_name['PlayerStats'] = _PLAYERSTATS
DESCRIPTOR.message_types_by_name['PlayerStatsBundle'] = _PLAYERSTATSBUNDLE
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['CharacterDecision'] = _CHARACTERDECISION
DESCRIPTOR.enum_types_by_name['DecisionType'] = _DECISIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Character = _reflection.GeneratedProtocolMessageType('Character', (_message.Message,), {

  'TaggedPlayersDamageEntry' : _reflection.GeneratedProtocolMessageType('TaggedPlayersDamageEntry', (_message.Message,), {
    'DESCRIPTOR' : _CHARACTER_TAGGEDPLAYERSDAMAGEENTRY,
    '__module__' : 'character_pb2'
    # @@protoc_insertion_point(class_scope:character.Character.TaggedPlayersDamageEntry)
    })
  ,
  'DESCRIPTOR' : _CHARACTER,
  '__module__' : 'character_pb2'
  # @@protoc_insertion_point(class_scope:character.Character)
  })
_sym_db.RegisterMessage(Character)
_sym_db.RegisterMessage(Character.TaggedPlayersDamageEntry)

Monster = _reflection.GeneratedProtocolMessageType('Monster', (_message.Message,), {
  'DESCRIPTOR' : _MONSTER,
  '__module__' : 'character_pb2'
  # @@protoc_insertion_point(class_scope:character.Monster)
  })
_sym_db.RegisterMessage(Monster)

Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), {
  'DESCRIPTOR' : _PLAYER,
  '__module__' : 'character_pb2'
  # @@protoc_insertion_point(class_scope:character.Player)
  })
_sym_db.RegisterMessage(Player)

PlayerStats = _reflection.GeneratedProtocolMessageType('PlayerStats', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERSTATS,
  '__module__' : 'character_pb2'
  # @@protoc_insertion_point(class_scope:character.PlayerStats)
  })
_sym_db.RegisterMessage(PlayerStats)

PlayerStatsBundle = _reflection.GeneratedProtocolMessageType('PlayerStatsBundle', (_message.Message,), {

  'StatsEntry' : _reflection.GeneratedProtocolMessageType('StatsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PLAYERSTATSBUNDLE_STATSENTRY,
    '__module__' : 'character_pb2'
    # @@protoc_insertion_point(class_scope:character.PlayerStatsBundle.StatsEntry)
    })
  ,
  'DESCRIPTOR' : _PLAYERSTATSBUNDLE,
  '__module__' : 'character_pb2'
  # @@protoc_insertion_point(class_scope:character.PlayerStatsBundle)
  })
_sym_db.RegisterMessage(PlayerStatsBundle)
_sym_db.RegisterMessage(PlayerStatsBundle.StatsEntry)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'character_pb2'
  # @@protoc_insertion_point(class_scope:character.Position)
  })
_sym_db.RegisterMessage(Position)

CharacterDecision = _reflection.GeneratedProtocolMessageType('CharacterDecision', (_message.Message,), {
  'DESCRIPTOR' : _CHARACTERDECISION,
  '__module__' : 'character_pb2'
  # @@protoc_insertion_point(class_scope:character.CharacterDecision)
  })
_sym_db.RegisterMessage(CharacterDecision)


DESCRIPTOR._options = None
_CHARACTER_TAGGEDPLAYERSDAMAGEENTRY._options = None
_PLAYERSTATSBUNDLE_STATSENTRY._options = None
# @@protoc_insertion_point(module_scope)
