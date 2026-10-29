
% Experiment 24: Water Jug Problem
% Aim: To obtain 2 litres using a 4-litre jug
% and a 3-litre jug.

% State: state(Jug4, Jug3)

% Initial state
initial(state(0, 0)).

% Goal state: exactly 2 litres in the 4-litre jug
goal(state(2, _)).

% Fill the 4-litre jug
move(state(_, B), state(4, B), 'Fill 4-litre jug').

% Fill the 3-litre jug
move(state(A, _), state(A, 3), 'Fill 3-litre jug').

% Empty the 4-litre jug
move(state(_, B), state(0, B), 'Empty 4-litre jug').

% Empty the 3-litre jug
move(state(A, _), state(A, 0), 'Empty 3-litre jug').

% Pour from 4-litre jug into 3-litre jug
move(state(A, B), state(A1, B1), 'Pour 4-litre into 3-litre') :-
    A > 0,
    B < 3,
    T is min(A, 3 - B),
    A1 is A - T,
    B1 is B + T.

% Pour from 3-litre jug into 4-litre jug
move(state(A, B), state(A1, B1), 'Pour 3-litre into 4-litre') :-
    B > 0,
    A < 4,
    T is min(B, 4 - A),
    A1 is A + T,
    B1 is B - T.

% Search for a solution without revisiting states
solve(State, _, []) :-
    goal(State).

solve(State, Visited, [Action-Next | Path]) :-
    move(State, Next, Action),
    \+ member(Next, Visited),
    solve(Next, [Next | Visited], Path).

main :-
    writeln('Water Jug Problem'),
    initial(Start),
    (   once(solve(Start, [Start], Path))
    ->  print_path(Path),
        writeln('Goal reached: 2 litres in the 4-litre jug')
    ;   writeln('No solution found')
    ).

print_path([]).
print_path([Action-State | Rest]) :-
    format('~w -> ~w~n', [Action, State]),
    print_path(Rest).

:- initialization(main, main).
