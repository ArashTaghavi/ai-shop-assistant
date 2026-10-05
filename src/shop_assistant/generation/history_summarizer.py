class HistorySummarizer:
    def __init__(self, generator):
        self.generator = generator

    def summarize(
        self,
        messages: list[dict],
        previous_summary: str = "",
    ) -> str:

        messages_text = "\n".join(
            f"{message['role']}: {message['content']}" for message in messages
        )

        prompt = f"""
تو وظیفه داری سابقه مکالمه را خلاصه کنی.

[خلاصه قبلی]:
{previous_summary}

[مکالمات جدید]:
{messages_text}

[ملاحظات]:
- خلاصه قبلی و مکالمات جدید را با هم ترکیب کن.
- اطلاعات مهم برای ادامه مکالمه را حفظ کن.
- درخواست‌ها و اطلاعات مهم کاربر را حفظ کن.
- پاسخ‌ها و تصمیم‌های مهم قبلی را حفظ کن.
- احوال‌پرسی، تکرار و اطلاعات غیرضروری را حذف کن.
- هیچ اطلاعات جدیدی از خودت اضافه نکن.
- اگر اطلاعات جدید با اطلاعات قبلی تناقض داشت، اطلاعات جدیدتر را نگه دار.
- خلاصه را کوتاه و واضح بنویس.
- فقط خلاصه نهایی را برگردان.
""".strip()

        return self.generator.answer(prompt)
