# Autor: Jakub Lisowski, Jlisowskyy

import unittest
import MailSendingLib as mLib

class MailManipulationTests(unittest.TestCase):
    def test_token_replace(self):
        self.assertEqual(mLib.InplaceLinkInMail("basic template [link_token]", "LINK"), "basic template LINK")


if __name__ == '__main__':
    unittest.main()