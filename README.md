# Monty-Hall-Problem
The Monty Hall Problem is a thought experiment, in the form of a probability excercise. This is the original form of the puzzle:

**Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?**
    
The answer is yes, it is to your advantage to switch, for you stand twice the chance of winning if you choose the second door.

There are mathematical explanations and derivations that give the same answer - to hopefully slow your probable immediate disbelief and shock at the seeming logical fallacy - including a particularly simple and interesting [Bayesian proof](https://en.wikipedia.org/wiki/Monty_Hall_problem#Bayes'_theorem).

When the question was posed to a study with 228 people, 87% said they would not switch. This was very surprising, as unlike what bad ads would have you believe, few, if any, puzzles come so close to fooling all the people all the time. If it offers a comfort, even Nobel physicists disagreed with the solution, and were adamant on their answer.

Sidenote: When the study was done on pigeons, they learned the right answer faster than humans did. Interesting fact, isn't that?
The solution has a very simple implementation in code, and thus, you can run the simulation on the Python code here. 

The code runs on a simple rule: 
* If you pick the door that had the car initially (a 1/3 probability), then switching, you would lose. 
* If you pick a door wiht a goat initially (a 2/3 probability), then switching, you would win.

If you still need further convincing, run the program, and see what your chances come to.

If you're still not convinced, you're welcome to pore over the program and the explanations until your eyes bleed.

If you still remain in disbelief, [I have a link that will finally help you.](https://www.lesswrong.com/posts/mypWLfu2degMzCBTe/how-to-enjoy-being-wrong)
