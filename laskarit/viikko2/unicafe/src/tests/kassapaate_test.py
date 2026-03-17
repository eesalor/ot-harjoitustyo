import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_konstruktori_asettaa_rahamaaran_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_konstruktori_asettaa_lounaiden_maaran_oikein_1(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
  
    def test_konstruktori_asettaa_lounaiden_maaran_2(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_kasvattaa_rahamaaraa_oikein_1(self):
        self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_kasvattaa_rahamaaraa_oikein_2(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_vaihtoraha_oikein_1(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(340)

        self.assertEqual(vaihtoraha, 100)

    def test_kateisosto_vaihtoraha_oikein_2(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(vaihtoraha, 100)

    def test_riittava_kateismaksu_kasvattaa_lounaiden_maaraa_1(self):
        self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_riittava_kateismaksu_kasvattaa_lounaiden_maaraa_2(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_riittamaton_kateismaksu_ei_muuta_kassan_rahamaaraa_1(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_riittamaton_kateismaksu_ei_muuta_kassan_rahamaaraa_2(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_riittamaton_kateismaksu_palauttaa_kaikki_rahat_1(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(10)

        self.assertEqual(vaihtoraha, 10)

    def test_riittamaton_kateismaksu_palauttaa_kaikki_rahat_2(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(10)

        self.assertEqual(vaihtoraha, 10)

    def test_riittamaton_kateismaksu_ei_lisää_lounaiden_maaraa_1(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_riittamaton_kateismaksu_ei_lisää_lounaiden_maaraa_2(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_veloittaa_summan_kortilta_1(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 760)

    def test_korttiosto_veloittaa_summan_kortilta_2(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 600)

    def test_riittava_korttimaksu_palauttaa_true_1(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_riittava_korttimaksu_palauttaa_true_2(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_korttimaksu_kasvattaa_myytyjen_lounaiden_maaraa_1(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttimaksu_kasvattaa_myytyjen_lounaiden_maaraa_2(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_riittamaton_korttimaksu_ei_muuta_kortin_saldoa_1(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 100)

    def test_riittamaton_korttimaksu_ei_muuta_kortin_saldoa_2(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 100)

    def test_riittamaton_korttimaksu_ei_muuta_lounaiden_maaraa_1(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_riittamaton_korttimaksu_ei_muuta_lounaiden_maaraa_2(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_riittamaton_korttimaksu_palauttaa_false_1(self):
        self.maksukortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_riittamaton_korttimaksu_palauttaa_false_2(self):
        self.maksukortti = Maksukortti(100)

        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_korttiosto_ei_muuta_kassassa_olevaa_rahamaaraa_1(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_ei_muuta_kassassa_olevaa_rahamaaraa_2(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_lataaminen_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)

        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_kortille_negatiivisen_summan_lataaminen_ei_muuta_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)

        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_kortille_lataaminen_kasvattaa_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortille_negatiivisen_summan_lataaminen_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_rahamaara_euroina_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
