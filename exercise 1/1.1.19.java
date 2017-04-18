public class Fibonacci { 
	public static long F(int N) { //faster one
		long current = 0;
		long after = 1;
		for (int i = 0; i < N; i++) {
			long temp;
			temp = after;
			after = after + current;
			current = temp;
		}
		return current;
	}
	
	public static long F1(int N) {
		if (N == 0) return 0;
		if (N == 1) return 1;
		return F1(N-1) + F1(N-2);
	}
	
	public static void main(String[] args) {
		for (int N = 0; N < 100; N++)
			StdOut.println(N + " " + F(N));
	}
