// https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem

public class Node {
  int data; 
  Node left; 
  Node right;
}

public class BinaryTreeChecker {
  public static boolean checkBST(Node root) {
    return checkNode(root, 0, (int)1e4);
  }

  private static boolean checkNode(Node node, int min, int max) {
    if (node == null) { return true; }
    if (node.data <= min || node.data >= max) { return false; }
    return checkNode(node.left, min, node.data) && checkNode(node.right, node.data, max);
  }
}



