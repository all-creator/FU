package com.lab3;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.concurrent.atomic.AtomicLong;
import java.util.function.Predicate;
import java.util.logging.Logger;

public class Input {

    static final Logger log = Logger.getGlobal();


    public static void main(String[] args) {
        var data = new Data();
        try (BufferedReader fr = new BufferedReader(new FileReader("src/main/java/com/lab3/input.txt"))) {
            data.main = fr.lines().reduce((x, y) -> x + " \n" + y).orElse(null);
        } catch (IOException e) {
            e.printStackTrace();
        }
        AtomicLong countW = new AtomicLong(0);
        assert data.main != null;
        data.main.lines().forEach(line -> countW.set(Arrays.stream(line.trim().split(" ")).filter(Predicate.not(String::isEmpty)).count() + countW.get()));
        data.countWords = countW.get();
        data.countSpaces = data.main.chars().filter(c -> c == ' ').count();
        log.info(data.toString());
    }

    static class Data {
        private String main;
        private long countWords;
        private long countSpaces;

        @Override
        public String toString() {
            return "Data: " +
                    "main='" + main + '\'' +
                    ", countWords=" + countWords +
                    ", countSpaces=" + countSpaces;
        }
    }

}
