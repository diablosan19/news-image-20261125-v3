import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
const out = outDir.endsWith(".png") ? outDir : join(outDir, "entry.png");

mkdirSync(dirname(out), { recursive: true });
copyFileSync(src, out);
console.log("wrote " + out);
