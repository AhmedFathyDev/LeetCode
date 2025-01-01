#define MAX(X, Y) ((X) < (Y) ? (Y) : (X))

class Solution
{
private:
    int max_path_sum;
    int maxPath(TreeNode *root)
    {
        if (!root)
            return -1000;

        int left_nodes = maxPath(root->left);
        int right_nodes = maxPath(root->right);

        max_path_sum = MAX(max_path_sum, MAX(MAX(root->val, root->val + MAX(left_nodes, right_nodes)), left_nodes + root->val + right_nodes));

        return MAX(root->val, root->val + MAX(left_nodes, right_nodes));
    }

public:
    Solution() : max_path_sum(-1000) {}

    int maxPathSum(TreeNode *root)
    {
        maxPath(root);
        return max_path_sum;
    }
};
