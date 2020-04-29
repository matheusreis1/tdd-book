from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ouviu falar de uma nova aplicacao online interessante para
        # lista de tarefas. Ela decide verificar sua homepage
        self.browser.get('http://localhost:8000')

        # Ela percebe que o titulo da pagina e o cabecalho mencionam listas de
        # tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Ela e convidada a inserir um item de tarefa imediatamente

        # Ela digita "Buy peacock feathers" (Comprar penas de pavao) em uma caixa
        # de texto (o hobby de Edith e fazer iscas para pesca com fly)

        # Quanto ela tecla enter, a pagina e atualizada, e agora a pagina lista
        # "1: Buy peacock feathers" como um item em uma lista de tarefas

        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro
        # item. Ela insere "Use peacock feathers to make a fly" (Usar penas de pavao
        # para fazer um fly - Edith e bem metodica)

        # A pagina e atualizada novamente e agora mostar os dois items em sua lista

        # Edith se pergunta se o site lembrara de sua lista. Entao ela nota
        # que o site gerou um URL unico para ela -- ha um pequeno
        # texto explicativo para isso

        # Ela acessa esse URL - sua lista de tarefas continua la

        # Satisfeita, ela volta a dormir

if __name__ == '__main__':
    unittest.main(warnings='ignore')