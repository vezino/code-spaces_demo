def monotonicDecreasing(nums):
    stack = []
    result = []
    print("Starting ...")
    print(f"nums: {nums}")
    print(f"stack: {stack}")

    # Traverse the array
    for num in nums:
        # While stack is not empty AND top of stack is less than the current element
        print(f"num: {num} ; stack: {stack}")
        # print(f"stack: {stack}")
        print("before while")
        t = 0
        while stack and stack[-1] < num:
            print(f"inside while: t: {t}")
            print(f"stack: {stack}")
            print(f"stack[-1]: {stack[-1]}")
            # Pop the top element from the stack
            stack.pop()
            print(f"after pop,stack: {stack}")
            t = t + 1

        print("End While")
        # Construct the result array
        if stack:
            result.append(stack[-1])

        else:
            result.append(-1)

        # Push the current element into the stack
        stack.append(num)

    return result


# Example usage:
nums_test = [3, 1, 4, 1, 5, 9, 2, 6]
result_test = monotonicDecreasing(nums_test)
print("Monotonic decreasing stack:", result_test)
