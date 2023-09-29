# API de Classificados

Esta é uma API de classificados construída usando Django e Django Rest Framework. Ele fornece endpoints para gerenciar empresas, prospectos e categorias.

## Endpoints

A API possui os seguintes endpoints:

- **Empresas:** Endpoint para gerenciar informações sobre empresas.

    - URL: [http://0.0.0.0:8000/empresas/](http://0.0.0.0:8000/empresas/)
    - Métodos suportados: GET

- **Prospectos:** Endpoint para gerenciar informações sobre prospectos.

    - URL: [http://0.0.0.0:8000/prospectos/](http://0.0.0.0:8000/prospectos/)
    - Métodos suportados: POST

- **Categorias:** Endpoint para gerenciar informações sobre categorias.

    - URL: [http://0.0.0.0:8000/categorias/](http://0.0.0.0:8000/categorias/)
    - Métodos suportados: GET

## Como Usar

1. Clone este repositório em seu ambiente de desenvolvimento:

   ```
   git clone https://github.com/mascDriver/api_classificados.git
   ```

2. Instale as dependências necessárias:

   ```
   pip install -r requirements.txt
   ```

3. Execute as migrações do banco de dados:

   ```
   python manage.py migrate
   ```

4. Inicie o servidor de desenvolvimento:

   ```
   python manage.py runserver
   ```

Agora, você pode acessar os endpoints da API usando as URLs fornecidas acima e os métodos HTTP suportados.

## Exemplos de Requisições

Aqui estão alguns exemplos de como você pode usar a API:

### Obtendo uma lista de empresas

```
GET http://0.0.0.0:8000/empresas/
```

Lembre-se de substituir `{id}` pelo ID real da empresa que você deseja atualizar ou excluir.

## Contribuindo

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir problemas (issues) ou enviar solicitações de pull (pull requests). Agradecemos o seu interesse e contribuição!

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

