def ln(N):
	lo = 0
	hi = N
	while lo < hi:
		mid = (lo+hi)/2
		if mid**2 < N:
			lo = mid
		if mid**2 > N:
			hi = mid
		if abs(mid**2 - N) < 0.01:
			return mid
	return 'Error'

def recursive(N):
    return recursive1(N,1)

def recursive1(N, result):
	if N == 1:
		return result
	if N > 1:
		result *= N
		return recursive1(N-1, result)

if __name__ == "__main__":
	N = (float)(input())
	print (ln(recursive(N)))
