% Experiment 30: Backward Chaining using Prolog

% Facts
fact(sunny).
fact(warm).
fact(holiday).

% Rules
rule(picnic, [sunny, warm]).
rule(beach_trip, [picnic, holiday]).

% Backward chaining
prove(X) :-
    fact(X).

prove(X) :-
    rule(X, Conditions),
    prove_all(Conditions).

% Check all conditions
prove_all([]).

prove_all([H|T]) :-
    prove(H),
    prove_all(T).

% Required queries:
% ?- prove(picnic).
% ?- prove(beach_trip).
% ?- prove(rainy).
