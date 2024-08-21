# Inj3ctLab

**Inj3ctLab** é uma aplicação web vulnerável, criada para simular cenários de SQL Injection. Esta ferramenta foi desenvolvida para auxiliar profissionais e entusiastas de cibersegurança a praticar e entender melhor essa vulnerabilidade crítica.

## Objetivo

O principal objetivo do Inj3ctLab é proporcionar um ambiente seguro e controlado onde os usuários possam explorar SQL Injection de diversas maneiras, variando desde ataques básicos até técnicas mais avançadas.

## Funcionalidades

- **Vulnerabilidade Controlada**: Configure diferentes níveis de dificuldade diretamente na página de login.
- **Ambiente Realístico**: Utiliza Flask no back-end, React no front-end e MySQL como banco de dados para simular uma aplicação real.
- **Aprendizado Progressivo**: Explore diversas técnicas de SQL Injection com cenários específicos para cada nível de dificuldade.

## Tecnologias Utilizadas

- **Back-end**: Flask (Python)
- **Front-end**: React (JavaScript)
- **Banco de Dados**: MySQL
- **Outras Ferramentas**: Docker para containerização (se aplicável)

## Instalação

Para configurar o Inj3ctLab localmente, siga os passos abaixo:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seuusuario/Inj3ctLab.git
   ```
2. **Instale as dependências do back-end**:
   ```bash
   cd Inj3ctLab/backend
   pip install -r requirements.txt
   ```
3. **Instale as dependências do front-end**:
   ```bash
   cd ../frontend
   npm install
   ```
4. **Configure o banco de dados**:
   - Crie um banco de dados MySQL e ajuste as configurações no arquivo `config.py` no diretório `backend`.

5. **Inicie a aplicação**:
   - **Back-end**:
     ```bash
     cd ../backend
     python app.py
     ```
   - **Front-end**:
     ```bash
     cd ../frontend
     npm start
     ```

## Uso

Após a instalação, acesse a aplicação no navegador através de `http://localhost:3000`. Use a página de login para acessar e ajustar a dificuldade da vulnerabilidade, conforme necessário.

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir, siga as etapas abaixo:

1. Fork o repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`).
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`).
4. Envie para a branch (`git push origin feature/AmazingFeature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações ou dúvidas, entre em contato através do [LinkedIn](https://www.linkedin.com/in/933d13b9/).

---

Sinta-se à vontade para ajustar qualquer parte ou adicionar mais detalhes! Se precisar de algo específico ou tiver sugestões, é só falar.
