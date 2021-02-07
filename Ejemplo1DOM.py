from xml.dom import minidom
doc = minidom.parse("archivo1.xml")
print("lISTA DE PERSONAS")
personas = doc.getElementsByTagName("persona")
for persona in personas:
    nombre = persona.getAttribute("nombre")
    edad = persona.getElementsByTagName("edad")[0]
    nacionalidad = persona.getElementsByTagName("nacionalidad")[0]
    print("nombre:%s " % nombre)
    print("nacionalidad:%s " % nacionalidad.firstChild.data)
    print("username:%s" % edad.firstChild.data)

