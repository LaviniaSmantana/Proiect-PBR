vocale(a).
vocale(e).
vocale(i).
vocale(o).
vocale(u).

consoane(b).
consoane(c).
consoane(d).
consoane(f).
consoane(g).
consoane(h).
consoane(j).
consoane(k).
consoane(l).
consoane(m).
consoane(n).
consoane(p).
consoane(q).
consoane(r).
consoane(s).
consoane(t).
consoane(v).
consoane(w).
consoane(x).
consoane(y).
consoane(z).

regula1(Cuvant, Rezultat) :-
    atom_chars(Cuvant, Litere),
    regula1_aux(Litere, RezultatChars),
    atomic_list_concat(RezultatChars, Rezultat).

regula1_aux([X], [X]).
regula1_aux([H, X, Y | T], [H, '-' | Result]) :-
    vocale(H),
    consoane(X),
    vocale(Y),
    regula1_aux([X, Y | T], Result).
regula1_aux([H, 'c', 'h', X | T], [H, '-', 'c', 'h' | Result]) :-
    vocale(H),
    vocale(X),
    regula1_aux([X | T], Result).
regula1_aux([H, X, Y, Z | T], [H, '-', X, Y, Z | Result]) :-
    vocale(H),
    vocale(X),
    vocale(Y),
    vocale(Z),
    regula1_aux(T, Result).
regula1_aux([H, X, Y | T], [H, '-', X, Y | Result]) :-
    vocale(H),
    vocale(X),
    vocale(Y),
    regula1_aux(T, Result).
regula1_aux([H | T], [H | Result]) :-
    regula1_aux(T, Result).

regula2(Cuvant, Rezultat) :-
    atom_chars(Cuvant, Litere),
    regula2_aux(Litere, RezultatChars),
    atomic_list_concat(RezultatChars, Rezultat).

regula2_aux([X], [X]).
regula2_aux([H, X, Y | T], [H, '-' | Result]) :-
    vocale(H),
    member(X, ['b', 'c', 'd', 'f', 'g', 'h', 'p', 't', 'v']),
    member(Y, ['l', 'r']),
    regula2_aux([X, Y | T], Result).
regula2_aux([H, X, Y | T], [H, X, '-' | Result]) :-
    vocale(H),
    consoane(X),
    consoane(Y),
    regula2_aux([ Y | T], Result).
regula2_aux([H | T], [H | Result]) :-
    regula2_aux(T, Result).


despartire(Cuvant, Rezultat) :-
    regula1(Cuvant, Rezultat1),
    regula2(Rezultat1, Rezultat).