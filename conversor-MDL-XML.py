# ScriptConversor-MDL-XML
# Produzido por Euclides Ramos

import matlab.engine

# É importante que o arquivo que será convertido esteja na mesma pasta deste script;
# O arquivo de saída terá o mesmo nome do arquivo de entrada, mudando apenas a extensão.
def convert(inputfile):
    eng = matlab.engine.start_matlab()
    eng.open(inputfile)
    eng.save_system(inputfile, inputfile + '.xml', 'ExportToXML', True)


# É recebidoo nome do arquivo (sem a extenção)
e = input()
convert(e)