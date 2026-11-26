// news-image-20261125 entry: the program ships a pre-rendered front page
// (entry.png, drawn by build.py in this repo) and copies it to the grader's
// output path. Node 22, standard library only; no network, no randomness,
// so both runs write byte-identical output.
//
// Run locally with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(
  new URL('./entry.png', import.meta.url),
  join(outDir, 'entry.png'),
);
