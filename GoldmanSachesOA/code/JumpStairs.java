package OA_GS;

public class JumpStairs {

    public static void main(String[] args){

        Jump s = new Jump();

        System.out.println( s.jump(3) ) ;
    }
}

class Jump{

    public int jump(int n){

        if(n<=2){
            return n;
        }

        int[] res = new int[n+1];

        int m = 3;

        res[0] = 1;
        res[1] = 1;
        res[2] = 2;



        for(int i = 3; i<=n; i++){

            res[i] = 0;
            for(int j = 1; j <= m && j <= i; j++){

                res[i] += res[i-j];
            }
        }


        return res[res.length-1];
    }
}
