# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from turtle_control/kf.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class kf(genpy.Message):
  _md5sum = "0d726d72060def9671484e9bd7b7c259"
  _type = "turtle_control/kf"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float32 x_kf
float32 x_odom
float32 x_sensor
float32 x_sensor_var"""
  __slots__ = ['x_kf','x_odom','x_sensor','x_sensor_var']
  _slot_types = ['float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x_kf,x_odom,x_sensor,x_sensor_var

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(kf, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.x_kf is None:
        self.x_kf = 0.
      if self.x_odom is None:
        self.x_odom = 0.
      if self.x_sensor is None:
        self.x_sensor = 0.
      if self.x_sensor_var is None:
        self.x_sensor_var = 0.
    else:
      self.x_kf = 0.
      self.x_odom = 0.
      self.x_sensor = 0.
      self.x_sensor_var = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_4f().pack(_x.x_kf, _x.x_odom, _x.x_sensor, _x.x_sensor_var))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.x_kf, _x.x_odom, _x.x_sensor, _x.x_sensor_var,) = _get_struct_4f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_4f().pack(_x.x_kf, _x.x_odom, _x.x_sensor, _x.x_sensor_var))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.x_kf, _x.x_odom, _x.x_sensor, _x.x_sensor_var,) = _get_struct_4f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4f = None
def _get_struct_4f():
    global _struct_4f
    if _struct_4f is None:
        _struct_4f = struct.Struct("<4f")
    return _struct_4f
