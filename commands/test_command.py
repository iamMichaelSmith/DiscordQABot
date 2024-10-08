from discord_lambda import Interaction, Embedding, CommandArg, CommandRegistry
import time


def ping_command(inter: Interaction) -> None:
    inter.send_response(content="*pong!*)
                        

def setup(registry: CommandRegistry) -> None:
    registry.register_cmd(func=ping_command, name="ping", desc="Pings the bot"
