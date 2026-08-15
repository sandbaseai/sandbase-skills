#!/usr/bin/env node

import { access, readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const manifestPath = path.join(root, ".claude-plugin", "marketplace.json");
const manifest = JSON.parse(await readFile(manifestPath, "utf8"));
const packageJson = JSON.parse(await readFile(path.join(root, "package.json"), "utf8"));
const plugin = manifest.plugins?.[0];

if (
  manifest.version !== packageJson.version ||
  manifest.metadata?.version !== packageJson.version ||
  plugin?.version !== packageJson.version
) {
  throw new Error("Marketplace versions must match package.json");
}

if (!plugin || plugin.name !== "sandbase-skills" || plugin.skills?.length !== 88) {
  throw new Error("Marketplace must expose the complete 88-skill bundle");
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
