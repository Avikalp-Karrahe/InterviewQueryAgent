# test_key.py  – works with openai ≥ 1.0
import os
from openai import OpenAI
from notion_client import Client

# ── 1. Keys ────────────────────────────────────────────────
os.environ["OPENAI_API_KEY"] = (
    "sk-proj-iu2oTinvWeUt8bcn91f_mRoxgdcr5URaVjeUnhJ6wrCjUx6X1xG5Aawjx3kcB3zWgi2xOYEbMQT3BlbkFJjkA9J4N7Bab5D"
    "-ZsPDcaHy06Af6g0IpFe8RK_ROkXXt9Quo3ZZvKVY42prpQp6QLBRc9SfTdQA"
)
NOTION_TOKEN  = "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"
NOTION_PARENT = "20344d2a2c28800eb2f4caec3cebfbd6"

# ── 2. Verify OpenAI key ───────────────────────────────────
client = OpenAI()                       # uses env var
models = [m.id for m in client.models.list().data]
print("✅ OpenAI key OK — first 3 models:", models[:3])

# ── 3. Verify Notion access ─────────────────────────────────
notion = Client(auth=NOTION_TOKEN)
page   = notion.pages.retrieve(page_id=NOTION_PARENT)
title  = page["properties"]["title"]["title"][0]["plain_text"]
print("✅ Notion token OK — page title:", title)
