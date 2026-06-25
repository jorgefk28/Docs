import type { Plugin } from "@opencode-ai/plugin"
import { tool } from "@opencode-ai/plugin"
import { writeFileSync, mkdirSync } from "fs"
import { join, isAbsolute, basename } from "path"

export const WriteArtifactPlugin: Plugin = async (_ctx) => {
  return {
    tool: {
      writeArtifact: tool({
        description:
          "Writes a file to `<repoPath>/OPENCODE-ARTIFACTS/<name>`. " +
          "Use this to persist any generated content (git output, reports, etc.) as a reviewable artifact.",
        args: {
          repoPath: tool.schema
            .string()
            .describe("Absolute path to the repository root"),
          name: tool.schema
            .string()
            .describe("Filename including extension (e.g. uncommitted_changes.md)"),
          contents: tool.schema
            .string()
            .describe("Full file contents to write"),
        },
        async execute(args, _context) {
          if (!isAbsolute(args.repoPath)) {
            throw new Error(`repoPath must be absolute, got: ${args.repoPath}`)
          }

          const safeName = basename(args.name)
          const artifactsDir = join(args.repoPath, "OPENCODE-ARTIFACTS")
          mkdirSync(artifactsDir, { recursive: true })

          const outPath = join(artifactsDir, safeName)
          writeFileSync(outPath, args.contents)

          return `Written to ${outPath}`
        },
      }),
    },
  }
}
