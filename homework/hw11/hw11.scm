(define (find s predicate)
  (cond ((predicate (car s)) (car s))
  ((null? (cdr-stream s)) #f)
  (else (find (cdr-stream s) predicate))
))

(define (scale-stream s k)
  ;; (cond ((null? s) s)
  ;;       (else (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k)))
  ;; )
  (if (null? s) s
      (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k))
  )
)

(define (has-cycle s)
  (define (helper-cycle s origin)
    (cond ((null? (cdr-stream s)) #f)
          ((eq? origin (cdr-stream s)) #t)
          (else (helper-cycle (cdr-stream s) origin))
    )
  )
  (helper-cycle s s)
)


(define (a-in-stream s a)
	(if (null? s)
		#f
		(if (eq? (car s) a)
			#t
			(a-in-stream (cdr-stream s) a))))

(define (has-cycle s)
	(define (helper s prev)
		(if (null? s)
			#f
			(if (a-in-stream prev (car s))
				#t
				(helper 
					(cdr-stream s) 
					(cons-stream 
						(car s) 
						prev))))
	)

	(helper s nil)
)


;; (define (has-cycle s)
;;   (define (cycle-tracker so-far cur)
;;     (cond ((null? cur) #f)
;;       ((contains s0-far cur) #t)
;;       (else (cycle-tracker (cons-stream cur so-far) (cdr-stream cur))
;;     )
;;   )
;;   (cycle-tracker nil s)
;; )

;; (define (contains lst s)
;;   (cond ((null? lst) #f)
;;         ((eq? s (car lst)) #t)
;;         (else (contains (cdr-stream lst) s))
;;   )
;; )
;; (define (has-cycle-constant s)
;;   'YOUR-CODE-HERE
;; )



;; (define (has-cycle-constant s)
;; 	(define (helper fast slow)
;; 		(cond 
;; 			((or (null? fast) 
;; 				 (null? (cdr-stream fast))) 
;; 					#f)
;; 			((or (eq? fast slow) 
;; 				 (eq? (cdr-stream fast) slow)) 
;; 					#t)
;; 			(helper (cdr-stream (cdr-stream fast)) 
;; 					(cdr-stream slow))
;; 		)
;; 	)
;; 	(helper (cdr-stream s) s)
;; )
