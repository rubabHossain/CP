import java.util.Map;
import java.util.HashMap;
import java.util.Random;


public class WeightedRandomNumbers {
    public static void main(String[] args) {
        
        testSimpleAdd();
        System.out.println();
        testSimpleRemove();
    }


    /**
     * Basic test, only adding things to tree
     */
    public static void testSimpleAdd() {
        
        // setup tree
        IntervalTree tree = new IntervalTree();
        tree.add("Bk", 1);
        tree.add("McD", 7);
        tree.add("AB", 1);
        tree.add("BC", 1);
        tree.add("CD", 1);
        tree.add("EF", 1);
        tree.add("GH", 1);
        tree.add("IJ", 1);

        // setup result tracking data structure
        Map<String, Integer> occurences = new HashMap<>();
        occurences.put("Bk", 0);
        occurences.put("McD", 0);
        occurences.put("AB", 0);
        occurences.put("BC", 0);
        occurences.put("CD", 0);
        occurences.put("EF", 0);
        occurences.put("GH", 0);
        occurences.put("IJ", 0);


        // test distribution
        int trials = 1000000;
        for(int i = 0; i < trials; i++) {
            String s = tree.query();
            occurences.put(s, occurences.get(s)+1);
        }

        // print distribution
        System.out.println("Simple AdditionTest Results:");
        for(String key: occurences.keySet()) 
            System.out.printf("%s occured %f\n", key, occurences.get(key) / ((float)trials));

    }


    /**
     * Basic test, adding and then reassigning existing things in tree
     */
    public static void testSimpleRemove() {
         
         // setup tree
        IntervalTree tree = new IntervalTree();
        tree.add("Bk", 1);
        tree.add("McD", 7);
        tree.add("AB", 1);
        tree.add("BC", 1);
        tree.add("CD", 1);
        tree.add("EF", 1);
        tree.add("GH", 1);
        tree.add("IJ", 1);

        // remap Bk and McD to be same
        tree.add("Bk", 4);
        tree.add("McD", 4);

        // setup result tracking data structure
        Map<String, Integer> occurences = new HashMap<>();
        occurences.put("Bk", 0);
        occurences.put("McD", 0);
        occurences.put("AB", 0);
        occurences.put("BC", 0);
        occurences.put("CD", 0);
        occurences.put("EF", 0);
        occurences.put("GH", 0);
        occurences.put("IJ", 0);
 
 
         // test distribution
         int trials = 1000000;
         for(int i = 0; i < trials; i++) {
             String s = tree.query();
             occurences.put(s, occurences.get(s)+1);
         }
 
         // print distribution
         System.out.println("Simple RemoveTest Results:");
         for(String key: occurences.keySet()) 
             System.out.printf("%s occured %f\n", key, occurences.get(key) / ((float)trials));
    }

}



/**
 * The actual data structure.
 * Note, I call this an 'Inteval Tree", but this isnt the same Interval Tree as used typically
 */
class IntervalTree {

    // inner tree node class
    private class Node {
        Node left, right;
        String key;
        int value;
        

        public Node() {
            this.value = 0;
        }

        public Node(String key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    

    Node root;
    int currId, capacity, height;
    Map<String, Integer> leafMap;
    
    Random rand = new Random();

    public IntervalTree() {
        root = new Node();
        currId = 0;                 // used to determine which leaf to put into
        capacity = 2;               // used to determine when to grow tree
        leafMap = new HashMap<>();  // used to detrmine which leaf a key is in (necessary if we are going to update the val of a key)
        height = 1;                 // used to how deep to recurse when adding to tree
    }




    public void add(String key, int value) {

        if(leafMap.containsKey(key)) {
            // if tree already has key, find cur val in tree, delete it, then add it there again
            int leafId = leafMap.get(key);
            removeFromTree(root, leafId, this.height);
            addToTree(root, key, value, leafId, this.height);
            return;
        }
        
        if(currId >= capacity) { 
            // need double tree size
            Node newRoot = new Node();
            newRoot .left = root;
            this.root = newRoot;
            this.root.value += this.root.left.value;
            this.height++;
            capacity *= 2;
        }
        addToTree(root, key, value, currId, this.height);
        leafMap.put(key, currId);
        this.currId++;
    }



    // private recursive helper for add()
    private void addToTree(Node node, String key, int value, int leafId, int height) {

        if (height == 0) {
            // have reached base of tree, return
            node.key = key;
            node.value = value;
            return;
        }

        // else, need to go down tree, going left or right
        // based on the bit at position 'height' of leafId,
        // 0 => left, 1 => right

        //get bit at index 'height' of leafId
        int direction = (leafId >> (height-1)) & 0x1;

        if(direction == 0) {

            if(node.left == null)
                node.left = new Node();
            addToTree(node.left, key, value, leafId, height -1);

        } else {

            if(node.right == null)
                node.right = new Node();
            addToTree(node.right, key, value, leafId, height -1);

        }

        node.value += value;
        return;

    }


    // private recusrive helper for add()
    private int removeFromTree(Node node, int leafId, int height) {
        if(height == 0) {
            // have reached base of tree, return
            int temp = node.value;
            node.value = 0;;
            return temp;
        }

        // else, need to go down tree, going left or right
        // based on the bit at position 'height' of leafId,
        // 0 => left, 1 => right
        int direction = (leafId >> (height-1)) & 0x1;
        int removedAmount = 0;
        if(direction == 0) {
            removedAmount = removeFromTree(node.left, leafId, height -1);
        } else {
            removedAmount = removeFromTree(node.right, leafId, height -1);
        }
        node.value -= removedAmount;
        return removedAmount;

    }



    public String query() {
        if(this.currId == 0) {
            return "Nothing inside tree";
        }
        int randomNum = rand.nextInt(this.root.value);

        return queryTree(this.root, randomNum, height);
    }



    // private recursive helper for query
    private String queryTree(Node node, int randomNum, int height) {
        if(height == 0) {
            return node.key;
        }

        if(node.left.value > randomNum) {
            // go left
            return queryTree(node.left, randomNum, height - 1);
        } else {
            // go right
            return queryTree(node.right, randomNum - node.left.value, height - 1);
        }
    }



    // debugging method
    @Override
    public String toString() {
        // TODO Auto-generated method stub
        printTree(this.root);
        return "";
    }


    // private recursive helper for toString()
    private void printTree(Node node) {

        System.out.printf("Key: %s, Value: %d\n", node.key, node.value);

        if(node.left != null) {
            System.out.println("going left");
            printTree(node.left);
            System.out.println("coming back up");
        }
        if(node.right != null) {
            System.out.println("going right");
            printTree(node.right);
            System.out.println("coming back up");
        }
    }
}