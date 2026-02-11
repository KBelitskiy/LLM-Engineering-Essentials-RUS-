# Тема 1. Основы LLM API

**Курс находится в разработке, новые материалы появляются регулярно.**

**Подпишитесь на обновления: [Будьте в курсе](https://academy.nebius.com/llm-engineering-essentials/update/)**.

## Содержание

* **1.1. Введение в API LLM** [ссылка на Colab](https://colab.research.google.com/github/Nebius-Academy/LLM-Engineering-Essentials/blob/main/topic1/1.1_intro_to_llm_apis.ipynb)

  Поэкспериментируйте с задачами text-to-image и image-to-text, отправкой API-запросов и разбором ответов через OpenAI API и [Nebius AI Studio](https://studio.nebius.ai/) (Llama, Mistral, DeepSeek, Qwen и др.).

* **1.2. Токенизация** [ссылка на Colab](https://colab.research.google.com/github/Nebius-Academy/LLM-Engineering-Essentials/blob/main/topic1/1.2_tokenization.ipynb)

  Разберитесь, что такое токены и как токенизация влияет на обработку текста в LLM.

* **1.3. Базовые рекомендации по промптингу** [ссылка на Colab](https://colab.research.google.com/github/Nebius-Academy/LLM-Engineering-Essentials/blob/main/topic1/1.3_basic_prompting_guidelines.ipynb)

  Практические приемы, которые помогают получать более качественные ответы от LLM.

* **1.4. Что может пойти не так при работе с LLM** [ссылка на Colab](https://colab.research.google.com/github/Nebius-Academy/LLM-Engineering-Essentials/blob/main/topic1/1.4_what_can_possibly_go_wrong_with_an_llm.ipynb)

  Галлюцинации, предвзятость, prompt injection и другие типовые риски.

* **1.5. Как выбирать LLM** [ссылка на Colab](https://colab.research.google.com/github/Nebius-Academy/LLM-Engineering-Essentials/blob/main/topic1/1.5_how_to_choose_an_llm.ipynb)

  Критерии выбора модели: размер, качество, стоимость, latency и reasoning-возможности.

* **1.6. Параметры инференса LLM** [ссылка на Colab](https://colab.research.google.com/github/Nebius-Academy/LLM-Engineering-Essentials/blob/main/topic1/1.6_llm_inference_parameters.ipynb)

  Как параметры генерации влияют на случайность ответа, креативность и воспроизводимость.

* **1.7. Создание персонажа на базе LLM** [ссылка на Colab](https://colab.research.google.com/github/Nebius-Academy/LLM-Engineering-Essentials/blob/main/topic1/1.7_creating_an_llm-powered_character.ipynb)

  Соберите чат-бота-персонажа и попробуйте расширенные механики, включая внутренний "блокнот мыслей".

## Часть проекта: развертывание сервиса на базе LLM

Материалы проекта находятся в [репозитории LLMOps Essentials](https://github.com/Nebius-Academy/LLMOps-Essentials). На этом этапе нужна ветка `main` с базовым API-сервисом. К RAG и self-hosted LLM вы перейдете в следующих темах.

Полезные видео:

1. [Проектирование чат-сервиса с LLM: простой вариант](https://youtu.be/pOXA7ZuB-98)
2. [Проектирование чат-сервиса с LLM: запуск сервиса](https://youtu.be/Ry0nXts6B0o)
3. [Проектирование чат-сервиса с LLM: продвинутый вариант](https://youtu.be/N6okNbcGjY8)
4. [Запуск чат-сервиса](https://youtu.be/pPFWefazyAQ)
5. (Опционально) [Дополнительные темы: развертывание в Kubernetes](https://youtu.be/uVEP4doSGQ4)

Инструкция по развертыванию: [DEPLOYMENT_MANUAL.md](https://github.com/Nebius-Academy/LLMOps-Essentials/blob/main/DEPLOYMENT_MANUAL.md).

**Задание:**

1. Обновите список доступных LLM и добавьте актуальную модель.
2. Найдите, где хранится история чата, и попробуйте получить ее через запрос из Colab.
3. Добавьте поддержку блокнота (notebook) для персонажа.

## Дополнительное чтение

* [**Обзор обучения LLM**](https://nebius-academy.github.io/knowledge-base/llm-training-overview/)