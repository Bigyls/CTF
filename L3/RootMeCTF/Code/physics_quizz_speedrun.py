import asyncio
import math
import websockets
import periodictable

ELEMENT = {}
ELEMENT["hydrogen"] = "1333-74-0"
ELEMENT["helium"] = "7440-59-7"
ELEMENT["lithium"] = "7439-93-2"
ELEMENT["beryllium"] = "7440-41-7"
ELEMENT["boron"] = "7440-42-8"
ELEMENT["carbon"]	="7440-44-0"
ELEMENT["nitrogen"] = "7727-37-9"
ELEMENT["oxygen"] = "7782-44-7"
ELEMENT["fluorine"] = "7782-41-4"
ELEMENT["neon"] = "7440-01-9"
ELEMENT["sodium"] = "7440-23-5"
ELEMENT["magnesium"] = "7439-95-4"
ELEMENT["aluminium"] = "7429-90-5"
ELEMENT["silicon"] = "7440-21-3"
ELEMENT["phosphorus"] = "7723-14-0"
ELEMENT["sulfur"] = "7704-34-9"
ELEMENT["chlorine"] = "7782-50-5"
ELEMENT["argon"] = "7440-37-1"
ELEMENT["potassium"] = "7440-09-7"
ELEMENT["calcium"] = "7440-70-2"
ELEMENT["scandium"] = "7440-20-2"
ELEMENT["titanium"] = "7440-32-6"
ELEMENT["vanadium"] = "7440-62-2"
ELEMENT["chromium"] = "7440-47-3"
ELEMENT["manganese"] = "7439-96-5"
ELEMENT["iron"] = "7439-89-6"
ELEMENT["cobalt"] = "7440-48-4"
ELEMENT["nickel"] = "7440-02-0"
ELEMENT["copper"] = "7440-50-8"
ELEMENT["zinc"] = "7440-66-6"
ELEMENT["gallium"] = "7440-55-3"
ELEMENT["germanium"] = "7440-56-4"
ELEMENT["arsenic"] = "7440-38-2"
ELEMENT["selenium"] = "7782-49-2"
ELEMENT["bromine"] = "7726-95-6"
ELEMENT["krypton"] = "7439-90-9"
ELEMENT["rubidium"] = "7440-17-7"
ELEMENT["strontium"] = "7440-24-6"
ELEMENT["yttrium"] = "7440-65-5"
ELEMENT["zirconium"] = "7440-67-7"
ELEMENT["niobium"] = "7440-03-1"
ELEMENT["molybdenum"] = "7439-98-7"
ELEMENT["technetium"] = "7440-26-8"
ELEMENT["ruthenium"] = "7440-18-8"
ELEMENT["rhodium"] = "7440-16-6"
ELEMENT["palladium"] = "7440-05-3"
ELEMENT["silver"] = "7440-22-4"
ELEMENT["cadmium"] = "7440-43-9"
ELEMENT["indium"] = "7440-74-6"
ELEMENT["tin"] = "7440-31-5"
ELEMENT["antimony"] = "7440-36-0"
ELEMENT["tellurium"] = "13494-80-9"
ELEMENT["iodine"] = "7553-56-2"
ELEMENT["xenon"] = "7440-63-3"
ELEMENT["cesium"] = "7440-46-2"
ELEMENT["barium"] = "7440-39-3"
ELEMENT["lanthanum"] = "7439-91-0"
ELEMENT["cerium"] = "7440-45-1"
ELEMENT["praseodymium"] = "7440-10-0"
ELEMENT["neodymium"] = "7440-00-8"
ELEMENT["promethium"] = "7440-12-2"
ELEMENT["samarium"] = "7440-19-9"
ELEMENT["europium"] = "7440-53-1"
ELEMENT["gadolinium"] = "7440-54-2"
ELEMENT["terbium"] = "7440-27-9"
ELEMENT["dysprosium"] = "7429-91-6"
ELEMENT["holmium"] = "7440-60-0"
ELEMENT["erbium"] = "7440-52-0"
ELEMENT["thulium"] = "7440-30-4"
ELEMENT["ytterbium"] = "7440-64-4"
ELEMENT["lutetium"] = "7439-94-3"
ELEMENT["hafnium"] = "7440-58-6"
ELEMENT["tantalum"] = "7440-25-7"
ELEMENT["tungsten"] = "7440-33-7"
ELEMENT["rhenium"] = "7440-15-5"
ELEMENT["osmium"] = "7440-04-2"
ELEMENT["iridium"] = "7439-88-5"
ELEMENT["platinum"] = "7440-06-4"
ELEMENT["gold"] = "7440-57-5"
ELEMENT["mercury"] = "7439-97-6"
ELEMENT["thallium"] = "7440-28-0"
ELEMENT["lead"] = "7439-92-1"
ELEMENT["bismuth"] = "7440-69-9"
ELEMENT["polonium"] = "7440-08-6"
ELEMENT["astatine"] = "7440-68-8"
ELEMENT["radon"] = "10043-92-2"
ELEMENT["francium"] = "7440-73-5"
ELEMENT["radium"] = "7440-14-4"
ELEMENT["actinium"] = "7440-34-8"
ELEMENT["thorium"] = "7440-29-1"
ELEMENT["protactinium"] = "7440-13-3"
ELEMENT["uranium"] = "7440-61-1"
ELEMENT["neptunium"] = "7439-99-8"
ELEMENT["plutonium"] = "7440-07-5"
ELEMENT["americium"] = "7440-35-9"
ELEMENT["curium"] = "7440-51-9"
ELEMENT["berkelium"] = "7440-40-6"
ELEMENT["californium"] = "7440-71-3"
ELEMENT["einsteinium"] = "7429-92-7"
ELEMENT["fermium"] = "7440-72-4"
ELEMENT["mendelevium"] = "7440-11-1"
ELEMENT["nobelium"] = "10028-14-5"
ELEMENT["lawrencium"] = "22537-19-5"
ELEMENT["rutherfordium"] = "53850-36-5"
ELEMENT["dubnium"] = "53850-35-4"
ELEMENT["seaborgium"] = "54038-81-2"
ELEMENT["bohrium"] = "54037-14-8"
ELEMENT["hassium"] = "54037-57-9"
ELEMENT["meitnerium"] = "54038-01-6"
ELEMENT["darmstadtium"] = "54083-77-1"
ELEMENT["roentgenium"] = "54386-24-2"
ELEMENT["copernicium"] = "54084-26-3"
ELEMENT["nihonium"] = "54084-70-7"
ELEMENT["flerovium"] = "54085-16-4"
ELEMENT["moscovium"] = "54085-64-2"
ELEMENT["livermorium"] = "54100-71-9"
ELEMENT["tennessine"] = "87658-56-8"
ELEMENT["oganesson"] = "54144-19-3"

