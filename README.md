# Klipus

A Discord bot for downloading Medal.tv clips.

## Usage

```
/medal <url>
```

Paste a `medal.tv` or `clips.medal.tv` link and the bot will upload the clip directly to Discord.

## Setup

1. Clone the repo
2. Create a `.env` file:
```
DISCORD_TOKEN=your_token_here
```
3. Create the temp directory:
```bash
mkdir -p /mnt/ssd/klipus/tmp
```
4. Run with Docker:
```bash
docker compose up -d --build
```

## Requirements

- Docker
- A Discord bot token ([Discord Developer Portal](https://discord.com/developers/applications))