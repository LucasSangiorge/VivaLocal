Semana 1 — Fundação do Backend
Stack
Python
FastAPI
PostgreSQL
SQLAlchemy
Alembic
Pydantic
Pytest
Docker
Git/GitHub
Estrutura
vemai/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── repositories/
│   │
│   ├── tests/
│   └── main.py
│
├── frontend/
│
├── database/
│
├── docs/
│
├── docker-compose.yml
├── README.md
└── .env.example
Banco inicial
users
cities
categories
establishments
addresses
opening_hours
API
POST /auth/register
POST /auth/login

GET /cities
GET /categories

GET /establishments
GET /establishments/{id}
Semana 2 — Lugares e experiências

Agora entra o conteúdo.

Categorias
🍽️ Restaurante
🍺 Bar
🏞️ Natureza
💦 Cachoeira
🥾 Trilha
🎭 Evento
🎵 Música
🏨 Hospedagem
🎟️ Experiência

Cada estabelecimento teria:

nome
descrição
categoria
endereço
latitude
longitude
telefone
Instagram/site
preço médio
horário
fotos
status
API
GET /places
GET /places/{id}

GET /restaurants
GET /events
GET /tourist-attractions

Filtros:

GET /places?category=restaurant
GET /places?city=lagoa-santa
GET /places?price_max=100
GET /places?open_now=true
Semana 3 — ⭐ O coração do projeto
“O que fazer hoje?”

Aqui começa a diferenciação.

O usuário responde:

📍 Onde?
Lagoa Santa

📅 Quando?
Hoje

💰 Quanto quer gastar?
Até R$ 150

🎯 O que você quer?
Comer + passeio

👥 Quantas pessoas?
2

A API processa.

Resultado
Seu programa para hoje:

15:30
🏞️ Passeio

18:30
☕ Café

20:00
🍽️ Restaurante

22:00
🎵 Música ao vivo
🧠 Motor de recomendação

Inicialmente não precisa de IA.

Faça regras determinísticas.

Exemplo:

+ categoria escolhida
+ aberto hoje
+ horário compatível
+ distância
+ orçamento
+ disponibilidade

Depois você pode evoluir para:

Recomendação personalizada
        ↓
Histórico
        ↓
Preferências
        ↓
IA

Isso é importante para seu portfólio porque mostra que você sabe construir regra de negócio antes de colocar IA em tudo.

Semana 4 — Frontend + Deploy

Frontend simples:

Next.js
TypeScript
Tailwind
Página inicial
----------------------------------

          VemAí

     O que fazer hoje?

📍 Lagoa Santa

[ 🍽️ Comer ]
[ 🏞️ Passear ]
[ 🎵 Curtir ]
[ 💰 Barato ]

        [ DESCOBRIR ]

----------------------------------

Resultado:

Hoje encontramos 18 opções

┌─────────────────────┐
│ 🍽️ Restaurante X   │
│ ⭐ 4.7              │
│ $$                  │
│ Aberto até 23:00    │
└─────────────────────┘
Deploy
Frontend → Vercel
Backend  → Render/Railway
Banco    → PostgreSQL
🟡 FASE 2 — PRODUTO COMERCIAL

Depois que o MVP estiver funcionando, começa a parte realmente interessante.

Mês 2 — Estabelecimentos

Criar:

POST /business/register
POST /business/login

Painel:

┌──────────────────────────────┐
│ Painel do estabelecimento    │
├──────────────────────────────┤
│ Visualizações       1.284    │
│ Cliques              347     │
│ Favoritos             82     │
│ Reservas               31    │
└──────────────────────────────┘

O comerciante poderá:

cadastrar estabelecimento;
alterar horário;
adicionar fotos;
criar promoção;
cadastrar evento;
criar disponibilidade;
acompanhar visualizações.
💰 Monetização

Aqui entram vários modelos.

1. Plano gratuito
Perfil básico
Informações
Fotos
Localização
2. Plano Premium

Exemplo:

R$ 49/mês

Com:

destaque;
promoções;
analytics;
mais fotos;
posição privilegiada em determinadas áreas.

O preço é uma hipótese inicial, não algo que você precisaria fixar agora.

3. Comissão por reserva

Imagine:

Cliente
   ↓
VemAí
   ↓
Restaurante
   ↓
Reserva

O estabelecimento poderia pagar uma comissão previamente acordada por uma reserva originada pela plataforma.

🟠 Mês 2 — Reservas

Criar:

tables
availability
reservations
reservation_items

Fluxo:

Cliente
   ↓
Restaurante
   ↓
Escolhe data
   ↓
Escolhe horário
   ↓
Número de pessoas
   ↓
