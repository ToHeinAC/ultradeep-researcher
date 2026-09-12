# SEC EDGAR User-Agent patch

**Status:** local patch required. Applies to `hyperresearch==0.11.1`.
**Fix:** `uv run python scripts/patch_edgar_ua.py` — re-run after every
environment rebuild.

## Symptom

`scholar search -s edgar` returns zero results for every query, with no error:

```
returned: 0 | per_source: {'edgar': 0} | failed: []
```

`scholar sources -j` reports EDGAR as healthy (`"available": true`), because
availability only checks that `HYPERRESEARCH_CONTACT_EMAIL` is set — it never
probes the endpoint. This is the dangerous part: the pipeline silently drops an
entire source class while reporting green, so a filings-dependent report is
built on nothing and nobody is told.

## Cause

The SEC's WAF rejects any `User-Agent` containing a URL. Measured against
`https://efts.sec.gov/LATEST/search-index?q=Apple`:

| User-Agent | Result |
|---|---|
| `hyperresearch (https://github.com/jordan-gibbs/hyperresearch) (mailto:…)` | **403** — as shipped |
| `hyperresearch (https://github.com/jordan-gibbs/hyperresearch)` | **403** — the URL alone is enough |
| `hyperresearch (mailto:…)` | 200 |
| `hyperresearch you@example.com` | 200 — SEC's documented form |

`scholar/base.py` builds every request's UA from a hardcoded constant:

```python
_UA = "hyperresearch (https://github.com/jordan-gibbs/hyperresearch)"

def user_agent() -> str:
    email = contact_email()
    return f"{_UA} (mailto:{email})" if email else _UA
```

`_UA` has no environment override and no config key, so EDGAR is unreachable in
0.11.1 for every user regardless of configuration. The 403 is swallowed by
`fetch_json`, which returns `None` on any failure, which the provider maps to an
empty result list — hence zero results and an empty `failed` list.

## The patch

Drop the URL from the constant. The contact address is what the SEC actually
requires, and it is still appended:

```diff
-_UA = "hyperresearch (https://github.com/jordan-gibbs/hyperresearch)"
+_UA = "hyperresearch"
```

Resulting UA: `hyperresearch (mailto:<HYPERRESEARCH_CONTACT_EMAIL>)`.

This edit lives in `.venv/lib/python3.11/site-packages/hyperresearch/`, which is
gitignored. **Any operation that reinstalls or upgrades the package reverts it**
— `uv pip install -U`, a version bump followed by `uv sync`, or a venv rebuild —
and EDGAR goes back to silently returning zero.

Operations that leave the patch intact: `uv run` and `uv sync` when the venv
already satisfies the lock, since uv then reinstalls nothing. Do not rely on
this. `scripts/patch_edgar_ua.py` is idempotent, so re-running it after any
environment change is always safe and costs nothing.

## Verifying

```bash
set -a; . ./.env; set +a
.venv/bin/python3 -c "from hyperresearch.scholar.base import user_agent; print(user_agent())"
.venv/bin/hyperresearch scholar search "Apple" -s edgar --limit 5 --fresh -j
```

Expect a UA with no URL, and five real filings. Zero results means the patch is
not applied.

## Upstream

Not yet reported. A proper fix would read the UA from an environment variable,
or omit the URL for hosts known to reject it. Until then this patch is the only
route to a working EDGAR provider.
