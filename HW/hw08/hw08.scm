(define (ascending? s)
    (if (or (null? s) (null? (cdr s)))
        #t
        (if (> (car s) (car (cdr s)))
            #f
            (ascending? (cdr s))
        )
    )
)

(define (my-filter pred s) 'YOUR-CODE-HERE)

(define (interleave lst1 lst2) 'YOUR-CODE-HERE)

(define (no-repeats s) 'YOUR-CODE-HERE)
