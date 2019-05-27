#ifndef _CACHE_H_
#define _CACHE_H_

#include <stdio.h>
#include <string>
#include <map>

#include <v8.h>
#include <node.h>
#include <nan.h>

#include <defines.h>

using namespace v8;
using namespace node;

namespace cache {

extern std::map<std::string, std::string> items;

NAN_METHOD(Get);
NAN_METHOD(Set);
Local<Object> Initialize(Isolate *isolate);
  
};

#endif