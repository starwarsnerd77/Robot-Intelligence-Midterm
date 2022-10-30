# CS 5510 Midterm

## Requirements
gym==0.21.0
pyglet

## Problem 1

    python3 midterm_problem1.py


## Problem 2
### Part A
Workspace volume is: $\pi \cdot 100^2 - \pi \cdot 20^2 = 30159.289 cm^2$

Picture in `images/problem 2.png`

### Part B
| Link | $a_i$ | $d_i$ | $\alpha_i$ | $\theta_i$ |
| :--: | :---: | :---: | :--------: | :--------: |
| 1    | 0     | 0     | 0          | $\theta_1$ |
| 2    | 60cm  | 0     | 0          | $\theta_2$ |
| 3    | 40cm  | 0     | 0          | $\theta_3$ |
| 4    | 0     | $d_4$ | 0          | $\theta_4$ |

### Part C

    python3 midterm_problem2.py

## Problem 3
    python3 midterm_problem3.py

## Problem 4
### Part B

    python3 midterm_problem4.py

## Problem 5
### Part A
Merits
1. using reinforcement learning is sometimes simpler than alernatives
2. using reinforcement learning can adapt given more data
3. Accidents that result from your code can be blamed on the data shifting liability.
Demerits
1. RL is a black box.
2. It is computationally expensive to train a model
3. RL can't beat an optimal controls algorithm for a particular task
### Part B

    images/5B.png

Reinforcement learning doesn't need to know the environment while controls does.

### Part C

    python3 midterm_problem5.py
### Part D
UNFINISHED

## Problem 6
### Parts A and B and D

    python3 midterm_problem6.py
### Part C
Logical applications for this tool are counting people in a line to predict wait times. For the emotion part it could detect dangerous situations before they happen. Ethically we can all agree that less chaotic crowds and predictable wait times in lines are good things. This technology is only better at reading your face then socially inadept people. There is only ethical concerns when the technology makes decisions on inaccurate or biased predictions.

## Problem 7
UNFINISHED
## Problem 8
UNFINISHED

## Problem 9 Ethics of Robotics - Open Ended Questions
1. Many people (particularly those in the robotics industry) believe that
robotics is purely within the purview of technical development and should not have
any ethical considerations. What do you feel can be a merit or demerit to this way
of thinking?

    We feel that robotics is purely technical. Most ethical complaints are flawed. AI doesn't have a consciousness and is entirely constucted. The use of robots shouldn't itself be a problem, if they are more effective than humans it simply makes sense.

    As far as being law abiding, that is a real concern. We can't have robots take and share pictures of people without their permission, nor drive over people via cars.

2. Isaac Asimov listed 3 laws of robotics, comment on the algorithmic complexity of implementing these into working intelligence. Define a scenario and write
Psuedo code to implement these rules.

    A robot may not injure a human being or, through inaction, allow a human being to come to harm. A robot must obey orders given it by human beings except where such orders would conflict with the First Law. A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.

        While true:
            observe all humans
            if any are soon to encounter harm
                prevent them from encountering harm
            listen
            if given order by human
                if order doesn't cause harm
                    comply
            if existance is threatened
                protect itself w/o harming humans or disobeying orders

3. In the event of an autonomous system causing harm or damages, who is
responsible? Read and comment on the following two documents: https://www.
callahan-law.com/articles-and-expert-advice/when-an-autonomous-vehicle-hits-a-peand https://en.wikipedia.org/wiki/Self-driving_car_liability

    Such an obvious answer. Currently these vehicles are sold with the understanding that the driver must be ready to take control at any time. Therefore currently it is the driver's fault. When self driving car companies are confident in their own technology their cars will become fully self driving. When that happens the company would be liable for any, hopefully for them, rare accidents. Right now is just not the time to look at your phone while in a self driving car. Cars aren't fully self driving until the companies are willing to foot the bill for accidents. A previously self driving car may become incapable after neglect, in this case there should be clear indicators so that the driver can be held responsible. As far as other autonomous systems are concerned, it should be similar. Either they are sold fully autonomous and the company foots accident bills, or the company admits their product is faulty and requires supervision for their product be safe. Due to being better for the customer those companies that foot the bill will succeed in the end. Footing the bill could discourage companies from developing fully autonomous products that, if they do decrease accident rates, are for the improvement of society. As a society level issue, the government could pay for a portion of automated accidents to enable the development of the technology. This would effectively make society itself liable.

4. What laws may be helpful for regulating or controlling autonomous systems? What drawbacks will this potentially have?

    Law for autonomous systems should be simple. The company is liable for defects if they claim their product is actually autonomous. If their product is safer than the current alternatives and therefore better for society the government should be liable and pay with taxes from related products. Similar to how gas taxes pay for roads, taxes on all vehicles (in the interest of making all vehicles safer) should also pay for safer than human autonomous car accidents. There are no drawbacks with this system. Useful automated systems can be brought into society with taxes. Systems that aren't safer than human equivelants should be payed for by the company. Current non-autonomous systems will have liability on the operator. I am generally of the opinion that government has a responsibility to improve society, to this end helping bleeding edge technology and thus consumers just makes sense. Like how Europe requires Apple devices to use USB-C since it is better for society.