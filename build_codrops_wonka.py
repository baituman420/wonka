import re

with open('public/assets/logos/wonka-top-hat.svg', 'r', encoding='utf-8') as f:
    svg_hat_raw = f.read().strip()

svg_hat = re.sub(r'<\?xml[^>]*\?>', '', svg_hat_raw).strip()

with open('build_theatrical_wonka.py', 'r', encoding='utf-8') as f:
    orig_code = f.read()

print("Original build script length:", len(orig_code))
