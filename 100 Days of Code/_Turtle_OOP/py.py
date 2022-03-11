import prettytable as pt

tbl = pt.PrettyTable()

tbl.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], "l")
tbl.add_column("Type", ["Electric", "Water", "Fire"], "l")

print(tbl)