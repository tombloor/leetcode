import { twoSum } from '../src/1_two_sum';

describe("example cases", () => {
    it.each([
        [[2,7,11,15], 9, [0,1]],
        [[3,2,4], 6, [1, 2]],
        [[3,3], 6, [0, 1]]
    ])("array %s, target %s", (arr, target, expected) => {
        let result = twoSum(arr, target);
        expect(result).toEqual(expected);
    });
});