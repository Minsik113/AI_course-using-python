# 1157번
name = input()
code_a = ord("a")
code_z = ord("z")
cnt = [0 for i in range(0,52)]

print(cnt)

for ch in name:
    code_ch = ord(ch)
    if code_a <= code_ch and code_z <= code_ch:
        index = code_ch - code_a
        cnt[index] += 1

print(cnt)