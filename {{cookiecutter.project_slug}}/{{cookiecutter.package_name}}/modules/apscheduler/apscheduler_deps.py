from functools import lru_cache

from apscheduler.schedulers.asyncio import AsyncIOScheduler


@lru_cache
def get_scheduler() -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler(
        timezone="UTC",
        jobstore_retry_interval=60,
        job_defaults={"coalesce": True, "replace_existing": True},
    )
    return scheduler
