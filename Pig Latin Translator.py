while 1 > 0:
    def pig_latin(message):
        new_message = "" 
        words = message.split()
        for word in words:
            result = "" 
            for i in range(1,len(word)):
                result += word[i]
            result += word[0] 
            result += "ay"
            new_message += result + " "
        return new_message

new_message = pig_latin(input("give a sentence to translate"))
print(new_message)
 