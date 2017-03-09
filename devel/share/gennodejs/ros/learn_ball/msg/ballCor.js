// Auto-generated. Do not edit!

// (in-package learn_ball.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ballCor {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.heading = null;
      this.color = null;
      this.x = null;
      this.y = null;
      this.radius = null;
      this.upperH = null;
      this.upperS = null;
      this.upperV = null;
      this.lowerH = null;
      this.lowerS = null;
      this.lowerV = null;
    }
    else {
      if (initObj.hasOwnProperty('heading')) {
        this.heading = initObj.heading
      }
      else {
        this.heading = '';
      }
      if (initObj.hasOwnProperty('color')) {
        this.color = initObj.color
      }
      else {
        this.color = '';
      }
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = 0;
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = 0;
      }
      if (initObj.hasOwnProperty('radius')) {
        this.radius = initObj.radius
      }
      else {
        this.radius = 0;
      }
      if (initObj.hasOwnProperty('upperH')) {
        this.upperH = initObj.upperH
      }
      else {
        this.upperH = 0;
      }
      if (initObj.hasOwnProperty('upperS')) {
        this.upperS = initObj.upperS
      }
      else {
        this.upperS = 0;
      }
      if (initObj.hasOwnProperty('upperV')) {
        this.upperV = initObj.upperV
      }
      else {
        this.upperV = 0;
      }
      if (initObj.hasOwnProperty('lowerH')) {
        this.lowerH = initObj.lowerH
      }
      else {
        this.lowerH = 0;
      }
      if (initObj.hasOwnProperty('lowerS')) {
        this.lowerS = initObj.lowerS
      }
      else {
        this.lowerS = 0;
      }
      if (initObj.hasOwnProperty('lowerV')) {
        this.lowerV = initObj.lowerV
      }
      else {
        this.lowerV = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ballCor
    // Serialize message field [heading]
    bufferOffset = _serializer.string(obj.heading, buffer, bufferOffset);
    // Serialize message field [color]
    bufferOffset = _serializer.string(obj.color, buffer, bufferOffset);
    // Serialize message field [x]
    bufferOffset = _serializer.int64(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = _serializer.int64(obj.y, buffer, bufferOffset);
    // Serialize message field [radius]
    bufferOffset = _serializer.int64(obj.radius, buffer, bufferOffset);
    // Serialize message field [upperH]
    bufferOffset = _serializer.int64(obj.upperH, buffer, bufferOffset);
    // Serialize message field [upperS]
    bufferOffset = _serializer.int64(obj.upperS, buffer, bufferOffset);
    // Serialize message field [upperV]
    bufferOffset = _serializer.int64(obj.upperV, buffer, bufferOffset);
    // Serialize message field [lowerH]
    bufferOffset = _serializer.int64(obj.lowerH, buffer, bufferOffset);
    // Serialize message field [lowerS]
    bufferOffset = _serializer.int64(obj.lowerS, buffer, bufferOffset);
    // Serialize message field [lowerV]
    bufferOffset = _serializer.int64(obj.lowerV, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ballCor
    let len;
    let data = new ballCor(null);
    // Deserialize message field [heading]
    data.heading = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [color]
    data.color = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [x]
    data.x = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [radius]
    data.radius = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [upperH]
    data.upperH = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [upperS]
    data.upperS = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [upperV]
    data.upperV = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [lowerH]
    data.lowerH = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [lowerS]
    data.lowerS = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [lowerV]
    data.lowerV = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.heading.length;
    length += object.color.length;
    return length + 80;
  }

  static datatype() {
    // Returns string type for a message object
    return 'learn_ball/ballCor';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a81fb488530784a24d84e3f7199f24f6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string heading
    string color
    int64 x
    int64 y
    int64 radius
    int64 upperH
    int64 upperS
    int64 upperV
    int64 lowerH
    int64 lowerS
    int64 lowerV
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ballCor(null);
    if (msg.heading !== undefined) {
      resolved.heading = msg.heading;
    }
    else {
      resolved.heading = ''
    }

    if (msg.color !== undefined) {
      resolved.color = msg.color;
    }
    else {
      resolved.color = ''
    }

    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = 0
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = 0
    }

    if (msg.radius !== undefined) {
      resolved.radius = msg.radius;
    }
    else {
      resolved.radius = 0
    }

    if (msg.upperH !== undefined) {
      resolved.upperH = msg.upperH;
    }
    else {
      resolved.upperH = 0
    }

    if (msg.upperS !== undefined) {
      resolved.upperS = msg.upperS;
    }
    else {
      resolved.upperS = 0
    }

    if (msg.upperV !== undefined) {
      resolved.upperV = msg.upperV;
    }
    else {
      resolved.upperV = 0
    }

    if (msg.lowerH !== undefined) {
      resolved.lowerH = msg.lowerH;
    }
    else {
      resolved.lowerH = 0
    }

    if (msg.lowerS !== undefined) {
      resolved.lowerS = msg.lowerS;
    }
    else {
      resolved.lowerS = 0
    }

    if (msg.lowerV !== undefined) {
      resolved.lowerV = msg.lowerV;
    }
    else {
      resolved.lowerV = 0
    }

    return resolved;
    }
};

module.exports = ballCor;
