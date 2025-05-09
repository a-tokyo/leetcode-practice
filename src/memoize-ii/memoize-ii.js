function memoize(fn) {
    const cache = new Map();

    return function (...args) {
        let node = cache;

        for (let arg of args) {
            if (!node.has(arg)) {
               node.set(arg, new Map());
            }
            node = node.get(arg);
        }

        if (node.has("__result__")) {
            return node.get("__result__");
        }

        const result = fn(...args);
        node.set("__result__", result);
        return result;
    };
}