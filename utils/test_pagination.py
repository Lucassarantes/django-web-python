from unittest import TestCase
from utils.pagination import make_pagination_range

class PaginationTest(TestCase):
    def test_make_pagination_range_return_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1,5)),
            qty_pages=2,
            current_page=1,
        )['pagination']
        self.assertEqual([1,2], pagination)

    def test_first_range_is_static_if_curr_page_is_less_than_middle_page(self):
        pagination = make_pagination_range(
            page_range=list(range(1,5)),
            qty_pages=2,
            current_page=1,
        )['pagination']
        self.assertEqual([1,2], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1,5)),
            qty_pages=2,
            current_page=2,
        )['pagination']
        self.assertEqual([2,3], pagination)

    def test_make_sure_middle_range_is_correct(self):
        pagination = make_pagination_range(
            page_range=list(range(1,5)),
            qty_pages=2,
            current_page=2,
        )['pagination']
        self.assertEqual([2, 3], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1,5)),
            qty_pages=2,
            current_page=3,
        )['pagination']
        self.assertEqual([3, 4], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        pagination = make_pagination_range(
            page_range=list(range(1,5)),
            qty_pages=2,
            current_page=4,
        )['pagination']
        self.assertEqual([3, 4], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1,5)),
            qty_pages=2,
            current_page=5,
        )['pagination']
        self.assertEqual([3, 4], pagination)