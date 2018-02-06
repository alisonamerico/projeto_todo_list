from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(
            response, '<h2>TODO LIST - APLICAÇÃO PARA REALIZAR LISTAGEM DE ATIVIDADES</h2>'
            )

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Olá! Eu não deveria estar na página.')


class LoginPageTests(SimpleTestCase):

    def test_login_page_status_code(self):
        response = self.client.get('/accounts/login/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_page_contains_correct_html(self):
        response = self.client.get('/accounts/login/')
        self.assertContains(
            response, '<h1 class="text-center">Acesso Restrito</h1>'
            )

    def test_login_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/accounts/login/')
        self.assertNotContains(
            response, 'Olá! Eu não deveria estar na página.')


class SignUpPageTests(SimpleTestCase):

    def test_login_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_page_contains_correct_html(self):
        response = self.client.get('/accounts/signup/')
        self.assertContains(
            response, '<h2 class="text-center">Formulário de Cadastro</h2>'
            )

    def test_signup_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/accounts/signup/')
        self.assertNotContains(
            response, 'Olá! Eu não deveria estar na página.')


class TodoListPageTests(SimpleTestCase):

    def test_todo_list_page_status_code_not_found_if_not_login(self):
        response = self.client.get('/todo/todo_list/')
        self.assertEquals(response.status_code, 404)
