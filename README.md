# SEL0337

## Resumo do funcionamento do projeto da Prática 5

A prática descrita visa configurar um sistema de inicialização automática de uma aplicação Python em um sistema embarcado com Linux, utilizando a unidade de serviço `systemd`. O objetivo é garantir que o programa (como um script Python) seja iniciado automaticamente durante o processo de boot, sem a necessidade de intervenção manual após a inicialização do sistema operacional.

A configuração envolve a criação de uma **unidade de serviço personalizada** [```colorblink.service```](https://github.com/fujiska/SEL0337/blob/main/colorblink.service) para gerenciar o processo de inicialização e execução do projeto. A unidade de serviço descreve como o sistema deve iniciar, parar e gerenciar o script Python. No caso dessa prática, um serviço foi configurado para iniciar o script [```colorblink.py```](https://github.com/fujiska/SEL0337/blob/main/colorblink.py) (um programa que faz transições de cores com LEDs RGB) e, quando o serviço for interrompido (via `systemctl stop`), o script [```buzzlightyear.py```](https://github.com/fujiska/SEL0337/blob/main/buzzlightyear.py) (que ativa um buzzer) será executado.

O `systemd` é o sistema de inicialização moderno utilizado no Linux, responsável por gerenciar a inicialização de serviços e processos. A prática envolve a criação de um arquivo de configuração de serviço (`colorblink.service`) que especifica as seguintes ações:

1. **Execução do Script Python:**
   - `ExecStart` define que, ao iniciar o serviço, o script [```colorblink.py```](https://github.com/fujiska/SEL0337/blob/main/colorblink.py) será executado usando o interpretador Python 3.
   - `ExecStop` define que, ao parar o serviço, o script [```buzzlightyear.py```](https://github.com/fujiska/SEL0337/blob/main/buzzlightyear.py) será executado, ativando o buzzer.

2. **Configuração do Sistema:**
   - O serviço é configurado para ser iniciado após o estágio `multi-user.target`, ou seja, após a inicialização de serviços essenciais.
   - A unidade de serviço é associada ao **multi-user.target** no momento da instalação, permitindo que o serviço seja iniciado automaticamente durante o boot.

O processo facilita a execução de aplicações em sistemas embarcados, garantindo que elas sejam iniciadas automaticamente após o boot, sem a necessidade de interação manual com o sistema operacional.

Como resultado do projeto, observa-se a imagem e o vídeo abaixo, que representam o funcionamento do serviço de inicialização acima.

<img src="midia/20241125_170002.jpg" width="432"/> 
![](https://github.com/fujiska/SEL0337/raw/refs/heads/main/midia/20241125_172305%20(online-video-cutter.com).mov)


O histórico de commits git realizados no terminal durante a aula está presente no arquivo [```historico_git.txt```](https://github.com/fujiska/SEL0337/blob/main/historico_git.txt).
