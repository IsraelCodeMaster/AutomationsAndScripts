#!/usr/bin/env bash

# Programando a hora para desligar a maquina
# Canal do Youtube: https://www.youtube.com/@israelalvespro

# Usando uma input para perguntar ao usuario qual horario do desligamento
read -p "Qual hora deseja desligar o notebook Israel? (HH:MM:SS): " resposta

# Verificar se a entrada está no formato correto
if ! [[ "$resposta" =~ ^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$ ]]; then
    echo "Formato de hora inválido. Use HH:MM:SS."
    exit 1
fi

# Loop enquanto for falso a resposta do usuário
while true; do 
    data=$(date +"%H:%M:%S")
    if [ "$data" = "$resposta" ]; then 
        echo "VOU DESLIGAR O NOTEBOOK EM 1 MINUTO"
        notify-send -u critical "Desligando em poucos segundos feche todos os serviços não salvos" "Hora de dormir Israel ('@_@')" 
        shutdown +2 
        break       
    else 
        echo "Hora Atual <=> $data | Desligar as: $resposta"
    fi   
    sleep 1
    clear
done
