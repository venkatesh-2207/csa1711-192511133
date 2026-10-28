
% Experiment 21: Towers of Hanoi

hanoi(0, _, _, _) :- !.

hanoi(N, A, C, B) :-
    N > 0,
    N1 is N - 1,
    hanoi(N1, A, B, C),
    write('Move disk '),
    write(N),
    write(' from '),
    write(A),
    write(' to '),
    writeln(C),
    hanoi(N1, B, C, A).

main :-
    writeln('Towers of Hanoi Problem'),
    write('Enter number of disks: '),
    read(N),
    ( integer(N), N >= 0 ->
        hanoi(N, a, c, b)
    ;
        writeln('Enter a non-negative integer')
    ).

:- initialization(main, main).
