
% Experiment 29: Forward Chaining using Prolog

rule(flu, [fever, cough, body_pain]).
rule(cold, [sneezing, runny_nose]).
rule(malaria, [fever, chills, headache]).

fact(fever).
fact(cough).
fact(body_pain).
fact(chills).
fact(headache).

all_true([]).
all_true([H|T]) :-
    fact(H),
    all_true(T).

derive(Disease) :-
    rule(Disease, Conditions),
    all_true(Conditions).

main :-
    write('Forward Chaining in Prolog'), nl,
    write('Known facts: fever, cough, body_pain, chills, headache'), nl,
    write('Derived conclusions:'), nl,
    ( derive(Disease),
      write('Disease: '),
      write(Disease), nl,
      fail
    ; true
    ).

:- initialization(main, main).
