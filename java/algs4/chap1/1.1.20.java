public static float ln(long N) {
		float lo = 0;
		float hi = N;
		while (lo < hi) {
			float mid = (lo + hi)/2;
			if ((mid*mid) < N)
				lo = mid;
			if ((mid*mid) > N)
				hi = mid;
			if (Math.abs(mid*mid - N) < 0.1)
				return mid;
		}
		return -1;
	}
	
	public static long recursive(long N) {
		return recursiveReal(N,1);
	}
	
	public static long recursiveReal(long N, long result) {
		if (N == 1) {
			return result;
		}
		if (N > 1) {
			result *= N;
			return recursiveReal(N-1, result);
		}
		return result;//This return can't be removed.It's confussing.
	}

	public static void main(String[] args) {
		int N = StdIn.readInt();
		StdOut.println(ln(recursive(N)));

	}
