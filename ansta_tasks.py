def codes_between( min, max ):
	min_num = int( min[:2] + min[3:] )
	max_num = int( max[:2] + max[3:] )
	codes = []
	for i in range( min_num+1, max_num, 1 ):
		length = len( str(i) )
		new_code = (5-length)*"0" + str(i)
		codes.append( new_code[:2] + "-" + new_code[2:] )
	return codes

def missing_in_list( numbers, n ):
	missing = []
	for i in range(1, n+1, 1):
		if not ( i in numbers ):
			missing.append(i)
	return missing

def list_of_decimals( min, max, step ):
	decimals = []
	current = min
	while( current <= max ):
		decimals.append( float(current) )
		current +=step
	return decimals



codes = codes_between( "79-900", "80-155" )
print(codes)

missing_numbers = missing_in_list( [2, 3, 7, 4, 9], 10 )
print(missing_numbers)

decimals = list_of_decimals( 2, 5.5, 0.5 )
print(decimals)