
% Experiment 21: Towers of Hanoi

hanoi(0, _, _, _) :- !.

hanoi(N, Source, Destination, Auxiliary) :-
    N > 0,
    N1 is N - 1,
    hanoi(N1, Source, Auxiliary, Destination),
    write('Move disk '),
    write(N),
    write(' from '),
    write(Source),
    write(' to '),
    writeln(Destination),
    hanoi(N1, Auxiliary, Destination, Source).

main :-
    writeln('Towers of Hanoi Problem'),
    write('Enter number of disks: '),
    read(N),
    (integer(N), N >= 0 ->
        hanoi(N, 'A', 'C', 'B')
    ;
        writeln('Enter a non-negative integer')
    ).

:- initialization(main, main).
