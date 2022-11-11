graph = [
    ("house", "school"), ("house", "church"), ("house", "bar"), ("church", "bar"), ("church", "cinema"),
         ("bar", "hospital"), ("hospital", "theater"), ("hospital", "cinema"),
    (" school", "house",), ("church", "house",), ("bar", "house",), ("bar", "church",), ("cinema", "church",),
    ("hospital", "bar", ), ("theater", "hospital",), ("cinema", "hospital",)

]
for edge in graph:
    start, end = edge
    print(start, "---", end)

# for i in graph:
#     for u in i:
#         if u == i[1]:
#             pass
#         else:
#             print(u, "-", i[1])


