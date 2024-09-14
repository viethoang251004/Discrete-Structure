main :-
    write('Enter your name: '),
    read_line_to_codes(user_input, Input),
    remove_trailing_whitespace(Input, CleanInput),
    atom_codes(Name, CleanInput),
    format('Hello ~w', [Name]).

remove_trailing_whitespace(Input, CleanInput) :-
    reverse(Input, Reversed),
    drop_while(=(0'\s), Reversed, Trimmed),
    reverse(Trimmed, CleanInput).

drop_while(_, [], []).
drop_while(P, [X|Xs], Trimmed) :-
    call(P, X),
    !,
    drop_while(P, Xs, Trimmed).
drop_while(_, Trimmed, Trimmed).

:- initialization(main).