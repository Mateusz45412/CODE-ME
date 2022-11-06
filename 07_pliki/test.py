


# items = ['tent', 'money', 'bag']
# with open('save.txt', mode='a') as f:
#     for i in items:
#         f.write(i)
#         f.write('\n')



items = ['tent', 'money', 'bag']
with open('save.txt', mode='a') as f:
        f.write('\t'.join(items))