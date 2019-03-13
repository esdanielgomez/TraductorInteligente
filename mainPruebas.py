import sys
from TextAPI import traducirTexto
from VozAPI import getAudioDeTexto, getTextoDeVoz, getVozPorIdiomaGeneroPersona


idiomaEntrada = "es-MX"
#idiomaEntrada = "en-US"

#idiomaSalida = "es-MX"
idiomaSalida = "en-US"

#generoVoz = "Femenino"
generoVoz = "Masculino"

mensajeCaptado = getTextoDeVoz(idiomaEntrada)
print(mensajeCaptado)

mensajeTraducido = traducirTexto(mensajeCaptado, idiomaEntrada, idiomaSalida)       
print(mensajeTraducido)

nombreAgente = getVozPorIdiomaGeneroPersona(idiomaSalida,generoVoz)
getAudioDeTexto(mensajeTraducido, nombreAgente, idiomaSalida)