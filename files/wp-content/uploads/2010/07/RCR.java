package org.jtheque.rcr;

import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.regex.Pattern;

/*
 * Copyright JTheque (Baptiste Wicht)
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * Replace Copyright. Really simple class that made a replace of a copyright from all
 * the files in one folder to an other copyright.
 *
 * @author Baptiste Wicht
 */
public final class RCR {
    private static final Pattern PATTERN = Pattern.compile("\n");

    /**
     * Launch the replacement.
     * Usage : java RCR old_file new_file folder
     *
     * @param args The args of the replace.
     */
    public static void main(String... args){
        if(args.length < 3){
            System.out.println("Not enough args");
            System.out.println("Usage : java RCR old_file new_file folder");
            System.exit(-1);
        }

        replaceCopyright(
                new File(args[2]),
                PATTERN.split(getContent(args[0])),
                getContent(args[1]));
    }

    /**
     * Return the content of the given file.
     *
     * @param path The path to the file.
     *
     * @return The content of the file. 
     */
    private static String getContent(String path) {
        StringBuilder content = new StringBuilder(500);

        Scanner scanner = null;

        try {
            scanner = new Scanner(new File(path));

            while (scanner.hasNextLine()) {
                content.append(scanner.nextLine()).append('\n');
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } finally {
            if (scanner != null) {
                scanner.close();
            }
        }

        return content.toString();
    }

    /**
     * Replace the copyright old with the copyright new in the given file. If the given file is a folder,
     * it will be browsed recursively and all the files will be copyright replaced.
     *
     * @param file The file, or folder, in which we must made the replace.
     * @param oldCopyright The old copyright.
     * @param newCopyright The new copyright.
     */
    private static void replaceCopyright(File file, String[] oldCopyright, String newCopyright){
        if(file.isHidden()){
            return;
        }

        if(file.isDirectory()){
            for(File f : file.listFiles()){
                replaceCopyright(f, oldCopyright, newCopyright);
            }

            return;
        }

        StringBuilder buffer = replaceContent(file, oldCopyright, newCopyright);

        if(buffer != null){
            replaceContent(file, buffer);

            System.out.println(file.getAbsolutePath()  + " changed copyright");
        } else {
            System.out.println(file.getAbsolutePath() + " no changes");
        }
    }

    /**
     * Return the content of the file with the new copyright instead of the old.
     *
     * @param file The file.
     * @param oldCopyright The old copyright.
     * @param newCopyright The new copyright.
     *
     * @return A StringBuilder containing the new content of the file or null if the file has not changed. 
     */
    private static StringBuilder replaceContent(File file, String[] oldCopyright, String newCopyright) {
        StringBuilder buffer = new StringBuilder((int) file.length());

        boolean changes = false;

        Scanner scanner = null;
        try {
            scanner = new Scanner(file);

            int current = 0;
            StringBuilder temp = new StringBuilder(500);

            while(scanner.hasNextLine()){
                String line = scanner.nextLine();

                if(line.trim().equals(oldCopyright[current].trim())){
                    temp.append(line).append('\n');
                    current++;

                    if(current == oldCopyright.length){
                        buffer.append(newCopyright).append('\n');
                        current = 0;
                        temp.setLength(0);
                        changes = true;
                    }
                } else {
                    if(current > 0){
                        current = 0;
                        buffer.append(temp.toString()).append(line).append('\n');
                        temp.setLength(0);
                    } else {
                        buffer.append(line).append('\n');
                    }
                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } finally {
            if (scanner != null) {
                scanner.close();
            }
        }

        return changes ? buffer : null;
    }

    /**
     * Replace the content of the file with the content of the given buffer.
     *
     * @param file The file to write in.
     * @param buffer The buffer to get the data. 
     */
    private static void replaceContent(File file, StringBuilder buffer) {
        PrintWriter writer = null;

        try {
            writer = new PrintWriter(new BufferedOutputStream(new FileOutputStream(file)));

            writer.write(buffer.toString());
            writer.flush();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } finally {
            if (writer != null) {
                writer.close();
            }
        }
    }
}