# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 2, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_aged_brie_one(self):
        items = [Item("Aged Brie", 11, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(10, items[0].sell_in)

    def test_aged_brie_one_complete(self):
        items = [Item("Aged Brie", 11, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_aged_brie_three(self):
        items = [Item("Aged Brie", 5, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_aged_brie_seven_passed(self):
        items = [Item("Aged Brie", 3, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() #2
        gilded_rose.update_quality() #3
        gilded_rose.update_quality() #4
        gilded_rose.update_quality() #6
        gilded_rose.update_quality() #8
        gilded_rose.update_quality() #10
        gilded_rose.update_quality() #12
        self.assertEqual(-4, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_aged_brie_four_passed_float(self):
        items = [Item("Aged Brie", 1, 2.35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() #3.35
        gilded_rose.update_quality() #5.35
        gilded_rose.update_quality() #7.35
        gilded_rose.update_quality() #9.35
        self.assertEqual(9.35, items[0].quality)

    def test_aged_brie_four_passed_floatsss(self):
        items = [Item("Aged Brie", 1, 1.78159135487945)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() #2.78159135487945
        gilded_rose.update_quality() #4.78159135487945
        gilded_rose.update_quality() #6.78159135487945
        gilded_rose.update_quality() #8.78159135487945
        self.assertEqual(8.78159135487945, items[0].quality) #FIXME

    def test_sulfuras_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 51)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() #1
        gilded_rose.update_quality() #1
        gilded_rose.update_quality() #1
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(51, items[0].quality) #FIXME

    def test_aged_three_quality(self):
        items = [Item("Aged Brie", 1, 51)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() #1
        gilded_rose.update_quality() #1
        gilded_rose.update_quality() #1
        self.assertEqual(51, items[0].quality) #FIXME

    def test_sulfuras_three_passed(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() #1
        gilded_rose.update_quality() #1
        gilded_rose.update_quality() #1
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_backstage_twelve_passed(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() #11
        self.assertEqual(11, items[0].quality)
        gilded_rose.update_quality() #13
        gilded_rose.update_quality() #15
        gilded_rose.update_quality() #17
        gilded_rose.update_quality() #19
        gilded_rose.update_quality() #21
        self.assertEqual(21, items[0].quality)
        gilded_rose.update_quality() #24
        gilded_rose.update_quality() #27
        gilded_rose.update_quality() #30
        gilded_rose.update_quality() #33
        gilded_rose.update_quality() #36
        self.assertEqual(36, items[0].quality)
        gilded_rose.update_quality() #0
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_multi_ten_limit(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 40),
                 Item("Aged Brie", 3, 42)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() #43, 43
        gilded_rose.update_quality() #46, 44
        gilded_rose.update_quality() #49, 45
        self.assertEqual(45, items[1].quality) #aged
        self.assertEqual(49, items[0].quality) #back
        gilded_rose.update_quality() #50, 47
        self.assertEqual(47, items[1].quality) #aged
        self.assertEqual(50, items[0].quality) #aback
        gilded_rose.update_quality() #50, 49
        self.assertEqual(0, items[0].sell_in) #back
        self.assertEqual(50, items[0].quality) #back
        gilded_rose.update_quality() #0, 50
        self.assertEqual(-1, items[0].sell_in) #back
        self.assertEqual(0, items[0].quality) #back
        self.assertEqual(-3, items[1].sell_in) #aged
        self.assertEqual(50, items[1].quality) #aged

    def test_multi_limit(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 26, 18),
                 Item("Sulfuras, Hand of Ragnaros", 5, 90),
                 Item("Aged Brie", 15, 35)]
        gilded_rose = GildedRose(items)
        for i in range(25):
            gilded_rose.update_quality() #43, 36

        self.assertEqual(1, items[0].sell_in) #back
        self.assertEqual(5, items[1].sell_in) #sulfuras
        self.assertEqual(-10, items[2].sell_in) #aged
        self.assertEqual(50, items[0].quality) #back
        self.assertEqual(90, items[1].quality) #sulfuras
        self.assertEqual(50, items[2].quality) #aged

if __name__ == '__main__':
    unittest.main()
