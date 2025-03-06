# flow_sync_solutions

FlowSync-Solutions/  
├── api-gateway/                # API Gateway (единая точка входа)  
│   ├── src/  
│   │   ├── main.py            # Логика маршрутизации и аутентификации  
│   │   └── config.py          # Конфигурация (адреса сервисов)  
│   └── Dockerfile             # Docker-файл для контейнеризации  
├── auth-service/              # Сервис авторизации  
│   ├── src/  
│   │   ├── main.py            # Логика API (логин, регистрация)  
│   │   ├── models.py          # Модели данных (User, Role)  
│   │   └── db.py              # Подключение к БД  
│   └── Dockerfile  
├── document-service/          # Сервис управления документами  
│   ├── src/  
│   │   ├── main.py            # Логика API (создание, получение документов)  
│   │   ├── models.py          # Модели (DocumentCreate, DocumentResponse)  
│   │   └── db.py              # Подключение к PostgreSQL  
│   └── Dockerfile  
├── workflow-service/          # Сервис согласования  
│   ├── src/  
│   │   ├── main.go           # Логика на Go (асинхронная обработка)  
│   │   └── kafka.go          # Интеграция с Kafka  
│   └── Dockerfile  
├── search-service/            # Сервис поиска   
│   ├── src/  
│   │   ├── main.py           # Логика поиска через Elasticsearch  
│   │   └── search.py         # Функции работы с Elasticsearch  
│   └── Dockerfile  
├── storage-service/           # Сервис хранения файлов  
│   ├── src/  
│   │   ├── main.js           # Логика на Node.js для работы с MinIO  
│   │   └── storage.js        # Функции загрузки/скачивания  
│   └── Dockerfile  
├── notification-service/      # Сервис уведомлений  
│   ├── src/  
│   │   ├── main.py           # Логика отправки уведомлений  
│   │   ├── tasks.py          # Асинхронные задачи через Celery  
│   │   └── kafka_consumer.py # Чтение событий из Kafka  
│   └── Dockerfile  
├── monitoring/                # Мониторинг и логирование  
│   ├── prometheus/           # Конфигурация Prometheus  
│   └── grafana/              # Конфигурация Grafana  
├── shared/                    # Общие библиотеки и конфигурации  
│   ├── db/                   # Схемы БД, миграции (например, Alembic)  
│   └── utils/                # Утилиты (логгеры, валидаторы)  
├── docker-compose.yml         # Файл для запуска всех сервисов  
├── .env                      # Переменные окружения (DB_URL, Kafka settings)  
└── README.md                 # Описание проекта и инструкции  
