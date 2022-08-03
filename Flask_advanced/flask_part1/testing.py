from articles.dictionary import data

new_list = []
for item in data:
    if item['status'] == 'published':
        new_list.append(item)

print(new list)
