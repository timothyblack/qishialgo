package OA_GS;

public class MinSliceWeight {

    public static void main(String[] args){

        int[][] matrix = {{1,2,3},{4,5,6},{7,8,9}};
        int res = minSliceWeight(matrix);

        System.out.println(res);

    }

    public static int minSliceWeight(int[][] matrix){

        if(matrix == null || matrix.length == 0){

            return 0;
        }

        int[][] dp = new int[matrix.length][matrix.length];

        for(int j = 0; j < matrix.length; j++){

            dp[0][j] = matrix[0][j];
        }


        for(int i = 1; i < matrix.length; i++){

            for(int j = 0; j < matrix.length; j++){

                if(j == 0){

                    dp[i][j] = Math.min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j];
                } else if(j == matrix.length - 1){

                    dp[i][j] = Math.min(dp[i-1][j-1], dp[i-1][j]) + matrix[i][j];
                } else{

                    dp[i][j] = Math.min(dp[i-1][j-1], dp[i-1][j]);
                    dp[i][j] = Math.min(dp[i][j], dp[i-1][j+1]) + matrix[i][j];
                }
            }
        }

        int globalMin = Integer.MAX_VALUE;

        for(int j = 0; j < matrix.length; j++){

            globalMin = Math.min(globalMin, dp[matrix.length-1][j] );
        }

        return globalMin;
    }
}
