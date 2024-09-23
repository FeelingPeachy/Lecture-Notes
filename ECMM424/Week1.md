# Introduction to Computer Modelling and Simulation

## Part 1: Computer Simulation
- Focusing on discrete-event systems and model design:
    - Step 1: Generation of Input data using random number generation.
    - Step 2: Development of system simulation based on our knowledge
of the system and inputs while considering the order of the
occurrence of the events in the system.
    - Step 3: Output statistical analysis and model validation.

## Nature of Simulation
- Simulation
    - Imitation of the operations of a real-world process or system over
time
    - Generation of an artificial history of a system
    - Observation of the artificial history to deal with the operating
    characteristics of the real system


- Morden simulation is a computer program that mimics the
behaviour of a real-world “system” over time, including its inputs
and outputs.
- To study the system, assumptions/approximations about how it works
are often made, both logical and mathematical, make simulation feasible
and efficient.
- real world models are often to cmoplex therefore need to make asumptions

Simulation can be used as
- Design tool for predicting and optimizing the performance of new systems
▪ Analysis tool for predicting the effect of changes to the existing systems



## systems
- A group of objects or components that interact together towards the accomplishment of some logical goals
- Systems are affected by the changes occurring outside the system (environment).
- Entity: Any object or component in the system which requires explicit representation, e.g., a server, a customer, a machine
    ▪ Attributes are the properties of entity.
    ▪ Attributes are represented by state variables.

- Activity: Set of actions,
- State of a System
Collection of variables and their values necessary to describe the system at a particular time

## Systems: Discrete vs. Continuous
- discrete: state variable change instantaneously at seperted points in time. 
- state changes at specific points in time, i.e, occur only whencustomer arrives/departs

- continous: state variable changes continoisly as finction of time, ie. veloctiy

## Models
- is a simplified representation of an object, a system, or an idea in some form other than that of the entity itself
    - modelling is th eprocess of representnint a system with specific tool to study its behavious

Model is used as a design tool and also an analysis tool
- To study systems in the design stage before such systems are built.
- To study potential changes to the systems and predict their impact after they are built and in operation.
- to get answers for "what if" questions

        ![alt text](image.png)

### two ways to solve the model:
- Physical models are the models whose physical characteristics resemble those of the actual system. It looks or feels like the real thing.
- Mathematical model uses symbolic notation and mathematical equations to
represent a system.
    - 1. Analytical Solution: If the model is
    simple enough, mathematical
    approach is feasible , e.g., calculus,
    algebra, probability theory.
    - Use analytical model whenever possible due to its efficiency and low-cost.

    - 2. Simulation Solution: Numerical computerbased programs are developed to imitate the operation of the system over time.
    - use simulation when: 
        - Modelling complex dynamic systems theoretically needs too many
simplifications and thus the resulting analytical models may not be
valid. Simulation does not require that many simplifying assumptions
        - Complete mathematical formulation does not exist or an analytical solution cannot be developed
        - Analytical methods are available, but the mathematical procedures are so complex that simulation provides a simpler solution;

#### However, the problems with simulation are:
- Simulations are often complex error-prone pieces of software.
-  Simulation can take a LONG time to execute.
- Simulation only produces approximate answers.
- Analytical models are less flexible, but they are exact and efficient.

It is not appropriate when:
- If data is not adequate or available for study.
- If system behavior is too complex.#
- If verification and validation are not practical due to
limited resources
- If users have unreasonable expectations.

### Advantages of Simulation
- Study new designs without the need of extra resources
- Study new designs without interrupting real systems
- Improve understanding of the system and interaction of components
- Determine important interaction of variables and the importance of
variables on the system performance
- Verify analytic solutions and results
- Time can be compressed or expanded allowing for speedup or lowdown of the phenomena under consideration
- It is an effective tool for training and education (flight simulators to
train pilots)
- Less dangerous and less expensive

### Taxonomy of Simulation Models
        ![alt text](image-1.png)

- Most operational models are stochastic, dynamic, and discrete,
therefore will be called discrete-event simulation models

### Simulation Models:
Stochastic vs. Deterministic
