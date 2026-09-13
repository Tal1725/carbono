# Arquitetura inicial do NEXO

## Cliente

Android-first. A primeira versão será pensada para Android para permitir integração adequada com armazenamento seguro, notificações e chamadas.

## Backend

O servidor deve armazenar apenas o mínimo necessário para entregar mensagens e sincronizar estado. O conteúdo de mensagens não deve ser armazenado em texto puro pelo servidor.

## E2EE

Cada instalação terá identidade criptográfica própria. A arquitetura deverá separar identidade, chaves de sessão e conteúdo. O servidor funciona como transporte, não como leitor das conversas.

## Recursos diferenciadores planejados

### Cofre
Conversas e mídias privadas protegidas localmente por biometria/PIN.

### Mensagens com regras
O remetente pode definir expiração, visualização única e outras políticas suportadas pelo protocolo.

### @NEXO
Usuários podem ser encontrados por um identificador público sem expor o número de telefone.

### Inteligência local
Sempre que possível, recursos de organização e resumo serão executados no dispositivo para reduzir exposição de dados.

### Modo grupos inteligentes
Resumo de mensagens, enquetes, tarefas e eventos dentro do grupo.

## Não fazer

- Não criar algoritmo criptográfico próprio.
- Não colocar chaves privadas no servidor.
- Não registrar conteúdo de mensagens em logs.
- Não usar dados de conversa para publicidade.
