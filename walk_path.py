#! /usr/bin/env python3

import sys
import os
import json
import hashlib

def sha256sum(filename):
  h  = hashlib.sha256()
  b  = bytearray(128*1024)
  mv = memoryview(b)
  with open(filename, 'rb', buffering=0) as f:
    while n := f.readinto(mv):
      h.update(mv[:n])
  return h.hexdigest()

if len(sys.argv) >= 3:
  data_path = sys.argv[1]
  walk_path = sys.argv[2]
else:
  exit(0)

with open(data_path, 'r') as f:
  d = json.load(f)

#print(f'{d}')
#for e in d:
#  print(f'{e["hash"]}')
#  n = [i for i in d if i["hash"] == "0820eb8eea90408047e3715424bc6be771417047f683950fecb4bdd2e2cbbc6e"]
#  print(f'vu sayse {n}')


for root, dirs, files in os.walk(walk_path, topdown=True, followlinks=False):
  for name in files:
    if os.path.islink(os.path.join(root, name)):
      continue
    #print(os.path.join(root, name))
    #print(f'{sha256sum(os.path.join(root, name))}')
    h = sha256sum(os.path.join(root, name))
    #i = next((item for item in d if item["hash"] == h), None)
    i = next((i for i, item in enumerate(d) if item["hash"] == h), None)
    #if i:
    #  print(f'{d[i]}')
    #  continue
    if i == None:
      print(f'INFO: File "{os.path.join(root, name)}" with digest "{h}" not found in results!')

 #for name in dirs:
 #   print(os.path.join(root, name))
