class Hero():
	def __init__(self, name, level, health, damage):
		#Initiate our hero
		self.name = name 
		self.level = level
		self.health = health
		self.damage = damage

	def show_hero(self):
		#Show our hero
		message = ('Name hero:' + self.name + ', Level: ' + str(self.level) + ', Health: ' + 
			str(self.health) + ', Damage:' +  str(self.damage)).title()
		
		print(message)
	def up_level(self):
		#Up level
		self.level += 1

	def up_health(self):
		#Up health
		self.health += 10



#-----------------------------------------------------------


class SuperHero(Hero):
	def __init__(self, name, level, health, magiclevel, damage):
		super().__init__(name, level, health, damage)
		self.magiclevel = magiclevel
		self.magic = 100
	
	def makemagic(self):
		#Magic reduction
		self.magic -= 10

	def show_hero(self):
		message = ('Name hero:' + self.name + ', Level: ' + str(self.level) + ', Health: ' + str(self.health) + ', Magic:' + 
			str(self.magic))+ ', Damage:' +  str(self.damage).title()
		print(message)



mysuperhero = SuperHero('Yaroslav', 100, 250, 50, 1000)
myhero = Hero('Mudila', 0, 0, 0)
myhero.show_hero()
mysuperhero.up_level()
mysuperhero.show_hero() 
	
