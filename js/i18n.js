/* Translation dictionary. Keys are matched against [data-i18n] attributes.
   HTML-bearing strings are used with elements that carry [data-i18n-html]. */
const translations = {
  pt: {
    "nav.home": "Início",
    "nav.about": "Sobre",
    "nav.experience": "Experiência",
    "nav.portfolio": "Portfólio de Arte",
    "nav.talks": "Palestras",
    "nav.contact": "Contato",
    "nav.toggle": "Menu",

    "footer.rights": "© 2026 Angelo Pixel. Feito à mão com HTML, CSS e JS.",
    "footer.linkedin": "LinkedIn",
    "footer.github": "GitHub",
    "footer.email": "Email",

    /* ---------------- HOME ---------------- */
    "home.title": "Angelo Pixel — Product Manager & Artista Digital",
    "home.eyebrow": "Product Manager & Artista Digital",
    "home.hero.title": "Construo produtos que funcionam — e mundos que emocionam.",
    "home.hero.lede":
      "Duas décadas transformando ideias em produtos, plataformas e experiências. Da Amazon à Amazônia, de dashboards de receita a realidade aumentada premiada pela Mozilla.",
    "home.cta.experience": "Ver experiência como PM",
    "home.cta.portfolio": "Ver portfólio de arte",

    "home.stat1.num": "587%",
    "home.stat1.label": "aumento de receita gerado num sistema de taxas (AutoNation)",
    "home.stat2.num": "100+",
    "home.stat2.label": "palestras, oficinas e exposições em 5 países",
    "home.stat3.num": "2018",
    "home.stat3.label": "Prêmio Mozilla para o Jandig, plataforma de RA open-source",
    "home.stat4.num": "2024",
    "home.stat4.label": "representou o Brasil na ONU (OSPOs for Good)",

    "home.intro.title": "Duas trilhas, uma mesma curiosidade",
    "home.intro.html":
      "Sou <strong>Angelo Pixel</strong> — no currículo, Senior Product Manager; nos palcos e exposições, fundador do <strong>Jandig</strong> e do <strong>memeLab</strong>. As duas coisas vêm do mesmo lugar: uma curiosidade antiga por pegar uma ideia e transformá-la em algo que as pessoas possam tocar, usar ou sentir.",

    "home.teaser.experience.title": "Experiência como Product Manager",
    "home.teaser.experience.body":
      "Amazon, AutoNation, Stefanini IHMI e InfoAmazonia — produtos que evoluíram de protótipo a impacto de milhões.",
    "home.teaser.portfolio.title": "Portfólio de Arte & Inovação Aberta",
    "home.teaser.portfolio.body":
      "Jandig e Rede InfoAmazonia, nascidos no memeLab — quase vinte anos criando tecnologia aberta fora do expediente.",
    "home.teaser.about.title": "Sobre mim",
    "home.teaser.about.body":
      "Da infância mexendo em um Atari até ser convidado pela ONU — a história por trás dos dois lados.",
    "home.teaser.contact.title": "Contato",
    "home.teaser.contact.body":
      "Vamos conversar sobre produto, arte, ou as duas coisas ao mesmo tempo.",
    "home.teaser.arrow": "→",

    /* ---------------- ABOUT ---------------- */
    "about.title": "Sobre — Angelo Pixel",
    "about.eyebrow": "Sobre mim",
    "about.hero.title":
      "Criei produtos premiados alternando entre estratégia de negócio e trabalho mão na massa.",
    "about.p1":
      "Quando criança, abri o cartucho de um Atari e, com a ajuda de alguns fios, tentei ligá-lo direto na tomada. O cartucho quebrou e a energia da casa caiu. É minha primeira lembrança de fracasso — muitas outras vieram depois. Elas guiam meus sucessos.",
    "about.p2":
      "Carrego essa curiosidade e essa ousadia para a vida. Foi o que me permitiu criar o <a href=\"https://jandig.app/\" target=\"_blank\" rel=\"noopener\">Jandig</a>, a única plataforma de realidade aumentada open-source voltada ao usuário final (premiada pela Mozilla depois de um pitch que fiz em Londres). Foi também o que me levou a criar a Rede InfoAmazonia, o primeiro hardware IoT open-source para monitoramento de água em tempo real (financiado por um prêmio do Google), que inspirou um grupo na China a criar sua própria versão — e me levou até lá.",
    "about.p3":
      "Além de criar produtos novos, também geri produtos já existentes. O que mais me orgulha é a InfoAmazonia. Quando entrei, os jornalistas atualizavam as notícias usando Git! Desenhei um novo sistema para o portal e tripliquei a média mensal de pageviews em 2013 — um número que se manteve estável até hoje. Também criei um produto a partir do sistema por trás do portal (o Jeo) e coordenei sua implementação em organizações da África, Ásia, América do Norte e América do Sul.",
    "about.p4":
      "Duas décadas gerenciando projetos me trouxeram aprendizados valiosos. Com a cabeça sempre borbulhando de ideias, priorização é meu mantra. Perdi a conta de quantos protótipos já criei — faço isso por prazer, e não me apego a ideias que não se provam úteis. Trabalhando com comunidades de desenvolvedores, aprendi que a melhor forma de gerenciar é entender as motivações das pessoas (e incentivá-las), e que a melhor forma de liderar é pelo exemplo.",

    "about.skills.title": "Como aprendi minhas habilidades",
    "about.skills.ideation.title": "Ideação",
    "about.skills.ideation.body":
      "Como artista, meu foco é criar uma sensação em um contexto específico — mas existem inúmeras formas de fazer isso. Aprendi técnicas de ideação para viabilizar a criação de obras interativas digitais: prototipagem, Análise dos Cinco Porquês, storyboarding, Crazy 8s.",
    "about.skills.prioritization.title": "Priorização",
    "about.skills.prioritization.body":
      "Isso remonta há mais de uma década, quando eu liderava uma pequena equipe de pessoas muito criativas. Todo mundo tinha muitas ideias, e precisávamos decidir juntos o que construir com recursos limitados. Uma ferramenta que gosto de usar é a matriz Valor vs. Esforço — simples de entender e que força a pensar nas variáveis mais importantes: resultado e recursos.",
    "about.skills.communication.title": "Comunicação",
    "about.skills.communication.body":
      "Adoro ensinar (somando todas as palestras e oficinas que já dei, o número passa de 100), e ensinar exige empatia com a audiência: um contexto com prazo apertado, sem poder assumir que as pessoas já sabem algo. Aplico o mesmo método quando preciso me comunicar com qualquer pessoa.",
    "about.skills.stakeholder.title": "Gestão de stakeholders",
    "about.skills.stakeholder.body":
      "Trabalhei num projeto do governo brasileiro com mais de 10 financiadores, alguns dos quais eram parceiros no dia a dia. Ao mesmo tempo, como Coordenador de Tecnologia, precisei sincronizar o trabalho da minha equipe com o de outras — para potencializar os resultados.",
    "about.skills.leadership.title": "Liderança",
    "about.skills.leadership.body":
      "Meu trabalho como gestor de comunidade em projetos open-source se baseia em \"vender\" ideias para que as pessoas invistam seu tempo nelas — de graça. Para isso, é preciso compartilhar uma visão do que se quer construir e liderar as pessoas na construção dela.",

    "about.curiosities.title": "Curiosidades",
    "about.curiosities.1": "Em 2018 passei um mês viajando ao redor do mundo — deixando adesivos do Jandig por onde passei.",
    "about.curiosities.2": "Tenho gêmeos de 16 anos.",
    "about.curiosities.3": "Países onde fiquei um mês ou mais: Índia, Espanha, Holanda, Reino Unido, EUA e Brasil (claro!).",
    "about.curiosities.4": "Nunca me canso de viajar para a Amazônia brasileira.",
    "about.curiosities.5": "Já fiz uma road trip de Los Angeles a San Francisco.",
    "about.curiosities.6": "Já viajei direto do verão da Amazônia brasileira para o inverno de Nova York.",
    "about.curiosities.7": "Um grande amigo me ensinou a mergulhar com cilindro — e mal posso esperar para fazer de novo!",
    "about.curiosities.8": "Já apresentei trabalhos (palestras, oficinas etc.) em 4 continentes — e como não há consumidores na Antártida, só faltam África e Oceania.",

    "about.tools.title": "Ferramentas, linguagens e metodologias",
    "about.tools.languages.title": "Linguagens em que já escrevi algumas linhas",
    "about.tools.languages.body": "Python, JavaScript, C++, SQL, Java, Shell, PHP, CSS, HTML.",
    "about.tools.tools.title": "Ferramentas que já usei",
    "about.tools.tools.body":
      "Notion, Miro, Figma, HotJar, Mailchimp, Slack, Jira, Trello, Google Analytics, MySQL, Google Workspace, Basecamp, WordPress, GitHub, Toggl, Todoist, TileMill, Arduino.",
    "about.tools.methods.title": "Metodologias",
    "about.tools.methods.body": "Scrum, Kanban, Lean Inception, Product Discovery, Design Sprint.",

    /* ---------------- EXPERIENCE ---------------- */
    "experience.title": "Experiência — Angelo Pixel",
    "experience.eyebrow": "Experiência",
    "experience.hero.title": "Uma trajetória em duas trilhas paralelas.",
    "experience.hero.lede":
      "Cargos em produto, lado a lado com um laboratório de arte e código aberto que nunca parou — desde 2009. Os pontos roxos são cargos formais; os pontos rosa são o memeLab rodando em paralelo.",

    "experience.job1.period": "10/2023 — 02/2025",
    "experience.job1.role": "Senior Product Manager",
    "experience.job1.org": "Software Mind / AutoNation",
    "experience.job1.body":
      "AutoNation é a maior rede de concessionárias automotivas dos EUA. Aumentei taxas de diferentes tipos em até 587%, evoluindo o sistema de cobrança de regras fixas no código para um dashboard totalmente gerenciável — do orçamento à fatura. Levei a Partner API do Mobile Service do zero ao primeiro cliente.",

    "experience.job2.period": "01/2022 — 01/2023",
    "experience.job2.role": "Technical Product Manager II",
    "experience.job2.org": "Amazon",
    "experience.job2.body":
      "Liderei o Spider, um produto de API que aumentou a lucratividade anual da Amazon Brasil em USD 11 milhões. Criei a visão e o plano de três anos, evoluindo o Spider de protótipo a produto, e aumentei seu impacto em 4,5 vezes em um ano. Encabecei o Innovation Pipeline, iniciativa de crowdsourcing e validação de novas ideias de produto.",

    "experience.job3.period": "10/2020 — 12/2021",
    "experience.job3.role": "Product Manager",
    "experience.job3.org": "Stefanini IHMI",
    "experience.job3.body":
      "Liderei a descoberta do Watchtower, produto de IA para manutenção industrial, à frente de um time diverso de cinco pessoas. Economizei recursos da empresa ao aconselhar a diretoria a descontinuar o produto por razões técnicas e comerciais. Eliminei um atraso de dois meses em uma semana ao assumir a gestão de desenvolvimento de outro produto.",

    "experience.job4.period": "03/2013 — 12/2016",
    "experience.job4.role": "Head of Product and Technology",
    "experience.job4.org": "InfoAmazonia",
    "experience.job4.body":
      "Mudei a estratégia de negócio e montei um time enxuto e produtivo, implementando práticas ágeis que aumentaram a receita em 80% em um ano. Lancei cinco produtos e liderei dois já existentes, alcançando até 400% de aumento de pageviews em um ano. Concebi e liderei a Rede InfoAmazonia, plataforma IoT premiada pelo Google Impact Challenge Brasil 2014.",

    "experience.job5.period": "01/2009 — presente",
    "experience.job5.role": "Fundador",
    "experience.job5.org": "memeLab (em paralelo às demais experiências)",
    "experience.job5.body":
      "Laboratório de realidade estendida (XR) open-source. Projeto pessoal desenvolvido fora do expediente — meu laboratório de inovação para experimentar novas tecnologias e retribuir à comunidade open-source. Criei e liderei o desenvolvimento de mais de 10 produtos em MR (Meta Quest), desktop e mobile, e já geri mais de 50 projetos na Europa, América do Norte e América do Sul.",

    "experience.recognition.title": "Reconhecimentos",
    "experience.rec1.year": "2024",
    "experience.rec1.body": "Convidado pela ONU para representar o Brasil no OSPOs for Good Symposium.",
    "experience.rec2.year": "2021",
    "experience.rec2.body": "Bolsa de estudos em AI Product Management, entre os 10% melhores alunos.",
    "experience.rec3.year": "2018",
    "experience.rec3.body": "Prêmio Mozilla Open Source Support para o Jandig.",
    "experience.rec4.year": "2018",
    "experience.rec4.body": "Prêmio Softwares Livres Culturais, do Ministério da Cultura, para o Jandig.",
    "experience.rec5.year": "2014",
    "experience.rec5.body": "Prêmio Google Impact Challenge para a Rede InfoAmazonia.",
    "experience.rec6.year": "TEDx",
    "experience.rec6.body": "Palestrante TEDx sobre tecnologia, arte e código aberto.",

    "experience.skills.title": "Skills",
    "experience.cta": "Currículo completo no LinkedIn",

    /* ---------------- PORTFOLIO ---------------- */
    "portfolio.title": "Portfólio de Arte — Angelo Pixel",
    "portfolio.eyebrow": "Portfólio de Arte & Inovação Aberta",
    "portfolio.hero.title": "Os projetos que fiz por paixão — e que me ensinaram a maior parte do que sei sobre produto.",
    "portfolio.hero.lede":
      "Quase vinte anos criando plataformas, hardware e experiências abertas fora do expediente. Nenhum cliente pedindo prazo — só curiosidade, comunidade, e a vontade de ver a ideia funcionar.",

    "portfolio.case1.tag": "Realidade Aumentada / Open Source",
    "portfolio.case1.title": "Jandig",
    "portfolio.case1.role.title": "Meu papel",
    "portfolio.case1.role.body":
      "Idealizei, prototipei e apresentei o Jandig no MozFest, em Londres, conquistando um Mozilla Seed Award. Desde então lidero seu desenvolvimento e sua presença em festivais e exposições.",
    "portfolio.case1.product.title": "Produto",
    "portfolio.case1.product.body":
      "A única plataforma de realidade aumentada open-source pensada para o usuário final, permitindo criar e publicar obras de RA sem escrever código — usada para contar mitologia brasileira em experiências imersivas.",
    "portfolio.case1.evolution.title": "Evolução",
    "portfolio.case1.evolution.body":
      "Do pitch em Londres a apresentações recorrentes no X-Reality USP (desde 2019, em parceria com o Raindance Film Festival), no Festival MARTE (Minas Gerais) e, mais recentemente, no Mozilla Festival 2025 em Barcelona e no painel \"XR Futures\" do São Paulo Innovation Week em abril de 2026.",
    "portfolio.case1.outcomes.title": "Resultados",
    "portfolio.case1.outcomes.body":
      "Prêmio Mozilla Open Source Support (2018); Prêmio Softwares Livres Culturais do Ministério da Cultura (2018); apoio de viagem da Mozilla Foundation (EUR 1.910) para o MozFest 2025.",

    "portfolio.other.title": "Outras experimentações",
    "portfolio.other.lede":
      "Fora do Jandig, o memeLab — o laboratório de realidade estendida que fundei em 2009 — já produziu mais de 10 experimentos em RA, RV e RM. Alguns registros:",
    "portfolio.other.1": "Narrative Navigation — app de navegação urbana em realidade aumentada",
    "portfolio.other.2": "Nowhere and Everywhere at the Same Time — instalação de dança com William Forsythe, filmada em 360°",
    "portfolio.other.3": "New/Old Games — Pac-Man gigante projetado e controlado pelo corpo",
    "portfolio.other.4": "Good Night, Sleep Tight — performance em realidade virtual",
    "portfolio.other.5": "Headset de VR testado no Festival X-Reality",
    "portfolio.other.6": "Mostra de Clipes 360° no Festival MARTE",
    "portfolio.other.cta": "Ver todas as palestras, prêmios e residências",

    "portfolio.case3.tag": "Hardware Aberto / IoT",
    "portfolio.case3.title": "Rede InfoAmazonia",
    "portfolio.case3.role.title": "Meu papel",
    "portfolio.case3.role.body":
      "Concebi e liderei o projeto dentro da InfoAmazonia, coordenando o desenvolvimento do hardware e a estratégia de financiamento.",
    "portfolio.case3.product.title": "Produto",
    "portfolio.case3.product.body":
      "O primeiro hardware IoT open-source para monitoramento de água em tempo real na Amazônia — sensores de baixo custo publicando dados abertos sobre rios da região.",
    "portfolio.case3.evolution.title": "Evolução",
    "portfolio.case3.evolution.body":
      "Um dos 10 projetos selecionados entre mais de 800 inscritos no Google Impact Challenge Brasil 2014. A abordagem aberta inspirou um grupo na China a desenvolver sua própria versão do sistema, o que me levou a apresentar o projeto por lá.",
    "portfolio.case3.outcomes.title": "Resultados",
    "portfolio.case3.outcomes.body":
      "Prêmio Google Impact Challenge Brasil (2014); dados usados por jornalistas e pesquisadores para reportagens sobre a Amazônia.",

    "portfolio.case4.tag": "Mídia / Plataforma Open Source",
    "portfolio.case4.title": "InfoAmazonia & Jeo",
    "portfolio.case4.role.title": "Meu papel",
    "portfolio.case4.role.body":
      "Fui contratado como consultor para diagnosticar a plataforma e propor melhorias. Depois de aprovado pela direção executiva, assumi a gestão do desenvolvimento e, em seguida, a gestão de produto — contratando e liderando um time de design, engenharia e dados.",
    "portfolio.case4.product.title": "Produto",
    "portfolio.case4.product.body":
      "Uma plataforma que agrega notícias (em português, espanhol e inglês) de parceiros e do público, georreferenciadas em mapas feitos com a ferramenta TileMill.",
    "portfolio.case4.evolution.title": "Evolução",
    "portfolio.case4.evolution.body":
      "Antes, um sistema manual baseado em Jekyll gerava conteúdo estático publicado direto num repositório Git — sem sequer um buscador. Sem orçamento para manter uma plataforma proprietária no longo prazo, propus criar um tema WordPress open-source e uma comunidade em torno dele. Esse foi o primeiro passo para o Jeo.",
    "portfolio.case4.outcomes.title": "Resultados",
    "portfolio.case4.outcomes.body":
      "As pageviews do site aumentaram 400% em um ano. Mais de sete anos depois do lançamento, o código continua mantido por outra organização, a Earth Journalism Network.",

    /* ---------------- TALKS ---------------- */
    "talks.title": "Palestras — Angelo Pixel",
    "talks.eyebrow": "Palestras & Reconhecimento",
    "talks.hero.title": "Vinte e quatro anos de palco, VJ booth e sala de aula.",
    "talks.hero.lede":
      "Mais de 100 palestras, debates, oficinas e exposições em 5 países e 14 estados brasileiros — do software livre e VJing à realidade aumentada premiada internacionalmente.",

    "talks.stat.talks.num": "100+",
    "talks.stat.talks.label": "palestras, oficinas e exposições desde 2002",
    "talks.stat.continents.num": "4",
    "talks.stat.continents.label": "continentes onde já apresentei trabalhos",
    "talks.stat.residencies.num": "4",
    "talks.stat.residencies.label": "residências artísticas (Holanda, Espanha, Reino Unido, Colômbia)",
    "talks.stat.awards.num": "5",
    "talks.stat.awards.label": "prêmios internacionais e nacionais recebidos",

    "talks.recent.title": "Destaques recentes",
    "talks.recent1.period": "Nov 2025",
    "talks.recent1.title": "Mozilla Festival — Barcelona",
    "talks.recent1.body":
      "Sessão \"Jandig - Brazilian Myths in Mixed Reality\", aceita pelo comitê do festival, com apoio de viagem da Mozilla Foundation (EUR 1.910).",
    "talks.recent2.period": "Abr 2026",
    "talks.recent2.title": "São Paulo Innovation Week",
    "talks.recent2.body":
      "Painel \"XR Futures: Games, Art, and the Expansion of Immersive Worlds\", com Almir Almas (USP) e Ana Arruda (curadora de RX), moderado por Daniel Lima.",
    "talks.recent3.period": "Desde 2019",
    "talks.recent3.title": "X-Reality USP",
    "talks.recent3.body":
      "Palestrante, idealizador e curador do festival, em parceria com o Raindance Film Festival — edição anual, sempre em novembro.",
    "talks.recent4.period": "2019",
    "talks.recent4.title": "Festival MARTE",
    "talks.recent4.body":
      "Projeto transmídia com realidade aumentada e mitologia estendida em Ouro Preto e Cataguases (Minas Gerais), em colaboração com a UEMG.",

    "talks.eras.title": "Duas décadas de palco",
    "talks.era1.period": "2012",
    "talks.era1.title": "O auge do Jandig",
    "talks.era1.body":
      "Ano de maior densidade de agenda: palestra \"Jandig – arte em realidade aumentada\" e debate \"Cidades Copyleft\" no FISL 12 (Porto Alegre); inauguração do SESC Sorocaba como artista expositor (\"VideoPong\", \"Experimentações Eletro-Orgânicas\"); Campus Party; Circuito Vivo Arte.mov.",
    "talks.era2.period": "2009 – 2011",
    "talks.era2.title": "Info-ativismo e VJing",
    "talks.era2.body":
      "Oficina no Info-Activism Camp em Bangalore, Índia; debate no Open Video Conference em Nova York; FISL 11 e Campus Party em Porto Alegre e São Paulo.",
    "talks.era3.period": "2002 – 2008",
    "talks.era3.title": "Primórdios do software livre",
    "talks.era3.body":
      "Carreira de VJ profissional (2002–2018, \"aposentada\" após uma apresentação na China); palestras e oficinas no FISL, Latinoware, Fórum Social Mundial e Fórum da Cultura Digital Brasileira.",

    "talks.awards.title": "Prêmios e bolsas",
    "talks.award1.year": "2018",
    "talks.award1.body": "Mozilla Open Source Support Award, para o Jandig.",
    "talks.award2.year": "2018",
    "talks.award2.body": "Prêmio Softwares Livres Culturais, do Ministério da Cultura, para o Jandig.",
    "talks.award3.year": "2014",
    "talks.award3.body": "Google Impact Challenge Brasil, para a Rede InfoAmazonia.",
    "talks.award4.year": "2012",
    "talks.award4.body": "Prêmio SESC Sorocaba, por \"Experimentações Eletro-Orgânicas\".",
    "talks.award5.year": "2012",
    "talks.award5.body": "Residência artística Nimk/Vivo Arte.mov (Brasil/Holanda).",
    "talks.award6.year": "2011",
    "talks.award6.body": "Prêmio CEMEC de Empreendedores Criativos.",
    "talks.award7.year": "2006",
    "talks.award7.body": "Premiação para Colaborações, do Estúdio Livre.",

    "talks.residencies.title": "Residências artísticas",
    "talks.residencies.body":
      "Holanda (Nimk/Vivo, 2012), Espanha, Reino Unido e Colômbia — além de múltiplas residências no Brasil.",

    "talks.mosaic.title": "Registros de campo",
    "talks.mosaic.1": "Instalação circular de 360° coberta por marcadores de RA",
    "talks.mosaic.2": "Carnaval: intervenção de RA no desfile da Rosas de Ouro",
    "talks.mosaic.3": "Intervenção urbana em Ouro Preto (Narrativas Territoriais)",
    "talks.mosaic.4": "Exposição itinerante do Jandig num SESC",
    "talks.mosaic.5": "Crianças brincando com cubos de RA numa oficina itinerante",
    "talks.mosaic.6": "Coleção Remexe: roupas upcycled com etiquetas de RA",
    "talks.mosaic.7": "Palestra no palco da Campus Party",
    "talks.mosaic.8": "Oficina de silkscreen com a identidade visual do Jandig",

    /* ---------------- CONTACT ---------------- */
    "contact.title": "Contato — Angelo Pixel",
    "contact.eyebrow": "Contato",
    "contact.hero.title": "Vamos conversar.",
    "contact.hero.lede":
      "Sobre produto, sobre arte, ou sobre como as duas coisas se cruzam — respondo email, mensagem no LinkedIn ou um bom papo cara a cara.",
    "contact.email.label": "Email",
    "contact.linkedin.label": "LinkedIn",
    "contact.github.label": "GitHub",
    "contact.jandig.label": "Jandig",
    "contact.email.channel": "Resposta em até 2 dias úteis",
    "contact.linkedin.channel": "Trajetória completa e recomendações",
    "contact.github.channel": "Código aberto e experimentos",
    "contact.jandig.channel": "A plataforma de RA que fundei",
  },

  en: {
    "nav.home": "Home",
    "nav.about": "About",
    "nav.experience": "Experience",
    "nav.portfolio": "Art Portfolio",
    "nav.talks": "Talks",
    "nav.contact": "Contact",
    "nav.toggle": "Menu",

    "footer.rights": "© 2026 Angelo Pixel. Handbuilt with HTML, CSS and JS.",
    "footer.linkedin": "LinkedIn",
    "footer.github": "GitHub",
    "footer.email": "Email",

    /* ---------------- HOME ---------------- */
    "home.title": "Angelo Pixel — Product Manager & Digital Artist",
    "home.eyebrow": "Product Manager & Digital Artist",
    "home.hero.title": "I build products that work — and worlds that move people.",
    "home.hero.lede":
      "Two decades turning ideas into products, platforms, and experiences — from Amazon to the Amazon rainforest, from revenue dashboards to Mozilla-awarded augmented reality.",
    "home.cta.experience": "See PM experience",
    "home.cta.portfolio": "See art portfolio",

    "home.stat1.num": "587%",
    "home.stat1.label": "revenue increase driven on a fee system (AutoNation)",
    "home.stat2.num": "100+",
    "home.stat2.label": "talks, workshops and exhibitions across 5 countries",
    "home.stat3.num": "2018",
    "home.stat3.label": "Mozilla Award for Jandig, an open-source AR platform",
    "home.stat4.num": "2024",
    "home.stat4.label": "represented Brazil at the UN (OSPOs for Good)",

    "home.intro.title": "Two tracks, one curiosity",
    "home.intro.html":
      "I'm <strong>Angelo Pixel</strong> — on paper, a Senior Product Manager; on stages and in exhibitions, the founder of <strong>Jandig</strong> and <strong>memeLab</strong>. Both come from the same place: a long-running curiosity about taking an idea and turning it into something people can touch, use, or feel.",

    "home.teaser.experience.title": "Experience as a Product Manager",
    "home.teaser.experience.body":
      "Amazon, AutoNation, Stefanini IHMI and InfoAmazonia — products that evolved from prototype to multi-million-dollar impact.",
    "home.teaser.portfolio.title": "Art & Open Innovation Portfolio",
    "home.teaser.portfolio.body":
      "Jandig and Rede InfoAmazonia, born inside memeLab — nearly twenty years building open technology outside business hours.",
    "home.teaser.about.title": "About me",
    "home.teaser.about.body":
      "From tinkering with an Atari as a kid to being invited by the UN — the story behind both sides.",
    "home.teaser.contact.title": "Contact",
    "home.teaser.contact.body":
      "Let's talk about product, art, or both at once.",
    "home.teaser.arrow": "→",

    /* ---------------- ABOUT ---------------- */
    "about.title": "About — Angelo Pixel",
    "about.eyebrow": "About me",
    "about.hero.title":
      "I created award-winning products by alternating between business strategy and hands-on work.",
    "about.p1":
      "As a child, I opened an Atari cartridge and, with the help of some cables, plugged it straight into the power socket. The cartridge broke and my home's power went out. It's my first memory of failure — many more came later. They guide my successes.",
    "about.p2":
      "I carry this curiosity and daring for life. It's what allowed me to create <a href=\"https://jandig.app/\" target=\"_blank\" rel=\"noopener\">Jandig</a>, the only open-source augmented reality platform aimed at the end user (awarded by Mozilla after a pitch I gave in London). It also led me to create Rede InfoAmazonia, the first open-source IoT hardware for real-time water monitoring (sponsored by a Google award), which inspired a group in China to build their own version — and took me there.",
    "about.p3":
      "In addition to creating new products, I also managed existing ones. The one I'm most proud of is InfoAmazonia. When I joined, journalists were updating the news using Git! I designed a new system for the portal and tripled its monthly average pageviews in 2013 — a number that has stayed stable ever since. I also built a product out of the system behind the portal (Jeo) and coordinated its rollout in organizations across Africa, Asia, North and South America.",
    "about.p4":
      "Two decades managing projects taught me some valuable lessons. With my mind constantly bubbling with ideas, prioritization is my mantra. I've lost count of how many prototypes I've built — I do it for pleasure, and I'm not attached to ideas that don't prove useful. Working with developer communities, I learned that the best way to manage is by understanding people's motivations (and encouraging them), and that the best way to lead is by example.",

    "about.skills.title": "How I learned my skills",
    "about.skills.ideation.title": "Ideation",
    "about.skills.ideation.body":
      "As an artist, my focus is to create a feeling in a specific context — but there are countless ways to do that. I've learned ideation techniques to enable the creation of interactive digital artworks: prototyping, Five Whys analysis, storyboarding, Crazy 8s.",
    "about.skills.prioritization.title": "Prioritization",
    "about.skills.prioritization.body":
      "This goes back more than a decade, when I was leading a small team of very creative people. Everyone had lots of ideas, and we needed to decide together what to build with limited resources. A tool I like to use is the Value vs. Effort matrix — simple to understand, and it forces you to think about the most important variables: outcomes and resources.",
    "about.skills.communication.title": "Communication",
    "about.skills.communication.body":
      "I love to teach (adding up all the talks and workshops I've given, the number goes well past 100), and teaching requires empathizing with the audience — a time-constrained context where you can't assume people already know something. I apply the same method whenever I need to communicate with anyone.",
    "about.skills.stakeholder.title": "Stakeholder management",
    "about.skills.stakeholder.body":
      "I worked on a Brazilian government project with more than 10 funders, some of whom we partnered with daily. At the same time, as Technology Coordinator, I needed to synchronize my team's work with others' — to maximize outcomes.",
    "about.skills.leadership.title": "Leadership",
    "about.skills.leadership.body":
      "My work as a community manager in open-source projects is based on \"selling\" ideas so people invest their time in them — for free. To make that happen, you need to share a vision of what you want to build and lead people in building it.",

    "about.curiosities.title": "Curiosities",
    "about.curiosities.1": "In 2018 I spent a month traveling around the world — leaving Jandig stickers wherever I went.",
    "about.curiosities.2": "I have 16-year-old twins.",
    "about.curiosities.3": "Countries I spent a month or more in: India, Spain, the Netherlands, the UK, the US, and Brazil (of course!).",
    "about.curiosities.4": "I'm never tired of traveling to the Brazilian Amazon.",
    "about.curiosities.5": "I once did a road trip from Los Angeles to San Francisco.",
    "about.curiosities.6": "I once traveled straight from the summer of the Brazilian Amazon to the winter of New York.",
    "about.curiosities.7": "A good friend taught me how to scuba dive — and I can't wait to do it again!",
    "about.curiosities.8": "I've presented work (talks, workshops, etc.) on 4 continents — and since there are no consumers in Antarctica, only Africa and Oceania are left.",

    "about.tools.title": "Tools, languages and methodologies",
    "about.tools.languages.title": "Languages I've written some lines in",
    "about.tools.languages.body": "Python, JavaScript, C++, SQL, Java, Shell, PHP, CSS, HTML.",
    "about.tools.tools.title": "Tools I've used",
    "about.tools.tools.body":
      "Notion, Miro, Figma, HotJar, Mailchimp, Slack, Jira, Trello, Google Analytics, MySQL, Google Workspace, Basecamp, WordPress, GitHub, Toggl, Todoist, TileMill, Arduino.",
    "about.tools.methods.title": "Methodologies",
    "about.tools.methods.body": "Scrum, Kanban, Lean Inception, Product Discovery, Design Sprint.",

    /* ---------------- EXPERIENCE ---------------- */
    "experience.title": "Experience — Angelo Pixel",
    "experience.eyebrow": "Experience",
    "experience.hero.title": "A career on two parallel tracks.",
    "experience.hero.lede":
      "Formal product roles, side by side with an art-and-open-source lab that never stopped — since 2009. Purple dots are formal roles; pink dots are memeLab running in parallel.",

    "experience.job1.period": "10/2023 — 02/2025",
    "experience.job1.role": "Senior Product Manager",
    "experience.job1.org": "Software Mind / AutoNation",
    "experience.job1.body":
      "AutoNation is the largest and most recognized automotive retailer in the USA. I increased fees of different types by up to 587% by evolving the fee system from hardcoded rules to a fully manageable dashboard — from quote to invoice. I led the Mobile Service's Partner API from zero to its first customer.",

    "experience.job2.period": "01/2022 — 01/2023",
    "experience.job2.role": "Technical Product Manager II",
    "experience.job2.org": "Amazon",
    "experience.job2.body":
      "I led Spider, an API product that increased Amazon Brazil's yearly profitability by USD 11MM. I created a vision and three-year plan, evolving Spider from prototype to product, and increased its impact 4.5x in one year. I spearheaded the Innovation Pipeline, an initiative focused on crowdsourcing and validating new product ideas.",

    "experience.job3.period": "10/2020 — 12/2021",
    "experience.job3.role": "Product Manager",
    "experience.job3.org": "Stefanini IHMI",
    "experience.job3.body":
      "I led the discovery of Watchtower, an AI product for industrial maintenance, leading a diverse team of five. I saved company resources by advising the C-level to discontinue the product for technical and commercial reasons. I eliminated a two-month delivery delay within one week of taking over another product's development management.",

    "experience.job4.period": "03/2013 — 12/2016",
    "experience.job4.role": "Head of Product and Technology",
    "experience.job4.org": "InfoAmazonia",
    "experience.job4.body":
      "I changed the business strategy and built a lean, highly productive team, implementing agile practices that increased revenue by 80% within a year. I launched five products and led two existing ones, achieving up to a 400% pageview increase in one year. I conceived and led Rede InfoAmazonia, an IoT platform awarded by Google Impact Challenge Brazil 2014.",

    "experience.job5.period": "01/2009 — present",
    "experience.job5.role": "Founder",
    "experience.job5.org": "memeLab (running in parallel to the roles above)",
    "experience.job5.body":
      "An open-source extended reality (XR) laboratory. A personal passion project developed outside regular business hours — my hands-on innovation lab to experiment with new technologies and give back to the open-source community. I created and led the development of 10+ products across MR (Meta Quest), desktop and mobile, and have managed 50+ projects across Europe, North and South America.",

    "experience.recognition.title": "Recognitions",
    "experience.rec1.year": "2024",
    "experience.rec1.body": "Invited by the United Nations to represent Brazil at the OSPOs for Good Symposium.",
    "experience.rec2.year": "2021",
    "experience.rec2.body": "Awarded a scholarship to study AI Product Management as a top 10% performing student.",
    "experience.rec3.year": "2018",
    "experience.rec3.body": "Won a Mozilla Open Source Support Award for Jandig.",
    "experience.rec4.year": "2018",
    "experience.rec4.body": "Won a Software Livres Culturais award from the Brazilian Ministry of Culture for Jandig.",
    "experience.rec5.year": "2014",
    "experience.rec5.body": "Won a Google Impact Challenge award for Rede InfoAmazonia.",
    "experience.rec6.year": "TEDx",
    "experience.rec6.body": "TEDx speaker on technology, art and open source.",

    "experience.skills.title": "Skills",
    "experience.cta": "Full résumé on LinkedIn",

    /* ---------------- PORTFOLIO ---------------- */
    "portfolio.title": "Art Portfolio — Angelo Pixel",
    "portfolio.eyebrow": "Art & Open Innovation Portfolio",
    "portfolio.hero.title": "The projects I built out of passion — and that taught me most of what I know about product.",
    "portfolio.hero.lede":
      "Nearly twenty years building open platforms, hardware and experiences outside business hours. No client deadlines — just curiosity, community, and the drive to see an idea actually work.",

    "portfolio.case1.tag": "Augmented Reality / Open Source",
    "portfolio.case1.title": "Jandig",
    "portfolio.case1.role.title": "My role",
    "portfolio.case1.role.body":
      "I conceived, prototyped and pitched Jandig at MozFest in London, winning a Mozilla Seed Award. I've led its development and its presence at festivals and exhibitions ever since.",
    "portfolio.case1.product.title": "Product",
    "portfolio.case1.product.body":
      "The only open-source augmented reality platform built for the end user, letting anyone create and publish AR artworks without writing code — used to tell Brazilian mythology through immersive experiences.",
    "portfolio.case1.evolution.title": "Evolution",
    "portfolio.case1.evolution.body":
      "From the London pitch to recurring presentations at X-Reality USP (since 2019, in partnership with the Raindance Film Festival), at Festival MARTE (Minas Gerais), and, most recently, at Mozilla Festival 2025 in Barcelona and the \"XR Futures\" panel at São Paulo Innovation Week in April 2026.",
    "portfolio.case1.outcomes.title": "Outcomes",
    "portfolio.case1.outcomes.body":
      "Mozilla Open Source Support Award (2018); Software Livres Culturais award from the Brazilian Ministry of Culture (2018); Mozilla Foundation travel support funding (EUR 1,910) for MozFest 2025.",

    "portfolio.other.title": "Other experiments",
    "portfolio.other.lede":
      "Beyond Jandig, memeLab — the extended-reality lab I founded in 2009 — has produced 10+ experiments across AR, VR and MR. A few records:",
    "portfolio.other.1": "Narrative Navigation — an augmented-reality app for urban wayfinding",
    "portfolio.other.2": "Nowhere and Everywhere at the Same Time — a dance installation with William Forsythe, shot in 360°",
    "portfolio.other.3": "New/Old Games — a giant Pac-Man projected and body-controlled",
    "portfolio.other.4": "Good Night, Sleep Tight — a virtual-reality performance",
    "portfolio.other.5": "VR headset demoed at the X-Reality Festival",
    "portfolio.other.6": "360° Video Showcase at Festival MARTE",
    "portfolio.other.cta": "See all talks, awards and residencies",

    "portfolio.case3.tag": "Open Hardware / IoT",
    "portfolio.case3.title": "Rede InfoAmazonia",
    "portfolio.case3.role.title": "My role",
    "portfolio.case3.role.body":
      "I conceived and led the project inside InfoAmazonia, coordinating hardware development and the funding strategy.",
    "portfolio.case3.product.title": "Product",
    "portfolio.case3.product.body":
      "The first open-source IoT hardware for real-time water monitoring in the Amazon — low-cost sensors publishing open data about the region's rivers.",
    "portfolio.case3.evolution.title": "Evolution",
    "portfolio.case3.evolution.body":
      "One of 10 projects selected out of 800+ applicants for Google Impact Challenge Brazil 2014. The open approach inspired a group in China to build their own version of the system, which took me there to present the project.",
    "portfolio.case3.outcomes.title": "Outcomes",
    "portfolio.case3.outcomes.body":
      "Google Impact Challenge Brazil award (2014); data used by journalists and researchers reporting on the Amazon.",

    "portfolio.case4.tag": "Media / Open-Source Platform",
    "portfolio.case4.title": "InfoAmazonia & Jeo",
    "portfolio.case4.role.title": "My role",
    "portfolio.case4.role.body":
      "I was hired as a consultant to diagnose the platform and propose improvements. After the Executive Director approved my research, I took over managing the development and, later, product management — hiring and leading a team of designers, engineers and data analysts.",
    "portfolio.case4.product.title": "Product",
    "portfolio.case4.product.body":
      "A platform that aggregates news (in Portuguese, Spanish and English) from partners and the public, geo-referenced on maps built with the TileMill tool.",
    "portfolio.case4.evolution.title": "Evolution",
    "portfolio.case4.evolution.body":
      "Before, a manual Jekyll-based system generated static content published straight to a Git repository — there wasn't even a search engine. With no budget to maintain a proprietary platform long-term, I proposed building an open-source WordPress theme and a community around it. That was the first step toward Jeo.",
    "portfolio.case4.outcomes.title": "Outcomes",
    "portfolio.case4.outcomes.body":
      "The site's pageviews increased 400% in one year. More than seven years after launch, the code is still maintained by another organization, the Earth Journalism Network.",

    /* ---------------- TALKS ---------------- */
    "talks.title": "Talks — Angelo Pixel",
    "talks.eyebrow": "Talks & Recognition",
    "talks.hero.title": "Twenty-four years of stages, VJ booths, and classrooms.",
    "talks.hero.lede":
      "100+ talks, panels, workshops and exhibitions across 5 countries and 14 Brazilian states — from free software and VJing to internationally awarded augmented reality.",

    "talks.stat.talks.num": "100+",
    "talks.stat.talks.label": "talks, workshops and exhibitions since 2002",
    "talks.stat.continents.num": "4",
    "talks.stat.continents.label": "continents where I've presented work",
    "talks.stat.residencies.num": "4",
    "talks.stat.residencies.label": "artist residencies (Netherlands, Spain, UK, Colombia)",
    "talks.stat.awards.num": "5",
    "talks.stat.awards.label": "international and national awards received",

    "talks.recent.title": "Recent highlights",
    "talks.recent1.period": "Nov 2025",
    "talks.recent1.title": "Mozilla Festival — Barcelona",
    "talks.recent1.body":
      "The session \"Jandig - Brazilian Myths in Mixed Reality\" was accepted by the festival committee, with Mozilla Foundation travel support funding (EUR 1,910).",
    "talks.recent2.period": "Apr 2026",
    "talks.recent2.title": "São Paulo Innovation Week",
    "talks.recent2.body":
      "Panel \"XR Futures: Games, Art, and the Expansion of Immersive Worlds\", with Almir Almas (USP) and Ana Arruda (XR curator), moderated by Daniel Lima.",
    "talks.recent3.period": "Since 2019",
    "talks.recent3.title": "X-Reality USP",
    "talks.recent3.body":
      "Speaker, creator and curator of the festival, in partnership with the Raindance Film Festival — an annual edition, always in November.",
    "talks.recent4.period": "2019",
    "talks.recent4.title": "Festival MARTE",
    "talks.recent4.body":
      "A transmedia project with augmented reality and extended mythology in Ouro Preto and Cataguases (Minas Gerais), in collaboration with UEMG.",

    "talks.eras.title": "Two decades on stage",
    "talks.era1.period": "2012",
    "talks.era1.title": "Jandig's peak year",
    "talks.era1.body":
      "The busiest year on record: the talk \"Jandig – art in augmented reality\" and the panel \"Copyleft Cities\" at FISL 12 (Porto Alegre); the SESC Sorocaba opening as an exhibiting artist (\"VideoPong\", \"Electro-Organic Experiments\"); Campus Party; Circuito Vivo Arte.mov.",
    "talks.era2.period": "2009 – 2011",
    "talks.era2.title": "Info-activism and VJing",
    "talks.era2.body":
      "A workshop at the Info-Activism Camp in Bangalore, India; a panel at the Open Video Conference in New York; FISL 11 and Campus Party in Porto Alegre and São Paulo.",
    "talks.era3.period": "2002 – 2008",
    "talks.era3.title": "Free-software beginnings",
    "talks.era3.body":
      "A professional VJ career (2002–2018, \"retired\" after a performance in China); talks and workshops at FISL, Latinoware, the World Social Forum, and the Brazilian Digital Culture Forum.",

    "talks.awards.title": "Awards and scholarships",
    "talks.award1.year": "2018",
    "talks.award1.body": "Mozilla Open Source Support Award, for Jandig.",
    "talks.award2.year": "2018",
    "talks.award2.body": "Software Livres Culturais award, from the Brazilian Ministry of Culture, for Jandig.",
    "talks.award3.year": "2014",
    "talks.award3.body": "Google Impact Challenge Brazil, for Rede InfoAmazonia.",
    "talks.award4.year": "2012",
    "talks.award4.body": "SESC Sorocaba award, for \"Electro-Organic Experiments\".",
    "talks.award5.year": "2012",
    "talks.award5.body": "Nimk/Vivo Arte.mov artist residency (Brazil/Netherlands).",
    "talks.award6.year": "2011",
    "talks.award6.body": "CEMEC Creative Entrepreneurs award.",
    "talks.award7.year": "2006",
    "talks.award7.body": "Estúdio Livre Collaboration Award.",

    "talks.residencies.title": "Artist residencies",
    "talks.residencies.body":
      "Netherlands (Nimk/Vivo, 2012), Spain, the UK and Colombia — plus multiple residencies across Brazil.",

    "talks.mosaic.title": "Field notes",
    "talks.mosaic.1": "A 360° circular installation covered in AR markers",
    "talks.mosaic.2": "Carnival: an AR intervention in the Rosas de Ouro parade",
    "talks.mosaic.3": "Urban intervention in Ouro Preto (Territorial Narratives)",
    "talks.mosaic.4": "Jandig's traveling exhibit at a SESC cultural center",
    "talks.mosaic.5": "Kids playing with AR marker cubes at a traveling workshop",
    "talks.mosaic.6": "Remexe collection: upcycled clothing tagged with AR markers",
    "talks.mosaic.7": "A talk on stage at Campus Party",
    "talks.mosaic.8": "Silkscreen workshop printing Jandig's visual identity",

    /* ---------------- CONTACT ---------------- */
    "contact.title": "Contact — Angelo Pixel",
    "contact.eyebrow": "Contact",
    "contact.hero.title": "Let's talk.",
    "contact.hero.lede":
      "About product, about art, or about where the two intersect — I'm reachable by email, a LinkedIn message, or a good conversation in person.",
    "contact.email.label": "Email",
    "contact.linkedin.label": "LinkedIn",
    "contact.github.label": "GitHub",
    "contact.jandig.label": "Jandig",
    "contact.email.channel": "I reply within 2 business days",
    "contact.linkedin.channel": "Full career history and recommendations",
    "contact.github.channel": "Open-source code and experiments",
    "contact.jandig.channel": "The AR platform I founded",
  },
};
