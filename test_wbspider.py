import unittest


class TestWeiboSpider(unittest.TestCase):
    def test_getrepostcounts(self):
        from data_process.do_statusprocess import status_parse
        with open('./tests/reposts_root.html') as f:
            cont = f.read()
            repost_count = status_parse.get_repostcounts(cont)
            self.assertEqual(repost_count, 0)

        with open('./tests/reposts_sub.html') as f:
            cont = f.read()
            repost_count = status_parse.get_repostcounts(cont)
            self.assertEqual(repost_count, 38)

    def test_getcomments(self):
        from data_process.do_statusprocess import status_parse
        with open('./tests/reposts_root.html') as f:
            cont = f.read()
            repost_count = status_parse.get_commentcounts(cont)
            self.assertEqual(repost_count, 0)

        with open('./tests/reposts_sub.html') as f:
            cont = f.read()
            repost_count = status_parse.get_commentcounts(cont)
            self.assertEqual(repost_count, 9)

    def test_update_repost_comment(self):
        from db_operation.weibosearch_dao import update_repost_comment
        mid = '3791583457149221'
        reposts = 42
        comments = 9
        update_repost_comment(mid=mid, reposts=reposts, comments=comments)

