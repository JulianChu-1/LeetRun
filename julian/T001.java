import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class T001 {
    public int[] twoSum(int[] nums, int target) {
        // 两层遍历，最简单的方法
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }

        return new int[]{};
    }

    public int[] twoSumMap1(int[] nums, int target) {
        // 维护一个哈希表
        Map<Integer, Integer> indexMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (indexMap.containsKey(target - nums[i])) { // 查找当前是否有满足条件的值
                return new int[]{i, indexMap.get(target - nums[i])}; // 有则返回
            } else {
                indexMap.put(nums[i], i); //没有就put进哈希表中
            }
        }

        return new int[]{};
    }

    public int[] twoSumTwoPoints(int[] nums, int target) {
        // 双指针，但需要排序，这就要求复制一次数组，以免排序后找不到index
        int m = 0, n = 0, k;
        int[] res = new int[2];
        int[] temp1 = new int[nums.length];

        System.arraycopy(nums, 0, temp1, 0, nums.length);
        Arrays.sort(nums);

        for (int i = 0, j = nums.length - 1; i < j;) {
            if (nums[i] + nums[j] < target) {
                i++;
            } else if (nums[i] + nums[j] > target) {
                j--;
            } else if (nums[i] + nums[j] == target) {
                m = i;
                n = j;
                break;
            }
        }

        for (k = 0; k < nums.length; k++) {
            if (temp1[k] == nums[m]) {
                res[0] = k;
                break;
            }
        }

        for (int i = 0; i < nums.length; i++) {
            if (temp1[i] == nums[n] && i!= k) {
                res[0] = i;
                break;
            }
        }

        return res;
    }
    public static void main(String[] args) {

    }
}
