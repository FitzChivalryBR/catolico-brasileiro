import os

# PRODUZINDO INDEX PAGE

# Definir caminhos dos arquivos
css_file = os.getcwd() + '\\styles.css'
js_file = os.getcwd() + '\\scripts.js'
html_index = os.getcwd() + '\\index_template.html'  # Modelo base
html_output = os.getcwd() + '\\index.html'  # Novo arquivo gerado
html_menu = os.getcwd() + '\\menu.html'  # Menu que será inserido

# Conteúdo variável do HEAD

meta_tags = {
    "description": "Explore a Bíblia Online, o Catecismo da Igreja Católica, obras traduzidas e artigos sobre espiritualidade no Portal Católico do Brasil.",
    "keywords": "Bíblia Online, Catecismo, Igreja Católica, Obras Católicas, Santos Modernos, Direito Canônico",
    "author": "Portal Católico do Brasil",
    "og:title": "Portal Católico do Brasil - Bíblia, Catecismo e Obras Católicas",
    "og:description": "Explore a Bíblia Online, o Catecismo da Igreja Católica, obras traduzidas e artigos sobre espiritualidade no Portal Católico do Brasil.",
    "og:image": "https://arquidiocesebh.org.br/wp-content/uploads/2017/06/13-stantonio-204x204.jpg",
    "og:url": "https://arquidiocesebh.org.br/wp-content/uploads/2017/06/13-stantonio-204x204.jpg",
    "twitter:card": "summary_large_image"
}

# titulos hero

hero_title = 'Portal Católico'
hero_description = 'Bem-vindo ao Portal Católico do Brasil,<br>sua fonte de conhecimento e espiritualidade.'


# Ler o template base do index.html
with open(html_index, "r", encoding="utf-8") as file:
    html_content = file.read()

# Ler o conteúdo do menu.html
if os.path.exists(html_menu):
    with open(html_menu, "r", encoding="utf-8") as menu_file:
        menu_content = menu_file.read()
else:
    menu_content = "<!-- Menu não encontrado -->"

# Substituir as meta tags no HEAD
for key, value in meta_tags.items():
    html_content = html_content.replace(f'<!-- {key} -->', f'<meta name="{key}" content="{value}">')


# Inserir o menu no local correto
html_content = html_content.replace("<!-- INSERIR MENU AQUI -->", menu_content)

# Substituir título e descrição do Hero Section
html_content = html_content.replace("<!-- HERO_TITLE -->", hero_title)
html_content = html_content.replace("<!-- HERO_DESCRIPTION -->", hero_description)


# Ler o conteúdo do JS
if os.path.exists(js_file):
    with open(js_file, "r", encoding="utf-8") as js_file_content:
        js_content = js_file_content.read()

html_content = html_content.replace("</body>", f"<script>\n{js_content}\n</script>\n</body>")


# Ler o conteúdo do CSS

if os.path.exists(css_file):
    with open(css_file, "r", encoding="utf-8") as css_file_content:
        css_content = css_file_content.read()

html_content = html_content.replace("</head>", f"<style>\n{css_content}\n</style>\n</head>")


# Escrever o novo index.html atualizado
with open(html_output, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"✅ Novo index.html gerado com sucesso:\n{html_output}")







# PRODUZINDO MAPA APOSTOLO PAULO


# Definir caminhos dos arquivos
css_file = os.getcwd() + '\\styles.css'
js_file = os.getcwd() + '\\scripts.js'
html_nova_pg = os.getcwd() + '\\nova_pagina_template.html'  # Modelo base
html_nova_pg_output = os.getcwd() + '\\linha_do_tempo\\viagens_sao_paulo_apostolo.html'  # Novo arquivo gerado
html_menu = os.getcwd() + '\\menu.html'  # Menu que será inserido

# conteudo_file = os.getcwd() + '\\linha_do_tempo\\mapa_viagens_sao_paulo_apostolo.html'

conteudo_file = '''

  <div class="mapa-py-html">
    <center>
      <iframe src="mapa_viagens_sao_paulo_apostolo.html" width="1250" height="600" class="no-border-iframe"></iframe>
    </center>
  </div>

  
'''


# Conteúdo variável do HEAD

