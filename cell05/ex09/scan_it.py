import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    key = sys.argv[1]
    text = sys.argv[2]

    matches = re.findall(rf"\b{re.escape(key)}\b", text)

    print(len(matches) if matches else "none")