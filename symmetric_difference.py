def diff(a, b, c, d):
	
	
	b =  b.split()
	
	d =  d.split()
	
	m = set(b)
	n = set(d)
	
	x = m.difference(n)
	y = n.difference(m)
	

	_A_ = x.union(y)
	
	nums = [int(item) for item in _A_]
	
	nums_sorted = sorted(nums)
	
	show =[ print(elems) for elems in nums_sorted]
	
	return show

diff(input(), input(), input(), input())

'''
Given 2 sets of integers, M and N, print their symmetric difference in
ascending order.  The term symmetric difference indicates those values
that exist in either M or N but do not exist in both.

Input Format

The first line of input contains an integer, . 
The second line contains  space-separated integers. 
The third line contains an integer, . 
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

'''
