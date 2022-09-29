#!/usr/bin/env python3

#Code based off lab demo

import os, json

#empty dict
env = {}

#go through env vars and put them in the env dict
for env_key, env_val in os.environ.items():
    env[env_key] = env_val

print("Content-Type: application/json")
print()

print(json.dumps(env))