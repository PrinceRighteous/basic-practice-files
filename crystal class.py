class Crystal:
	def __init__(self, name, color):
		self.name = name.title()
		self.color = color.title() 
		
	def show_all(self):
		print(self.name)
		print(self.color)
	
	def chakra_properties(self):
		return "Most crystals correspond to the chakra represented by the same color as the crystal."
		if color == "purple":
			print("the most well known purple crystals are Amethyst, Flourite, Kunzite, Jade, and Jasper.".title())
			print("Purple crystals are known for helping awaken the third eye chakra and arouse the crown chakra.")
		elif color == "blue":
			print("the most well known blue crystals are Sapphire Blue, Aquamarine, Turqoise, Spinel, and Tourmaline.".title())
			print("Blue crystals are known for healing the throat chakra, arousing the third eye and helping with speech problems.")
		elif color == "green":		
			pass


c1 = Crystal("amethyst", "purple")
c2 = Crystal("Aquamarine", "light blue")
print(c1.show_all())
print(c2.chakra_properties())

