# Generated by Django 4.2.6 on 2023-11-02 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycarmodel',
            name='make',
            field=models.CharField(choices=[('1', 'Abarth'), ('2', 'Alfa Romeo'), ('3', 'Aston Martin'), ('4', 'Audi'), ('5', 'Bentley'), ('6', 'BMW'), ('7', 'Bugatti'), ('8', 'Cadillac'), ('9', 'Chevrolet'), ('10', 'Chrysler'), ('11', 'Citroën'), ('12', 'Dacia'), ('13', 'Daewoo'), ('14', 'Daihatsu'), ('15', 'Dodge'), ('16', 'Donkervoort'), ('17', 'DS'), ('18', 'Ferrari'), ('19', 'Fiat'), ('20', 'Fisker'), ('21', 'Ford'), ('22', 'Honda'), ('23', 'Hummer'), ('24', 'Hyundai'), ('25', 'Infiniti'), ('26', 'Iveco'), ('27', 'Jaguar'), ('28', 'Jeep'), ('29', 'Kia'), ('30', 'KTM'), ('31', 'Lada'), ('32', 'Lamborghini'), ('33', 'Lancia'), ('34', 'Land Rover'), ('35', 'Landwind'), ('36', 'Lexus'), ('37', 'Lotus'), ('38', 'Maserati'), ('39', 'Maybach'), ('40', 'Mazda'), ('41', 'McLaren'), ('42', 'Mercedes-Benz'), ('43', 'MG'), ('44', 'Mini'), ('45', 'Mitsubishi'), ('46', 'Morgan'), ('47', 'Nissan'), ('48', 'Opel'), ('49', 'Peugeot'), ('50', 'Porsche'), ('51', 'Renault'), ('52', 'Rolls-Royce'), ('53', 'Rover'), ('54', 'Saab'), ('55', 'Seat'), ('56', 'Skoda'), ('57', 'Smart'), ('58', 'SsangYong'), ('59', 'Subaru'), ('60', 'Suzuki'), ('61', 'Tesla'), ('62', 'Toyota'), ('63', 'Volkswagen'), ('64', 'Volvo')], max_length=2),
        ),
    ]
