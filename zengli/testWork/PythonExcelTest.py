# 使用Python对EXCEL表格进行处理
# 参考：http://www.jb51.net/article/77626.htm
# http://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html
# http://blog.csdn.net/xiaoputao0903/article/details/25633513
import xlrd #用来读取excel文件,不能修改数据
import xlwt #创建Excel文件并对其进行操作，但不能对已有的Excel文件进行修改
import xlutils #对已有的Excel文件进行修改
#
# 模块的安装
# 笔者使用anaconda来管理python的各个包，因此要安装可以直接在命令行界面中使用如下代码

# conda install xlrd
# conda install xlwt
# conda install xlutils

# 当然，也可以使用pip安装或者直接去官网找package安装包
# 分析excel文件的层级对象
# 要读取excel的数据，就要了解excel的结构，根据excel的结构一层一层的去读取数据。

# excel有三层级对象，workbook，sheet，和cell。一个excel文件就是一个workbook，所以在最初我们必须要打开这个excel文件，也就是workbook。sheet我们都很熟悉，就是表，我们都知道一个excel文件有时候会有很多的表，所以我们必须要选择是读取哪个表的数据，最后才是cell，cell其实就是格子，excel的表格就是一个二维数组，cell就是这个表格中的最小单元，也就是我们读取数据存储的地方。
#
# xlrd部分
# 打开Excel文件读取内容

workbook= xlrd.open_workbook('excelFile.xls')

# 抓取所有sheet页的名称

worksheets = workbook.sheet_names()

# 获取工作表

table = workbook.sheets()[0]          #通过索引顺序获取
table = workbook.sheet_by_index(0)    #通过索引顺序获取
table = workbook.sheet_by_name(u'Sheet1') #通过名称获取

# 获取整行和整列的值（数组）

# table.row_values(i)
# table.col_values(i)

# 获取行数和列数

nrows = table.nrows
ncols = table.ncols

# 读取单元格数据

cell_A2 = table.cell(0,1).value
cell_A2 = table.cell_value(0,1)
cell_A2 = table.row(0)[1].value #使用行索引
cell_A2 = table.col(1)[0].value #使用列索引

# 获取单元格中值的类型

# cell_type = table.cell_type(rown,coln)

# xlwt部分
# 创建workbook和sheet对象

workbook = xlwt.Workbook(encoding = 'ascii') #注意Workbook的开头W要大写
sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
sheet2 = workbook.add_sheet('sheet2',cell_overwrite_ok=True)


# 向sheet页中写入数据

sheet1.write(0,0,'this should overwrite1')
sheet1.write(0,1,'1111111111111111')
sheet2.write(0,0,'this should overwrite2')
sheet2.write(1,2,'2222222222222222')

# 使用样式

#初始化样式
style = xlwt.XFStyle()
#为样式创建字体
font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True
#设置样式的字体
style.font = font
#使用样式
sheet1.write(0,1,'some bold Times text',style)

# 保存该excel文件,有同名文件时直接覆盖

workbook.save('E:\\Code\\Python\\test2.xls')

# xlutils部分
# 打开一个workbook

readbook = xlrd.open_workbook('test.xls')
workbook= xlutils.copy.copy(readbook)

# 获取sheet对象，通过sheet_by_index()获取的sheet对象没有write()方法

writesheet= workbook.get_sheet(0)

# 写入数据

writesheet.write(1, 1, 'changed!')

# 添加sheet页

workbook.add_sheet('sheetnnn2',cell_overwrite_ok=True)
1
# 保存该Excel文件，利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变

workbook.save('test.xls')