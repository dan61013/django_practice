from django import forms
from .models import Bboy

# class BboyForm(forms.ModelForm):
#     class Meta:
#         model = Bboy
#         fields = '__all__' # 導入Bboy全部的attutribe
#         # 部分導入寫法
#         # fields = ('name', 'age', )

class BboyForm(forms.ModelForm):
    model = Bboy
    fields = '__all__' # 導入Bboy全部的attutribe
    # 部分導入寫法
    # fields = ('name', 'age', )