def getInfo(name):
    for el in periodictable.elements:
        if el.name == name and el.name in ELEMENT:
            return [el.name, str( round(el.mass, 1)), str(el.number), ELEMENT[el.name]]

def BinaryToDecimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal)   

def BinaryToString(binary):
    str_data = ''
    for i in range(0, len(binary), 8):
        temp_data = int(binary[i:i + 8])
        decimal_data = BinaryToDecimal(temp_data)
        str_data = str_data + chr(decimal_data)
    return str_data

def StringToBinary(str):
    return ''.join( format(ord(i), '08b') for i in str)

async def Connect():
    async with websockets.connect("ws://ctf10k.root-me.org:8000") as wSocket:
        while True:
            response = await wSocket.recv()
            str_response = BinaryToString(response)
            bA, bB, bC = False, False, False
            tElement = ""
            print(str_response)
            for i in str_response.split(" "):
                i = i.lower()
                
                if i == "atomic":
                    bA = True
                if i == "electrons":
                    bB = True
                if i == "cas":
                    bC = True

                if i in ELEMENT:
                    tElement = getInfo(i)
            
            print(bA, bB, bC, tElement)
            if bA:
                await wSocket.send( StringToBinary( tElement[1]))

            if bB:
                await wSocket.send( StringToBinary( tElement[2]))

            if bC:
                await wSocket.send( StringToBinary( tElement[3]) )

asyncio.get_event_loop().run_until_complete(Connect())