import * as THREE from 'three';

export const level = [
  'x x x x x x x x x x',
  'x . . . . . . . . x',
  'x . x x x x x x . x',
  'x . x . . . . x . x',
  'x . x . x x . x . x',
  'x . x . x x . x . x',
  'x . x . . . . x . x',
  'x . x x x x x x . x',
  'x . . . . . . . . x',
  'x x x x x x x x x x',
];

let cells = [];
let ghosts = [];
let foodCount = 0;

export const setCells = (newCells) => { cells = newCells; };
export const setGhosts = (newGhosts) => { ghosts = newGhosts; };
export const setFoodCount = (count) => { foodCount = count; };

export const getCells = () => cells;
export const getGhosts = () => ghosts;
export const getFoodCount = () => foodCount;
