import re

with open(r'C:\Users\user\.gemini\antigravity-ide\brain\f1a8339b-3f7b-4a25-b0bf-fb087dd75fab\.system_generated\steps\5337\content.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

out = []
started = False

for line in lines:
    match = re.match(r'^\d+:\s?(.*)$', line)
    if match:
        content = match.group(1)
        if '<!DOCTYPE html>' in content:
            started = True
        if started:
            out.append(content)

with open(r'C:\Users\user\Downloads\paysonism_clone\index.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
