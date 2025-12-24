"""Lightweight app entry point for Reachy Mini Apps discovery."""

from __future__ import annotations

import asyncio
import threading

from reachy_mini import ReachyMini, ReachyMiniApp


class ReachyMiniConversationApp(ReachyMiniApp):  # type: ignore[misc]
    """Reachy Mini Apps entry point for the conversation app."""

    custom_app_url = "http://0.0.0.0:7860/"
    dont_start_webserver = False

    def run(self, reachy_mini: ReachyMini, stop_event: threading.Event) -> None:
        """Run the Reachy Mini conversation app."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # Import heavy modules only when actually running the app.
        from reachy_mini_conversation_app.main import run
        from reachy_mini_conversation_app.utils import parse_args

        args, _ = parse_args()
        instance_path = self._get_instance_path().parent
        run(
            args,
            robot=reachy_mini,
            app_stop_event=stop_event,
            settings_app=self.settings_app,
            instance_path=instance_path,
        )
