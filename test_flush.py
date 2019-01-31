#!/usr/bin/env python
# -*- coding: utf-8 -*-
all_streets = [u'A2345',
               u'23456',
               u'34567',
               u'45678',
               u'56789',
               u'6789T',
               u'789TJ',
               u'89TJQ',
               u'9TJQK',
               u'TJQKA',
               u'5432A',
               u'65432',
               u'76543',
               u'87654',
               u'98765',
               u'T9876',
               u'JT987',
               u'QJT98',
               u'KQJT9',
               u'AKQJT']

def card_ranks(hand):
    """Возвращает список рангов (его числовой эквивалент),
    отсортированный от большего к меньшему"""
    ranks = []
    for x in range(len(hand)):
        ranks.append(int(hand[x][:1].replace(u'T',u'10').replace(u'J', u'11').replace(u'Q', u'12').replace(u'K', u'13').replace(u'A', u'14')))
        print ranks
    ranks.sort(reverse=True)
    for x in range(len(ranks)):
        ranks[x]=str(ranks[x]).replace(u'10',u'T').replace(u'11', u'J').replace(u'12', u'Q').replace(u'13', u'K').replace(u'14', u'A')

    return ranks

def flush(hand):
    """Возвращает True, если все карты одной масти"""
    for x in range(len(hand)):
        # Берем масть первой карты и сравнимаем с мастью всех остальных. Если хоть одна отличается, то нет флэша
        # Хм... но ведь неизвестно какие карты у игрока? Флэш же это 5 карт...
        if hand[x][1:2] != hand[1][1:2]:
            return False
        else:
            x+=1
    return True

def straight(ranks):
    """Возвращает True, если отсортированные ранги формируют последовательность 5ти,
    где у 5ти карт ранги идут по порядку (стрит)"""
    ranks = ''.join(ranks)
    for x in range(len(all_streets)):
        if all_streets[x] in ranks:
            print u'Street'
            return True
        else:
            x+=1
    return None


a = [u'9', u'4', u'2']
b = [[1,2,3],[4,2,6],[u'9',u'4',u'2']]


#card_ranks([u'QC', u'4C', u'JR', u'TC', u'AC', u'2C', u'KC'])\
#card_ranks([u'6C', u'4C', u'7R'])

straight([u'9', u'8', u'7', u'6', u'5', u'4', u'2'])