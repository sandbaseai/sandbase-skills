#!/usr/bin/env node

import { readdir, readFile, writeFile, mkdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const packageJson = JSON.parse(await readFile(path.join(root, "package.json"), "utf8"));

async function discoverSkills(parent) {
  const entries = await readdir(path.join(root, parent), { withFileTypes: true });
  const skills = [];

  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    const skillPath = path.join(root, parent, entry.name, "SKILL.md");
    try {
      await readFile(skillPath, "utf8");
      skills.push(`./${parent}/${entry.name}`);
    } catch (error) {
      if (error.code !== "ENOENT") throw error;
    }
  }

  return skills.sort();
}

const skills = [
  ...(await discoverSkills("marketing")),
  ...(await discoverSkills("research")),
];

if (skills.length !== 88) {
  throw new Error(`Expected 88 skills, found ${skills.length}`);
}

const marketplace = {
  $schema: "https://json.schemastore.org/claude-code-marketplace.json",
  name: "sandbase-agent-skills",
  version: packageJson.version,
  description: "Installable SandBase Agent Skills for research, social intelligence, marketing, and business workflows.",
  metadata: {
    description: "Installable SandBase Agent Skills for research, social intelligence, marketing, and business workflows.",
    version: packageJson.version,
  },
  owner: {
    name: "SandBase AI",
    url: "https://github.com/sandbaseai",
  },
  plugins: [
    {
      name: "sandbase-skills",
      version: packageJson.version,
      description: "88 Agent Skills for evidence-led research, social intelligence, marketing, and business workflows.",
      author: {
        name: "SandBase AI",
        url: "https://github.com/sandbaseai",
      },
      homepage: "https://github.com/sandbaseai/sandbase-skills",
      repository: "https://github.com/sandbaseai/sandbase-skills",
      license: "Apache-2.0",
      keywords: ["agent-skills", "research", "social-intelligence", "marketing"],
      source: "./",
      category: "productivity",
      strict: false,
      skills,
    },
  ],
};

await mkdir(path.join(root, ".claude-plugin"), { recursive: true });
await writeFile(
  path.join(root, ".claude-plugin", "marketplace.json"),
  `${JSON.stringify(marketplace, null, 2)}\n`,
);

console.log(`Generated Claude Code marketplace with ${skills.length} skills.`);
