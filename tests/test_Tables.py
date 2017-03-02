from __future__ import absolute_import
import unittest

from pybufrkit.renderer import FlatTextRenderer
from pybufrkit.tables import get_table_group
from pybufrkit.descriptors import flat_member_ids


table_group_01_cmp = """340009 (Normalized differential vegetation index (NDVI))
    001007 SATELLITE IDENTIFIER
    001031 IDENTIFICATION OF ORIGINATING/GENERATING CENTRE
    002019 SATELLITE INSTRUMENTS
    002020 SATELLITE CLASSIFICATION
    301011 (Year, month, day)
        004001 YEAR
        004002 MONTH
        004003 DAY
    301013 (Hour, minute, second)
        004004 HOUR
        004005 MINUTE
        004006 SECOND
    005040 ORBIT NUMBER
    201136
    005041 SCAN LINE NUMBER
    201000
    025071 FRAME COUNT
    005001 LATITUDE (HIGH ACCURACY)
    005001 LATITUDE (HIGH ACCURACY)
    006001 LONGITUDE (HIGH ACCURACY)
    006001 LONGITUDE (HIGH ACCURACY)
    107064
        106032
            008012 LAND/SEA QUALIFIER
            008013 DAY/NIGHT QUALIFIER
            008065 SUN-GLINT INDICATOR
            008072 PIXEL(S) TYPE
            013039 TERRAIN TYPE (ICE/SNOW)
            040015 NORMALIZED DIFFERENTIAL VEGETATION INDEX (NDVI)"""

table_group_02_cmp = """340008 (IASI sequence combining PC scores, channel selection and enhanced data)
    001007 SATELLITE IDENTIFIER
    001031 IDENTIFICATION OF ORIGINATING/GENERATING CENTRE
    002019 SATELLITE INSTRUMENTS
    002020 SATELLITE CLASSIFICATION
    004001 YEAR
    004002 MONTH
    004003 DAY
    004004 HOUR
    004005 MINUTE
    202131
    201138
    004006 SECOND
    201000
    202000
    005001 LATITUDE (HIGH ACCURACY)
    006001 LONGITUDE (HIGH ACCURACY)
    007024 SATELLITE ZENITH ANGLE
    005021 BEARING OR AZIMUTH
    007025 SOLAR ZENITH ANGLE
    005022 SOLAR AZIMUTH
    005043 FIELD OF VIEW NUMBER
    005040 ORBIT NUMBER
    201133
    005041 SCAN LINE NUMBER
    201000
    201132
    025070 MAJOR FRAME COUNT
    201000
    202126
    007001 HEIGHT OF STATION
    202000
    103003
        025140 START CHANNEL
        025141 END CHANNEL
        033060 GQISFLAGQUAL - INDIVIDUAL IASI-SYSTEM QUALITY FLAG
    033061 GQISQUALINDEX - INDICATOR FOR INSTRUMENT NOISE PERFORMANCE (CONTRIBUTIONS FROM SPECTRAL AND RADIOMETRIC CALIBRATION)
    033062 GQISQUALINDEXLOC - INDICATOR FOR GEOMETRIC QUALITY INDEX
    033063 GQISQUALINDEXRAD - INDICATOR FOR INSTRUMENT NOISE PERFORMANCE (CONTRIBUTIONS FROM RADIOMETRIC CALIBRATION)
    033064 GQISQUALINDEXSPECT - INDICATOR FOR INSTRUMENT NOISE PERFORMANCE (CONTRIBUTIONS FROM SPECTRAL CALIBRATION)
    033065 GQISSYSTECSONDQUAL - OUTPUT OF SYSTEM TEC (TECHNICAL EXPERTISE CENTRE) QUALITY FUNCTION
    040020 GQISFLAGQUALDETAILED - QUALITY FLAG FOR THE SYSTEM
    101010
        340002 (IASI Level 1c band description)
            025140 START CHANNEL
            025141 END CHANNEL
            025142 CHANNEL SCALE FACTOR
    104000
    ....031002 EXTENDED DELAYED DESCRIPTOR REPLICATION FACTOR
        201136
        005042 CHANNEL NUMBER
        201000
        014046 SCALED IASI RADIANCE
    108003
        025140 START CHANNEL
        025141 END CHANNEL
        040026 SCORE QUANTIZATION FACTOR
        040016 RESIDUAL RMS IN BAND
        025062 DATABASE IDENTIFICATION
        101000
        ....031002 EXTENDED DELAYED DESCRIPTOR REPLICATION FACTOR
            040017 NON-NORMALIZED PRINCIPAL COMPONENT SCORE
    002019 SATELLITE INSTRUMENTS
    025051 AVHRR CHANNEL COMBINATION
    101007
        340004 (IASI Level 1c AVHRR single scene)
            005060 Y ANGULAR POSITION FROM CENTRE OF GRAVITY
            005061 Z ANGULAR POSITION FROM CENTRE OF GRAVITY
            025085 FRACTION OF CLEAR PIXELS IN HIRS FOV
            105006
                005042 CHANNEL NUMBER
                025142 CHANNEL SCALE FACTOR
                014047 SCALED MEAN AVHRR RADIANCE
                025142 CHANNEL SCALE FACTOR
                014048 SCALED STANDARD DEVIATION AVHRR RADIANCE
    020081 CLOUD AMOUNT IN SEGMENT
    008029 SURFACE TYPE
    020083 AMOUNT OF SEGMENT COVERED BY SCENE
    008029 SURFACE TYPE
    040018 GIACAVGIMAGIIS - AVERAGE OF IMAGER MEASUREMENTS
    040019 GIACVARIMAGIIS - VARIANCE OF IMAGER MEASUREMENTS
    040021 FRACTION OF WEIGHTED AVHRR PIXEL IN IASI FOV COVERED WITH SNOW/ICE
    040022 NUMBER OF MISSING, BAD OR FAILED AVHRR PIXELS"""


class TablesTests(unittest.TestCase):

    def setUp(self):
        self.table_group = get_table_group()
        self.flat_text_renderer = FlatTextRenderer()

    def tearDown(self):
        pass

    def test_table_group_01(self):
        template = self.table_group.lookup(340009)
        assert self.flat_text_renderer.render(template) == table_group_01_cmp
        assert flat_member_ids(template) == [
            1007, 1031, 2019, 2020, 4001, 4002, 4003, 4004, 4005, 4006, 5040,
            201136, 5041, 201000, 25071, 5001, 5001, 6001, 6001,
            107064, 106032, 8012, 8013, 8065, 8072, 13039, 40015]

    def test_table_group_02(self):
        template = self.table_group.lookup(340008)
        assert self.flat_text_renderer.render(template) == table_group_02_cmp
