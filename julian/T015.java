import java.util.*;

public class T015 {
    public List<List<Integer>> threeSum(int[] nums) {
        // 双指针解法
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) { return res; }

            if (i > 0 && nums[i] == nums[i - 1]) { continue; } //i去重

            int left = i + 1, right = nums.length - 1;

            while (left < right) {
                if (nums[i] + nums[left] + nums[right] == 0) {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    while (left < right && nums[left] == nums[left + 1]) { left++;}
                    while (left < right && nums[right] == nums[right - 1]) { right--;}

                    left++;
                    right--;
                } else if (nums[i] + nums[left] + nums[right] < 0) {
                    left++;
                } else if (nums[i] + nums[left] + nums[right] > 0) {
                    right--;
                }
            }
        }

        return res;
    }

    public static void main(String[] args) {

    }
}
