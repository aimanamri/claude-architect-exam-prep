#!/usr/bin/env node
// Validates the bundled question data exactly as the site will load it.
// Usage: python3 quiz-site/build_static.py --out _site && node quiz-site/validate.js _site/sets.json
// Exits 1 (failing CI) if any set has skipped questions, a track is unknown, or the config is malformed.
"use strict";
const fs = require("fs");
const path = require("path");

global.window = undefined;
require(path.join(__dirname, "parser.js")); // defines globalThis.QuizParser

const file = process.argv[2] || path.join(__dirname, "..", "_site", "sets.json");
const payload = JSON.parse(fs.readFileSync(file, "utf8"));
const cfg = payload.config || {};
const tracks = cfg.tracks || {};
const modNames = cfg.moduleNames || {};
const problems = [];
const summary = {};

if (payload.errors && payload.errors.length) problems.push(...payload.errors.map((e) => `source: ${e}`));
if (!Object.keys(tracks).length) problems.push("config: no tracks defined");

for (const [t, tc] of Object.entries(tracks)) {
  if (!tc.code || !tc.name) problems.push(`config.tracks.${t}: needs "code" and "name"`);
  (tc.placeholders || []).forEach((p, i) => {
    if (!p.title || !p.code) problems.push(`config.tracks.${t}.placeholders[${i}]: needs "title" and "code"`);
  });
  summary[t] = { sets: 0, questions: 0, placeholders: (tc.placeholders || []).length };
}

const seenKeys = new Set();
for (const f of payload.files || []) {
  let sets;
  try { sets = QuizParser.parseFile(f); } catch (e) { problems.push(`${f.file}: parser error: ${e.message}`); continue; }
  for (const s of sets) {
    const t = s.track || "F";
    if (!tracks[t]) problems.push(`${s.key}: track "${t}" is not defined in quiz.config.json`);
    if (seenKeys.has(s.key)) problems.push(`${s.key}: duplicate set key`);
    seenKeys.add(s.key);
    s.warnings.forEach((w) => problems.push(`${s.key}: ${w}`));
    if (!s.questions.length) problems.push(`${s.key}: no valid questions`);
    s.questions.forEach((q) => {
      if (q.module !== "—" && Object.keys(modNames).length && !modNames[q.module]) problems.push(`${s.key} ${q.id}: unknown module/course "${q.module}"`);
      if (!q.reasoning) problems.push(`${s.key} ${q.id}: answer has no reasoning`);
    });
    if (summary[t]) { summary[t].sets++; summary[t].questions += s.questions.length; }
    console.log(`  ✓ ${s.key.padEnd(36)} track ${t}  ${String(s.questions.length).padStart(3)} Q  ${s.minutes || "?"} min`);
  }
}

for (const [t, v] of Object.entries(summary)) {
  console.log(`Track ${t} (${(tracks[t] || {}).code || t}): ${v.sets} sets, ${v.questions} questions, ${v.placeholders} planned`);
  if (!v.sets && !v.placeholders) problems.push(`track ${t}: no sets and no placeholders`);
}

if (problems.length) {
  console.error(`\n✗ ${problems.length} problem(s):`);
  problems.forEach((p) => console.error("  - " + p));
  process.exit(1);
}
console.log("\n✓ All question data is valid.");
