alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha += alpha.upper()

def encrypt(key, text):
    new = ''
    for i in text:
        if i in alpha:
            new += alpha[(alpha.index(i) + key) % len(alpha)]
        else:
            new += i
    return new

def decrypt(key, text):
    new = ''
    for i in text:
        if i in alpha:
            new += alpha[(alpha.index(i) - key) % len(alpha)]
        else:
            new += i
    return new


def hack(text):
    counter = {}
    for i in text:
        if i in alpha:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
    most = max(counter.items(), key=lambda x: x[1])[0]
    key = alpha.index(most) - alpha.index('e')
    return decrypt(key, text)


def vernam_e(key, text):
    j = 0
    new = []
    for i in text:
        if j < len(key):
            new.append(ord(i) ^ ord(key[j]))
        else:
            j = 0
            new.append(ord(i) ^ ord(key[j]))
    return new

    
def vernam_d(key, text):
    j = 0
    new = []
    for i in text:
        if j < len(key):
            new.append(chr(i ^ ord(key[j])))
        else:
            j = 0
            new.append(chr(i ^ ord(key[j])))
    return ''.join(new)

    



e = encrypt(1, '''"Well, Prince, so Genoa and Lucca are now just family estates of the Buonapartes. But I warn you, if you don't tell me that this means war, if you still try to defend the infamies and horrors perpetrated by that Antichrist—I really believe he is Antichrist—I will have nothing more to do with you and you are no longer my friend, no longer my 'faithful slave,' as you call yourself! But how do you do? I see I have frightened you—sit down and tell me all the news."
It was in July, 1805, and the speaker was the well-known Anna Pavlovna Scherer, maid of honor and favorite of the Empress Marya Fedorovna. With these words she greeted Prince Vasili Kuragin, a man of high rank and importance, who was the first to arrive at her reception. Anna Pavlovna had had a cough for some days. She was, as she said, suffering from la grippe; grippe being then a new word in St. Petersburg, used only by the elite.
All her invitations without exception, written in French, and delivered by a scarlet-liveried footman that morning, ran as follows:
"If you have nothing better to do, Count (or Prince), and if the prospect of spending an evening with a poor invalid is not too terrible, I shall be very charmed to see you tonight between 7 and 10—Annette Scherer."
"Heavens! what a virulent attack!" replied the prince, not in the least disconcerted by this reception. He had just entered, wearing an embroidered court uniform, knee breeches, and shoes, and had stars on his breast and a serene expression on his flat face. He spoke in that refined French in which our grandfathers not only spoke but thought, and with the gentle, patronizing intonation natural to a man of importance who had grown old in society and at court. He went up to Anna Pavlovna, kissed her hand, presenting to her his bald, scented, and shining head, and complacently seated himself on the sofa.
"First of all, dear friend, tell me how you are. Set your friend's mind at rest," said he without altering his tone, beneath the politeness and affected sympathy of which indifference and even irony could be discerned.
"Can one be well while suffering morally? ''')
d = decrypt(1, e)
print(e)
print()
print(d)
print()
print(hack(e))
print()

e = vernam_e('vernam', 'Hello, world!')
print(e)
print(vernam_d('vernam', e))