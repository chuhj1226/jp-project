def solution(numbers):
    var = 0
    var2 = 0
    var = max(numbers)
    numbers.remove(var)
    var2 = max(numbers)
    return var*var2