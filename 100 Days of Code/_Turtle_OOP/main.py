# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle"), timmy.pencolor("aquamarine"), timmy.fillcolor("red")
# timmy.fd(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
# table = PrettyTable()
# table2 = PrettyTable()
table3 = PrettyTable()
#
# table.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
# table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])
#
# table2.add_column("Dia", ["Martes", "Miercoles", "Jueves"])
# table2.add_column("Hora", ["9AM | 2PM", "9AM | 10:30AM | 3PM", "8:30AM | 10AM | 2PM"])
# table2.add_column("Equipo", ["P2-Bocina con mic | P4-Proyector, pc y screen",\
#                              "P2-Bocina con mic | P3-Proyector, pc y screen | P2-Proyector, pc y screen",\
#                              "P4-Bocina con mic | P4-Proyector, pc y screen | P4-Proyector, pc y screen"])
# table2.align = "l"
# print(table2)
#
#
table3.add_column('Fecha', ['08/10/21', '08/10/21', '08/11/21', '08/11/21', '08/11/21', '08/12/21', '08/12/21', '08/12/21'])
table3.add_column('Hora', ['09:00AM', '02:00PM', '09:00AM', '10:30AM', '03:00PM', '08:30AM', '10:00AM', '02:00PM'])
table3.add_column('Piso', ['2', '4', '2', '3', '2', '4', '4', '4'])
table3.add_column('Bocina + Mic', ['x', '', 'x', '', '', 'x', '', ''])
table3.add_column('Proyector + Pantalla', ['', 'x', '', 'x', 'x', '', 'x', 'x'])


txt = open('Equipos Semana 330.txt', 'w')
txt.writelines(str(table3))
txt.close()