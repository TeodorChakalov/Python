annual_tax_basketball = int(input())

basketball_shoots = annual_tax_basketball - 0.4 * annual_tax_basketball
basketball_equipment = basketball_shoots - 0.2 * basketball_shoots
basketball_ball = basketball_equipment - 0.75 * basketball_equipment
basketball_accessories = basketball_ball - 0.8 * basketball_ball

sum = annual_tax_basketball + basketball_shoots + basketball_equipment + basketball_ball + basketball_accessories
print(sum)