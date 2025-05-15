type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    const cache = {};
    return function(...args) {
        const args_key = JSON.stringify(args);
        if (cache.hasOwnProperty(args_key)) {
            return cache[args_key];
        }
        const result = fn(...args);
        cache[args_key] = result;
        return result;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */