package com.lab3;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.text.DecimalFormat;
import java.util.*;
import java.util.function.Predicate;


public class Input {

    static final Logger log = LoggerFactory.getLogger(Input.class);


    public static void main(String[] args) {
        try (BufferedReader fr = new BufferedReader(new FileReader("src/main/java/com/lab3/input.txt"))) {
            log.info("{}", new Data(fr.lines().reduce((x, y) -> x + "\n" + y).orElse(null)).search());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static class Data {
        private final String main;
        private final long countWords;
        private final long countSpaces;

        private final long countUppercase;

        private final long countLowercase;

        private final long countChars;
        private long countSymbol = 0;

        private final List<Long> ints = new ArrayList<>();
        private final List<Double> doubles = new ArrayList<>();

        private final SearchEngine engine = new SearchEngine(this);

        public Data(String main) {
            this.main = main;
            countWords = getMain().lines().reduce(0L, (s, l) -> s + Arrays.stream(l.trim().split(" ")).filter(Predicate.not(String::isEmpty)).count(), Long::sum);
            countSpaces = getMain().chars().filter(c -> c == ' ').count();
            countUppercase = getMain().chars().filter(c -> Character.isUpperCase(c) && c != ' ').count();
            countLowercase = getMain().chars().filter(c -> Character.isLowerCase(c) && c != ' ').count();
            countChars = countLowercase + countUppercase;
            scanNum();
            withoutSymbol();
        }

        private static class SearchEngine implements Runnable {

            Data parent;

            public SearchEngine(Data parent) {
                this.parent = parent;
            }

            @Override
            public void run() {
                Scanner scanner = new Scanner(System.in);
                log.info("Engine is started.");
                var isFindByOneWord = true;
                while (true) {
                    log.info("Enter find match: ");
                    var input = scanner.nextLine();
                    if (Objects.equals(input, "exit") || Objects.equals(input, "quit") ||
                            Objects.equals(input, "q") || Objects.equals(input, "Q")) {
                        log.info("Search engine is stopped.");
                        break;
                    }
                    if (Objects.equals(input, "word-mode")) {
                        isFindByOneWord = true;
                        log.info("Search mode is word-mode");
                    }
                    else if (Objects.equals(input, "line-mode")) {
                        isFindByOneWord = false;
                        log.info("Search mode is line-mode");
                    }
                    else if (Objects.equals(input, "m")) {
                        isFindByOneWord = !isFindByOneWord;
                        log.info("Search mode is switched");
                    }
                    else {
                        log.info("Find...");
                        var fr = parent.getMain().indexOf(input);
                        if (isFindByOneWord && fr != -1) {
                            List<int[]> wordsIndex = new ArrayList<>();
                            String data = parent.getMain();
                            while (fr != -1) {
                                wordsIndex.add(new int[]{fr, fr + input.length()-1});
                                data = data.substring(fr+input.length());
                                fr = data.indexOf(input);
                            }
                            String r = listIntToString(wordsIndex);
                            log.info("Search result is: {}", r);
                        } else {
                            if (fr == -1) {
                                log.error("No match found");
                                continue;
                            }
                            var r = parent.getMain().substring(fr).split("\n")[0];
                            log.info("Search result is: {}", r);
                        }
                    }
                }
            }

            private String listIntToString(List<int[]> list) {
                StringBuilder sb = new StringBuilder();
                for (int[] i : list) {
                    sb.append(Arrays.toString(i)).append("; ");
                }
                return sb.toString();
            }
        }

        public Data search() {
            log.info("Starting search engine...");
            new Thread(engine).start();
            return this;
        }

        public void scanNum() {
            var allNum = Arrays.stream(getMain().replace(",", ".").replaceAll("[^1-9.]+", " ")
                    .split(" ")).filter(Predicate.not(String::isEmpty)).toList();
            DecimalFormat df = new DecimalFormat("#.##");
            allNum.forEach(num -> {
                try {
                    ints.add(Long.parseLong(num, 16));
                } catch (Exception e) {
                    try {
                        doubles.add(Double.valueOf(df.format(Double.parseDouble(num)).replace(",", ".")));
                    } catch (Exception ignore) {}
                }
            });
        }

        public String withoutSymbol() {
            // Реализация через StringBuilder
            StringBuilder sb = new StringBuilder();
            sb.append(getMain());
            int[] s = {-1, -1, -1, -1, -1};
            while ((s[0] = sb.indexOf("!")) != -1 || (s[1] = sb.indexOf("?")) != -1 || (s[2] = sb.indexOf(",")) != -1 ||
                    (s[3] = sb.indexOf(".")) != -1 || (s[4] = sb.indexOf("\"")) != -1) {
                for (int i : s) {
                    incS(i, sb);
                }
            }
            return sb.toString();
            // Реализация через StreamAPI
            // return getMain().replaceAll("[!?,.\"]+", "");
        }

        private void incS(int s, StringBuilder data){
            if (s != -1) {
                data.replace(s, ++s, "");
                countSymbol++;
            }
        }

        @Override
        public String toString() {
            return "input.txt content: \n'" +
                    getMain() + "'\nData of file:" +
                    " countWords=" + getCountWords() +
                    ", countSpaces=" + getCountSpaces() +
                    ", countUppercase=" + getCountUppercase() +
                    ", countLowercase=" + getCountLowercase() +
                    ", countChars=" + getCountChars() +
                    ", countSymbol=" + getCountSymbol() +
                    ", countInt=" + getInts().size() +
                    ", countDouble=" + getDoubles().size() +
                    "\nData of numbers: \nInt:" + getInts() +
                    "\nDouble:" + getDoubles() +
                    "\nContentWithoutSymbol: '" + withoutSymbol() + "'";
        }

        public String getMain() {
            return main;
        }

        public long getCountWords() {
            return countWords;
        }

        public long getCountSpaces() {
            return countSpaces;
        }

        public long getCountUppercase() {
            return countUppercase;
        }

        public long getCountLowercase() {
            return countLowercase;
        }

        public long getCountChars() {
            return countChars;
        }

        public List<Long> getInts() {
            return ints;
        }

        public List<Double> getDoubles() {
            return doubles;
        }

        public long getCountSymbol() {
            return countSymbol;
        }
    }
}
