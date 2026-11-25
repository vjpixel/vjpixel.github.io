"""Builds tools/activities.txt (English, public) from the private event list.

Usage: python tools/import_activities.py <path to dados.txt> tools/activities.txt
Only confirmed rows are imported. Output fields: date|place|event|type|title|abroad (1 or 0)
"""
import io
import re
import sys

SRC, DST = sys.argv[1], sys.argv[2]

TYPES = {
    "oficina": "Workshop", "palestra": "Talk", "exposição": "Exhibition",
    "instalação": "Installation", "organização": "Organization", "debate": "Discussion",
    "performance de VJ": "VJ set", "painel": "Panel", "apresentação": "Presentation",
    "residência": "Residency", "curso": "Course", "curadoria": "Curation",
    "mediação": "Moderation", "direção de tecnologia": "Technology direction",
    "performance": "Performance", "aula": "Guest lecture", "pitch": "Pitch",
    "júri": "Jury", "entrevista": "Interview",
}

# Rows left out of the public page: (date, start of the event name).
SKIP = [
    ("2023-09", "Antler Brasil"),
    ("2015-03-06", "Ciclo de oficinas Jornalismo"),
    ("2015-10-14", "Rede InfoAmazonia, oficinas"),
    ("2022-11-19", "X-Reality USP 2022"),
]

