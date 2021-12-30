# LottoEnv
<a href="https://gym.openai.com/" target="_blank">OpenAI Gym</a> and Agent for <a href="https://www.national-lottery.co.uk/" target="_blank">UK National Lottery</a>

### Status
* gym - beta, handles single ticket
* agent - wip
* gym, multiple tickets - planned

# Premise
### The Goal
Train an agent to beat the UK National Lottery

### The game
Player selects 6 numbers from possible 1-59

The Env will draw 
* 6 numbers, and 
* 1 bonus ball

### Prize rules
Depending on number of balls matched: 
```
reward_rules = {
            6: 1000000,
            # 5 + bb = 100000
            5: 10000,
            4: 1000,
            3: 25,
            2: 0,
            1: 0,
            0: 0
        }
```


### What to learn
Find a combination of #tickets and spread of numbers to make a profit...

The Agent should decide:
* number of tickets to buy (cost £2)
* lucky-dip or select own numbers
* starting capital = £10000

# Usage
```
git clone https://github.com/dcolley/lotto-env
cd lotto-env
pip3 install gym tensorflow numpy random matplotlib
python3 lotto_main.py
```

### Dependencies
* tensorflow 2
* python 3

# Refs & cudos
Inspiration from the examples from Dr. Phil Tabor
* https://www.youtube.com/channel/UC58v9cLitc8VaCjrcKyAbrw
* https://www.youtube.com/watch?v=vmrqpHldAQ0
* https://www.youtube.com/watch?v=w1jd0Dpbc2o
