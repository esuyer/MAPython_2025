weather= input("Give me words separated by spaces:")
weatherList=weather.split(" ")
print(weatherList)
for i in range (len(weatherList)):
  if weatherList[i]=="rain":
     print("rain in list")
  else:
    print("rain not in list")