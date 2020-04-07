// 01.02.2020
// https://projecteuler.net/problem=205
// Problem 205
// Dice Game

// Most of this wasn't necessary, I was just lazy.
// BigInteger class was also not necessary,
// I just Had a bug that I couldn't track for a while,
// so I just tried some random things.
import java.math.BigInteger; 


public class Problem205 {
    public static void main(String[] args) {
        
        int[] numWays_4 = new int[37]; 
        int[] numWays_6 = new int[37]; 

        for(int d1 = 1; d1 <= 4; d1++)
        for(int d2 = 1; d2 <= 4; d2++)
        for(int d3 = 1; d3 <= 4; d3++)
        for(int d4 = 1; d4 <= 4; d4++)
        for(int d5 = 1; d5 <= 4; d5++)
        for(int d6 = 1; d6 <= 4; d6++)
        for(int d7 = 1; d7 <= 4; d7++)
        for(int d8 = 1; d8 <= 4; d8++)
        for(int d9 = 1; d9 <= 4; d9++)
            numWays_4[d1+d2+d3+d4+d5+d6+d7+d8+d9]++;
        
        for(int d1 = 1; d1 <= 6; d1++)
        for(int d2 = 1; d2 <= 6; d2++)
        for(int d3 = 1; d3 <= 6; d3++)
        for(int d4 = 1; d4 <= 6; d4++)
        for(int d5 = 1; d5 <= 6; d5++)
        for(int d6 = 1; d6 <= 6; d6++)
            numWays_6[d1+d2+d3+d4+d5+d6]++;

        
        // for(int i = 9; i < numWays_4.length; i++)
        //     System.out.print(numWays_4[i] + " ");
        
        // System.out.println();

        // for(int i = 6; i < numWays_6.length; i++)
        //     System.out.print(numWays_6[i] + " ");
        
        // System.out.println();
        BigInteger p_wins = BigInteger.ZERO;
        BigInteger total = BigInteger.ZERO;

        for(int p_index = 9; p_index <= 36; p_index++) {
            for(int c_index = p_index-1; c_index >= 6; c_index--) {
                long t = (numWays_4[p_index] * numWays_6[c_index]);
                p_wins = p_wins.add(BigInteger.valueOf(t));
            }
        }
        for(int p_index = 9; p_index <= 36; p_index++) {
            for(int c_index = 6; c_index <= 36; c_index++) {
                long t = (numWays_4[p_index] * numWays_6[c_index]);
                total = total.add(BigInteger.valueOf(t));
            }
        }

        System.out.println(p_wins);
        System.out.println(total);
        
    }

    
}

