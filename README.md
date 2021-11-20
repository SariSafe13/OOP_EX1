# University-Ariel-OOP_EX1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 ##Objective:
In a building that contains multiple floors and multiple elevators. A certain human-being calls an elevator, and our objective is to grant him the fastest elevator (Time-Based Speed) among the whole building's elevators that will reach our human-being's current floor and then to pick him up to his targeted floor.
/*-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
Offline Algorithm & Analysis:
According to Offline Algorithm's definition - our elevators users will be flowing 1 by 1. We were requested to implement an offline algorithm in order to solve our discussed issue. First, we managed to conclude various scenarios of how an elevator that is farther than our user can perform a faster process than an elevator that is closer to our user. Obviously, each elevator contains multiple attributes that actually influence pretty well. For instance, speed, its time to close its doors, its time to open its doors, its time to start moving, its time to start stopping and a lot more. Therefore, according to (Distance = Time * Velocity) rule we succeeded to plan our whole calculations in order to extract each elevator's total speed time to perform its goal for a single call. Now, we will include a simple schema that illustrates what we have explained so far:

























