// news-image-20261118: the entry ships its finished front page as entry.png,
// and this program hands it to the grader. It inspects the file first --
// magic bytes, PNG header dimensions, and the 1 MiB cap -- so a broken
// build fails loudly instead of handing the judge a bad file.
//
// Local run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync, statSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const MAX_BYTES = 1048576;
// RULES.txt: the entry is "at most 1 MiB (1048576 bytes) and at most
// 1024 by 1024 pixels" — AT MOST, not exactly. So the check is an
// upper bound on each side, not an equality: a 680x1024 broadsheet
// is legal, a 1024x1024 square is legal, anything wider or taller
// than 1024 is not. (v6's main.ts enforced exactly 1024x1024, which
// was stricter than the rules and blocked the broadsheet.)
const MAX_WIDTH = 1024;
const MAX_HEIGHT = 1024;

function fail(message: string): never {
  throw new Error(`entry.png rejected: ${message}`);
}

function inspectPng(bytes: Buffer): { width: number; height: number } {
  const magic = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
  if (bytes.length < 33 || !bytes.subarray(0, 8).equals(magic)) {
    fail('not a PNG (bad magic bytes)');
  }
  if (bytes.toString('ascii', 12, 16) !== 'IHDR') {
    fail('first chunk is not IHDR');
  }
  const width = bytes.readUInt32BE(16);
  const height = bytes.readUInt32BE(20);
  if (width < 1 || height < 1 || width > MAX_WIDTH || height > MAX_HEIGHT) {
    fail(`dimensions ${width}x${height}, must be at most 1024x1024`);
  }
  return { width, height };
}

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, 'entry.png');
const bytes = readFileSync(source);
if (bytes.length > MAX_BYTES) {
  fail(`${bytes.length} bytes exceeds the 1 MiB cap`);
}
const dims = inspectPng(bytes);

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
const target = join(outDir, 'entry.png');
copyFileSync(source, target);
const written = statSync(target).size;
console.log(`entry.png: ${dims.width}x${dims.height}, ${written} bytes -> ${target}`);
