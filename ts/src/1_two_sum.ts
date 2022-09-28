export function twoSum(nums: number[], target: number): number[] {
    let compliments: {[key: number]: number} = {};

    for (let i = 0; i < nums.length; i++) {
        let c = target - nums[i];
        
        if (compliments[nums[i]] !== undefined) {
            return [compliments[nums[i]], i];
        } else {
            compliments[c] = i;
        }
    }

    return [];
};