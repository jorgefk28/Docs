import type { Plugin } from "@opencode-ai/plugin"
import { tool } from "@opencode-ai/plugin"
import { readFileSync } from "fs"
import { join, dirname } from "path"
import { fileURLToPath } from "url"

const JIRA_BASE = "https://candidly.atlassian.net/rest/api/2"

function parseEnv(path: string): Record<string, string> {
  try {
    return Object.fromEntries(
      readFileSync(path, "utf-8")
        .split("\n")
        .filter((line) => line.trim() && !line.startsWith("#"))
        .flatMap((line) => {
          const idx = line.indexOf("=")
          if (idx === -1) return []
          const key = line.slice(0, idx).trim()
          const val = line.slice(idx + 1).trim().replace(/^["']|["']$/g, "")
          return [[key, val]]
        }),
    )
  } catch {
    return {}
  }
}

export const JiraPlugin: Plugin = async (_ctx) => {
  const pluginDir = dirname(fileURLToPath(import.meta.url))
  const { JIRA_EMAIL: email, JIRA_API_TOKEN: token } = parseEnv(join(pluginDir, "..", ".env"))

  const authorization =
    email && token ? `Basic ${Buffer.from(`${email}:${token}`).toString("base64")}` : null

  async function jiraGet(path: string): Promise<Response> {
    if (!authorization) throw new Error("Missing JIRA_EMAIL or JIRA_API_TOKEN in .opencode/.env")
    const url = `${JIRA_BASE}${path}`
    console.log(`GET ${url}`)
    return fetch(url, { headers: { Authorization: authorization, Accept: "application/json" } })
  }

  async function jiraJson(path: string): Promise<string> {
    const response = await jiraGet(path)
    console.log(`Response: ${response.status} ${response.statusText}`)
    if (!response.ok) throw new Error(`Jira ${response.status} ${response.statusText}: ${await response.text()}`)
    return JSON.stringify(await response.json(), null, 2)
  }

  return {
    tool: {
      getJiraIssue: tool({
        description: "Fetches a Jira issue from candidly.atlassian.net by ID or key and returns its full JSON.",
        args: {
          issueIdOrKey: tool.schema.string().describe("Issue ID or key (e.g. CAI-123)"),
        },
        async execute(args, _context) {
          return jiraJson(`/issue/${encodeURIComponent(args.issueIdOrKey.toLowerCase().trim())}`)
        },
      }),
    },
  }
}
