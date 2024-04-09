from .SendToDiscordWebhook import SendToDiscordWebhook

# Add this new node to the dictionary of all nodes
NODE_CLASS_MAPPINGS = {
    "SendToDiscordWebhook": SendToDiscordWebhook,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SendToDiscordWebhook": "Send To Discord Webhook",
}
