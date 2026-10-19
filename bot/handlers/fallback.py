from __future__ import annotations

import logging

from aiogram import Router
from aiogram.types import CallbackQuery, ErrorEvent, Message

from bot.templates import render

logger = logging.getLogger(__name__)
router = Router()


@router.callback_query()
async def on_stale_button(cb: CallbackQuery) -> None:
    logger.info("user %s: stale button %r", cb.from_user.id, cb.data)
    await cb.answer(render("error_stale_button"), show_alert=True)


@router.message()
async def on_unhandled_message(message: Message) -> None:
    logger.info("user %s: unhandled message", message.from_user.id)  # type: ignore[union-attr]
    await message.answer(render("error_unhandled_message"), parse_mode="HTML")


@router.errors()
async def on_error(event: ErrorEvent) -> None:
    update = event.update
    user = getattr(update.event, "from_user", None)
    logger.error(
        "update %s from user %s failed", update.update_id, user.id if user else None,
        exc_info=event.exception,
    )
    message = update.message or (update.callback_query.message if update.callback_query else None)
    if message is not None:
        await message.answer(render("error_internal"), parse_mode="HTML")
