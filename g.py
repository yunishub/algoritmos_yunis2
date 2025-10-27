# g. Desenvolva um programa que leia uma distância de metros e mostre os valores relativos em outras medidas.
dist = input("Digite a distância em metros: ").strip().replace(',', '.')
m = float(dist)

print(f"{m} m = {m} m")
print(f"{m} km = {m*1000} quilômetros")
print(f"{m} hm = {m*100} hectômetros")
print(f"{m} dam = {m*10} decâmetros")
print(f"{m} m = {m/10} decímetros") 
print(f"{m} m = {m/100} centímetros")    

print(f"{m} m = {m/1000} milímetros")
