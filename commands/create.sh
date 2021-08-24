#!/bin/bash

for ITEM in $(ls)
do
  touch "$ITEM/$ITEM.py"
  touch "$ITEM/__init__.py"
done