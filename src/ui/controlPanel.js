import { FeatureManager } from '../featureManager/featureManager';

const featureManager = new FeatureManager();

export const createControlPanel = () => {
  const panel = document.createElement('div');
  panel.classList.add('control-panel');

  Object.keys(featureManager.features).forEach((feature) => {
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.id = feature;
    checkbox.checked = featureManager.isFeatureEnabled(feature);
    checkbox.addEventListener('change', (event) => {
      featureManager.toggleFeature(feature, event.target.checked);
    });

    const label = document.createElement('label');
    label.htmlFor = feature;
    label.textContent = feature;

    panel.appendChild(checkbox);
    panel.appendChild(label);
  });

  document.body.appendChild(panel);
};
