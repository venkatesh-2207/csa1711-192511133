% Experiment 30: Backward Chaining using Prolog

fact(sunny).
fact(warm).
fact(holiday).

rule(picnic, [sunny, warm]).
rule(beach_trip, [picnic, holiday]).

prove(X) :-
    fact(X).

prove(X) :-
    rule(X, Conditions),
    prove_all(Conditions).

prove_all([]).

prove_all([H|T]) :-
    prove(H),
    prove_all(T).
