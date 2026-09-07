import json, re

# Inspect Stull chapters
with open('data/stull-data.js', 'r', encoding='utf-8') as f:
    stull = json.loads(f.read()[f.read().find('['):f.read().rfind(']')+1])

print("--- STULL CAP 6 ---")
c6 = next(c for c in stull if c['number'] == 6)
idx = c6['summary'].find('$$')
print(c6['summary'][max(0, idx-100):min(len(c6['summary']), idx+200)])

print("\n--- STULL CAP 9 ---")
c9 = next(c for c in stull if c['number'] == 9)
idx = c9['summary'].find('$$')
print(c9['summary'][max(0, idx-100):min(len(c9['summary']), idx+200)])

print("\n--- STULL CAP 10 ---")
c10 = next(c for c in stull if c['number'] == 10)
idx = c10['summary'].find('$$')
print(c10['summary'][max(0, idx-100):min(len(c10['summary']), idx+300)])

print("\n--- STULL CAP 23 ---")
c23 = next(c for c in stull if c['number'] == 23)
idx = c23['summary'].find('$$')
print(c23['summary'][max(0, idx-100):min(len(c23['summary']), idx+200)])
