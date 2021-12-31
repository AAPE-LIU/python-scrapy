# xpath 是在XML文档中搜索内容的一门语言
# html是XML的一个子集
# XML中把html中被称为标签的东西称为节点
# 是根据节点路径进行查找的

from lxml import etree
xml = '''
<annotation>
	<folder>Img</folder>
	<filename>00001.bmp</filename>
	<path>./Img</path>
	<source>
		<database>Unknown</database>
	</source>
	<width>annotation_width</width>
	<size>
		<width>size_width</width>
		<height>1504</height>
		<depth>3</depth>
	</size>
	<xmin>annotation_xmin</xmin>
	<object>
	    <width>object_width</width>
		<name>airplane</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>airplane</difficult>
		<bndbox>
			<xmin>bndbox_xmin</xmin>
			<ymin>556</ymin>
			<xmax>552</xmax>
			<ymax>692</ymax>
		</bndbox>
	</object>
</annotation>
'''
tree = etree.XML(xml)
result1 = tree.xpath('/annotation//xmin/text()')  # ['annotation_xmin', 'bndbox_xmin']
# //代表找annotation的所有后代节点名为xmin的节点
# text()表示
result2 = tree.xpath('/annotation/object/text()')  # ['\n\t\t', '\n\t\t', '\n\t\t', '\n\t\t', '\n\t\t', '\n\t']
result3 = tree.xpath('/annotation/size/height/text()')  # ['1504']
result4 = tree.xpath('/annotation/*/width/text()')  # ['size_width', 'object_width']
# *是指通配符，表示随意哪个，什么都行
print(result4)