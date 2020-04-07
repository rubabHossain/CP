// https://codeforces.com/contest/474/problem/B
// CodeForces Round 271
// B. Worms

import java.util.Scanner;


public class CF474B {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in); 
        
        // int numPiles = Integer.parseInt(in.nextLine());
        int numPiles = in.nextInt();
        int[] piles = new int[numPiles];
        for(int i = 0; i < numPiles; i++) {
            int t = in.nextInt();
            piles[i] = i == 0 ? t : t + piles[i-1];
        }


        // int numTargets = Integer.parseInt(in.nextLine());
        int numTargets = in.nextInt();
        int[] targets = new int[numTargets];
        for(int i = 0; i < numTargets; i++)
            targets[i] = in.nextInt();
        
        for(int t : targets)
            System.out.println(binSearch(t, piles) + 1);
        
        // int target = 11;
        // int[] piles = {2, 7, 3, 4, 9};

        // int[] prefix = new int[piles.length];
        // int cumSum = 0;
        // for(int i = 0; i < piles.length; i++) {
        //     cumSum += piles[i];
        //     prefix[i] = cumSum;
        // }
        // for(int p: prefix)
        //     System.out.println(p);

        // System.out.println(binSearch(target, prefix) + 1);

    }

    public static int binSearch(int target, int[] piles) {
        int left = 0, right = piles.length - 1;
        int bestGuess;

        while(right-left > 1) {
            // System.out.println("Left: " + left + " Right: " + right);
            bestGuess = (left + right) / 2;
            int mid = piles[bestGuess];
            // System.out.println(bestGuess);
            if(target <= mid) {
                right = bestGuess;
            } else if (target > mid) {
                left = bestGuess;
            } else { System.out.println("sth went wrong;"); return -1; }

            
        }

        return (piles[left] >= target)? left : right;
    }
}

