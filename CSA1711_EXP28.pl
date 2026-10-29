
% Experiment 28: Medical Diagnosis using Prolog

symptom(fever, flu).
symptom(cough, flu).
symptom(body_pain, flu).

symptom(sneezing, cold).
symptom(runny_nose, cold).
symptom(cough, cold).

symptom(fever, malaria).
symptom(chills, malaria).
symptom(headache, malaria).

diagnosis(Patient, Disease) :-
    has_symptom(Patient, Symptom),
    symptom(Symptom, Disease).

has_symptom(john, fever).
has_symptom(john, cough).
has_symptom(john, body_pain).

has_symptom(mary, sneezing).
has_symptom(mary, runny_nose).

main :-
    write('Medical Diagnosis System'), nl,
    write('John symptoms: fever, cough, body_pain'), nl,
    write('Possible diagnosis for John:'), nl,
    ( diagnosis(john, Disease),
      write(Disease), nl,
      fail
    ; true
    ),
    write('Mary symptoms: sneezing, runny_nose'), nl,
    write('Possible diagnosis for Mary:'), nl,
    ( diagnosis(mary, Disease2),
      write(Disease2), nl,
      fail
    ; true
    ).

:- initialization(main, main).
