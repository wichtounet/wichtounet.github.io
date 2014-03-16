package com.wicht;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.Closeable;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.Reader;
import java.io.Writer;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;

import bb.science.FormatUtil;
import bb.util.Benchmark;
import bb.util.Benchmark.Params;

public final class FileCopyBenchmark {
    private static final Params params = new Params();

    static {
        params.setConsoleFeedback(false);
        params.setEstimateNoiseFloor(true);
    }

    public static void main(String[] args) {
        System.out.println("Bench on the same disk");
        bench("/home/wichtounet/Desktop/src/", "/home/wichtounet/Desktop/target/");

        System.out.println("Bench between two disks");
        bench("/home/wichtounet/Desktop/src/", "/media/Data3/tmp/");
    }

    private static void bench(String disk1, String disk2) {
        bench(disk1, disk2, true, "little-text", "medium-text", "big-text", "fat-text");
        bench(disk1, disk2, false, "little-binary", "medium-binary", "big-binary", "fat-binary", "enormous-binary");
    }

    private static void bench(String disk1, String disk2, boolean text, String... files) {
        int size = 1;

        for (String file : files) {
            System.out.println("Start benchmark with " + file);

            File fileIn = new File(disk1 + file);
            File fileOut = new File(disk2 + file);

            bench(fileIn, fileOut, size++, text);
        }
    }

    private static void bench(final File in, final File out, int size, boolean text) {
        bench("Native Copy", new Runnable() {
            @Override
            public void run() {
                nativeCopy(in, out);
                out.delete();
            }
        });

        if (size < 3) {
            bench("Naive Streams", new Runnable() {
                @Override
                public void run() {
                    naiveStreamsCopy(in, out);
                    out.delete();
                }
            });
        }

        if (size < 4 && text) {
            bench("Naive Readers", new Runnable() {
                @Override
                public void run() {
                    naiveReaderCopy(in, out);
                    out.delete();
                }
            });
        }

        if (size < 5) {
            bench("Buffered Streams", new Runnable() {
                @Override
                public void run() {
                    bufferedStreamsCopy(in, out);
                    out.delete();
                }
            });
        }

        if (size < 5 && text) {
            bench("Buffered Readers", new Runnable() {
                @Override
                public void run() {
                    bufferedReaderCopy(in, out);
                    out.delete();
                }
            });
        }

        bench("Custom Buffer Streams", new Runnable() {
            @Override
            public void run() {
                customBufferStreamCopy(in, out);
                out.delete();
            }
        });

        if (text) {
            bench("Custom Buffer Readers", new Runnable() {
                @Override
                public void run() {
                    customBufferReaderCopy(in, out);
                    out.delete();
                }
            });
        }

        bench("Custom Buffer Buffered Streams", new Runnable() {
            @Override
            public void run() {
                customBufferBufferedStreamCopy(in, out);
                out.delete();
            }
        });

        if (text) {
            bench("Custom Buffer Buffered Readers", new Runnable() {
                @Override
                public void run() {
                    customBufferBufferedReaderCopy(in, out);
                    out.delete();
                }
            });
        }

        bench("NIO Buffer", new Runnable() {
            @Override
            public void run() {
                nioBufferCopy(in, out);
                out.delete();
            }
        });

        bench("NIO Transfer", new Runnable() {
            @Override
            public void run() {
                nioTransferCopy(in, out);
                out.delete();
            }
        });
    }

    private static void bench(String methodName, Runnable runnable) {
        Benchmark nativeBenchmark = new Benchmark(runnable, params);

        System.out.println(methodName + " results : " + FormatUtil.toEngineeringTime(nativeBenchmark.getMean(), 3));
        System.out.println(nativeBenchmark.toStringFull());
    }

