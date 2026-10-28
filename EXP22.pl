
% Experiment 22: Bird Flying Ability
% Aim: To check whether a bird can fly using Prolog.

% Facts
bird(sparrow).
bird(parrot).
bird(eagle).
bird(penguin).
bird(ostrich).

% Birds that cannot fly
flightless(penguin).
flightless(ostrich).

% Rule to determine whether a bird can fly
can_fly(X) :-
    bird(X),
    \+ flightless(X).

% Display the result
check_bird(X) :-
    (   can_fly(X)
    ->  format('~w can fly~n', [X])
    ;   format('~w cannot fly~n', [X])
    ).

% Main program
main :-
    writeln('Bird Flying Ability'),
    check_bird(sparrow),
    check_bird(parrot),
    check_bird(eagle),
    check_bird(penguin),
    check_bird(ostrich).

:- initialization(main, main).
