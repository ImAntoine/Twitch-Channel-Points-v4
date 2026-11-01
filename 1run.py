import logging
import os
import sys
from colorama import Fore
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.logger import LoggerSettings, ColorPalette
from TwitchChannelPointsMiner.classes.Chat import ChatPresence
from TwitchChannelPointsMiner.classes.Settings import Priority, Events, FollowersOrder
from TwitchChannelPointsMiner.classes.entities.Bet import Strategy, BetSettings, Condition, OutcomeKeys, FilterCondition, DelayMode
from TwitchChannelPointsMiner.classes.entities.Streamer import Streamer, StreamerSettings

TWITCH_USERNAME = os.environ.get("TWITCH_USERNAME", "")

if not TWITCH_USERNAME or TWITCH_USERNAME == "your-twitch-username":
    print("=" * 80)
    print("ERROR: Twitch username not configured!")
    print("=" * 80)
    print("\nPlease configure your Twitch username using one of these methods:\n")
    print("1. RECOMMENDED: Add TWITCH_USERNAME to Replit Secrets")
    print("   - Click the lock icon in the left sidebar")
    print("   - Add a new secret with key: TWITCH_USERNAME")
    print("   - Set the value to your actual Twitch username")
    print("   - Restart the workflow\n")
    print("2. ALTERNATIVE: Edit run.py line 13")
    print("   - Change: TWITCH_USERNAME = os.environ.get(\"TWITCH_USERNAME\", \"\")")
    print("   - To: TWITCH_USERNAME = \"your-actual-username\"\n")
    print("=" * 80)
    sys.exit(1)

twitch_miner = TwitchChannelPointsMiner(
    username=TWITCH_USERNAME,
    claim_drops_startup=False,
    priority=[
        Priority.STREAK,
        Priority.DROPS,
        Priority.ORDER
    ],
    enable_analytics=True,
    disable_ssl_cert_verification=False,
    disable_at_in_nickname=False,
    logger_settings=LoggerSettings(
        save=True,
        console_level=logging.INFO,
        console_username=False,
        auto_clear=True,
        time_zone="",
        file_level=logging.DEBUG,
        emoji=True,
        less=False,
        colored=True,
        color_palette=ColorPalette(
            STREAMER_online="GREEN",
            streamer_offline="red",
            BET_wiN=Fore.MAGENTA
        ),
    ),
    streamer_settings=StreamerSettings(
        make_predictions=True,
        follow_raid=True,
        claim_drops=True,
        claim_moments=True,
        watch_streak=True,
        community_goals=False,
        chat=ChatPresence.ONLINE,
        bet=BetSettings(
            strategy=Strategy.SMART,
            percentage=5,
            percentage_gap=20,
            max_points=50000,
            stealth_mode=True,
            delay_mode=DelayMode.FROM_END,
            delay=6,
            minimum_points=20000,
            filter_condition=FilterCondition(
                by=OutcomeKeys.TOTAL_USERS,
                where=Condition.LTE,
                value=800
            )
        )
    )
)

twitch_miner.analytics(host="0.0.0.0", port=5000, refresh=5, days_ago=7)

twitch_miner.mine(
    [
        "streamer-username01",
        "streamer-username02",
        "streamer-username03",
    ],
    followers=False,
    followers_order=FollowersOrder.ASC
)
