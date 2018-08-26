// Time: O(N)
// Space: O(N)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> nums_map;
        for (int i = 0; i < nums.size(); ++i) {
            int cmp_val = target - nums[i];
            auto ptr = nums_map.find(cmp_val);
            if (ptr != nums_map.end())
                return {ptr->second, i}; // return a vector as result
            nums_map[nums[i]] = i;
        }
    }
};