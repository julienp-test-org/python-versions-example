"""A Python Pulumi program"""

import pulumi
import sys

pulumi.export("version", sys.version)
