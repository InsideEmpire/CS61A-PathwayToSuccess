(define (ascending? s)
    (if (or (null? s) (null? (cdr s)))
        #t
        (if (> (car s) (car (cdr s)))
            #f
            (ascending? (cdr s))
        )
    )
)

(define (my-filter pred s)
    (if (null? s)
        nil
        (if (pred (car s))
            (cons (car s) (my-filter pred (cdr s)))
            (my-filter pred (cdr s))
        )
    )
)

(define (interleave lst1 lst2) 
    (cond ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (append (list (car lst1) (car lst2)) (interleave (cdr lst1) (cdr lst2))))
    )
)

(define (no-repeats s) 
    (define (not_equal_maker a)
        (define (not_equal b)
            (not (= a b))
        )
        not_equal
    )
    (if (null? s)
        nil
        (cons (car s) (filter (not_equal_maker (car s)) (no-repeats (cdr s))))
    )
)