meta_tags = {
    "description": "Explore a Bíblia Online, o Catecismo da Igreja Católica, obras traduzidas e artigos sobre espiritualidade no Portal Católico do Brasil.",
    "keywords": "Bíblia Online, Catecismo, Igreja Católica, Obras Católicas, Santos Modernos, Direito Canônico",
    "author": "Portal Católico do Brasil",
    "og:title": "Portal Católico do Brasil - Bíblia, Catecismo e Obras Católicas",
    "og:description": "Explore a Bíblia Online, o Catecismo da Igreja Católica, obras traduzidas e artigos sobre espiritualidade no Portal Católico do Brasil.",
    "og:image": "https://arquidiocesebh.org.br/wp-content/uploads/2017/06/13-stantonio-204x204.jpg",
    "og:url": "https://arquidiocesebh.org.br/wp-content/uploads/2017/06/13-stantonio-204x204.jpg",
    "twitter:card": "summary_large_image"
}

# titulos hero

hero_title = 'Viagens de São Paulo Apóstolo'
hero_description = 'Neste mapa interativo, navegue pelas Missões do Apóstolo São Paulo'


# Ler o template base do index.html
with open(html_nova_pg, "r", encoding="utf-8") as file:
    html_content = file.read()

# Ler o conteúdo do menu.html
if os.path.exists(html_menu):
    with open(html_menu, "r", encoding="utf-8") as menu_file:
        menu_content = menu_file.read()
else:
    menu_content = "<!-- Menu não encontrado -->"

# Substituir as meta tags no HEAD
for key, value in meta_tags.items():
    html_content = html_content.replace(f'<!-- {key} -->', f'<meta name="{key}" content="{value}">')


# Inserir o menu no local correto
html_content = html_content.replace("<!-- INSERIR MENU AQUI -->", menu_content)

# Substituir título e descrição do Hero Section
html_content = html_content.replace("<!-- HERO_TITLE -->", hero_title)
html_content = html_content.replace("<!-- HERO_DESCRIPTION -->", hero_description)


if os.path.exists(conteudo_file):
    with open(conteudo_file, "r", encoding="utf-8") as conteudo_file_content:
        conteudo_content = conteudo_file_content.read()
# Inserir conteúdo
# html_content = html_content.replace("<!-- INSIRA_CONTEUDO_AQUI -->", conteudo_content)

html_content = html_content.replace("<!-- INSIRA_CONTEUDO_AQUI -->", conteudo_file)

# Ler o conteúdo do JS
if os.path.exists(js_file):
    with open(js_file, "r", encoding="utf-8") as js_file_content:
        js_content = js_file_content.read()

html_content = html_content.replace("</body>", f"<script>\n{js_content}\n</script>\n</body>")


# Ler o conteúdo do CSS

if os.path.exists(css_file):
    with open(css_file, "r", encoding="utf-8") as css_file_content:
        css_content = css_file_content.read()

html_content = html_content.replace("</head>", f"<style>\n{css_content}\n</style>\n</head>")


# Escrever o novo index.html atualizado
with open(html_nova_pg_output, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"\n✅ Mapa apóstolo Paulo criado com sucesso:\n{html_nova_pg_output}")






# PRODUZINDO PÁGINA PRINCIPAL CATENA AUREA


# Definir caminhos dos arquivos
css_file = os.getcwd() + '\\styles.css'
js_file = os.getcwd() + '\\scripts.js'
html_nova_pg = os.getcwd() + '\\nova_pagina_template.html'  # Modelo base
html_nova_pg_output = os.getcwd() + '\\catena_aurea_online\\pagina-principal.html'  # Novo arquivo gerado
html_menu = os.getcwd() + '\\menu.html'  # Menu que será inserido

# conteudo_file = os.getcwd() + '\\linha_do_tempo\\mapa_viagens_sao_paulo_apostolo.html'

conteudo_file = '''


            <ul class="evangelho-list">
                <li><a href="sao-mateus/filtros.html">Evangelho Segundo São Mateus</a></li>
                <li><a href="sao-marcos/filtros.html">Evangelho Segundo São Marcos</a></li>
                <li><a href="sao-lucas/filtros.html">Evangelho Segundo São Lucas</a></li>
                <li><a href="sao-joao/filtros.html">Evangelho Segundo São João</a></li>
            </ul>


  
'''


# Conteúdo variável do HEAD

meta_tags = {
    "description": "Explore a Bíblia Online, o Catecismo da Igreja Católica, obras traduzidas e artigos sobre espiritualidade no Portal Católico do Brasil.",
    "keywords": "Bíblia Online, Catecismo, Igreja Católica, Obras Católicas, Santos Modernos, Direito Canônico",
    "author": "Portal Católico do Brasil",
    "og:title": "Portal Católico do Brasil - Bíblia, Catecismo e Obras Católicas",
    "og:description": "Explore a Bíblia Online, o Catecismo da Igreja Católica, obras traduzidas e artigos sobre espiritualidade no Portal Católico do Brasil.",
    "og:image": "https://arquidiocesebh.org.br/wp-content/uploads/2017/06/13-stantonio-204x204.jpg",
    "og:url": "https://arquidiocesebh.org.br/wp-content/uploads/2017/06/13-stantonio-204x204.jpg",
    "twitter:card": "summary_large_image"
}

