#!/usr/bin/env node
import { availableSkills, installSkill, removeSkill } from '../lib/dsh-installer.mjs';

const args = process.argv.slice(2);
const json = args.includes('--json');
const force = args.includes('--force');
const projectFlag = args.indexOf('--project');
const project = projectFlag >= 0 ? args[projectFlag + 1] : process.cwd();
const positional = args.filter((arg, index) =>
  !arg.startsWith('--') && index !== projectFlag + 1,
);

function output(value, human) {
  console.log(json ? JSON.stringify(value, null, 2) : human);
}

try {
  if (args.includes('--list') || positional[0] === 'list') {
    const names = [...(await availableSkills()).keys()];
    output({ skills: names }, names.join('\n'));
  } else if (positional[0] === 'add' && positional[1]) {
    const destination = await installSkill(positional[1], project, { force });
    output({ skill: positional[1], destination }, `Installed ${positional[1]} to ${destination}`);
  } else if (positional[0] === 'remove' && positional[1]) {
    const destination = await removeSkill(positional[1], project);
    output({ skill: positional[1], destination }, `Removed ${positional[1]} from ${destination}`);
  } else {
    throw new Error('Usage: sandbase-dsh-skills <list|add NAME|remove NAME> [--project PATH] [--force] [--json]');
  }
} catch (error) {
  console.error(error.message);
  process.exitCode = 1;
}
