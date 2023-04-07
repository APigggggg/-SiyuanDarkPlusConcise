import os
# 转换一下深色主题
f1 = open('custom-dark.css','r')
f2 = open('custom.css','r')
out = open('converted-dark.txt','w')
lines1 = f1.readlines()
lines2 = f2.readlines()

for i in lines1:
    out.write(i.split('\n')[0])
    out.write('\\n')
for i in lines2:
    out.write(i.split('\n')[0])
    out.write('\\n')
f1.close()
f2.close()
out.close()

# 转换一下浅色主题
f1 = open('custom-light.css','r')
f2 = open('custom.css','r')
out = open('converted-light.txt','w')
lines1 = f1.readlines()
lines2 = f2.readlines()

for i in lines1:
    out.write(i.split('\n')[0])
    out.write('\\n')
for i in lines2:
    out.write(i.split('\n')[0])
    out.write('\\n')
f1.close()
f2.close()
out.close()

# 合并成main.js
f = open('main_template.js','r')
lines = f.readlines()

lines[8]  = "            elementStyle.appendChild(document.createTextNode('"+open('converted-dark.txt','r').readline() +"'));\n" 
lines[14] = "            elementStyle.appendChild(document.createTextNode('"+open('converted-light.txt','r').readline()+"'));\n" 
out = open('main.js','w')
for i in lines:
    out.write(i)

os.system('rm converted-light.txt converted-dark.txt')
