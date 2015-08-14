#!/bin/bash

PORT=8001 venv/bin/sp -c examples/etc/spanky enroll -n api-nodes -H localhost python server.py &
PORT=8002 venv/bin/sp -c examples/etc/spanky enroll -n api-nodes -H localhost python server.py &
PORT=8003 venv/bin/sp -c examples/etc/spanky enroll -n api-nodes -H localhost python server.py &
