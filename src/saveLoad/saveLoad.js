export const saveGame = (player) => {
  const gameState = {
    playerPosition: player.position.toArray(),
    // Add other game state data here
  };
  localStorage.setItem('gameState', JSON.stringify(gameState));
};

export const loadGame = (player) => {
  const gameState = JSON.parse(localStorage.getItem('gameState'));
  if (gameState) {
    player.position.fromArray(gameState.playerPosition);
    // Load other game state data here
  }
};
