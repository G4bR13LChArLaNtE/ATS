import pytest

from unittest.mock import Mock
from ..src.blog import Blog


class ExcecaoPostsNaoEncontrados(Exception):
    pass



@pytest.fixture
def blog1():
    posts = Blog.posts()
    return posts

def test_buscar_todos_posts(blog1):
    blog1Repositorio = Mock()
    blog1Repositorio.posts.return_value = blog1
    blog1Repositorio.numero_de_postagens.return_value = 'todas'
    resultado = blog1Repositorio.posts()

    assert resultado[0]['userId']== 1
    assert resultado[0]['id'] == 1
    assert resultado[0]['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'
    assert resultado[0]['body'] == 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'
    assert blog1Repositorio.numero_de_postagens() == 'todas'

def test_buscar_todos_posts_inexistente_excecao(blog1):
    blog1Repositorio = Mock()
    blog1Repositorio.posts.side_effect = ExcecaoPostsNaoEncontrados

    with pytest.raises(ExcecaoPostsNaoEncontrados):
        blog1Repositorio.posts()


@pytest.fixture
def blog2():
    post1 = Blog.post_by_user_id('1')
    return post1

def test_buscar_blog_por_id(blog2):
    blog2Repositorio = Mock()
    blog2Repositorio.post_by_user_id.return_value = blog2
    blog2Repositorio.numero_de_postagens.return_value = 1
    resultado = blog2Repositorio.post_by_user_id('1')

    assert resultado['userId']== 1
    assert resultado['id'] == 1
    assert resultado['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'
    assert resultado['body'] == 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'
    assert blog2Repositorio.numero_de_postagens() == 1

def test_buscar_blog_por_id_inexistente_excecao(blog2):
    blog2Repositorio = Mock()
    blog2Repositorio.post_by_user_id.side_effect = ExcecaoPostsNaoEncontrados

    with pytest.raises(ExcecaoPostsNaoEncontrados):
        blog2Repositorio.post_by_user_id('1')