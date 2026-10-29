
% Experiment 21: Towers of Hanoi
% Aim: Solve Towers of Hanoi using recursion.

hanoi(0, _, _, _) :- !.

hanoi(N, Source, Destination, Auxiliary) :-
    N > 0,
    N1 is N - 1,
    hanoi(N1, Source, Auxiliary, Destination),
    format('Move disk ~w from ~w to ~w~n',
           [N, Source, Destination]),
    hanoi(N1, Auxiliary, Destination, Source).

main :-
    writeln('Towers of Hanoi Problem'),
    writeln('Number of disks: 3'),
    hanoi(3, a, c, b),
    writeln('Total moves: 7').

:- initialization(main, main).
