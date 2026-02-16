"""
Единая настройка LLM API для курса LLM Engineering Essentials.

Используется любой OpenAPI-совместимый провайдер:
- Задайте OPENAI_API_KEY (ключ API).
- Если провайдер использует свой URL — задайте OPENAI_BASE_URL.
- Ключ можно загрузить из файла api_key или openai_api_key (например, в Colab).
"""

import os
from pathlib import Path
from typing import Optional


def _load_key_from_file(filename: str) -> Optional[str]:
    """Загрузить ключ из файла в текущей директории (например, в Colab после загрузки)."""
    path = Path(filename)
    if path.exists():
        return path.read_text().strip()
    return None


def setup_llm_api_env(
    api_key_file: Optional[str] = None,
    openai_api_key_file: Optional[str] = None,
) -> None:
    """
    Настроить переменные окружения для LLM API из env или из файлов.

    Вызывайте в начале блокнота. Ключ читается из OPENAI_API_KEY или из файлов
    api_key / openai_api_key.

    Args:
        api_key_file: имя файла с ключом (по умолчанию "api_key")
        openai_api_key_file: имя файла с ключом (по умолчанию "openai_api_key")
    """
    if api_key_file is None:
        api_key_file = "api_key"
    if openai_api_key_file is None:
        openai_api_key_file = "openai_api_key"

    if not os.environ.get("OPENAI_API_KEY"):
        key = _load_key_from_file(api_key_file) or _load_key_from_file(openai_api_key_file)
        if key:
            os.environ["OPENAI_API_KEY"] = key


def get_llm_api_key() -> Optional[str]:
    """Вернуть API-ключ (OPENAI_API_KEY)."""
    return os.environ.get("OPENAI_API_KEY")


def get_llm_base_url() -> Optional[str]:
    """
    Вернуть base_url для OpenAI-клиента.
    Если задан OPENAI_BASE_URL — возвращается он (с завершающим слэшем), иначе None.
    """
    url = os.environ.get("OPENAI_BASE_URL")
    if not url:
        return None
    return url.rstrip("/") + "/"


def get_openai_client():
    """
    Создать и вернуть синхронный OpenAI-клиент.

    Использует get_llm_api_key() и get_llm_base_url(). Вызовите setup_llm_api_env()
    перед первым использованием или задайте OPENAI_API_KEY в окружении.
    """
    from openai import OpenAI

    key = get_llm_api_key()
    if not key:
        raise ValueError(
            "Не задан API-ключ. Укажите OPENAI_API_KEY в окружении "
            "или загрузите ключ в файл api_key / openai_api_key и вызовите setup_llm_api_env()."
        )
    base_url = get_llm_base_url()
    kwargs = {"api_key": key}
    if base_url:
        kwargs["base_url"] = base_url
    return OpenAI(**kwargs)


def get_async_openai_client():
    """Создать и вернуть асинхронный AsyncOpenAI-клиент. Аналогично get_openai_client()."""
    from openai import AsyncOpenAI

    key = get_llm_api_key()
    if not key:
        raise ValueError(
            "Не задан API-ключ. Укажите OPENAI_API_KEY в окружении "
            "или загрузите ключ в файл api_key / openai_api_key и вызовите setup_llm_api_env()."
        )
    base_url = get_llm_base_url()
    kwargs = {"api_key": key}
    if base_url:
        kwargs["base_url"] = base_url
    return AsyncOpenAI(**kwargs)
