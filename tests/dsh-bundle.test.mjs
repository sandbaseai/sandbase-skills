import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

test('declares an installable DSH bundle with both Skill roots', async () => {
  const packageJson = JSON.parse(await readFile('package.json', 'utf8'));
  assert.equal(packageJson.dsh?.bundle?.patch, './dsh/cordis.patch.yml');
  assert.ok(packageJson.files.includes('dsh'));

  const patch = await readFile('dsh/cordis.patch.yml', 'utf8');
  assert.match(patch, /id: skill-filesystem/);
  assert.match(patch, /name: '@deepseek-ai\/dsh-skill-filesystem'/);
  assert.match(patch, /includeDefaultRoots: true/);
  assert.match(patch, /new URL\('\.\.\/marketing\/', baseUrl\)/);
  assert.match(patch, /new URL\('\.\.\/research\/', baseUrl\)/);
});
