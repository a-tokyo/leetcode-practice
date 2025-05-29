function fizzBuzz(n: number): string[] {
    return Array(n).fill('').map((_, i) => {
        if ((i+1) % 15 === 0) return "FizzBuzz"
        if ((i+1) % 3 === 0) return "Fizz"
        if ((i+1) % 5 === 0) return "Buzz"
        return String(i + 1)
    });
};