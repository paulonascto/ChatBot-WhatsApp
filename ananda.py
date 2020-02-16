# IMPORTAR AS LIBS
import os
import time

#pip3 install --user pyYAML==5.1
#pip3 install chatterbot
#pip3 install chatterbot_corpus
#pip3 install Pillow
#pip3 install selenium

import wikipedia

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

#INSTANCIAR CHATBOT
chatbot = ChatBot('Ananda')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.portuguese')
trainerer = ListTrainer(chatbot)

# ARMAZENAR DIRETORIO PRINCIPAL EM VARIAVEL
dir_path = os.getcwd()

# INICIAR APLICAÇÃO
driver = webdriver.Chrome(dir_path+'/chromedriver') 
driver.get('https://web.whatsapp.com/')
#driver.implicitly_wait(15)

# FUNÇÕES BÁSICAS DE COMUNICAÇÃO
def pegaConversa():
	post = driver.find_elements_by_class_name("_12pGw")
	ultimo = len(post) - 1
	texto = post[ultimo].find_element_by_css_selector("span.selectable-text").text
	return texto

def enviaMensagem(mensagem):
    caixa_de_texto = driver.find_element_by_class_name('_3u328')
    valor = "*Ananda:* "+str(mensagem)
    for part in valor.split("\n"):
        caixa_de_texto.send_keys(part)
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).perform()
    time.sleep(0.5)
    botao_enviar = driver.find_element_by_class_name('_3M-N-')
    botao_enviar.click()

def treinar(mensagem):
	resposta = 'Como respondo isso? me ensina, por favor...? utilize ;"'+str(mensagem)+'"'
	enviaMensagem(resposta)
	novo = []
	try:
		while True:
			ultima = pegaConversa()
			if ultima == "!":
				enviaMensagem("Você desativou meu aprendizado.")
				break
			elif ultima.replace(';','') != '' and ultima != mensagem and ultima[0] == ";" :
				auxiliar = ultima
				print(mensagem.lower().strip())
				print(ultima.replace(';','').lower().strip())
				novo.append(mensagem.lower().strip())
				novo.append(ultima.replace(';','').lower().strip())
				trainerer.train(novo)
				enviaMensagem("Pronto, aprendi! Obrigada <3")
				break
	except:
		pass

# BLOCO PRINCIPAL DE EXECUÇÃO
lista_contatos = []
lista_contatos.append(1)
contato_contador = 0
i=0
while True:
	try:
		#conta_msg = driver.find_element_by_class_name('P6z4j').text
		#if int(conta_msg) > 0:
			#contato_contador = driver.find_element_by_class_name('_3NWy8')
			#conta_msg.click()
			#print(contato_contador.text)
		#try:
		#	conta_msg = driver.find_element_by_class_name('P6z4j')
		#	contato_contador = driver.find_element_by_class_name('_19RFN._1ovWX._F7Vk').text
		#	if contato_contador not in lista_contatos:
		#		lista_contatos.append(contato_contador)
		#	
		#	print(contato_contador)
		#	print(lista_contatos)
		#	time.sleep(5)
		#	conta_msg.click()
		#except:
			#pass  
		try:
			conta_msg = driver.find_element_by_class_name('P6z4j')
			time.sleep(3)
			conta_msg.click()
		except:
			pass

		if pegaConversa() != "" and pegaConversa()[:8] != "Ananda: " and pegaConversa().strip() != "!" and pegaConversa().strip() != ";" and pegaConversa().strip().lower()[:2] != "2" and pegaConversa().strip().lower()[:2] != "1" and pegaConversa().strip().lower() != "noticias" and pegaConversa().strip().lower() != "notícias" and pegaConversa().strip().lower() != "visão computacional" and pegaConversa().strip().lower() != "email":
			contato_contador = driver.find_element_by_class_name('_19RFN._1ovWX._F7Vk').text

			if contato_contador not in lista_contatos:
				enviaMensagem("Olá Tudo Bem ? Me Chamo Ananda e vou auxiliar você em seu atendimento. Digite a opção desejada: \n\n*[1]Acessar MENU*\n*[2]Fazer PEDIDO*\n*[3]Acompanhar PEDIDO*\n*[4]Falar com ATENDENTE*")
				lista_contatos.append(contato_contador)
				print(lista_contatos)
			#if contato_contador == lista_contatos[(len(lista_contatos)-1)]: # SEMPRE O ULTIMO A SER ADICIONADO NAO VAI TER RECEBIDO O CARDAPIO AINDA
			#	enviaMensagem("Olá Tudo Bem ? Me Chamo Ananda e vou auxiliar você em seu atendimento. Digite a opção desejada: \n\n*[1]Acessar MENU*\n*[2]Fazer PEDIDO*\n*[3]Acompanhar PEDIDO*\n*[4]Falar com ATENDENTE*")
			#else:
			#	pass

			# texto = str(pegaConversa().strip().lower())
			# response = chatbot.get_response(texto)
			# print(texto)
			# print(response)
			# if float(response.confidence) > 0.6:
			# 	enviaMensagem(response)

		elif pegaConversa().strip().lower()[:2] == "1":
			enviaMensagem("Ok, vamos lá! Qual é o seu NOME COMPLETO ?")
		elif pegaConversa().strip().lower()[:2] == "2":
			enviaMensagem("Ok, vamos lá! Qual é o seu NOME COMPLETO ?")
			time.sleep(15)
			nomeCliente = pegaConversa().strip().lower()
			enviaMensagem("Quantos hamburgueres serão?")
			time.sleep(15)
			qtdePedido = pegaConversa().strip().lower()
			for x in range(qtdePedido):
				print('TESTANDO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n\n\nTESTANDO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
				enviaMensagem("O ",x," º hambuguer será qual sabor?")
				sabor = pegaConversa()
				array_sabor.append(sabor)
		elif pegaConversa().strip().lower() == "email":
			try:
				email()
				enviaMensagem("Enviado!")
			except Exception as aiaiai:
				enviaMensagem("Agora não...")
				print(aiaiai)
				pass
		else:
			pass
	except Exception as ok:
		print(ok)
		pass  

		# if contato_contador == lista_contatos[(len(lista_contatos)-1)]: # SEMPRE O ULTIMO A SER ADICIONADO NAO VAI TER RECEBIDO O CARDAPIO AINDA
		# 	enviaMensagem("Olá Tudo Bem ? Me Chamo Ananda e vou auxiliar você em seu atendimento. Digite a opção desejada: \n\n*[1]Acessar MENU*\n*[2]Fazer PEDIDO*\n*[3]Acompanhar PEDIDO*\n*[4]Falar com ATENDENTE*")
		# 	i=1
		# 	time.sleep(5)
		# 	inicio = pegaConversa()
		# 	if inicio == 2:
		# 		time.sleep(1)
		# 		enviaMensagem("O que deseja?")
		# 		escolha = pegaConversa()