# titulos hero

hero_title = 'Bem-vindo à Catena Áurea'
hero_description = 'Escolha um Evangelho abaixo para explorar os comentários e ensinamentos dos Padres da Igreja:'


# Ler o template base do index.html
with open(html_nova_pg, "r", encoding="utf-8") as file:
    html_content = file.read()

# Ler o conteúdo do menu.html
if os.path.exists(html_menu):
    with open(html_menu, "r", encoding="utf-8") as menu_file:
        menu_content = menu_file.read()
else:
    menu_content = "<!-- Menu não encontrado -->"

# Substituir as meta tags no HEAD
for key, value in meta_tags.items():
    html_content = html_content.replace(f'<!-- {key} -->', f'<meta name="{key}" content="{value}">')


# Inserir o menu no local correto
html_content = html_content.replace("<!-- INSERIR MENU AQUI -->", menu_content)

# Substituir título e descrição do Hero Section
html_content = html_content.replace("<!-- HERO_TITLE -->", hero_title)
html_content = html_content.replace("<!-- HERO_DESCRIPTION -->", hero_description)


if os.path.exists(conteudo_file):
    with open(conteudo_file, "r", encoding="utf-8") as conteudo_file_content:
        conteudo_content = conteudo_file_content.read()
# Inserir conteúdo
# html_content = html_content.replace("<!-- INSIRA_CONTEUDO_AQUI -->", conteudo_content)

html_content = html_content.replace("<!-- INSIRA_CONTEUDO_AQUI -->", conteudo_file)

# Ler o conteúdo do JS
if os.path.exists(js_file):
    with open(js_file, "r", encoding="utf-8") as js_file_content:
        js_content = js_file_content.read()

html_content = html_content.replace("</body>", f"<script>\n{js_content}\n</script>\n</body>")


# Ler o conteúdo do CSS

if os.path.exists(css_file):
    with open(css_file, "r", encoding="utf-8") as css_file_content:
        css_content = css_file_content.read()
        additional = '''  

            .evangelho-list {
                list-style: none;
                padding: 0;
                text-align: center;
            }

            .evangelho-list li {
                margin: 1rem 0;
            }

            .evangelho-list a {
                display: inline-block;
                padding: 0.75rem 1.5rem;
                background-color: #4CAF50;
                color: #fff;
                text-decoration: none;
                font-size: 1.2rem;
                font-weight: bold;
                border-radius: 5px;
                transition: background-color 0.3s ease, transform 0.2s ease;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }

            .evangelho-list a:hover {
                background-color: #45a049;
                transform: translateY(-3px);
                box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
            }

            .evangelho-list a:active {
                transform: translateY(0);
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }

        '''
        css_content += additional

html_content = html_content.replace("</head>", f"<style>\n{css_content}\n</style>\n</head>")


# Escrever o novo index.html atualizado
with open(html_nova_pg_output, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"\n✅ Nova página gerada com sucesso:\n{html_nova_pg_output}")


















# PRODUZINDO PÁGINA SÃO JOÃO DE CADA CATENA AUREA



# Definir caminhos dos arquivos
css_file = os.getcwd() + '\\styles.css'
css_file_add = os.getcwd() + '\\catena_aurea_online\\sao-joao\\styles.css'
js_file = os.getcwd() + '\\scripts.js'
js_file_add = os.getcwd() + '\\catena_aurea_online\\sao-joao\\script.js'
html_nova_pg = os.getcwd() + '\\nova_pagina_template.html'  # Modelo base
html_nova_pg_output = os.getcwd() + '\\catena_aurea_online\\sao-joao\\filtros.html'  # Novo arquivo gerado
html_menu = os.getcwd() + '\\menu.html'  # Menu que será inserido

# conteudo_file = os.getcwd() + '\\linha_do_tempo\\mapa_viagens_sao_paulo_apostolo.html'

