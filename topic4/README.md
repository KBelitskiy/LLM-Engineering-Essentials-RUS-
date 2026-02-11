# Тема 4. Self-hosted LLM

**Курс находится в разработке, новые материалы появляются регулярно.**

## Содержание

* **Как устроен трансформер**

  Раздел для тех, кто хочет лучше понимать внутреннюю механику модели.

  Для старта по архитектуре трансформера и QKV-attention посмотрите видео [Татьяны Гаинцевой](https://www.linkedin.com/in/tgaintseva/):

  **[1. Seq2seq](https://youtu.be/z-pebP9NuC4)**

  **[2. Механизм внимания](https://youtu.be/e-xQKzi2Hxc)**

  **[3а. Архитектура энкодера трансформера](https://youtu.be/u_hxAuShuZQ)**

  **[3б. Многоголовое внимание и позиционное кодирование](https://youtu.be/eoQTzGi1BkQ)**

  **[3в. Декодер трансформера](https://youtu.be/W4nJnW9R3IE)**

  **[3д. QKV-attention](https://youtu.be/1oMAF55sRls)**

  Дополнительно: [**подробный обзор современных компонентов трансформеров**](https://nebius-academy.github.io/knowledge-base/transformer-architectures/).

* **4.1. Open-source LLM и экосистема Hugging Face** [ссылка на Colab](https://colab.research.google.com/github/Nebius-Academy/LLM-Engineering-Essentials/blob/main/topic4/4.1_open_source_models.ipynb)

  Практика работы с open-source моделями: от базового инференса до мультимодальности и tool use.

* **4.2. Разбор LLM изнутри** [ссылка на Colab](https://colab.research.google.com/github/Nebius-Academy/LLM-Engineering-Essentials/blob/main/topic4/4.2_dissecting_an_llm.ipynb)

  Анализ скрытых состояний и использование хуков PyTorch для исследования поведения модели.

* [**Основы инференса LLM**](https://nebius-academy.github.io/knowledge-base/llm-inference-essentials/)

  Теория по метрикам инференса, производительности и практическим ограничениям в продакшене.

  **4.3. Метрики инференса LLM** [ссылка на Colab](https://colab.research.google.com/github/Nebius-Academy/LLM-Engineering-Essentials/blob/main/topic4/4.3_llm_inference_metrics.ipynb)

## Часть проекта: интеграция open-source LLM в сервис

Материалы находятся в репозитории [LLMOps Essentials](https://github.com/Nebius-Academy/LLMOps-Essentials), ветка `open-source-llm`.

Для этой части потребуется GPU-виртуальная машина.

Инструкция по развертыванию: [DEPLOYMENT_MANUAL.md](https://github.com/Nebius-Academy/LLMOps-Essentials/blob/main/DEPLOYMENT_MANUAL.md).

**Задание:**

1. Обновите список доступных LLM и добавьте актуальную модель.
2. Оцените максимальный размер истории, который выдерживает ваш GPU.
3. (Продвинуто) Реализуйте batching запросов перед отправкой в LLM и продумайте стратегию паддинга для историй разной длины.