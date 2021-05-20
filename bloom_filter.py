from bloomfilter import BloomFilter
from random import shuffle
 
n = 20 #no of items to add
p = 0.05 #false positive probability
 
bloomf = BloomFilter(n,p)
print("Size of bit array:{}".format(bloomf.size))
print("False positive Probability:{}".format(bloomf.fp_prob))
print("Number of hash functions:{}".format(bloomf.hash_count))
 
# numbers to be added
number_present = [1,2,3,4,5,6,7,8,9,10]
             
 
# number not added
number_absent = [11,12,13,14,15,16,17,18,19,20]
 
for item in number_present:
    bloomf.add(item)
 
shuffle(number_present)
shuffle(number_absent)
 
test_number = number_present[:10] + number_absent
shuffle(test_number)
for number in test_number:
    if bloomf.check(number):
        if number in number_absent:
            print("'{}' is a false positive!".format(number))
        else:
            print("'{}' is probably present!".format(number))
    else:
        print("'{}' is definitely not present!".format(number))
