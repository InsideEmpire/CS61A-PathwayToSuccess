(define (square n) (* n n))

(define (pow base exp)
  (if (= exp 0)
    1
    (if (even? exp)
      (pow (square base) (/ exp 2))
      (* base (pow base (- exp 1)))
    )
  )
)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let (_________________)
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) 'YOUR-CODE-HERE)

(define (caddr s) 'YOUR-CODE-HERE)
