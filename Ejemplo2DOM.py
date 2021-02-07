from xml.dom import minidom
doc = minidom.parse("archivo2.xml")
autos = doc.getElementsByTagName("auto")
colornuevo = input("Ingresa un nuevo color para los autos ")
for auto in autos:
    marca = auto.getElementsByTagName("marca")[0]
    color = auto.getElementsByTagName("color")[0].childNodes[0].nodeValue = colornuevo
    print("marca:%s " % marca.firstChild.data)
    print("color:%s" % color)
