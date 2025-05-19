def converter_celsius(graus_celsius):
    Faherenheit= graus_celsius * 1.8 + 32
    return Faherenheit
def converter_kelvin(graus_celsius):
    Kelvin= graus_celsius + 273
    return Kelvin
print(converter_kelvin(80),"Kelvin")
print(converter_celsius(70),"Celsius") 