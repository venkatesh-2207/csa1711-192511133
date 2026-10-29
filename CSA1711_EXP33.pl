
% Experiment 33: Count vowels in a word

vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

count_vowels([], 0).
count_vowels([H|T], N) :-
    count_vowels(T, N1),
    (vowel(H) -> N is N1 + 1 ; N is N1).
