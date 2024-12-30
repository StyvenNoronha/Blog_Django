# Django Blog Project

Este é um projeto de blog desenvolvido em Django, que inclui as seguintes funcionalidades principais:

- Visualização de posts publicados na página inicial com paginação.
- Filtragem de posts por autor, categoria e tags.
- Exibição de páginas estáticas e posts individuais.
- Funcionalidade de busca com resultados baseados no título, resumo e conteúdo dos posts.

## Requisitos

- Python 3.12+
- Django 5.1+
- Pillow

## Instalação

1. Clone o repositório:

```sh
git clone https://github.com/StyvenNoronha/Blog_Django
```

2. Crie um ambiente virtual e ative-o:

```sh
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:

```sh
pip install -r requirements.txt
```

4. Aplique as migrações:

```sh
python manage.py makemigrations
python manage.py migrate
```

5. Crie um superusuário para acessar o admin:

```sh
python manage.py createsuperuser
```

6. Inicie o servidor de desenvolvimento:

```sh
python manage.py runserver
```


## Funcionalidades das Views

### Páginas e Endpoints

1. **Página Inicial**
   - URL: `/`
   - Exibe os posts publicados com paginação (9 posts por página).

   ```python
   def index(request):
       posts = Post.objects.get_published()
       paginator = Paginator(posts, 9)
       page_number = request.GET.get("page")
       page_obj = paginator.get_page(page_number)
       return render(request, 'blog/pages/index.html', {'page_obj': page_obj})
   ```

2. **Posts por Autor**
   - URL: `/author/<author_id>`
   - Filtra e exibe os posts de um autor específico.

   ```python
   def author(request, author_id):
       posts = Post.objects.get_published().filter(created_by__pk=author_id)
       paginator = Paginator(posts, 9)
       page_number = request.GET.get("page")
       page_obj = paginator.get_page(page_number)
       return render(request, 'blog/pages/index.html', {'page_obj': page_obj})
   ```

3. **Posts por Categoria**
   - URL: `/category/<slug>`
   - Filtra e exibe os posts de uma categoria específica.

   ```python
   def category(request, slug):
       posts = Post.objects.get_published().filter(category__slug=slug)
       paginator = Paginator(posts, 9)
       page_number = request.GET.get("page")
       page_obj = paginator.get_page(page_number)
       return render(request, 'blog/pages/index.html', {'page_obj': page_obj})
   ```

4. **Posts por Tag**
   - URL: `/tag/<slug>`
   - Filtra e exibe os posts de uma tag específica.

   ```python
   def tag(request, slug):
       posts = Post.objects.get_published().filter(tags__slug=slug)
       paginator = Paginator(posts, 9)
       page_number = request.GET.get("page")
       page_obj = paginator.get_page(page_number)
       return render(request, 'blog/pages/index.html', {'page_obj': page_obj})
   ```

5. **Página Estática**
   - URL: `/page/<slug>`
   - Exibe uma página estática baseada no slug fornecido.

   ```python
   def page(request, slug):
       page = Page.objects.filter(is_published=True).filter(slug=slug).first()
       return render(request, 'blog/pages/page.html', {'page': page})
   ```

6. **Post Individual**
   - URL: `/post/<slug>`
   - Exibe um post específico baseado no slug fornecido.

   ```python
   def post(request, slug):
       post = Post.objects.get_published().filter(slug=slug).first()
       return render(request, 'blog/pages/post.html', {'post': post})
   ```

7. **Busca**
   - URL: `/search`
   - Permite buscar posts pelo título, resumo ou conteúdo. Retorna no máximo 9 resultados.

   ```python
   def search(request):
       search_value = request.GET.get('search', '').strip()
       posts = Post.objects.get_published().filter(
           Q(title__icontains=search_value) |
           Q(excerpt__icontains=search_value) |
           Q(content__icontains=search_value)
       )[:9]
       return render(request, 'blog/pages/index.html', {'page_obj': posts, 'search_value': search_value})
   ```