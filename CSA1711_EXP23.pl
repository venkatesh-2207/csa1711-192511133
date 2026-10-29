
% Experiment 23: Family Tree using Prolog
% Aim: To represent family relationships using facts and rules.

% Parent facts
parent(john, mary).
parent(john, david).
parent(mary, alice).
parent(mary, bob).
parent(david, charlie).

% Gender facts
male(john).
male(david).
male(bob).
male(charlie).

female(mary).
female(alice).

% Rules
father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% Display results
main :-
    writeln('Family Tree using Prolog'),
    (father(john, mary) ->
        writeln('John is the father of Mary')
    ; true),
    (mother(mary, alice) ->
        writeln('Mary is the mother of Alice')
    ; true),
    (grandparent(john, alice) ->
        writeln('John is the grandparent of Alice')
    ; true),
    (sibling(alice, bob) ->
        writeln('Alice and Bob are siblings')
    ; true).

:- initialization(main, main).
