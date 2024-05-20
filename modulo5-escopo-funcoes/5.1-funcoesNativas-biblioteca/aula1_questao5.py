import emoji

print ("Emojis disponíveis:")
print (emoji.emojize(':red_heart:  - red_heart'))
print (emoji.emojize(':thumbs_up:  - thumbs_up'))
print (emoji.emojize(':thinking_face:  - thinking_face'))
print (emoji.emojize(':partying_face:  - partying_face'))

red_heart = (emoji.emojize(':red_heart:'))
thumbs_up = (emoji.emojize(':thumbs_up:'))
thinking_face = (emoji.emojize(':thinking_face:'))
partying_face = (emoji.emojize(':partying_face:'))

frase = input(str("Digite uma frase e ela será emojizada: "))
emoji_escolhido = input(str("Qual emoji gostaria de usar (red_heart, thumbs_up, thinking_face ou partying_face? "))

if  emoji_escolhido == "red_heart":
    print (f'{frase} {red_heart}')
elif emoji_escolhido == "thumbs_up":
    print (f'{frase} {thumbs_up}')
elif emoji_escolhido == "thinking_face":
    print (f'{frase} {thinking_face}')
elif emoji_escolhido == "partying_face":
    print (f'{frase} {partying_face}')
