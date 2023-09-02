"""
@Author: D. Petridis
"""

# Import necessary libraries:
import numpy as np
import matplotlib.pyplot as plt

class XFlags:

    def __init__(self,
                 total_flags: int,
                 max_flags: int):
        """
        Initialize the XFlags class.

        Parameters:
        - total_flags (int): Total number of flags in the game.
        - max_flags (int): Maximum number of flags a player can pick in one turn.

        Raises:
        - ValueError: If any of the inputs are not positive integers or max_flags > total_flags.
        """

        # Perform validity checks:
        if not isinstance(total_flags, int) or not isinstance(max_flags, int):
            raise ValueError("Both total_flags and max_flags parameters must be integers.")
        if total_flags <= 0 or max_flags <= 0:
            raise ValueError("Both total_flags and max_flags must be positive integers.")
        if max_flags > total_flags:
            raise ValueError("max_flags cannot be greater than total_flags.")

        # Define the class parameters:
        self.total_flags = total_flags
        self.max_flags = max_flags
        self.current_flags = total_flags

    def optimal_strategy(self):
        """
        Determine the initial optimal strategy based on the total_flags and max_flags.

        Returns:
        - tuple: ('first' or 'second', flags to pick if 'first' else None)
        """

        # Calculate the division remainder based on the given starting parameters:
        remainder = self.total_flags % (self.max_flags + 1)

        # Return the optimal strategy in a tuple:
        return ("first", remainder) if remainder != 0 else ("second", None)

    def optimal_move(self):
        """
        Determine the optimal move (number of flags to pick) based on the current game state.

        Returns:
        - int: Number of flags to pick.
        """

        # Calculate the division remainder based on the current parameters:
        remainder = self.current_flags % (self.max_flags + 1)

        # Return the optimal move:
        return remainder if remainder != 0 and remainder <= self.max_flags else np.random.randint(1, self.max_flags + 1)

    def simulate_game(self):
        """
        Simulate the game based on the optimal strategy.

        Returns:
        - list: Sequence of moves. Each move is a tuple ('first' or 'second', flags picked, remaining flags).
        """

        # Define variables:
        player_turn = self.optimal_strategy()[0]
        moves = []

        # Simulate the game until the final round, modify the variables and store the moves:
        while self.current_flags > 0:
            move = self.optimal_move()
            if self.current_flags <= self.max_flags:
                move = self.current_flags

            self.current_flags -= move
            moves.append((player_turn, move, self.current_flags))
            player_turn = "second" if player_turn == "first" else "first"

        # Return all the sequential moves of the game:
        return moves

    def visualize_moves(self, moves):
        """
        Visualize the final state of the game and display the moves in a textual form.

        Parameters:
        - moves (list): Sequence of moves from simulate_game.
        """

        # Print the title with the game parameters:
        print(f"X Flags - Total Flags: {self.total_flags}, Max Flags per Turn: {self.max_flags}\n{'-'*60}")

        # Display the optimal strategy:
        print(f"The optimal strategy is: {self.optimal_strategy()}\n{'-'*60}")

        # Display the moves of the game:
        for step in moves:
            player, move, remaining_flags = step
            print(f"{player} player picked {move} flags. Remaining flags: {remaining_flags}")

        # Set visualization's parameters:
        fig, ax = plt.subplots(figsize=(15, 3))
        x_coords = [i for i in range(1, self.total_flags + 1)]
        y_coords = [1 for _ in range(self.total_flags)]
        colors = ['gray' for _ in range(self.total_flags)]  # Start with all flags as gray
        player_colors = {'first': 'blue', 'second': 'red'}
        taken_by = {i: None for i in range(self.total_flags)}

        total_picked = 0
        for idx, move in enumerate(moves):
            player, flags_picked, _ = move

            # Color the flags chosen by the current player:
            for _ in range(flags_picked):
                colors[total_picked] = player_colors[player]
                taken_by[total_picked] = player
                total_picked += 1

        for i, (x, y) in enumerate(zip(x_coords, y_coords)):
            ax.scatter(x, y, color=colors[i], s=100)
            ax.text(x, y + 0.1, f'P{1 if taken_by[i] == "first" else 2}' if taken_by[i] else '',
                    verticalalignment='center', horizontalalignment='center', fontsize=10, fontweight='bold')

        # Set visualization space:
        ax.set_ylim(0, 2)
        ax.set_xlim(0, self.total_flags + 1)
        ax.axis('off')  # Turn off the axis
        ax.set_title(f'Visualization ({self.total_flags},{self.max_flags})', fontsize=14)

        # Set the legend:
        ax.scatter([], [], color='blue', s=100, label='First Player')
        ax.scatter([], [], color='red', s=100, label='Second Player')
        ax.legend(loc='upper right', title=None, fontsize=10)

        # Plot the visualization:
        plt.show()