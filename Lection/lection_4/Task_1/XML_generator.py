from user_interface import temperatere_view
from user_interface import wind_speed_view
from user_interface import pressure_view


def create(device=1):
    xml = '<xml>\n'
    xml += '     <temperature units = "c">{}</teperature>\n'\
        .format(temperatere_view(device))
    xml += '     <wind_speed units = "m/s">{}</wind_speed>\n'\
        .format(wind_speed_view(device))
    xml += '     <pressure units = "mmHg">{}</pressure>\n'\
        .format(pressure_view(device))
    xml += '</xml>'

    with open('Lection/lection_4/Task_1/data.xml', 'w') as page:
        page.write(xml)

    return xml
