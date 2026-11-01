# Twitch Channel Points Miner - Replit Setup

## Overview
This is a Twitch Channel Points Miner application that automatically farms channel points on Twitch by watching streams, claiming bonuses, and optionally participating in predictions. It includes a web-based analytics dashboard to track your point accumulation.

## Project Structure
- **TwitchChannelPointsMiner/**: Main application package
- **run.py**: Main configuration file for running the miner
- **assets/**: Frontend files for the analytics dashboard
- **logs/**: Application logs (created at runtime)
- **analytics/**: Analytics data files (created at runtime)
- **cookies/**: Session cookies (created at runtime)

## Setup Instructions

### 1. Configure Your Twitch Account
The application reads your Twitch username from the `TWITCH_USERNAME` environment variable (Replit Secret).

**To set up:**
1. Go to the Secrets tab in Replit (lock icon in left sidebar)
2. Add a new secret:
   - Key: `TWITCH_USERNAME`
   - Value: Your Twitch username
3. To support password authentication, add another secret:
   - Key: `TWITCH_PASSWORD`
   - Value: Your Twitch password

Do not hardcode passwords, API tokens, or webhook URLs in `run.py`.

### Optional Notification Integrations

- Add `TELEGRAM_BOT_TOKEN` to Replit Secrets to enable Telegram alerts.
- Add `DISCORD_WEBHOOK_URL` to Replit Secrets to enable Discord alerts.
- These alerts stay disabled when their corresponding secret is unset. Never commit bot tokens or webhook URLs.
- Revoke and replace any token that was previously committed; storing a replacement in Secrets does not invalidate the exposed one.

### 2. Add Streamers to Monitor
In `run.py`, update the streamers list:

```python
twitch_miner.mine(
    [
        "streamer-username01",  # Replace with actual streamer usernames
        "streamer-username02",
        "streamer-username03",
    ],
    followers=False,
    followers_order=FollowersOrder.ASC
)
```

### 3. Optional: Enable Auto-Follow Your Followers
Set `followers=True` in the `mine()` method to automatically load your followed streamers.

### 4. Authentication
On first run, the application will:
1. Use `TWITCH_PASSWORD` when password authentication is required. If it is not set, the script may prompt interactively.
2. Open a browser for authentication
3. Save session cookies for future runs

Do not put your Twitch password directly in `run.py` or commit it to Git.

**Note**: In Replit, you may need to authenticate manually by copying the authentication URL.

## Features Enabled

### Analytics Dashboard
- **URL**: Runs on port 5000 (automatically shown in webview)
- **Features**:
  - Real-time point tracking charts
  - Historical data visualization
  - Per-streamer statistics
  - Live log viewer

### Auto Claiming
- Watch streak bonuses (up to 450 points)
- Channel point bonuses (50 points)
- Raid participation (250 points)
- Moments claiming
- Drop claiming

### Predictions (Optional)
- Smart betting strategy enabled
- Minimum 20,000 points to bet
- 5% of points wagered per prediction
- Stealth mode to avoid detection

## Configuration Options

### Logger Settings
Configured in `run.py`:
- Logs saved to `logs/` directory
- Console level: INFO
- File level: DEBUG
- Colored output with emojis

### Streamer Settings
Default settings (can be customized per streamer):
- Make predictions: Yes
- Follow raids: Yes
- Claim drops: Yes
- Claim moments: Yes
- Watch streak: Yes
- Chat presence: ONLINE

### Betting Strategy
- Strategy: SMART
- Percentage: 5%
- Max points per bet: 50,000
- Minimum points to bet: 20,000
- Stealth mode: Enabled

## Running the Application

The application runs automatically via the configured workflow. To restart:
1. Click the restart button in the workflow panel
2. Check the console logs for any errors
3. Access the analytics dashboard via the webview

## Important Notes

### Replit Environment
- Analytics server is configured for 0.0.0.0:5000 for Replit compatibility
- Port 5000 is the only accessible port for web preview
- Session data is stored in the `cookies/` folder

### Privacy & Security
- Never share your cookies or session files
- Keep your Twitch password secure
- Use Replit Secrets for sensitive data if needed

#### Twitch account access review
- Reviewed Twitch Security and Privacy settings and the Connections page on 2026-11-01 (user-reported).
- No unfamiliar active sessions or connected applications were found.
- No credentials, session identifiers, or app tokens were recorded.

### Limitations
- Requires active Replit session to run
- Authentication may need to be refreshed periodically
- Consider Replit's usage limits for long-running applications

## Troubleshooting

### "No username, exiting..."
- Add `TWITCH_USERNAME` to Replit Secrets (lock icon in left sidebar)
- Or edit `run.py` and hardcode your username (line 10)

### Authentication Issues
- Delete files in `cookies/` folder to force re-authentication
- Check console logs for error messages

### Analytics Dashboard Not Loading
- Ensure workflow is running
- Check that port 5000 is accessible
- Verify no errors in console logs

### Points Not Accumulating
- Verify streamers are online
- Check that authentication is valid
- Review logs for any errors

## Resources
- [Original Repository](https://github.com/rdavydov/Twitch-Channel-Points-Miner-v2)
- [Twitch Channel Points Guide](https://help.twitch.tv/s/article/channel-points-guide)

## Quick Start (First Time Setup)

⚠️ **IMPORTANT**: The workflow will not start until you configure your Twitch username!

### Required Steps:

1. **Set Your Username** (REQUIRED):
   - Click the lock icon (🔒) in the left Replit sidebar
   - Add a new secret:
     - Key: `TWITCH_USERNAME`
     - Value: Your actual Twitch username
   - OR edit `run.py` line 13 to hardcode your username

2. **Configure Streamers**:
   - Edit `run.py` and update the streamers list (lines 83-87)
   - Replace placeholder usernames with actual Twitch streamers you want to monitor

3. **First Authentication**:
   - After setting username, restart the workflow
   - Add `TWITCH_PASSWORD` to Replit Secrets for unattended password authentication, or enter it interactively when prompted
   - Session cookies will be saved for future runs

4. **Access Dashboard**:
   - Once running, the analytics dashboard will be available on port 5000
   - View your point accumulation in real-time

## Recent Changes
- **Setup Date**: October 15, 2025
- Configured for Replit environment
- Analytics server set to 0.0.0.0:5000
- Workflow configured for automatic startup
- Python 3.11 with all dependencies installed
- Username configured via TWITCH_USERNAME environment variable/secret
