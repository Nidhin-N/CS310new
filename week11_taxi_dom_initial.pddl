;Header and description

(define (domain taxi_simplest)

    (:requirements :strips :equality :typing :conditional-effects)

    (:types person taxi location)

    ; un-comment following line if constants are needed
    ;(:constants )

    (:predicates ;todo: define predicates here
        (at ?obj - location)
        (outsidetaxi ?p - person)
        (intaxi ?p - person)
        (plocation ?p - person ?loc - location)
        (tlocation ?t - taxi ?loc - location)
        (connects ?from - location ?to - location)
    )


    ;define actions here
    (:action get_in
        :parameters (?p - person ?t - taxi ?loc - location)
        :precondition (and (at ?p ?loc) (at ?t ?loc) (outsidetaxi ?p))
        :effect (and (intaxi ?p) (not (outsidetaxi ?p)))
    )

    (:action get_out
        :parameters (?p - person ?t - taxi ?loc - location)
        :precondition (and (at ?p ?loc) (at ?t ?loc) (outsidetaxi ?p))
        :effect (and )
    )

    (:action move
        :parameters (?t - taxi ?from - location ?to - location)
        :precondition (and )
        :effect (and )
    )



)