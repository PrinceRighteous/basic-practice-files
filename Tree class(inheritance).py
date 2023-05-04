class object:
	def __init__(self,color_of_leaves,avg_height):
		self.color_of_leaves = color_of_leaves
		self.avg_height = avg_height
	
	def show_all(self):
		print(self.color_of_leaves)
		print(self.avg_height)
	
class Tree(object):
	def name_of_tree(self):
		if self.avg_height >= 150 and self.avg_height <= 210:
			name = "Eastern White Pine"
		#add more elifs and trees	 
	def descrip_of_tree(self):
		if self.avg_height >= 150 and self.avg_height <= 210:
			print("This tree is called the Eastern White Pine tree.")
			print("With a height ranging from 150 to 210 Feet tall.")
			return ("This tree is Native to Eastern North America.")
		elif self.avg_height >= 75 and self.avg height <= 200:
			print("this tree is called the Red Pine Tree.".title())
			print("With a height Ranging from 75 to 200 feet tall.")
			return ("This tree is native to the Northeastern regio of the united states.")
		elif self.avg_height >= 40 and self.avg_height <= 60:
			print("This tree is called the Red Maple Tree")
			print("With a height ranging from 40 to 60 feet tall.")
			return ("This tree is native to the eastern and southeastern regions of North America.")
		else:
			return ("im sorry but we do not have information on this tree at this time.")
		
class color_group_trees(object):
	def __init__(self,color_of_leaves,avg_height, Name_of_tree):
		super().__init__(color_of_leaves,avg_height)
		self.Name_of_tree = Name_of_tree
		
	
	def	colored_group_trees(self):
		self.red_group = red_group
		self.red_group = []
		self.green_group = green_group
		self.green group = []
		self.yellow_group = yellow_group	
		self.yellow_group = [] 		
		self.pink_group = pink_group
		self.pink_group = []
	def add_tree(self):
		#figure out how to add your name of tree parameter to the list of group trees.
				 
T1 = Tree("Green",150)
print(T1.descrip_of_tree())			
 
