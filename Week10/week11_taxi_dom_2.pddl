;Header and description

(define (domain taxi_advance)

    (:requirements :strips :equality :typing :conditional-effects)

    (:types person taxi location)


    (:predicates ;todo: define predicates here
        (outsidetaxi ?p - person)
        (intaxi ?p - person ?t - taxi)
        (plocation ?p - person ?loc - location)
        (tlocation ?t - taxi ?loc - location)
        (connects ?from - location ?to - location)
    )


    ;;define actions here
    (:action get_in
       :parameters (?p - person ?t - taxi ?loc - location)
       :precondition (and (plocation ?p ?loc) (tlocation ?t ?loc) (outsidetaxi ?p))
       :effect (and (intaxi ?p ?t) (not (outsidetaxi ?p)) (not (plocation ?p ?loc)))
    )

    (:action get_out
        :parameters (?p - person ?t - taxi ?loc - location)
        :precondition (and (tlocation ?t ?loc) (intaxi ?p ?t))
        :effect (and (outsidetaxi ?p) (not (intaxi ?p ?t)) (plocation ?p ?loc))
    )

    (:action move
        :parameters (?t - taxi ?from - location ?to - location)
        :precondition (and (tlocation ?t ?from) (connects ?from ?to))
        :effect (and 
                    (not (tlocation ?t ?from))
                    (tlocation ?t ?to)
                )
    )



)