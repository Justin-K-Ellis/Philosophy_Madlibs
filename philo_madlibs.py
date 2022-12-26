def republic():
    past_verb1 = input("Give me a past-tense verb: ")
    noun1 = input("Give me a noun: ")
    noun2 = input("Give me another noun: ")
    verb1 = input("Give me a present-tense verb: ")
    adj1 = input("Give me an adjective: ")
    past_verb2 = input("Give me another past-tense verb: ")
    noun3 = input("Give me another noun: ")
    cont_verb = input("Give me a continuous (-ing) verb: ")
    cloth_or_body = input("Give me an article of clothing (or body part): ")
    verb2 = input("Last, give me one more present-tense verb: ")

    republic_intro = f"""
    I {past_verb1} yesterday to the Piraeus with Glaucon the {noun1} of Ariston, 
    that I might offer up my prayers to the {noun2}; and also because I wanted to see in what 
    manner they would {verb1} the festival, which was a new thing. I was delighted with the 
    procession of the inhabitants; but that of the Thracians was equally, if not more, {adj1}. 
    When we had {past_verb2} our prayers and viewed the spectacle, we turned in the direction of the city; 
    and at that instant Polemarchus the {noun3} of Cephalus chanced to catch sight of us from a distance as 
    we were {cont_verb}, and told his servant to run and bid us wait for him. The servant 
    took hold of me by the {cloth_or_body}, and said: Polemarchus desires you to {verb2}.\nPlato, Republic\n"""

    print(republic_intro)

def metaphysics():
    noun1 = input("Give me a plural noun: ")
    verb1 = input("Give me a verb: ")
    noun2 = input("Give me another plural noun: ")
    noun3 = input("And another plural noun, please: ")
    past_verb1 = input("Now give me a past-tense verb: ")
    body_part = input("Now give me a body part: ")
    verb3 = input("Now give me another present-tense verb: ")
    noun4 = input("Last plural noun, I swear: ")
    verb4 = input("Last, one more present-tense verb: ")

    metaphysics_intro = f"""
    All {noun1} by nature desired to {verb1}. An indication of this is our liking for {noun2}.
    For even apart from their {noun3}, these are {past_verb1} because of themselves--and most of all because of the 
    {body_part}. For it is not only in order to {verb3} an action, but even when we are not going to do anything
    whatsoever, that we choose {noun4} over (one might almost say) all the others. The cause of this is that of all
    {noun1} it enables us to {verb4} most fully and makes clear many difficulties.\nAristotle, Metaphysics\n"""

    print(metaphysics_intro)

def mediations():
    pass

def enquiry():
    noun1 = input("Give me a noun: ")
    adj1 = input("Give me an adjective: ")
    noun2 = input("Give me another noun: ")
    adv1 = input("Give me an adverb: ")
    verb1 = input("Give me a present-tense verb: ")
    verb2 = input("Give me another present-tense verb: ")
    adj2 = input("Give me another adjective: ")
    ing_verb1 = input("Give me a continuous (-ing) verb: ")
    noun3 = input("Last, give me a plural noun: ")

    enquiry_intro = f"""
    Moral philosophy, or the science of {noun1}, may be treated after two different manners; 
    each of which has its {adj1} merit, and may contribute to the entertainment, instruction, and {noun2} of 
    mankind. The one considers man {adv1} as born for action; and as influenced in his measures by taste and sentiment; 
    pursuing one object, and avoiding another, according to the value which these objects seem to {verb1}, and according 
    to the light in which they {verb2} themselves. As virtue, of all objects, is allowed to be the most {adj2}, this 
    species of philosophers paint her in the most amiable colours; {ing_verb1} all helps from poetry and eloquence, and 
    treating their subject in an easy and obvious manner, and such as is best fitted to please the imagination, and 
    engage the {noun3}.\n"""

    print(enquiry_intro)

def tractatus():
    pass

def main():
    while True:
        print("Welcome to Philosophy Madlibs, where you can customize the opening words of great philosophical works.")
        choice = input("Choose one of the following numbers (enter 'q' to quit):\n1 for Plato\n2 for Aristotle\n3 for Descartes\n4 for Hume\n5 for Wittgenstein\n")
        choice = choice.lower()
        if choice == "q" or choice == "quit":
            print("Goodbye.")
            break
        elif choice == "1":
            republic()
        elif choice == "2":
            metaphysics()
        elif choice == "3":
            mediations()
        elif choice == "4":
            enquiry()
        elif choice == "5":
            tractatus()
        else:
            print("Try again.")

main()