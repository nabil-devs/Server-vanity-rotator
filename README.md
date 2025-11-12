# Server-vanity-rotator

Short description
: A small educational project that demonstrates the concept of rotating a Discord server vanity string from a list. This repository is provided for study and code-read purposes only. See the **Disclaimer** section.

Repository reference: https://github.com/nabil-devs/Server-vanity-rotator. :contentReference[oaicite:1]{index=1}

---

## Disclaimer — Read before using

This project includes code patterns that, if executed as a *selfbot* (an automated script using a user account), violate Discord's Terms of Service. Do not run or deploy the code against accounts or servers for which you do not have explicit ownership or written permission.

If your goal is automation on Discord, use a proper **bot account** created via the Discord Developer Portal and invite it with the correct OAuth2 scopes and server permissions (for example, `applications.commands` and `manage_guild` / `manage_roles` where required). Converting this project to a legitimate bot is the recommended and supported path for production or shared deployments.

---

## Contents

- `.env` — example environment file (sensitive values removed in this repo).
- `main.py` — primary script present in the repository. Contains the core logic for reading a vanity list and attempting periodic updates.
- `vanity.txt` — newline-separated list of candidate vanity strings.
- `LICENSE` — MIT license.

---

## Purpose

This repository exists to illustrate the following concepts in an educational context:

- reading configuration from environment variables,
- loading candidate values from a simple text file,
- scheduling repeated asynchronous tasks,
- basic error handling around external API requests.

The repository does not provide or endorse running unauthorized automation against third-party services.

---

## Architecture (high level)

- `main.py` loads configuration from environment variables and `vanity.txt`.
- A background loop periodically selects a random vanity string and attempts to apply it via an API client.
- Basic protections are included in the code to avoid repeating the immediately previous selection and to catch common HTTP/permission errors.

---

## Safe alternative / How to adapt for a compliant bot

If you want to achieve similar behavior while staying within Discord's rules, follow this high-level approach:

1. Create a bot application at the Discord Developer Portal.
2. Add a bot user to the application.
3. Invite the bot to the target server using an OAuth2 invite link with the appropriate scopes and permissions. For server configuration tasks the bot needs the server-level permissions assigned by server admins (for example `Manage Guild` if applicable).
4. Replace any code that uses a user token with the bot token and run the code with `bot=True` (or the equivalent in your chosen library).
5. Respect rate limits. Design your rotation so it does not attempt frequent changes that may be rejected by the API or flagged as abusive.
6. Obtain explicit permission from server owners before making any configuration changes.

---

## Configuration (example, non-actionable)

Keep sensitive values out of source control. Use environment variables or a secrets manager for tokens and IDs. The repository contains an example `.env` file for illustration only.