conteudo_file = '''



        <main>
            <section id="doacao-pix">
                <center>
                    <button id="btn-doar">
                        <i class="fa-brands fa-pix"></i> Doar via Pix
                    </button>            
                    <div id="pix-info" style="display: none; margin-top: 10px; text-align: center;">
                        <img src="https://fastprint.com.br/wp-content/uploads/2023/06/Detalhe-prod-qrcode-full2x-1010x718-1.jpg.webp" alt="QR Code Pix" style="width: 200px; height: auto; margin-bottom: 10px;">
                        <p>Chave Pix: <strong>ivivergasta@gmail.com</strong></p>
                    </div>
                </center>
            </section>

            <div id="filter">
                <label for="capitulo">Selecionar Capítulo:</label>
                <select id="capitulo"></select>

                <label for="versiculo">Selecionar Versículo:</label>
                <select id="versiculo"></select>
                <button id="buscar">Buscar</button>
            </div>

            <article>
                <h2>São João</h2>
                <p class="verse"><em>
                    <!-- Dynamic content will be injected here -->
                </em></p>

                <div class="cntr" style="margin-top: 10px; display: flex; align-items: center; gap: 10px;">
                    <div class="row press" style="margin-bottom: 0;">
                        <input type="checkbox" id="toggle-structure" class="cbx hidden"/>
                        <label for="toggle-structure" class="lbl"></label>
                    </div>
                    <span style="font-size: 15px; color: #333;">Ocultar outras línguas</span>
                </div>

                <section id="tooltip-section">
                    <!-- Dynamic content will be injected here -->
                </section>
            </article>
        </main>


  
'''


# Conteúdo variável do HEAD

meta_tags = {
    "description": "Explore a Bíblia Online, o Catecismo da Igreja Católica, obras traduzidas e artigos sobre espiritualidade no Portal Católico do Brasil.",
    "keywords": "Bíblia Online, Catecismo, Igreja Católica, Obras Católicas, Santos Modernos, Direito Canônico",
    "author": "Portal Católico do Brasil",
    "og:title": "Portal Católico do Brasil - Bíblia, Catecismo e Obras Católicas",
    "og:description": "Explore a Bíblia Online, o Catecismo da Igreja Católica, obras traduzidas e artigos sobre espiritualidade no Portal Católico do Brasil.",
    "og:image": "https://arquidiocesebh.org.br/wp-content/uploads/2017/06/13-stantonio-204x204.jpg",
    "og:url": "https://arquidiocesebh.org.br/wp-content/uploads/2017/06/13-stantonio-204x204.jpg",
    "twitter:card": "summary_large_image"
}

# titulos hero

hero_title = 'Bem-vindo aos comentários do Evangelho de São João'
hero_description = 'Selecione o Capítulo e Versículo abaixo:'


# Ler o template base do index.html
with open(html_nova_pg, "r", encoding="utf-8") as file:
    html_content = file.read()

# Ler o conteúdo do menu.html
if os.path.exists(html_menu):
    with open(html_menu, "r", encoding="utf-8") as menu_file:
        menu_content = menu_file.read()
else:
    menu_content = "<!-- Menu não encontrado -->"

# Substituir as meta tags no HEAD
for key, value in meta_tags.items():
    html_content = html_content.replace(f'<!-- {key} -->', f'<meta name="{key}" content="{value}">')


# Inserir o menu no local correto
html_content = html_content.replace("<!-- INSERIR MENU AQUI -->", menu_content)

# Substituir título e descrição do Hero Section
html_content = html_content.replace("<!-- HERO_TITLE -->", hero_title)
html_content = html_content.replace("<!-- HERO_DESCRIPTION -->", hero_description)


if os.path.exists(conteudo_file):
    with open(conteudo_file, "r", encoding="utf-8") as conteudo_file_content:
        conteudo_content = conteudo_file_content.read()
# Inserir conteúdo
# html_content = html_content.replace("<!-- INSIRA_CONTEUDO_AQUI -->", conteudo_content)

html_content = html_content.replace("<!-- INSIRA_CONTEUDO_AQUI -->", conteudo_file)

# Ler o conteúdo do JS
if os.path.exists(js_file):
    with open(js_file, "r", encoding="utf-8") as js_file_content:
        js_content = js_file_content.read()
        if os.path.exists(js_file_add):
            with open(js_file_add, "r", encoding="utf-8") as js_file_add_content:
                js_content += js_file_add_content.read()

html_content = html_content.replace("</body>", f"<script>\n{js_content}\n</script>\n</body>")


# Ler o conteúdo do CSS

if os.path.exists(css_file):
    with open(css_file, "r", encoding="utf-8") as css_file_content:
        css_content = css_file_content.read()
        if os.path.exists(css_file_add):
            with open(css_file_add, "r", encoding="utf-8") as css_file_add_content:
                css_content += css_file_add_content.read()

html_content = html_content.replace("</head>", f"<style>\n{css_content}\n</style>\n</head>")


# Escrever o novo index.html atualizado
with open(html_nova_pg_output, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"\n✅ Nova página gerada com sucesso:\n{html_nova_pg_output}")





























