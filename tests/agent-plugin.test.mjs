import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

test('portable Agent Plugin manifest targets the published 1.0 schema', async () => {
  const manifest = JSON.parse(
    await readFile(path.join(root, 'agent-plugin', 'plugin.json'), 'utf8'),
  );

  assert.equal(
    manifest.$schema,
    'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json',
  );
  assert.equal(manifest.name, 'sandbase-research');
  assert.match(manifest.version, /^\d+\.\d+\.\d+$/);
  assert.equal(manifest.license, 'Apache-2.0');
  assert.deepEqual(Object.keys(manifest).sort(), [
    '$schema',
    'author',
    'description',
    'homepage',
    'keywords',
    'license',
    'name',
    'repository',
    'version',
  ]);
});

test('portable Agent Plugin exposes the canonical flagship skill', async () => {
  const packaged = await readFile(
    path.join(root, 'agent-plugin', 'skills', 'multi-source-search', 'SKILL.md'),
    'utf8',
  );
  const canonical = await readFile(
    path.join(root, 'research', 'multi-source-search', 'SKILL.md'),
    'utf8',
  );

  assert.equal(packaged, canonical);
  assert.match(packaged, /^---\nname: multi-source-search\n/);
});
