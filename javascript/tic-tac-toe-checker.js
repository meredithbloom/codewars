// 5 kyu - Tic Tac Toe checker
/*
If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
We want our function to return:

-1 if the board is not yet finished AND no one has won yet (there are empty spots),
1 if "X" won,
2 if "O" won,
0 if it's a cat's game (i.e. a draw).
You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

*/
const board1 = 
[[0,0,1],
[0,1,2],
[2,1,0]]

const board2 = 
[[2,1,1],
[0,1,2],
[2,1,2]]

function isSolved(board) {
  // 0 is empty
  // 1 is X
  // 2 is O

// check for winning conditions
  const rows = [board[0], board[1], board[2]];
  const columns = [[board[0][0], board[1][0], board[2][0]], [board[0][1], board[1][1][2], board[2][1]], [board[0][2], board[1][2], board[2][2]]];
  const diagonals = [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]];
  // find if there is a winning row
  for (let i = 0; i < rows.length; i++) {
    if (rows[i][0] === rows[i][1] && rows[i][1] === rows[i][2]) {
      return rows[i][0];
    }
  }
  // find if there is a winning column
  for (let i = 0; i < columns.length; i++) {
    if (columns[i][0] === columns[i][1] && columns[i][1] === columns[i][2]) {
      console.log(`winning column is column ${i}`)
      return columns[i][0];
    }
  }
  // find if there is a winning diagonal
  for (let i = 0; i < diagonals.length; i++) {
    if (diagonals[i][0] === diagonals[i][1] && diagonals[i][1] === diagonals[i][2]) {
      return diagonals[i][0];
    }
  }
  // check if no one has won and there are still empty spots
  if (board.some(row => row.includes(0))) {
    return -1;
  }
  // check if it's a draw
  return 0;
}

console.log(isSolved(board1)); // 0
console.log(isSolved(board2)); // 1