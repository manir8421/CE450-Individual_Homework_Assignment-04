            
 San Francisco Bay University

Python Programming
Homework Assignment #4
Due day: 4/9/2024

Instruction: 

1. DON’T allow to call the functions from the existing library.
2. Push the source code to Github platform.
3. Please follow the code style rule like programs on handout.
4. Overdue homework submission could not be accepted.
4. Takes academic honesty and integrity seriously (Zero Tolerance of Cheating & Plagiarism)


1.	Write a function to check if the element exists or not in the linked list.

def   cntn_link(s, elm):
 
  """Return True if elm is in the linked list s 
  >>> cntn_link (link(1, link(2, link(3, empty))), 1) 
  True 
  >>> cntn_link (link(1, link(2, link(3, empty))), 4) 
  False 
  """

2.	Create a function to print linked list as follows.

def prnt_lnk(s):
""" 
>>> prnt_lnk ( link(1, link(2, link(3, link(4, empty)))) ) 
<1 2 3 4>
"""

3.	Implement a function to create a new linked list in the reverse order.

def rvrs_lnk(s):

    """Return linked list reversed
    >>> rvrs_lnk (link(1, link(2, link(3, link(4, empty)))))
    [4, [3, [2, [1, [ ] ]]]]
  """

4.	Write a function srt (lnk) function, which returns True if the linked list lnk is sorted ascendingly from the left to right. If two adjacent elements are equal, the linked list can still be considered sorted.

def   srt (lnk):

    """ if the linked list lnk is sorted, then return True

    >>> lnk1 = link(1, link(2, link(3, link(4,empty))))
    >>> srt (lnk1)
    True
    >>> lnk2 = link(1, link(3, link(2, link(4, link(5, empty)))))
    >>> srt (lnk2)
    False
    >>> lnk3 = link(3, link(3, link(3, empty)))
    >>> srt (lnk3)
    True
   """

5.	Write a function with arguments a linked list lnk and a function g, which is applied to each number in lnk and returns the sum. If the linked list is empty, the sum is 0.

def   sum_lnk(lnk, g):

    """Applies a function g to each element in lnk and returns the sum
    of them

    >>> sqr = lambda x: x * x
    >>> dbl = lambda y: 2 * y
    >>> lnk1 = link(1, link(2, link(3, link(4, empty))))
    >>> sum_lnk (lnk1, sqr)		
    30				# sqr(1) + sqr(2)  + sqr(3)  + sqr(4) 
    >>> lnk2 = link(3, link(5, link(4, link(6, empty))))
    >>> sum_lnk (lnk2, dbl)
    36				# dbl(3)+ dbl(5)+ dbl(4)+ dbl(6)
   """

6.	Define a function with input parameters a linked list, lnk, and two elements, u & v. The function returns linked list but with all elements of u substituted with v.

def change(lnk, u, v):

"""Returns a linked list matching lnk but with all elements of u replaced by v. If u does not appear in lnk, then return lnk

 >>> l = link(1, link(2, link(3, empty)))
 >>> n=change(l, 3, 1)
 >>> n
 [1, [2, [1, [ ] ]]]
 >>> m=change(n, 1, 2)
 >>> m
 [2, [2, [2, [ ]]]]
 >>> change(m, 5, 1)
 [2, [2, [2, [ ]]]]
 """

7.	Generate a function to append element to the end of linked list.

def apnd(lnk, m):

   	 """Adds the element m to the end of lnk

    	>>> l = link(1, link(2, link(3, empty)))
    	>>> n = apnd (l, 4)                    # n = [1, [2, [3, [4, [] ]]]]
    	>>> first(rest(rest(rest(n))))
   	 4
    	"""


8.	Implement the insert function that creates a copy of the original list with an item inserted at the specific index. If the index is greater than the current length, you should insert the item at the end of the list.

def insrt(l, elm, ind):

    """
    >>> l = link(11, link(12, link(13, empty)))
    >>> n = insrt (l, 2021, 1)
    >>> n
    [11, [2021, [12, [13, [ ] ]]]]
   >>> m = insrt(n, 2022, 20)
   >>> m
    [11 [2021 [12 [13 [2022, [ ] ]]]]]
"""
