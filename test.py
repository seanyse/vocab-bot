questionData = "reclusive,repetitive,symmetrical,cooperative,antisocial"
answerData = 'The adjective reclusive describes a desire for seclusion or privacy. A reclusive movie star is the one tabloid photographers dream of capturing on film.:The root word of reclusive is recluse, which came from the Old French word reclus, originally meaning "a person shut up from the world for purposes of religious meditation." Today, maybe you just want to be alone — reclusive describes a person who is withdrawn from society or seeks solitude, like a hermit. Grocery shopping late at night is a reclusive habit, because few people are in the store then.:indrawn, introverted, nongregarious, recessive, reserved, unsocial, withdrawn aloof, antisocial, asocial, buttoned-up, cold, cold-eyed, cool, detached, distant, dry, frosty, offish, remote, standoff, standoffish, unbending, unclubbable, unsociable misanthropic apathetic, hard, indifferent, unconcerned clinical, dispassionate, impersonal, professional disinterested, incurious, uninterested reticent, silent, taciturn, uncommunicative diffident, shy, timid cliquey, cliquish, clubbish boon, clubbable (alsoclubable), clubby, companionable, convivial, extroverted (alsoextraverted), gregarious, outgoing (alsoclubable), clubby, companionable, convivial, extroverted (alsoextraverted), gregarious, outgoing (alsoextraverted), gregarious, outgoing communicative, expansive, garrulous, talkative affable, folksy, genial, gracious, hospitable agreeable, amiable, congenial, kindly, neighborly cordial, friendly, sociable, social, warm'

questionData = questionData.split(",")

question_1 = questionData[1].split(" ")
question_2 = questionData[2].split(" ")
question_3 = questionData[3].split(" ")
question_4 = questionData[4].split(" ")

num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0

for x in range(0, len(question_1)):
    if question_1[x] in answerData: 
        num_1+=1
        
for x in range(0, len(question_2)):
    if question_2[x] in answerData: 
        num_2+=1

for x in range(0, len(question_3)):
    if question_3[x] in answerData: 
        num_3+=1

for x in range(0, len(question_4)):
    if question_4[x] in answerData: 
        num_4+=1


print(num_1)
print(num_2)
print(num_3)
print(num_4)