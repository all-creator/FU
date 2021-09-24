package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.function.UnaryOperator;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MainActivity extends AppCompatActivity {

    TextView mainTextView;
    Button mainButton;
    private static long score = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mainTextView = findViewById(R.id.clicks);
        mainButton = findViewById(R.id.click_add_btn);
        mainButton.setOnClickListener(updateScore(v -> score++));

        mainButton = findViewById(R.id.set_zero_btn);
        mainButton.setOnClickListener(updateScore(v -> score = 0L));

        mainButton = findViewById(R.id.click_remove_btn);
        mainButton.setOnClickListener(updateScore(v -> score--));
    }

    private String getScoreString() {
        String s_score = String.valueOf(score);
        String s;
        byte numeric = (byte) (score % 10);
        return mainTextView.getText().toString().replaceFirst("[-0-9]", "*")
                .replaceAll("[-0-9]", "").replaceAll("\\*", s_score)
                .replaceAll(numeric <= 1 || numeric >= 5 ? "раза+" : "раз.*",
                        numeric == 1 || numeric >= 5 ? "раз" : "раза");
    }

    private View.OnClickListener updateScore(final UnaryOperator<Long> operator) {
        return view -> {
            operator.apply(score);
            this.mainTextView.setText(getScoreString().toCharArray(), 0, getScoreString().length());
        };
    }
}