# Titles that are descriptions, or that need a different wording. "" drops the title.
# "Type::title" also replaces the type.
TITLES = {
    '"Beberibe" (instalação coletiva)': '"Beberibe", group installation',
    '"Memórias" (video mapping)': '"Memórias", projection mapping',
    '"Photolink" (mosaico com 24 projetores)': '"Photolink", a mosaic of 24 projectors',
    '"oficina INSPER" (publicação)': '',
    '"oficina CM Kabum"': '"Chronica Mobilis"',
    '"VJ pixel na Festa do Vinil"': '',
    '"Jandig - augmented reality exhibition"': 'Session::"Jandig - augmented reality exhibition"',
    'Comissão de Seleção': 'selection committee',
    'Jandig em RA no desfile ("Passista 4.0")': 'Jandig augmented reality in the parade',
    'LAB "Dinner Date" com ZU-UK e TAG Montréal': 'lab "Dinner Date", with ZU-UK and TAG Montréal',
    'Mostra de Clipes 360º': 'showcase of 360° music videos',
    'VJ': '',
    'VJ e articulação do festival': 'VJ set and festival organizing',
    'VJ nas festas e coordenação das mostras de vídeo (14 a 16/05)': 'VJ sets and coordination of the video showcases',
    'VJ no show de Gilberto Gil': "VJ at Gilberto Gil's concert",
    'abertura do tema "Building networks across regions" (com Benjamin Sugar)': 'opening of the theme "Building networks across regions"',
    'apoio à mostra de VR (4 a 7/10)': 'Collaboration::support for the VR showcase',
    'apresentação da Rede InfoAmazonia (um ano de projeto e próximos passos)': 'Rede InfoAmazonia, one year on',
    "apresentação da Rede InfoAmazonia / Mãe d'Água": 'Rede InfoAmazonia',
    'apresentação do VJ Pixel': '',
    'apresentação final da residência': 'final presentation of the residency',
    'apresentação pública dos residentes': 'public presentation by the residents',
    'articulação do lançamento': 'organizing the launch',
    'assistência de produção': 'production assistant',
    'captação e projeção mapeada': 'video capture and projection mapping',
    'colaboração na Arena Arte Livre': 'collaboration on the Arena Arte Livre',
    'comissão organizadora e curadoria': 'organizing committee and curation',
    'comissão organizadora, curadoria internacional e produção executiva': 'organizing committee, international curation and executive production',
    'comitê científico, equipe executiva e making-of': 'scientific committee, executive team and making-of',
    'conferência sobre modelos de LAB e residência': 'co-host of the conference on lab and residency models',
    'coordenação': 'coordination',
    'coordenação da Mostra do Vídeo Livre': 'coordination of the Mostra do Vídeo Livre',
    'coordenação da TV Criei, Tive Como!': 'coordination of TV Criei, Tive Como!',
    'coordenação da plataforma online de vídeo e transmissão ao vivo': 'coordination of the online video platform and live streaming',
    'coordenação da área de Vídeo': 'coordination of the Video area',
    'coordenação de produção (fundador da rede VJBR)': 'production coordination, as founder of the VJBR network',
    'coordenação de tecnologia da informação': 'IT coordination',
    'coordenação de tecnologia e transmissão ao vivo': 'coordination of technology and live streaming',
    'curadoria de vídeo': 'video curation',
    'curso de RA "Rejunte" (2 dias)': 'augmented reality course "Rejunte"',
    'episódio com Angelo Pixel (trajetória, open source, Antler)': 'podcast episode',
    'estande do InfoAmazonia / Jeo na Media Feria': 'InfoAmazonia and Jeo stand at the Media Feria',
    'estágio de produção': 'production intern',
    'exposição Jandig (tema Japão)': 'Jandig exhibition, Japan theme',
    'idealização, comissão organizadora, comitê científico e produção técnica': 'creation, organizing committee, scientific committee and technical production',
    'instalação em Realidade Mista e álbum de figurinhas em AR': 'mixed reality installation and AR sticker album',
    'laboratório de experimentos tecnológicos': 'lab of technology experiments',
    'laboratório de interação entre pessoas e plantas': 'lab on interaction between people and plants',
    'mesa de abertura': 'opening panel',
    'oficina de produção audiovisual (videocast) do LABmais (agenda: aulas de jul a set/2023)': 'videocast production',
    'oficina de streaming/IPTV': 'streaming and IPTV',
    'oficina de video mapping': 'projection mapping',
    'oficina de video mapping (19 a 22/08) e mostra (23/08)': 'projection mapping, with a closing showcase',
    'organização e seleção da residência (videodança 360º)': 'organization and selection of the 360° video dance residency',
    'participação em discussões representando o Brasil e o Projeto LiVES': 'discussions, representing Brazil and the LiVES project',
    'piloto de rede de monitoramento ambiental ("Código Urbano")': 'pilot of an environmental monitoring network, "Código Urbano"',
    'plataforma do Observatório de Áreas Protegidas e Clima (com Vitor George)': 'platform of the Observatory of Protected Areas and Climate',
    'playteste, demonstração e fala sobre o projeto': 'playtest, demo and talk about the project',
    'produção executiva (Media Sana)': 'executive production',
    'projeto "memeLab" (curso imersivo e reality show)': 'project "memeLab"',
    'seleção do torneio de VJ': 'selection for the VJ tournament',
    'seminário sobre mundo VUCA e trajetória': 'seminar on the VUCA world and my career',
    'sessão de escrita colaborativa do Narrative Navigation (14h às 17h, com Sander Veenhof, Labmovel)': 'collaborative writing session for Narrative Navigation',
    'set de VJ no Zona Mundi': '',
    'tour digital da exposição (Prezi e vídeo)': 'digital tour of the exhibition',
    'webinário "Arte, Cultura e Tecnologia"': 'webinar "Arte, Cultura e Tecnologia"',
    'última apresentação como VJ': 'my last VJ performance',
}

