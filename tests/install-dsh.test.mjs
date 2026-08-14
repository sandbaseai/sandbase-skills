import assert from 'node:assert/strict';
import { mkdtemp, readFile, writeFile, mkdir } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import test from 'node:test';
import { availableSkills, installSkill, removeSkill } from '../lib/dsh-installer.mjs';

async function fixture() {
  const root = await mkdtemp(join(tmpdir(), 'sandbase-skills-'));
  const source = join(root, 'marketing', 'example-skill');
  await mkdir(source, { recursive: true });
  await writeFile(join(source, 'SKILL.md'), '# Example\n');
  return root;
}

test('discovers and installs a complete DSH skill directory', async () => {
  const root = await fixture();
  const project = await mkdtemp(join(tmpdir(), 'dsh-project-'));
  assert.deepEqual([...(await availableSkills(root)).keys()], ['example-skill']);
  const destination = await installSkill('example-skill', project, { root });
  assert.equal(await readFile(join(destination, 'SKILL.md'), 'utf8'), '# Example\n');
});

test('refuses overwrite and supports explicit removal', async () => {
  const root = await fixture();
  const project = await mkdtemp(join(tmpdir(), 'dsh-project-'));
  await installSkill('example-skill', project, { root });
  await assert.rejects(() => installSkill('example-skill', project, { root }), /already exists/);
  await removeSkill('example-skill', project);
  await assert.rejects(() => removeSkill('example-skill', project), /not installed/);
});

test('rejects path-like skill names', async () => {
  await assert.rejects(() => installSkill('../escape', process.cwd()), /Invalid skill name/);
});
