import xlrd
import pymysql


wb = xlrd.open_workbook('C:\\Users\\admin\Desktop\\loadconfig测试数据.xlsx')
sh1 = wb.sheet_by_index(0)
# print(sh1.nrows, sh1.ncols)
nrows=sh1.nrows       #  行数
res=''
for a in range(1,nrows):
    b=sh1.row_values(a)    # 获取每一行数据的列表
    # print(b[2])
    c=b[2].split('    ')
    # print(c)
    # print(type(b[2]))
    if a==nrows-1:
        s='''('%s', '%s', 1, 0, '%s', '2022-10-01 12:00:00','%s', 4, '2022-10-01 12:00:00');'''%(b[0],b[1],c[0],c[1])
    else:
        s='''('%s', '%s', 1, 0, '%s', '2022-10-01 12:00:00','%s', 4, '2022-10-01 12:00:00'),'''%(b[0],b[1],c[0],c[1])
    res=res+s     # 生成sql的values
sql = '''INSERT INTO `ipvacloud`.`site_camera_map_history` 
(`SiteId`, `CameraId`, `Direction`, `IsVirtual`, `CreateTime`, `ModifiedTime`,`DeleteTime`, `Source`, `lastUpdateTime`)
    VALUES
    '''+res
print(sql)
coon = pymysql.connect(host='192.168.2.226',
                        user='root',
                        passwd='winner@001',
                        port=3306,
                        db='ipvacloud')       # 连接数据库
cur = coon.cursor()
cur.execute(sql)
coon.commit()
# data=cur.fetchall()
# for i in data[:5]:
#     print(i)
cur.close()
coon.close()




