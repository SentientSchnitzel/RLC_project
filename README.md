# RLC_project
Reinforcement Learning and Control DTU - Project 1

Main script is the [evaluate_chess_positions.py](../master/ChessEngine2.0/evaluate_chess_positions.py) which gives data for the table.

## Installation
Clone the repo and install dependencies
```bash
git clone https://github.com/SentientSchnitzel/RLC_project

cd RLC_project

pip install -r requirements.txt
```

## Play vs the Engine
To play against the engine, run file/path below.
Playing is done in algebraic notation, e.g. white knight to e4 is just writing ' Ne4 '. 
Standard is playing as white, cannot be changed atm. mostly for demonstration
```bash

python ChessEngine2.0\humanvsmachine.py

```

### Acknowledgements
Code is based on [Andreas Stöckl's](https://medium.datadriveninvestor.com/an-incremental-evaluation-function-and-a-testsuite-for-computer-chess-6fde22aac137) article about chess, minimax, alphabeta pruning and quiesensce search.
