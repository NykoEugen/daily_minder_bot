from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery

from handlers.db_handler import create_table_user, insert_user
from keyboards.inline_keyboard import inline_keyboard, main_menu_buttons

router = Router()


@router.message(Command('start'))
async def start_handler(message: Message):
    kb = main_menu_buttons()

    await message.answer('Hello in Minder Bot', reply_markup=kb)

    print(message)

    user_id = message.from_user.id

    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    create_table_user()
    insert_user(user_id, username, first_name, last_name)


@router.callback_query(Text('reminder', ignore_case=True))
async def handle_reminder(callback: CallbackQuery):
    kb = inline_keyboard(reminder_list='List of reminds', set_remind='Set remind',
                         remove_remind='Remove remind')
    await callback.message.answer('Reminder Menu', reply_markup=kb)
    await callback.answer()


# message_id=3357 date=datetime.datetime(2023, 8, 29, 8, 28, 24, tzinfo=datetime.timezone.utc)
# chat=Chat(id=385833312, type='private', title=None, username='Astro_Raph', first_name='Евгений',
# last_name='Николенко', is_forum=None, photo=None, active_usernames=None, emoji_status_custom_emoji_id=None,
# bio=None, has_private_forwards=None, has_restricted_voice_and_video_messages=None, join_to_send_messages=None,
# join_by_request=None, description=None, invite_link=None, pinned_message=None, permissions=None,
# slow_mode_delay=None, message_auto_delete_time=None, has_aggressive_anti_spam_enabled=None,
# has_hidden_members=None, has_protected_content=None, sticker_set_name=None, can_set_sticker_set=None,
# linked_chat_id=None, location=None) message_thread_id=None from_user=User(id=385833312, is_bot=False,
# first_name='Евгений', last_name='Николенко', username='Astro_Raph', language_code='ru', is_premium=None,
# added_to_attachment_menu=None, can_join_groups=None, can_read_all_group_messages=None,
# supports_inline_queries=None) sender_chat=None forward_from=None forward_from_chat=None
# forward_from_message_id=None forward_signature=None forward_sender_name=None forward_date=None
# is_topic_message=None is_automatic_forward=None reply_to_message=None via_bot=None edit_date=None
# has_protected_content=None media_group_id=None author_signature=None text='/start'
# entities=[MessageEntity(type='bot_command', offset=0, length=6, url=None, user=None,
# language=None, custom_emoji_id=None)] animation=None audio=None document=None photo=None
# sticker=None video=None video_note=None voice=None caption=None caption_entities=None
# has_media_spoiler=None contact=None dice=None game=None poll=None venue=None
# location=None new_chat_members=None left_chat_member=None new_chat_title=None
# new_chat_photo=None delete_chat_photo=None group_chat_created=None supergroup_chat_created=None
# channel_chat_created=None message_auto_delete_timer_changed=None migrate_to_chat_id=None migrate_from_chat_id=None
# pinned_message=None invoice=None successful_payment=None user_shared=None chat_shared=None connected_website=None
# write_access_allowed=None passport_data=None proximity_alert_triggered=None forum_topic_created=None
# forum_topic_edited=None forum_topic_closed=None forum_topic_reopened=None general_forum_topic_hidden=None
# general_forum_topic_unhidden=None video_chat_scheduled=None video_chat_started=None video_chat_ended=None
# video_chat_participants_invited=None web_app_data=None reply_markup=None