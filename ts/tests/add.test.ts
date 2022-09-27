import { add } from "../src/add";

describe("valid inputs", () => {
    it.each([
        [1, 2, 3],
        [10, 11, 21],
        [1000, 9000, 10000],
        [-1, -2, -3],
        [-10, -11, -21],
        [-1000, -9000, -10000],
        [1, -2, -1],
    ])("when input is '%s' and '%s'", (a, b, expected) => {
        expect(add(a, b)).toBe(expected);
    })
});