#define MAX(X, Y) ((X) < (Y) ? (Y) : (X))

class Solution
{
private:
    int max_path_sum;

    int maxPath(TreeNode *root)
    {
        if (!root)
            return -1000;

        int root_left = maxPath(root->left);
        int root_right = maxPath(root->right);

        max_path_sum = MAX(max_path_sum, MAX(MAX(root->val, root->val + MAX(root_left, root_right)), root_left + root->val + root_right));

        return MAX(root->val, root->val + MAX(root_left, root_right));
    }

public:
    Solution() : max_path_sum(-1000) {}
    int maxPathSum(TreeNode *root)
    {
        maxPath(root);
        return max_path_sum;
    }
};
