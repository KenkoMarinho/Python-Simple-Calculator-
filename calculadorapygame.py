import pygame
def main():
    #definindo cores:
    cor_branca=(255,255,255)
    cor_azul=(0,0,255)
    cor_verde=(0,128,0)
    cor_preto=(0,0,0) 
    cor_vermelho=(255,0,0)

    #declarando a fonte
    pygame.font.init()
    fontearial=pygame.font.SysFont('Arial', 40)

    #Definições Dos Objetos(variaveis):
    pygame.init()                                   #inicia a classe pygame
    tela=pygame.display.set_mode([370,480])         #define o tamanho da tela
    pygame.display.set_caption("Calculadaora") #titulo da janela
    relogio=pygame.time.Clock()                     #controle de frames
    superficie=pygame.Surface((370,480))            #cria uma superficie de 200x200, mas não a mostra na tela
    superficie.fill(cor_preto)                      #muda a cor da superficie
    visor=pygame.Rect(10,10,350,100)
    numero1=pygame.Rect(10,120,80,80)
    numero2=pygame.Rect(100,120,80,80)
    numero3=pygame.Rect(190,120,80,80)
    numero4=pygame.Rect(10,210,80,80)
    numero5=pygame.Rect(100,210,80,80)
    numero6=pygame.Rect(190,210,80,80)
    numero7=pygame.Rect(10,300,80,80)
    numero8=pygame.Rect(100,300,80,80)
    numero9=pygame.Rect(190,300,80,80)
    numero0=pygame.Rect(100,390,80,80)
    soma=pygame.Rect(10,390,80,80)
    multiplicação=pygame.Rect(280,210,80,80)
    divisão=pygame.Rect(280,120,80,80)
    subtracao=pygame.Rect(190,390,80,80)
    limpar=pygame.Rect(280,300,80,80)
    resultado=pygame.Rect(280,390,80,80)
    cursor=pygame.Rect(1,1,1,1)
    
    numerox=""
    numeroy=""
    operacao=""
    operador=""
    resultadooperacao=""
    aux1=""
    aux2=""
    #condições de loopings:
    sair=False

    tela.fill(cor_branca)           #preenche o fundo da tela com uma cor em hexadecimal
    
    while sair==False:                                  #resumidamente, mantem a janela aberta enquanto o looping se manter.
        (cursor.left,cursor.top)=pygame.mouse.get_pos() # define a localização do cursor pra onde o mouse for
        for event in pygame.event.get():                #busca qual evento está acontecendo na tela
            if event.type == pygame.QUIT:               #se o evento for o usuario clicando no X para fechar
                sair=True                               #seta sair para  True, dando fim ao looping e executando pygame.quit.
            if event.type == pygame.MOUSEBUTTONDOWN:    #detecta click do mouse
                if cursor.colliderect(numero1):
                    if operacao=="":
                        numerox+="1"
                    else:
                        numeroy+="1"
                if cursor.colliderect(numero2):
                    if operacao=="":
                        numerox+="2"
                    else:
                        numeroy+="2"
                if cursor.colliderect(numero3):
                    if operacao=="":
                        numerox+="3"
                    else:
                        numeroy+="4"
                if cursor.colliderect(numero4):
                    if operacao=="":
                        numerox+="4"
                    else:
                        numeroy+="4"
                if cursor.colliderect(numero5):
                    if operacao=="":
                        numerox+="5"
                    else:
                        numeroy+="5"
                if cursor.colliderect(numero6):
                    if operacao=="":
                        numerox+="6"
                    else:
                        numeroy+="6"
                if cursor.colliderect(numero7):
                    if operacao=="":
                        numerox+="7"
                    else:
                        numeroy+="7"
                if cursor.colliderect(numero8):
                    if operacao=="":
                        numerox+="8"
                    else:
                        numeroy+="8"
                if cursor.colliderect(numero9):
                    if operacao=="":
                        numerox+="9"
                    else:
                        numeroy+="9"
                if cursor.colliderect(numero0):
                    if operacao=="":
                        numerox+="0"
                    else:
                        numeroy+="0"
                if cursor.colliderect(soma):
                    operador="+"
                    operacao="soma"
                if cursor.colliderect(multiplicação):
                    operador="*"
                    operacao="multiplicação"
                if cursor.colliderect(subtracao):
                    operador="-"
                    operacao="subtração"
                if cursor.colliderect(divisão):
                    operador="/"
                    operacao="divisão"
                if cursor.colliderect(limpar):
                    numerox=""
                    numeroy=""
                    operacao=""
                    operador=""
                    resultadooperacao=""
                    visor=pygame.draw.rect(tela,cor_branca,visor)
                if cursor.colliderect(resultado):
                    if numeroy=="":
                        numeroy="0"
                    if operacao=="":
                        operacao="soma"
                        operador="+"
                    if numerox=="":
                        numerox="0"
                    if operacao=="soma":
                        resultadooperacao=str(int(numerox)+int(numeroy))
                    if operacao=="subtração":
                        resultadooperacao=str(int(numerox)-int(numeroy))
                    if operacao=="multiplicação":
                        resultadooperacao=str(int(numerox)*int(numeroy))
                    if operacao=="divisão":
                        resultadooperacao=str(int(numerox)/int(numeroy))
                

        relogio.tick(30)
        #print("X:",retangulo.left,"Y:",retangulo.top)      #configuração da taxa de frames por segundo
        tela.blit(superficie,[0,0])                           #instancia a superficie de 200x200 na tela na posicao 10(x) e 10(y) respectivamente



        visor=pygame.draw.rect(tela,cor_branca,visor)
        numero1=pygame.draw.rect(tela,cor_verde,numero1)
        numero2=pygame.draw.rect(tela,cor_verde,numero2)
        numero3=pygame.draw.rect(tela,cor_verde,numero3)
        numero4=pygame.draw.rect(tela,cor_verde,numero4)
        numero5=pygame.draw.rect(tela,cor_verde,numero5)
        numero6=pygame.draw.rect(tela,cor_verde,numero6)
        numero7=pygame.draw.rect(tela,cor_verde,numero7)
        numero8=pygame.draw.rect(tela,cor_verde,numero8)
        numero9=pygame.draw.rect(tela,cor_verde,numero9)
        show0=pygame.draw.rect(tela,cor_verde,numero0)
        soma=pygame.draw.rect(tela,cor_vermelho,soma)
        multiplicação=pygame.draw.rect(tela,cor_vermelho,multiplicação)
        subtracao=pygame.draw.rect(tela,cor_vermelho,subtracao)
        divisão=pygame.draw.rect(tela,cor_vermelho,divisão)
        limpar=pygame.draw.rect(tela,cor_azul,limpar)
        resultado=pygame.draw.rect(tela,cor_azul,resultado)
        cursor=pygame.draw.rect(tela,cor_branca,cursor)

        show1=fontearial.render('1',1,cor_branca)
        show2=fontearial.render('2',1,cor_branca)
        show3=fontearial.render('3',1,cor_branca)
        show4=fontearial.render('4',1,cor_branca)
        show5=fontearial.render('5',1,cor_branca)
        show6=fontearial.render('6',1,cor_branca)
        show7=fontearial.render('7',1,cor_branca)
        show8=fontearial.render('8',1,cor_branca)
        show9=fontearial.render('9',1,cor_branca)
        show0=fontearial.render("0",1,cor_branca)
        showplus=fontearial.render('+',1,cor_branca)
        showminus=fontearial.render('-',1,cor_branca)
        showmultiply=fontearial.render('*',1,cor_branca)
        showresult=fontearial.render('=',1,cor_branca)
        showdivisao=fontearial.render("/",1,cor_branca)
        showclear=fontearial.render("CE",1,cor_branca)
        resultadotela=fontearial.render(resultadooperacao,1,cor_preto)
        igualtela=fontearial.render("=",1,cor_preto)
        operadortela=fontearial.render(operador,1,cor_preto)
        tela.blit(show1,(40,140))
        tela.blit(show2,(130,140))
        tela.blit(show3,(220,140))
        tela.blit(show4,(40,230))
        tela.blit(show5,(130,230))
        tela.blit(show6,(220,230))
        tela.blit(show7,(40,320))
        tela.blit(show8,(130,320))
        tela.blit(show9,(220,320))
        tela.blit(show0,(130,410))
        tela.blit(showplus,(40,410))
        tela.blit(showminus,(220,410))
        tela.blit(showmultiply,(310,230))
        tela.blit(showresult,(310,410))
        tela.blit(showdivisao,(315,140))
        tela.blit(showclear,(295,320))
        
        tela.blit(resultadotela,(240,40))
        if resultadooperacao!="":
            tela.blit(igualtela,(220,40))
        if operador!="":
            tela.blit(operadortela,(110,40))
        if numeroy!="":
            aux1=fontearial.render(str(numeroy),1,cor_preto)
            tela.blit(aux1,(130,40))
        if numerox!="":
            aux2=fontearial.render(str(numerox),1,cor_preto)
            tela.blit(aux2,(20,40))
        pygame.display.update()                                 #atualiza o display com novos eventos ao fim do ciclo

        
    pygame.quit()           #o programa se fecha já que pygame.quit() fecha a janela.

main()
