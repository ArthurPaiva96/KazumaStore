from django import forms
from produtos.models import Produto
class CadastrarProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'foto', 'classe']

    def is_valid(self):
        valid = True

        if not super(CadastrarProdutoForm, self).is_valid() or \
                float(self.data['preco']) < 0 or \
                self.data['foto'][:26] != 'static/kazumaStore/images/' or \
                (self.data['classe'] != 'card text-center anime' and self.data['classe'] != 'card text-center figure'):

            self.adiciona_erro('Verificar os dados inseridos!')
            valid = False

        return valid

    def adiciona_erro(self, message):
        erro = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        erro.append(message)