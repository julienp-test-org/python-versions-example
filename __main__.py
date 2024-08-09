"""A Python Pulumi program"""

import pulumi
import sys

v = sys.version_info

pulumi.export("version", f"{v.major}.{v.minor}.{v.micro}")
