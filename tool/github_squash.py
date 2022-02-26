#!/usr/bin/env python

"""
Squash github commits starting from a point
"""

from devrepo import shell

point = "c74017277bf409c2fafaf71cbe0672acd8fcc360"
message = "Develop"

shell(f"git reset --soft {point}")
shell(f"git add --all")
shell(f"git commit --message='{message}'")
shell(f"git push --force --follow-tags")