    private static void naiveStreamsCopy(File source, File target) {
        InputStream fin = null;
        OutputStream fout = null;
        try {
            fin = new FileInputStream(source);
            fout = new FileOutputStream(target);

            int c;
            while ((c = fin.read()) != -1) {
                fout.write(c);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            close(fin);
            close(fout);
        }
    }

    private static void naiveReaderCopy(File source, File target) {
        Reader fin = null;
        Writer fout = null;
        try {
            fin = new FileReader(source);
            fout = new FileWriter(target);

            int c;
            while ((c = fin.read()) != -1) {
                fout.write(c);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            close(fin);
            close(fout);
        }
    }

    private static void bufferedStreamsCopy(File source, File target) {
        InputStream fin = null;
        OutputStream fout = null;
        try {
            fin = new BufferedInputStream(new FileInputStream(source));
            fout = new BufferedOutputStream(new FileOutputStream(target));

            int data;
            while ((data = fin.read()) != -1) {
                fout.write(data);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            close(fin);
            close(fout);
        }
    }

    private static void bufferedReaderCopy(File source, File target) {
        Reader fin = null;
        Writer fout = null;
        try {
            fin = new BufferedReader(new FileReader(source));
            fout = new BufferedWriter(new FileWriter(target));

            int c;
            while ((c = fin.read()) != -1) {
                fout.write(c);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            close(fin);
            close(fout);
        }
    }

    private static void customBufferStreamCopy(File source, File target) {
        InputStream fis = null;
        OutputStream fos = null;
        try {
            fis = new FileInputStream(source);
            fos = new FileOutputStream(target);

            byte[] buf = new byte[4096];

            int i;
            while ((i = fis.read(buf)) != -1) {
                fos.write(buf, 0, i);
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        } finally {
            close(fis);
            close(fos);
        }
    }

    private static void customBufferReaderCopy(File source, File target) {
        Reader fin = null;
        Writer fout = null;
        try {
            fin = new FileReader(source);
            fout = new FileWriter(target);

            char[] buf = new char[2048];

            int i;
            while ((i = fin.read(buf)) != -1) {
                fout.write(buf, 0, i);
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        } finally {
            close(fin);
            close(fout);
        }
    }

    private static void customBufferBufferedStreamCopy(File source, File target) {
        InputStream fis = null;
        OutputStream fos = null;
        try {
            fis = new BufferedInputStream(new FileInputStream(source));
            fos = new BufferedOutputStream(new FileOutputStream(target));

            byte[] buf = new byte[4096];

            int i;
            while ((i = fis.read(buf)) != -1) {
                fos.write(buf, 0, i);
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        } finally {
            close(fis);
            close(fos);
        }
    }

    private static void customBufferBufferedReaderCopy(File source, File target) {
        Reader fin = null;
        Writer fout = null;
        try {
            fin = new BufferedReader(new FileReader(source));
            fout = new BufferedWriter(new FileWriter(target));

            char[] buf = new char[2048];

            int i;
            while ((i = fin.read(buf)) != -1) {
                fout.write(buf, 0, i);
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        } finally {
            close(fin);
            close(fout);
        }
    }

    private static void nioBufferCopy(File source, File target) {
        FileChannel in = null;
        FileChannel out = null;

        FileInputStream inStream = null;
        FileOutputStream outStream = null;

        try {
            inStream = new FileInputStream(source);
            outStream = new FileOutputStream(target);

            in = inStream.getChannel();
            out = outStream.getChannel();

            ByteBuffer buffer = ByteBuffer.allocate(4096);
            while (in.read(buffer) != -1) {
                buffer.flip();
                out.write(buffer);
                buffer.clear();
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            close(inStream);
            close(in);
            close(outStream);
            close(out);
        }
    }

    private static void nioTransferCopy(File source, File target) {
        FileChannel in = null;
        FileChannel out = null;

        FileInputStream inStream = null;
        FileOutputStream outStream = null;

        try {
            inStream = new FileInputStream(source);
            outStream = new FileOutputStream(target);

            in = inStream.getChannel();
            out = outStream.getChannel();

            in.transferTo(0, in.size(), out);
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            close(inStream);
            close(in);
            close(outStream);
            close(out);
        }
    }

    private static void nativeCopy(File source, File target) {
        String[] args = new String[]{
                "/bin/cp",
                source.getAbsolutePath(),
                target.getAbsolutePath()
        };

        Process p = null;
        try {
            p = Runtime.getRuntime().exec(args);
            p.waitFor();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            if (p != null) {
                close(p.getInputStream());
                close(p.getErrorStream());
                close(p.getOutputStream());

                p.destroy();
            }
        }
    }

    private static void close(Closeable closable) {
        if (closable != null) {
            try {
                closable.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
