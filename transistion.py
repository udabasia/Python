kilo = float(input("Enter the amount in KG: "))
pound = kilo*2.20462
remainderStone = round(pound//14)
remainderPound = round(pound%14)
print(str(remainderStone)+" Stones and "+str(remainderPound)+" Pounds")
