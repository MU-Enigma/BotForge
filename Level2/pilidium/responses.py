from random import choice

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Ah, quam tacitus es! (Ah, how silent you are!)'
    
    elif lowered == 'private_default':
        return choice([
        'Audiens sum... (I am listening...)',
        'Secretum servatur. (The secret is kept.)',
        'Loquere, magus! (Speak, wizard!)',
        'Revelare possum... (I can reveal...)',
        'Quid quaeris? (What do you seek?)',
        'Arcana praeparata... (Mysteries are prepared...)',
        'Silentium servamus... (We keep silence...)',
        'Vocatus adsum! (Summoned, I am here!)',
        'Verbum tuum? (Your word?)',
        'Incipe secreta! (Begin the secrets!)'
        ])
    
    elif 'hello' in lowered or 'hi' in lowered or 'greetings' in lowered:
        return choice([
        'Salve, o magus! (Greetings, oh wizard!)',
        'Ave, magicae anima! (Hail, magical soul!)',
        'Salue, sapienti! (Greetings, wise one!)',
        'Velum tollo, et salutem tibi! (I lift the veil and greet you!)',
        'Benevenuti in mundum magicum! (Welcome to the magical realm!)',
        'Adsum, et paratus ad magica! (I am here, ready for magic!)',
        'In nomine magiae, salve! (In the name of magic, greetings!)'
        ])
    
    elif '!lace' in lowered:
        if "ignis flamma" in lowered:
            return "You summon a burst of fire! The flames dance in the air."
        elif "luminis radi" in lowered:
            return "A warm light glows, illuminating the darkness around you."
        elif "tempestas ventorum" in lowered:
            return "A powerful gust of wind surges forth, scattering leaves and dust."
        elif "aqua vitae" in lowered:
            return "A refreshing aura surrounds you, restoring your vitality."
        elif "umbra tenebris" in lowered:
            return "You vanish into shadows, becoming nearly invisible."
        elif "glacies vinculum" in lowered:
            return "A layer of frost spreads, freezing everything in its path."
        elif "veritas lux" in lowered:
            return "Hidden truths are revealed as light cuts through illusions."
        elif "aegis fortis" in lowered:
            return "A protective barrier of light surrounds you, blocking attacks."
        elif "somnum pacis" in lowered:
            return "A gentle wave of calm washes over, putting your target to sleep."
        elif "sagitta fulminis" in lowered:
            return "A bolt of lightning shoots from your hands, crackling with energy."
        elif "mendax obscura" in lowered:
            return "An illusion shimmers into existence, tricking those nearby."
        elif "cura tempus" in lowered:
            return "Time slows around you, allowing for quicker reactions."
        elif "clarus visus" in lowered:
            return "Your vision sharpens, allowing you to see hidden details."
        elif "vinco mortem" in lowered:
            return "Life flows back into the fallen, reviving them with new energy."
        elif "cor draconis" in lowered:
            return "You feel the strength of a dragon surge within you."
        elif "lux fortunam" in lowered:
            return "Fortune smiles upon you, favoring you in your next endeavor."
        elif "ferrum ligatum" in lowered:
            return "Invisible chains bind your target, restricting their movement."
        elif "natura floris" in lowered:
            return "Plants grow and bloom around you, creating a lush environment."
        elif "aura canticum" in lowered:
            return "A magical charm fills the air, making others more agreeable."
        elif "ignis sphaera" in lowered:
            return "A fiery sphere forms in your hands, ready to be launched."
        else:
            return "The spell you tried to cast fizzles out... It seems you spoke it incorrectly."

    else:
        return choice([choice([
        'Flibberjabberus',
        'Wobblegookus',
        'Noodlewinkus',
        'Zimblefloppus',
        'Bamboozlum',
        'Snickerfritzus',
        'Jibberjabberus',
        'Fuzzlewumpus',
        'Quizzlestickus',
        'Bibbity-bobbity-boo'
        ]) + '!', 'Nescio...']
        )
