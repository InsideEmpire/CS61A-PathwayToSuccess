(define (curry-cook formals body)
  (if (null? (cdr formals))
      (list 'lambda formals body)
      (list 'lambda
            (list (car formals))
            (curry-cook (cdr formals) body))
  )
)

(define (curry-consume curry args)
  'YOUR-CODE-HERE)

(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr)
  (cons _________
        (map (lambda (option)
               (cons _______________ (cdr option)))
             (car (cdr (cdr switch-expr))))))
