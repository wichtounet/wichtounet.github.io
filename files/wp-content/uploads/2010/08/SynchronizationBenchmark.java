package com.wicht;

import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

import com.wicht.benchmark.utils.Benchs;

public class SynchronizationBenchmark {
    private static final int ITERATIONS = 8388608;
    private static final int MAX_THREADS = 256;

    public static void main(String[] args) {
        new SynchronizationBenchmark().start();
    }

    private void start() {
        startSimpleBenchmark();
        startMultiThreadedBenchmark();
    }

    private void startSimpleBenchmark() {
        Benchs benchmarks = new Benchs("Synchronization benchmark");

        benchmarks.setFolder("/home/wichtounet/Desktop/Graphs/");

        benchmarks.bench("Synchronized method", new SynchronizedRunnable());
        benchmarks.bench("Reentrant Lock (Unfair)", new ReentrantLockRunnable(false));
        benchmarks.bench("Reentrant Lock (Fair)", new ReentrantLockRunnable(true));
        benchmarks.bench("Semaphore (Unfair)", new SemaphoreRunnable(false));
        benchmarks.bench("Semaphore (Fair)", new SemaphoreRunnable(true));
        benchmarks.bench("Atomic Integer", new AtomicIntegerRunnable());

        benchmarks.generateCharts();
    }

    private void startMultiThreadedBenchmark() {
        for (int i = 2; i <= MAX_THREADS; i *= 2) {
            startThreaded(i);
        }
    }

    private void startThreaded(int threads) {
        Graphs graphs = new Graphs("Synchronization - " + threads + " threads");

        graphs.setFolder("/home/wichtounet/Desktop/Graphs/");

        bench("Synchronized Method", threads, new SynchronizedRunnable(), graphs);

        bench("Reentrant Lock (Unfair)", threads, new ReentrantLockRunnable(false), graphs);

        if (threads < 8) {
            bench("Reentrant Lock (Fair)", threads, new ReentrantLockRunnable(true), graphs);
        }

        bench("Semaphore (Unfair)", threads, new SemaphoreRunnable(false), graphs);

        if (threads < 8) {
            bench("Semaphore (Fair)", threads, new SemaphoreRunnable(true), graphs);
        }

        bench("Atomic Integer", threads, new AtomicIntegerRunnable(), graphs);
        
        graphs.generateCharts();
    }

    private void bench(String name, int threads, final Runnable runnable, Graphs graphs) {
        ExecutorService pool = Executors.newCachedThreadPool();

        final CyclicBarrier ready = new CyclicBarrier(threads);
        final CyclicBarrier end = new CyclicBarrier(threads + 1);

        long nanoTime = System.nanoTime();

        for (int i = 0; i < threads; i++) {
            pool.submit(new Runnable() {
                @Override
                public void run() {
                    try {
                        ready.await();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    } catch (BrokenBarrierException e) {
                        e.printStackTrace();
                    }

                    for (int j = 0; j < ITERATIONS; j++) {
                        runnable.run();
                    }

                    try {
                        end.await();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    } catch (BrokenBarrierException e) {
                        e.printStackTrace();
                    }
                }
            });
        }

        try {
            end.await();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (BrokenBarrierException e) {
            e.printStackTrace();
        }

        double duration = (double) (System.nanoTime() - nanoTime);

        graphs.addResult(name, duration / 1000 / 1000 / 1000);

        pool.shutdown();
    }

    private class SynchronizedRunnable implements Runnable {
        private int counter = 0;

        @Override
        public synchronized void run() {
            counter++;
        }
    }

    private class ReentrantLockRunnable implements Runnable {
        private int counter = 0;

        private Lock lock;

        private ReentrantLockRunnable(boolean fair) {
            super();

            lock = new ReentrantLock(fair);
        }

        @Override
        public void run() {
            lock.lock();

            try {
                counter++;
            } finally {
                lock.unlock();
            }
        }

    }

    private class SemaphoreRunnable implements Runnable {
        private int counter = 0;

        private final Semaphore semaphore;

        private SemaphoreRunnable(boolean fair) {
            super();

            semaphore = new Semaphore(1, fair);
        }

        @Override
        public void run() {
            try {
                semaphore.acquire();
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }

            try {
                counter++;
            } finally {
                semaphore.release();
            }
        }

    }

    private class AtomicIntegerRunnable implements Runnable {
        private AtomicInteger counter = new AtomicInteger(0);

        @Override
        public void run() {
            counter.incrementAndGet();
        }
    }
}
