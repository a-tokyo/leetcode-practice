import java.util.concurrent.CountDownLatch;

class Foo {
    private final CountDownLatch latchFirst = new CountDownLatch(1);
    private final CountDownLatch latchSecond = new CountDownLatch(1);

    public Foo() {
        
    }

    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        latchFirst.countDown();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        latchFirst.await();
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        latchSecond.countDown();
    }

    public void third(Runnable printThird) throws InterruptedException {
        latchSecond.await();
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}