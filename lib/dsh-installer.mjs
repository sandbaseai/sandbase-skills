import { cp, mkdir, readdir, rm, stat } from 'node:fs/promises';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const packageRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const categories = ['marketing', 'research'];

export async function availableSkills(root = packageRoot) {
  const result = new Map();
  for (const category of categories) {
    const categoryPath = join(root, category);
    let entries;
    try {
      entries = await readdir(categoryPath, { withFileTypes: true });
    } catch (error) {
      if (error?.code === 'ENOENT') continue;
      throw error;
    }
    for (const entry of entries) {
      if (!entry.isDirectory()) continue;
      const skillPath = join(categoryPath, entry.name);
      try {
        if ((await stat(join(skillPath, 'SKILL.md'))).isFile()) {
          result.set(entry.name, skillPath);
        }
      } catch (error) {
        if (error?.code !== 'ENOENT') throw error;
      }
    }
  }
  return new Map([...result].sort(([a], [b]) => a.localeCompare(b)));
}

function assertSkillName(name) {
  if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(name)) {
    throw new Error(`Invalid skill name: ${name}`);
  }
}

export async function installSkill(name, project = process.cwd(), options = {}) {
  assertSkillName(name);
  const skills = await availableSkills(options.root ?? packageRoot);
  const source = skills.get(name);
  if (!source) throw new Error(`Unknown skill "${name}". Run with --list to inspect names.`);

  const destination = join(resolve(project), '.dsh', 'skills', name);
  try {
    await stat(destination);
    if (!options.force) {
      throw new Error(`${destination} already exists. Pass --force to replace it.`);
    }
    await rm(destination, { recursive: true, force: true });
  } catch (error) {
    if (error?.code !== 'ENOENT') throw error;
  }
  await mkdir(dirname(destination), { recursive: true });
  await cp(source, destination, { recursive: true });
  return destination;
}

export async function removeSkill(name, project = process.cwd()) {
  assertSkillName(name);
  const destination = join(resolve(project), '.dsh', 'skills', name);
  try {
    const marker = await stat(join(destination, 'SKILL.md'));
    if (!marker.isFile()) throw new Error(`${destination} is not a DSH skill installation.`);
  } catch (error) {
    if (error?.code === 'ENOENT') throw new Error(`${name} is not installed in ${resolve(project)}.`);
    throw error;
  }
  await rm(destination, { recursive: true });
  return destination;
}
