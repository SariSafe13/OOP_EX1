# University-Ariel-OOP_EX1

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 # Objective:

In a building that contains multiple floors and multiple elevators. A certain human-being calls an elevator, and our objective is to grant him the fastest elevator (Time-Based Speed) among the whole building's elevators that will reach our human-being's current floor and then to pick him up to his targeted floor.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 # Offline Algorithm & Analysis:
According to Offline Algorithm's definition - our elevators users will be flowing 1 by 1. We were requested to implement an offline algorithm in order to solve our discussed issue. First, we managed to conclude various scenarios of how an elevator that is farther than our user can perform a faster process than an elevator that is closer to our user. Obviously, each elevator contains multiple attributes that actually influence pretty well. For instance, speed, its time to close its doors, its time to open its doors, its time to start moving, its time to start stopping and a lot more. Therefore, according to (Distance = Time * Velocity) rule we succeeded to plan our whole calculations in order to extract each elevator's total speed time to perform its goal for a single call. Now, we will include a simple schema that illustrates what we have explained so far:



![צילום מסך 2021-11-20 211913](https://user-images.githubusercontent.com/88654426/142738479-86933c2e-83e8-47f8-94d9-827c3e33b977.png)

According to our schema, Sam is currently in floor 4 and is intending to go to his targeted
floor – floor 0. In Sam's building, there are 3 different elevators that each one of them has
its own attributes and stats. Each elevator has also its own total speed time (that was
calculated) to pick up Sam from floor 4 and to reach him to floor 0.
Elevator 1 (E1): Needs 19 seconds in order to meet Sam's need.
Elevator 2 (E2): Needs 11.5 seconds in order to meet Sam's need.
Elevator 3 (E3): Needs 6.583 seconds in order to meet Sam's need.
In conclusion, our algorithm must allocate Elevator 3 to Sam. In other words, the elevator
that has the lowest value of time is basically our fastest elevator that must be sent to our
user. Eventually, the whole process that was just introduced is actually done for every call
that happens in our building.

Similar Mechanism:
• Waze – gives us the fastest route to use.
• Choosing an uber driver – more like choosing the fastest driver.
• Fire department – more like sending the closest fire engine; the fastest to arrive to the fireplace.

# Objects We Created:

Call: Represents a call.
Elevator: Represents a Elevator.
Building: Represents the Building we have.
Allocation:  Responsible to allocate and there all methods and function we created and the case to read+load Json and CSV Files.
























