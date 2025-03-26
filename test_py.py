#import pytest
from Lb2 import (
    fact,
    simple,
    elements,
    group_words
)

def test_fact():
    assert fact(0) == 1
    assert fact(2) == 2
    assert fact(3) == 6
    assert fact(4) == 24
    assert fact(5) == 120
    assert fact(6) == 720
    assert fact(7) == 5040
    assert fact(8) == 40320
    assert fact(9) == 362880
    assert fact(10) == 3628800
    assert fact(11) == 39916800

def test_simple():
    assert simple(1) == "Составное"
    assert simple(2) == "Простое"
    assert simple(3) == "Простое"
    assert simple(4) == "Составное"
    assert simple(5) == "Простое"
    assert simple(6) == "Составное"
    assert simple(7) == "Простое"
    assert simple(8) == "Составное"
    assert simple(9) == "Составное"
    assert simple(10) == "Составное"
    assert simple(11) == "Простое"

def test_element():
    assert elements([1,2,2,3,4,5,8]) == {1,2,3,4,5,8}
    assert elements([2,2,6,6,8,5,5]) == {2,6,5,8}
    assert elements([3,5,9,9,8,4,4]) == {3,5,9,8,4}
    assert elements([4,18,1,15,15,6,6]) == {4,18,1,15,6}
    assert elements([5,36,45,52,52,5,36]) == {5,36,45,52}
    assert elements([9,9,6,3,1,4,4]) == {9,6,3,1,4}
    assert elements([10,10,3,3,6,5,5]) == {10,3,6,5}
    assert elements([11,12,12,13,15,16,16]) == {11,12,13,15,16}
    assert elements([15,15,96,9,3,6,3]) == {15,96,9,3,6}
    assert elements([15,36,25,52,15,6,7]) == {15,36,25,52,6,7}
    assert elements([85,85,96,36,52,2,3]) == {85,96,36,52,2,3}

def test_group_words():
    assert group_words(words = ["apple", "banana", "pear", "kiwi", "grape", "fig"]) == {5: ['apple', 'grape'], 6: ['banana'], 4: ['pear', 'kiwi'], 3: ['fig']}
    assert group_words(words = ["adult", "age", "baby", "birth", "boy", "childhood"]) == {5: ['adult', 'birth'], 3: ['age', 'boy'], 4: ['baby'], 9: ['childhood']}
    assert group_words(words =["woman", "neighbour", "name", "surname", "address", "single"]) == {5: ['woman'], 9: ['neighbour'], 4: ['name'], 7: ['surname', 'address'], 6: ['single']}
    assert group_words(words =["parents", "father", "mother ", "husband", "wife", "daughter"]) == {7: ['parents', 'mother ', 'husband'], 6: ['father'], 4: ['wife'], 8: ['daughter']}
    assert group_words(words =["brother", "sister", "grandmother ", "grandfather", "uncle", "aunt"]) == {7: ['brother'], 6: ['sister'], 12: ['grandmother '], 11: ['grandfather'], 5: ['uncle'], 4: ['aunt']}
    assert group_words(words =["nephew", "niece", "cousin ", "arm", "back", "beard"]) == {6: ['nephew'], 5: ['niece', 'beard'], 7: ['cousin '], 3: ['arm'], 4: ['back']}
    assert group_words(words =["bone", "buttocks", "cheek ", "chin", "ear", "elbow"]) == {4: ['bone', 'chin'], 8: ['buttocks'], 6: ['cheek '], 3: ['ear'], 5: ['elbow']}
    assert group_words(words =["eye", "eyebrow", "face ", "finger", "foot ", "forehead"]) == {3: ['eye'], 7: ['eyebrow'], 5: ['face ', 'foot '], 6: ['finger'], 8: ['forehead']}
    assert group_words(words =["hair", "hand", "head ", "heart", "heel ", "knee"]) == {4: ['hair', 'hand', 'knee'], 5: ['head ', 'heart', 'heel ']}
    assert group_words(words =["hello world", "bool", "int ", "tel", "yes ", "no"])== {11: ['hello world'], 4: ['bool', 'int ', 'yes '], 3: ['tel'], 2: ['no']}
    assert group_words(words =["girl", "boy", "t-shirt ", "shirt", "jins ", "hat"]) == {4: ['girl'], 3: ['boy', 'hat'], 8: ['t-shirt '], 5: ['shirt', 'jins ']}