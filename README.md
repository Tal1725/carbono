# NEXO

Mensageiro privado com identidade por `@username`, sem número de telefone como identificador de contato.

## Identidade

Cada conta possui um identificador único no formato `@usuario`. Esse identificador é usado para encontrar e adicionar contatos.

O número de telefone não faz parte do cadastro nem é usado para descobrir contatos.

## Recuperação da conta

O objetivo do NEXO é permitir que uma pessoa perca ou troque o celular e continue com a mesma conta usando:

1. `@usuario`
2. senha da conta
3. uma chave de recuperação criptográfica criada na primeira configuração

A senha nunca será armazenada em texto puro e não será usada diretamente como chave de criptografia.

O histórico e as mídias serão armazenados como backup criptografado de ponta a ponta. O servidor deverá receber somente dados cifrados e os metadados mínimos necessários para autenticação, entrega e sincronização.

A recuperação deve liberar a chave de descriptografia somente no dispositivo autenticado. O servidor não terá uma cópia da chave privada em claro.

## Regra de segurança

`@usuario` identifica a conta, mas não é segredo. Quem tentar recuperar uma conta precisará provar conhecimento da credencial de autenticação e, para o histórico E2EE, possuir o material de recuperação necessário.

Isso evita o erro de tratar o `@usuario` como se fosse uma senha.

## Diferencial

- Sem número de telefone para cadastro ou contato.
- O mesmo `@usuario` permanece com o cliente quando ele troca de aparelho.
- Recuperação em novo celular.
- Mensagens e mídias com criptografia ponta a ponta.
- Backup criptografado para permitir recuperação sem transformar o servidor em leitor das conversas.
