import { FeatureManager } from '../featureManager/featureManager';

const featureManager = new FeatureManager(); // Singleton or shared instance

export const loadLevel = (level) => {
  if (featureManager.isFeatureEnabled('levels')) {
    // Load and initialize the level
  }
};
