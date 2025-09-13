temp=eval(input('请输入温度：'))
sort=input('请输入该温度类型（输入大写的C或者F）：')
if sort == 'F':
    sort_C=(temp-32)/1.8
    print('该温度的摄氏度是：',sort_C,'摄氏度')
else:
    sort_F=temp*1.8+32
    print('该温度的华氏度是：',sort_F,'华氏度')



