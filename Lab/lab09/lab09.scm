(define (over-or-under num1 num2) 
  (cond 
    ((< num1 num2) -1)
    ((< num2 num1) 1)
    ((= num1 num2) 0)
  )
)

(define (make-adder num) 
  (define (adder inc)
    (+ num inc)
  )
  adder
)

(define (composed f g) 
  (define (compose_f_g num)
    (f (g num))
  )
  compose_f_g
)

(define (repeat f n) 'YOUR-CODE-HERE)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 'YOUR-CODE-HERE)
