#!/usr/bin/bash

# Um script para monitorar a conexão de rede com a internet em caso de perda de conexao, tocar um alerta sonoro ao reestabelecer a conexão.
# Canal do Youtube: https://www.youtube.com/@israelalvespro

# Testando a conexão de rede 
ping -c 1 google.com.br

# Variavel para saber o status do comando anterior 0 or 1..2..3
status=$?
echo "#1 Codigo do status é:" $status

# Condição se status for == 0 parar o código por aqui mesmo
if [ $status -eq 0 ]; then 
     echo -e "\nIsrael sua conexão com a internet voltou. Você pode acessar a internet agora!!"
     echo "#2 Codigo do status é:" $status #status 0
     
fi

# Loop infinito para verificar o status enquanto ele for diferente de 0
while [ $status -ne 0 ]; do
  ping -c 1 google.com # novo comando ping dentro do loop para atualizar o valor do status
  status_02=$?
  
  # Criando uma condição para que se a saida for igual a 0 ele retorna Conexão de Internet
  if [ $status_02 -eq 0 ]; then 
     echo -e "\nIsrael sua conexão com a internet voltou. Você pode acessar a internet agora!!"
     echo "#2#2 Codigo do status é:" $status_02  # status code == 0
     while : ;  do 
     	echo -ne "\033[10;900]\a" 
     	sleep 0.1 
     	done
        #break
    
# Se o resultado da saido do ultimo comando gerar error status 2 emite msg de erro    
  else 
     echo -e '\nSem conexão de internet Israel!!'
     echo "#3 Codigo do status é:" $status_02 #status do codigo é 2
     sleep 5 #aguarde em segundos
  fi
done
#Israel Alves
