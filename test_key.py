# test_key.py  – works with openai ≥ 1.0
import os
from openai import OpenAI
from notion_client import Client

# ── 1. Keys ────────────────────────────────────────────────


# ── 2. Verify OpenAI key ───────────────────────────────────
client = OpenAI()                       # uses env var
models = [m.id for m in client.models.list().data]
print("✅ OpenAI key OK — first 3 models:", models[:3])

# ── 3. Verify Notion access ─────────────────────────────────
notion = Client(auth=NOTION_TOKEN)
page   = notion.pages.retrieve(page_id=NOTION_PARENT)
title  = page["properties"]["title"]["title"][0]["plain_text"]
print("✅ Notion token OK — page title:", title)
