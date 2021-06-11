files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
result = []

# 1) 일반함수
def selectfile(files):
    for file in files:
        if ".jpg" in file or '.png' in file:
            result.append(file)
    return result
selectfile(files)
print(result)

# 2) lambda사용
print(list(filter(lambda x: '.jpg' in x or '.png' in x, files)))