Reserva

API:

GET  /restaurants/{id}/availability
POST /reservations
GET  /reservations/me
PATCH /reservations/{id}/cancel
🟠 Mês 3 — Marketplace

Agora entram:

🎟️ Eventos
Evento
Data
Horário
Local
Preço
Ingressos
Quantidade
🥾 Experiências

Exemplo:

Trilha guiada
Passeio de bicicleta
Tour gastronômico
Passeio de barco
Visita a atrativo
🏨 Hospedagem

Aqui você pode trabalhar com parceiros/afiliados de plataformas de hospedagem quando houver programas e condições aplicáveis.

Fluxo:

VemAí
   ↓
"Encontrar hospedagem"
   ↓
Parceiro
   ↓
Reserva
   ↓
Comissão
🔵 FASE 3 — O diferencial

Depois que houver dados suficientes, você pode construir algo muito mais interessante.

🤖 “Monte meu rolê”

O usuário escreve:

“Quero sair sábado com minha namorada, gastar no máximo R$300 e não quero algo muito cansativo.”

O sistema poderia montar:

🌅 15:00
Passeio

☕ 17:30
Café

🍽️ 20:00
Jantar

🎵 22:00
Música ao vivo

💰 Total estimado
R$ 270

Aí sim entra IA.

📍 Geolocalização

Adicionar:

latitude
longitude

E calcular:

distância do usuário

Exemplo:

Restaurantes até 5 km

ou:

Passeios a até 30 minutos.

☁️ Clima

Integração com API meteorológica.

A recomendação pode mudar:

☀️ Sol
🏞️ Cachoeira
🥾 Trilha
🚤 Passeio
🌧️ Chuva
🍽️ Restaurante
🎬 Cinema
☕ Café
🎭 Evento fechado

Isso deixa o “O que fazer hoje?” muito mais interessante.

📱 WhatsApp

Depois:

VemAí
   ↓
Reserva
   ↓
WhatsApp
   ↓
"Olá Lucas, sua reserva..."

Também poderia permitir que estabelecimentos recebam notificações.

💳 Pagamentos

Somente depois da validação do modelo.

Você poderia ter:

Cliente
   ↓
Pagamento
   ↓
VemAí
   ↓
Comissão
   ↓
Estabelecimento

Mas eu não colocaria isso no MVP.

Pagamento traz:

conciliação;
estorno;
webhook;
segurança;
fraude;
split;
regras fiscais;
suporte.

É uma complexidade desnecessária no começo.

📊 Arquitetura futura

Eu imaginaria algo assim:

                       ┌──────────────┐
                       │   FRONTEND   │
                       │   Next.js    │
                       └──────┬───────┘
                              │
                              ▼
                       ┌──────────────┐
                       │   FastAPI    │
                       │     API      │
                       └──────┬───────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
        ┌──────────┐    ┌───────────┐   ┌───────────┐
        │PostgreSQL│    │  Redis    │   │ Serviços  │
        └──────────┘    └───────────┘   │ externos  │
                                        └───────────┘
                                             │
                            ┌────────────────┼────────────┐
                            ▼                ▼            ▼
                         Clima           Mapas       Reservas

Mais tarde:

                  ┌──────────────┐
                  │ Recommendation│
                  │    Engine     │
                  └──────┬───────┘
                         │
                         ▼
                       IA
🗄️ Banco de dados futuro

Você poderia chegar aproximadamente a:

users
user_preferences

cities
regions
addresses

categories
places
restaurants
hotels
attractions
events
experiences

opening_hours
availability
tables

reservations
reservation_items

favorites
reviews

promotions
coupons

businesses
business_users

payments
commissions

affiliate_clicks
affiliate_conversions

notifications

Isso já vira um projeto de backend bastante completo para seu portfólio.

🎯 Roadmap resumido
ETAPA 1
────────────────────────────
FastAPI
PostgreSQL
Alembic
Auth
Places
Categories
Search
Filters
        ↓
ETAPA 2
────────────────────────────
"O que fazer hoje?"
Regras de recomendação
Geolocalização
Favoritos
        ↓
ETAPA 3
────────────────────────────
Frontend
Deploy
Testes
Docker
        ↓
ETAPA 4
────────────────────────────
Painel dos estabelecimentos
Eventos
Promoções
        ↓
ETAPA 5
────────────────────────────
Reservas
Disponibilidade
        ↓
ETAPA 6
────────────────────────────
Comissões
Afiliados
Pagamentos
        ↓
ETAPA 7
────────────────────────────
Clima
WhatsApp
Roteiros
IA
        ↓
ETAPA 8
────────────────────────────
Marketplace regional