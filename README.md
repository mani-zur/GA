# GA for optimization of nuclear problem with Serpent
This software is script implementing genetics algorithm to optimize nuclear problem. 

## Enviroment requirements
*	Firstly you need python interpreter.
*	You need also Serptent in version higher than v2.30. 
*	The script was tested on Ubuntu 18.04 OS.
*	**Probably** script run correctly on other linux.

## Runing the code
To run this code you need proper file structure.
```
<<PROJECT DIR>>
 ┣━ sss2
 ┣━ scripts 
 ┃   ┣━ FileInterface.py
 ┃   ┣━ Individual.py
 ┃   ┣━ main.py
 ┃   ┗━ Population.py
 ┣━ inp
 ┃   ┗━ <<input_name.inp>>
 ┣━ results
 ┗━ xs
 ```
 If you have folowing structure now you can run the *main.py*
 ```
 $ python main.py
 ```
