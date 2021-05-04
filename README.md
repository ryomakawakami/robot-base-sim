# robot-base-sim
Drivetrain simulator

w is the width of the drive train (100 px), theta_r is current absolute angle of robot

delta theta is relative change in angle, phi is chord angle (?), a is chord length

![Delta theta equation](https://latex.codecogs.com/svg.latex?\Delta%20\theta%20%3D%20\frac%20{\Delta%20L%20-%20\Delta%20R}{w})

![Phi equation](https://latex.codecogs.com/svg.latex?%5Cphi%20%3D%20%5Cfrac%20%7B%5Cpi%20-%20%5CDelta%20%5Ctheta%7D%7B2%7D%20-%20%5Ctheta_r)

![a equation](https://latex.codecogs.com/svg.latex?a%20%3D%20%5Cfrac%20%7B%5CDelta%20L%20&plus;%20%5CDelta%20R%7D%7B%5CDelta%20%5Ctheta%7D%20%5Csin%28%5Cfrac%20%7B%5CDelta%20%5Ctheta%7D%7B2%7D%29)
