import { cp, mkdir, readdir, readFile, rm } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const source = path.join(root, 'research', 'multi-source-search');
const destination = path.join(root, 'agent-plugin', 'skills', 'multi-source-search');
const check = process.argv.includes('--check');

async function filesUnder(directory, prefix = '') {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];

  for (const entry of entries.sort((a, b) => a.name.localeCompare(b.name))) {
    const relative = path.join(prefix, entry.name);
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await filesUnder(absolute, relative)));
    } else if (entry.isFile()) {
      files.push(relative);
    } else {
      throw new Error(`Unsupported entry in Agent Plugin source: ${relative}`);
    }
  }

  return files;
}

async function assertSynchronized() {
  const sourceFiles = await filesUnder(source);
  const destinationFiles = await filesUnder(destination);

  if (JSON.stringify(sourceFiles) !== JSON.stringify(destinationFiles)) {
    throw new Error('Agent Plugin file list is stale; run npm run agent-plugin:build');
  }

  for (const relative of sourceFiles) {
    const [canonical, packaged] = await Promise.all([
      readFile(path.join(source, relative)),
      readFile(path.join(destination, relative)),
    ]);
    if (!canonical.equals(packaged)) {
      throw new Error(`Agent Plugin copy is stale: ${relative}`);
    }
  }

  console.log(`Validated Agent Plugin copy with ${sourceFiles.length} files.`);
}

if (check) {
  await assertSynchronized();
} else {
  await rm(destination, { recursive: true, force: true });
  await mkdir(path.dirname(destination), { recursive: true });
  await cp(source, destination, { recursive: true });
  console.log(`Generated ${path.relative(root, destination)}.`);
}
