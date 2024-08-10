from django.core.management.base import BaseCommand
from core.models import Vehiculo

class Command(BaseCommand):
    help = 'Insertar vehículos en la BDD'

    def handle(self, *args, **kwargs):
        vehicles_data = [
            {
                "patente": "JSPW98",
                "modelo": "NEW 3",
                "version": None,
                "cilindrada": 2.0,
                "anno": 2017,
                "vin": "JM7BN3273J1146657",
                "numero_motor": "PE20897153",
                "marca": "MAZDA"
            },
            {
                "patente": "LRKJ19",
                "modelo": "RAV4",
                "version": "OTTO AUT",
                "cilindrada": 2.0,
                "anno": 2019,
                "vin": "JTMW43FV5LD017957",
                "numero_motor": "M20AV056411",
                "marca": "TOYOTA"
            },
            {
                "patente": "PKRP48",
                "modelo": "ACCENT",
                "version": "HCI",
                "cilindrada": 1.4,
                "anno": 2021,
                "vin": "MALC741BAMM235210",
                "numero_motor": "G4LCLU385336",
                "marca": "HYUNDAI"
            },
            {
                "patente": "SKRP27",
                "modelo": "WR",
                "version": "V LX AUT",
                "cilindrada": 1.5,
                "anno": 2023,
                "vin": "93HGH8820PK600340",
                "numero_motor": "L15Z93600305",
                "marca": "HONDA"
            },
            {
                "patente": "PJTH11",
                "modelo": "VERSA",
                "version": "SEDAN",
                "cilindrada": 1.6,
                "anno": 2021,
                "vin": "94DBCAN17MB100156",
                "numero_motor": "HR16361833T",
                "marca": "NISSAN"
            },
            {
                "patente": "LXPR25",
                "modelo": "-",
                "version": None,
                "cilindrada": 0.0,
                "anno": 2023,
                "vin": "TSMYD21S4LM693690",
                "numero_motor": "M16A-2304664",
                "marca": "SUZUKI"
            },
            {
                "patente": "LDHH27",
                "modelo": "MORNING",
                "version": "EZ",
                "cilindrada": 1.2,
                "anno": 2019,
                "vin": "KNAB3512ALT436790",
                "numero_motor": "G4LAJP132646",
                "marca": "KIA"
            },{
                "patente" : "GFBP30",
                "modelo" : "LAND",
                "version" : "CRUISER PRADO AUT",
                "cilindrada" : 4.0,
                "anno" : 2014,
                "vin" : "JTEBU3FJ0D5045507",
                "numero_motor" : "1GRA719814",
                "marca" : "TOYOTA"
            },
            {
                "patente" : "PJFC65",
                "modelo" : "L200",
                "version" : "WORK CR WF",
                "cilindrada" : 2.4,
                "anno" : 2021,
                "vin" : "MMBJJKK10LH031325",
                "numero_motor" : "4N15UGM6501",
                "marca" : "MITSUBISHI"
            },
            {
                "patente" : "KSGS79",
                "modelo" : "SWIFT",
                "version" : "GLX",
                "cilindrada" : 1.2,
                "anno" : 2018,
                "vin" : "JS2ZC63S9K6101669",
                "numero_motor" : "K12M5027782",
                "marca" : "SUZUKI"
            }
            
        ]

        for vehicle_data in vehicles_data:
            Vehiculo.objects.create(**vehicle_data)
            self.stdout.write(self.style.SUCCESS(f'Vehículo {vehicle_data["patente"]} agregado con éxito'))
