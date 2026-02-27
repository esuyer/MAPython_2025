print("\nQuestion 1\n")
def transform_text(text):
    res = text.replace('a', 'z')
    res = res.replace('A', 'z')
    return res

print(transform_text('pkAirea'))

print("\nQuestion 2\n")
k_text = "Kazuya_Mishima_Wins"
k_list = list(k_text)

for i in range(len(k_list)):
    if i % 2 == 0:
        k_list[i] = "."

print("".join(k_list))
