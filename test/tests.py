from textwrap import dedent
import unittest
from unittest import TestCase

from heconvert.converter import *


class TestKSX5002(TestCase):
    def test_all(self):
        # h2e test
        self.assertEqual('rsef', h2e('ㄱㄴㄷㄹ'))
        self.assertEqual('kiju', h2e('ㅏㅑㅓㅕ'))
        self.assertEqual('0123', h2e('0123'))
        self.assertEqual('!@#', h2e('!@#'))
        self.assertEqual('r s e f', h2e('ㄱ ㄴ ㄷ ㄹ'))
        self.assertEqual('qlgodrlrk skfdkrksek Tbd~', h2e('비행기가 날아간다 쓩~'))
        self.assertEqual('Wlvckfmf xkrh dhs vpvtlaosrhk Tytekfl Ehaqkdrkrgk', h2e('찦차를 타고 온 펲시맨과 쑛다리 똠방각하'))
        self.assertEqual('tkfkdgksek thathadk', h2e('사랑한다 솜솜아'))
        self.assertEqual(dedent("""\
            skeh snrnsrkdprp...
            thwndgks aksskadlrh tlvek

            sork rmeo ruxdp dlTdj...
            rmeork dhlfhqwl dksgekaus
            rmeodml snsanfdl ehldj wnrh

            rktmadl ehldj wnrh...
            rmeork skfmf vlfdyfh gkf Eo
            djswpemswl rmeo ruxdp ajanfmrh tlvek

            skeh snrnsrkdprp...
            Rhr vlfdygks aksskadlrh tlvek
            so qlfhr dusdirgkrh anelrh

            rkwlsrjt djqtek gkdueh...
            snrnsrkdprp wnf tn dlTsms rjs
            qnRmfjqwleh dksgdms akdma gksk

            snrnsrk skfmf vlfdyfh gkf Eo...
            wnwj djqtdl ekffurk wkqdk wnrh

            snrnsrk skfmf qnffj wnfEos...
            rmeo akdma rlvdl skadmf dmlalgkrh tlvek
            skeh snrnsrkdprp thwndgks aksskadlrh tlvek

            aksskarhk aksskadps gkscldml...
            rjwltdl djqtdjdi gkrh aksska rmwkcprk
            so toddodp rlQmadl ehldjdi gksksl

            gkfn gkfnrk...
            snrnsrkdprp thwndgks aksskadlrh tlvek....."""), dedent(h2e("""\
            나도 누군가에게...
            소중한 만남이고 싶다

            내가 그대 곁에 있어...
            그대가 외롭지 않다면
            그대의 눈물이 되어 주고

            가슴이 되어 주고...
            그대가 나를 필요로 할 때
            언제든지 그대 곁에 머무르고 싶다

            나도 누군가에게...
            꼭 필요한 만남이고 싶다
            내 비록 연약하고 무디고

            가진것 없다 하여도...
            누군가에게 줄 수 있는 건
            부끄럽지도 않은 마음 하나

            누군가 나를 필요로 할 때...
            주저 없이 달려가 잡아 주고

            누군가 나를 불러 줄땐...
            그대 마음 깊이 남을 의미하고 싶다
            나도 누군가에게 소중한 만남이고 싶다

            만남과 만남엔 한치의...
            거짓이 없어야 하고 만남 그자체가
            내 생애에 기쁨이 되어야 하나니

            하루 하루가...
            누군가에게 소중한 만남이고 싶다.....""")))

        h2e_builder = HangulToEnglishConverter()
        h2e_builder.update('서해번쩍')
        self.assertEqual('tjgoqjsWjr', h2e_builder.convert())
        self.assertEqual('tjgoqjsWjrehdgoqjsWjr', h2e_builder.update('동해번쩍', True))

        # e2h test
        self.assertEqual('10을 2로 나눈 몫은 5이다', e2h('10dmf 2fh sksns ahrtdms 5dlek'))
        self.assertEqual('비행기가 날아간다 쓩~', e2h('qlgodrlrk skfdkrksek Tbd~'))
        self.assertEqual('찦차를 타고 온 펲시맨과', e2h('Wlvckfmf xkrh dhs vpvtlaosrhk'))
        self.assertEqual('쑛다리 똠방각하', e2h('Tytekfl Ehaqkdrkrgk'))
        self.assertEqual('뽀빠이괍귘뜧귁뷁썆와위ㅡㄱ', e2h('QhQkdlrhkqrnlzEbgrnlrqnpfrTiwdhkdnlmr'))

        self.assertEqual(dedent("""\
        나도 누군가에게...
        소중한 만남이고 싶다

        내가 그대 곁에 있어...
        그대가 외롭지 않다면
        그대의 눈물이 되어 주고

        가슴이 되어 주고...
        그대가 나를 필요로 할 때
        언제든지 그대 곁에 머무르고 싶다

        나도 누군가에게...
        꼭 필요한 만남이고 싶다
        내 비록 연약하고 무디고

        가진것 없다 하여도...
        누군가에게 줄 수 있는 건
        부끄럽지도 않은 마음 하나

        누군가 나를 필요로 할 때...
        주저 없이 달려가 잡아 주고

        누군가 나를 불러 줄땐...
        그대 마음 깊이 남을 의미하고 싶다
        나도 누군가에게 소중한 만남이고 싶다

        만남과 만남엔 한치의...
        거짓이 없어야 하고 만남 그자체가
        내 생애에 기쁨이 되어야 하나니

        하루 하루가...
        누군가에게 소중한 만남이고 싶다....."""), dedent(e2h("""\
        skeh snrnsrkdprp...
        thwndgks aksskadlrh tlvek

        sork rmeo ruxdp dlTdj...
        rmeork dhlfhqwl dksgekaus
        rmeodml snsanfdl ehldj wnrh

        rktmadl ehldj wnrh...
        rmeork skfmf vlfdyfh gkf Eo
        djswpemswl rmeo ruxdp ajanfmrh tlvek

        skeh snrnsrkdprp...
        Rhr vlfdygks aksskadlrh tlvek
        so qlfhr dusdirgkrh anelrh

        rkwlsrjt djqtek gkdueh...
        snrnsrkdprp wnf tn dlTsms rjs
        qnRmfjqwleh dksgdms akdma gksk

        snrnsrk skfmf vlfdyfh gkf Eo...
        wnwj djqtdl ekffurk wkqdk wnrh

        snrnsrk skfmf qnffj wnfEos...
        rmeo akdma rlvdl skadmf dmlalgkrh tlvek
        skeh snrnsrkdprp thwndgks aksskadlrh tlvek

        aksskarhk aksskadps gkscldml...
        rjwltdl djqtdjdi gkrh aksska rmwkcprk
        so toddodp rlQmadl ehldjdi gksksl

        gkfn gkfnrk...
        snrnsrkdprp thwndgks aksskadlrh tlvek.....""")))

        e2h_builder = EnglishToHangulConverter()
        e2h_builder.update('ehdgoqjsWjr')
        self.assertEqual('동해번쩍', e2h_builder.convert())
        self.assertEqual('동해번쩍서해번쩍', e2h_builder.update('tjgoqjsWjr', True))

if __name__ == '__main__':
    unittest.main()
