# ─── Type alias ──────────────────────────────────────────────

ToolDef = dict  # Anthropic tool schema dict

# ─── Tool definitions ───────────────────────────────────────

tool_definitions: list[ToolDef] = [1,2,3] # 只提示，不报错 Expected type 'list[dict]', got 'list[int]' instead

