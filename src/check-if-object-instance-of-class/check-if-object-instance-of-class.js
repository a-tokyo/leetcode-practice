function checkIfInstanceOf(obj: any, classFunction: any): boolean {
    if (obj == null || typeof classFunction !== 'function') return false;
    
    let prototype = Object.getPrototypeOf(obj);
    const prototypeOfClass = classFunction.prototype;
    
    while (prototype != null) {
        if (prototype === prototypeOfClass) return true;
        prototype = Object.getPrototypeOf(prototype);
    }
    return false;
}