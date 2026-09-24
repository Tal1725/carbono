# IA LIVRE

Projeto independente construído no repositório que antes hospedava o NEXO/Carbono. O PULSO permanece em seu próprio repositório e não é alterado por este projeto.

## O que já está aqui
- Interface PWA para conversar com Ollama local.
- Histórico da conversa na sessão do navegador.
- Configuração do endereço e modelo do Ollama.
- Área de criação de vídeos curtos preparada para um gerador local.
- Sem API paga obrigatória para o chat.

## Vídeo sem cobrança por geração
O código da interface não promete geração em nuvem ilimitada. Para manter o custo de uso em zero, o caminho é geração local. Um backend local pode expor POST /prompt e devolver { "video_url": "..." }. ComfyUI/Wan e outros modelos locais podem ocupar vários GB e dependem do hardware disponível.

## Publicação
O projeto é estático e pode ser publicado pelo GitHub Pages. O chat local precisa de acesso do navegador ao Ollama. Dependendo da configuração do Ollama, pode ser necessário permitir a origem da página.

## Próxima etapa técnica
Adicionar um backend local que inicialize/verifique Ollama e o pipeline de vídeo e exponha uma única API local para a interface.