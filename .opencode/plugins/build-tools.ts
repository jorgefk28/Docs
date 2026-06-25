import type { Plugin } from "@opencode-ai/plugin"
import { tool } from "@opencode-ai/plugin"
import { spawnSync } from "child_process"

const MAX_BUFFER = 10 * 1024 * 1024

function runStep(cmd: string, args: string[], cwd: string): { ok: boolean; out: string } {
  const result = spawnSync(cmd, args, { cwd, encoding: "utf-8", maxBuffer: MAX_BUFFER })
  const out = [result.stdout, result.stderr].filter(Boolean).join("\n").trim()
  if (result.error) return { ok: false, out: result.error.message }
  return { ok: result.status === 0, out: out || "(no output)" }
}

export const BuildToolsPlugin: Plugin = async (_ctx) => {
  return {
    tool: {
      validateAndBuild: tool({
        description:
          "Runs `pnpm run tsc`, `pnpm run lint:fix`, and `pnpm run build` in sequence. " +
          "Stops and reports on the first failure. Returns combined output of all steps.",
        args: {},
        async execute(_args, context) {
          const steps = [
            { label: "tsc", cmd: "pnpm", args: ["run", "tsc"] },
            { label: "lint:fix", cmd: "pnpm", args: ["run", "lint:fix"] },
            { label: "build", cmd: "pnpm", args: ["run", "build"] },
          ]

          const lines: string[] = []

          for (const step of steps) {
            const { ok, out } = runStep(step.cmd, step.args, context.directory)
            lines.push(`## ${step.label}\n${out}`)
            if (!ok) {
              lines.push(`\n❌ Stopped at step: ${step.label}`)
              return lines.join("\n\n")
            }
          }

          lines.push("\n✅ All steps passed.")
          return lines.join("\n\n")
        },
      }),
    },
  }
}
