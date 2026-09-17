# Google Maps Leads API

> Turn Maps queries into lead lists: businesses, phones, websites, and reviews with async job control.

Part of the **DataLeads** API suite (Business category). Requests render in a real browser with anti-bot handling and protected-page support built in - no proxies to manage, no infrastructure to run.

## Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/maps/search` | V1 Maps Search |
| POST | `/maps/status` | V1 Maps Status |
| POST | `/maps/results` | V1 Maps Results |
| POST | `/maps/jobs` | V1 Maps Jobs |

## Quick start

```bash
curl -X POST https://data.dataleads.pro/v1/maps/search \
  -H 'Content-Type: application/json' \
  -d '{"clientKey": "YOUR_CLIENT_KEY", "query": "coffee shops in Austin TX"}'
```

Replace `YOUR_CLIENT_KEY` with your key. Get one at [https://data.dataleads.pro](https://data.dataleads.pro) - free tier included.

## MCP server

- **Remote (Streamable HTTP):** `https://data.dataleads.pro/mcp/google-maps-leads`
- **Stdio (Docker):** `docker run -e DATALEADS_API_KEY=yourkey ghcr.io/dataleads/google-maps-leads-mcp:latest`

## Pricing

| Tier | Price | Requests |
|---|---|---|
| Free | $0 | 500/mo |
| Starter | $9/mo | 5,000 |
| Pro | $29/mo | 25,000 |
| Business | $99/mo | 100,000 |
| Enterprise | custom | custom |

Full plan details at [https://data.dataleads.pro](https://data.dataleads.pro).

## License

MIT - see [LICENSE](LICENSE).
