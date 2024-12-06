"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact
from math import log2

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    num_points_array = []
    num_points_sum = 0
    for i in range(num_rolls):
        num_points = dice()
        num_points_array.append(num_points)
        num_points_sum += num_points
    if 1 in num_points_array:
        return 1
    else:
        return num_points_sum
    # END PROBLEM 1


def tail_points(opponent_score):
    """Return the points scored by rolling 0 dice according to Pig Tail.

    opponent_score:   The total score of the other player.

    """
    # BEGIN PROBLEM 2
    tens = (opponent_score // 10) % 10
    ones = opponent_score % 10
    return 2 * abs(tens - ones) + 1
    # END PROBLEM 2


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    # BEGIN PROBLEM 3
    if num_rolls == 0:
        return tail_points(opponent_score)
    else:
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3


def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Square Swine.
    """
    return player_score + take_turn(num_rolls, opponent_score, dice)


def square_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Square Swine.
    """
    score = player_score + take_turn(num_rolls, opponent_score, dice)
    if perfect_square(score):  # Implement perfect_square
        return next_perfect_square(score)  # Implement next_perfect_square
    else:
        return score


# BEGIN PROBLEM 4
def perfect_square(score):
    i = 1
    while i ** 2 <= score:
        if i ** 2 == score:
            return True
        i += 1
    return False

def next_perfect_square(score):
    i = 1
    while i ** 2 <= score:
        if i ** 2 == score:
            break
        i += 1
    return (i + 1) ** 2
# END PROBLEM 4


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the oppononent's score.
    """
    return 5


def play(strategy0, strategy1, update,
         score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, square_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Square
    Swine rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as square_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    while score0 < goal and score1 < goal:
        if who == 0:
            score0 = update(strategy0(score0, score1), score0, score1, dice)
        elif who == 1:
            score1 = update(strategy1(score1, score0), score1, score0, dice)
        who = 1 - who
    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    def always_roll_n(score, opponent_score):
        return n
    return always_roll_n
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether strategy always chooses the same number of dice to roll.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    num_of_dices = strategy(0, 0)
    for i in range(100):
        for j in range(100):
            if num_of_dices != strategy(i, j):
                return False
    return True
    # END PROBLEM 7


def make_averaged(original_function, total_samples=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TOTAL_SAMPLES times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8
    def average(*original_args):
        total = 0
        for i in range(total_samples):
            total += original_function(*original_args)
        return total / total_samples
    return average
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, total_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of TOTAL_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    heighest_average = 0
    heighest_average_num_rolls = 0
    for i in range(1, 11):
        average = make_averaged(roll_dice, total_samples)(i, dice)
        if average > heighest_average:
            heighest_average = average
            heighest_average_num_rolls = i
    return heighest_average_num_rolls
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, square_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)

    print('always_roll(6) win rate:', average_win_rate(always_roll(6)))  # near 0.5
    print('catch_up win rate:', average_win_rate(catch_up))
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    print('tail_strategy win rate:', average_win_rate(tail_strategy))
    print('square_strategy win rate:', average_win_rate(square_strategy))
    print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"


def tail_strategy(score, opponent_score, threshold=12, num_rolls=6):
    """This strategy returns 0 dice if Pig Tail gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Square Swine.
    """
    # BEGIN PROBLEM 10
    if tail_points(opponent_score) >= threshold:
        return 0
    else:
        return num_rolls
    # END PROBLEM 10


def square_strategy(score, opponent_score, threshold=12, num_rolls=6):
    """This strategy returns 0 dice when your score would increase by at least threshold."""
    # BEGIN PROBLEM 11
    new_score = square_update(0, score, opponent_score)
    if new_score - score >= threshold:
        return 0
    else:
        return num_rolls
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Remove this line once implemented.
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
