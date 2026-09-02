#!/usr/bin/env node

import { access, readFile, readdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const manifestPath = path.join(root, ".claude-plugin", "marketplace.json");
const manifest = JSON.parse(await readFile(manifestPath, "utf8"));
const packageJson = JSON.parse(await readFile(path.join(root, "package.json"), "utf8"));
const plugin = manifest.plugins?.[0];

async function discoverSkills(parent) {
  const entries = await readdir(path.join(root, parent), { withFileTypes: true });
  const skills = [];

  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    try {
      await access(path.join(root, parent, entry.name, "SKILL.md"));
      skills.push(`./${parent}/${entry.name}`);
    } catch (error) {
      if (error.code !== "ENOENT") throw error;
    }
  }

  return skills.sort();
}

const expectedSkills = [
  ...(await discoverSkills("marketing")),
  ...(await discoverSkills("research")),
];

if (
  manifest.version !== packageJson.version ||
  manifest.metadata?.version !== packageJson.version ||
  plugin?.version !== packageJson.version
) {
  throw new Error("Marketplace versions must match package.json");
}

if (!plugin || plugin.name !== "sandbase-skills") {
  throw new Error("Marketplace must expose the sandbase-skills plugin");
}

if (JSON.stringify(plugin.skills) !== JSON.stringify(expectedSkills)) {
  throw new Error(
    `Marketplace skills do not match the ${expectedSkills.length} discovered Skill directories`,
  );
}

if (new Set(plugin.skills).size !== plugin.skills.length) {
  throw new Error("Marketplace contains duplicate skill paths");
}

for (const skill of plugin.skills) {
  if (!/^\.\/(marketing|research)\/[a-z0-9-]+$/.test(skill)) {
    throw new Error(`Invalid skill path: ${skill}`);
  }
  await access(path.join(root, skill, "SKILL.md"));
}

console.log(`Validated Claude Code marketplace with ${plugin.skills.length} skills.`);
