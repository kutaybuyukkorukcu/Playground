import random
class Enemy:

  def __init__(self, name = "Enemy", remaining_hp = 500, attack_power = 10, number_of_rounds = 5):
    self.name = name 
    self.remaining_hp = remaining_hp
    self.attack_power = attack_power
    self.number_of_rounds = number_of_rounds

  def attack(self):
    print(self.name + " attacking!")
    remaining_number_of_rounds = random.randrange(0, 10)
    print(str(remaining_number_of_rounds) + " bullet has been used.")
    self.number_of_rounds -= remaining_number_of_rounds

    return (remaining_number_of_rounds, self.attack_power)

  def attacked(self, remaining_number_of_rounds, attack_power):
    print(self.name + " :Shoots")
    self.remaining_hp -= (remaining_number_of_rounds * attack_power)

  def outOfBullet(self):
    if(self.number_of_rounds <= 0):
      print(self.name + "speaks : I'm out of bullet. I'm out")
      return True
    return False

  def amIAlive(self):
    if(self.remaining_hp <= 0):
      print("I'm dying!")  

  def print(self):
    print("Creating")
    print("Name: ", self.name, "Remaining HP: ",self.remaining_hp,"Attack Power: ", self.attack_power, "Number of Rounds :", self.number_of_rounds)

enemies = []

i = 0 
while(i < 10):
  random_hp = random.randrange(100, 200)
  random_ap = random.randrange(10, 20)
  random_bullet = random.randrange(20, 30)
  newEnemy = Enemy("Enemy" + str(i+1), random_hp, random_ap, random_bullet)
  enemies.append(newEnemy)
  i += 1

i = 0
while(i < 3):
  randomenemy1 = random.randrange(0, 10)
  randomenemy2 = random.randrange(0, 10)

  returned_value = enemies[randomenemy1].attack()

  enemies[randomenemy2].attacked(returned_value[0], returned_value[1])

  print("The round is over...")

  i += 1