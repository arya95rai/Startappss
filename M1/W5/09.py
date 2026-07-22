# 9.
# Combine three dictionaries using ChainMap.
# Priority
# User
# ↓
# Company
# ↓
# System
from collections import ChainMap
User={
    "arya":1,
    "pehu":2
}
Company={
    "arya":"morgan",
    "pehu":"celine"
}
System={
    "finance":"arya",
    "fashion":"pehu"
}
cm=ChainMap(User,Company,System)
print(cm["arya"])
print(dict(cm))