PLACES = {
    "não informado": "",
    "Vitória, ES; Rio de Janeiro, RJ; São Paulo, SP; Florianópolis, SC; Curitiba, PR; Porto Alegre, RS":
        "Vitória, Rio de Janeiro, São Paulo, Florianópolis, Curitiba and Porto Alegre",
    "São Paulo (São Miguel Paulista, Itaim Paulista, São Mateus), Vale do Ribeira (Ilha Comprida, Iporanga, Itariri) e litoral (Cubatão, Bertioga, Peruíbe), SP":
        "Nine stops in São Paulo state",
    "Bebedouro, Itápolis, Novo Horizonte, Araçatuba, Andradina, Lins, Lucélia, Osvaldo Cruz e Presidente Venceslau, SP":
        "Nine cities in São Paulo state",
    "Miguel Pereira e Vera Cruz, RJ (Centro Popular de Conspiração Gargarullo)": "Miguel Pereira, RJ",
    "Belo Horizonte, MG ou online": "Belo Horizonte, MG or online",
    "Cocodrie, EUA (LUMCON, Louisiana)": "Cocodrie, Louisiana, USA",
    "San Francisco e Berkeley, EUA": "San Francisco and Berkeley, USA",
    "Amsterdã, Holanda; São Paulo, SP": "Amsterdam, Netherlands and São Paulo, SP",
    "São Paulo, SP; Rio de Janeiro, RJ": "São Paulo, SP and Rio de Janeiro, RJ",
    "São Paulo, SP (Sesc Bom Retiro) e online": "São Paulo, SP and online",
}
PLACE_WORDS = [
    ("Bangalore, Índia", "Bangalore, India"), ("Nova York, EUA", "New York, USA"),
    ("Amsterdã, Holanda", "Amsterdam, Netherlands"), ("Montevidéu, Uruguai", "Montevideo, Uruguay"),
    ("Barcelona, Espanha", "Barcelona, Spain"), ("Londres, Reino Unido", "London, UK"),
    ("Bogotá, Colômbia", "Bogotá, Colombia"), ("Montreal, Canadá", "Montreal, Canada"),
]

EVENTS = [
    ('Lançamento brasileiro do filme', 'Brazilian launch of the film'),
    ('Aniversário de um ano do Desafio de Impacto Social Google (sede do Google)',
     'First anniversary of the Google Impact Challenge Brazil (Google office)'),
    ('Inauguração do Sesc', 'Opening of Sesc'),
    (', peça "', ', play "'),
    ('Exposição "Caipirismo', 'Exhibition "Caipirismo'),
    ('Imersão de IA da diar.ia.br, turma', 'diar.ia.br AI Immersion, cohort'),
    ('Rede iVoz, oficinas de IPTV', 'Rede iVoz, IPTV workshops'),
    ('Residência Artística #plural (memeLab e PlanoP)', 'Artist residency #plural (memeLab and PlanoP)'),
    ('26º Raindance', '26th Raindance'),
    ('(parceria Jandig e Lá da Favelinha)', '(Jandig and Lá da Favelinha)'),
    ('(ateliê e FUMEC)', '(studio and FUMEC)'),
    ('(estande do Senac)', '(Senac stand)'),
    ('(games, RV e RA)', '(games, VR and AR)'),
    ('Conferência Acadêmica', 'Academic Conference'),
]


def place(p):
    if p in PLACES:
        return PLACES[p]
    if "provável" in p:
        return ""
    p = re.sub(r"\s*\(.*\)$", "", p)
    for a, b in PLACE_WORDS:
        p = p.replace(a, b)
    return p


def title(t):
    if t in TITLES:
        return TITLES[t]
    assert t.startswith('"'), "sem tradução: " + t
    return re.sub(r'"\s*\(.*\)$', '"', t)


out = []
for line in io.open(SRC, encoding="utf-8"):
    f = line.rstrip("\n").split("|")
    if len(f) != 10 or f[7] != "c":
        continue
    data, local, pais, evento, tipo, titulo, papel = f[:7]
    if any(data == d and evento.startswith(e) for d, e in SKIP):
        continue
    typ = "Keynote" if "keynote" in papel else TYPES[tipo]
    ti = title(titulo)
    if "::" in ti:
        typ, ti = ti.split("::", 1)
    for a, b in EVENTS:
        evento = evento.replace(a, b)
    abroad = "0" if pais in ("Brasil", "n/i", "online") else "1"
    row = [data, place(local), evento, typ, ti, abroad]
    assert not any("|" in x or "—" in x for x in row), row
    out.append(row)

out.sort(key=lambda r: r[0])
io.open(DST, "w", encoding="utf-8", newline="\n").write(
    "\n".join("|".join(r) for r in out) + "\n")
print(len(out), "activities")
