public class EX_1_1_30 {

	public static void main(String[] args) {
		int N = 10;
		boolean[][] a= new boolean[N][N];
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (i == j) {
					a[i][j] = false;
				}else {
					a[i][j] = true;
				}
			}
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				StdOut.print(a[i][j] + " ");
			}
			StdOut.print("\n");
		}

	}

}
