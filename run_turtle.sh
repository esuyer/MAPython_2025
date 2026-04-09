#!/bin/bash
export PYTHONPATH="/nix/store/pjn7rx1d3jnjsif6wnz5im0fdm8pp7xa-python3-3.11.13/lib/python3.11/lib-dynload:$PYTHONPATH"
python3.11 "$@"
