export const scenes = {
  intro: {
    type: 'cutscene',
    content: [
      { type: 'text', value: "In the beginning, there was silence...", duration: 3000 },
      { type: 'text', value: "But silence was about to be broken...", duration: 3000 },
      { type: 'text', value: "The adventure begins now...", duration: 3000 }
    ]
  },
  level1: {
    type: 'interactive',
    setup: () => {
      // Initialize level 1: create enemies, place objects, etc.
    },
    cleanup: () => {
      // Clean up level 1: remove temporary objects, etc.
    }
  },
  levelComplete: {
    type: 'cutscene',
    content: [
      { type: 'text', value: "Congratulations! You've completed the first level.", duration: 3000 },
      { type: 'text', value: "Prepare for the challenges ahead...", duration: 3000 }
    ]
  }
};
