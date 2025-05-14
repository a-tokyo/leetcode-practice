type Entry = { value: number; expires_at: number };

const isExpired = (entry: Entry, now: number = Date.now()): boolean => entry.expires_at <= now;

class TimeLimitedCache {
    private store: Record<number, Entry> = {};
    
    set(key: number, value: number, duration: number): boolean {
        const now = Date.now();
        if (this.store[key] == undefined || isExpired(this.store[key])) {
            this.store[key] = {
                value,
                expires_at: now + duration,
            };
            return false;
        } else {
            this.store[key] = {
                value,
                expires_at: now + duration,
            };
            return true;
        }
    }
    
    get(key: number): number {
        const entry = this.store[key];
        return entry && !isExpired(entry) ? entry.value : -1;
    }
    
    count(): number {
        const now = Date.now();
        return Object.values(this.store).filter(entry => !isExpired(entry, now)).length
    }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */