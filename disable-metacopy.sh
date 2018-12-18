#!/bin/bash

# In linux 4.19, there is a problem in unionfs with metacopy that
# causes the package installation in the spark deps script to fail

# This will disable metacopy so that the script works

echo N | sudo tee /sys/module/overlay/parameters/metacopy
