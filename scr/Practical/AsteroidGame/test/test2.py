import time

words = ["engineer", "slavery", "black", "behind", "poor", "entrance", "from", "native", "page", "steam", "eye", "familiar", "relation", "question", "inn", "fold", "lamp", "factory", "bush", "enjoy", "shelter", "thicken", "leather", "thorough", "bunch", "ahead", "square", "sharpen", "lesson", "effect", "brush", "round", "berry", "anger", "stiffen", "bottom", "golden", "thank", "join", "essence", "bill", "reward", "sugar", "suspect", "royalty", "feather", "block", "circle", "tempt", "employee", "pigeon", "laughter", "union", "street", "foot", "sick", "stripe", "pay", "save", "shut", "boast", "verse", "ago", "library", "garden", "forward", "pass", "lesson", "cushion", "insect", "proposal", "everyday", "dark", "sick", "deafen", "earn", "soft", "sheet", "mixture", "pleasant", "collect", "seize", "tighten", "title", "sleep", "fright", "rotten", "deal", "road", "cupboard", "against", "reflect", "bed", "dead", "destroy", "below", "slave", "rail", "heal", "fill", "succeed", "sharpen", "fault", "week", "dust", "bell", "tail", "bear", "live", "elder", "animal", "whom", "play", "milk", "into", "park", "rubber", "gaiety", "black", "grass", "these", "mix", "minute", "record", "way", "loyalty", "proper", "funeral", "anything", "clever", "row", "human", "sweet", "bake", "brown", "science", "bay", "pipe", "seat", "selfish", "language", "poor", "group", "smooth", "explode", "real", "insult", "ease", "main", "never", "hour", "lodge", "early", "decision", "shine", "tour", "garden", "another", "honor", "anyone", "bravery", "bath", "nation", "coal", "root", "union", "tin", "map", "empty", "night", "complete", "ruin", "manage", "calm", "vote", "cautious", "just", "most", "lodge", "able", "electric", "forth", "musician", "close", "expect", "flat", "duck", "system", "coin", "stuff", "mend", "about", "nowadays", "account", "sword", "subject", "worse", "monkey", "obey", "conquer", "shape", "spoon", "return", "fry", "rivalry", "scenery", "serious", "scratch", "trunk", "clear", "happy", "fill", "even", "cruel", "argue", "ready", "lately", "suit", "bay", "upon", "fur", "bus", "visitor", "quarrel", "sell", "remind", "instead", "defend", "away", "result", "widow", "accuse", "war", "sale", "sail", "failure", "field", "faith", "finger", "hello", "believe", "weave", "rain", "cautious", "match", "write", "loss", "bill", "pull", "ditch", "soldier", "toe", "jewel", "captain", "grand", "secrecy", "dig", "under", "thicken", "kingdom", "pleasure", "season", "feed", "grace", "sailor", "angry", "towel", "tray", "stick", "news", "quantity", "merry", "nest", "fine", "upright", "request", "scenery", "only", "about", "bitter", "guest", "run", "correct", "pot", "revenge", "take", "nursery", "dozen", "ever", "revenge", "cheese", "roast", "ring", "latter", "wire", "sight", "west", "choice", "beak", "whiten", "lodge", "mix", "dip", "day", "treasure", "live", "stock", "stiffen", "nowadays", "belief", "state", "terrible", "people", "female", "speak", "resist", "shape", "run", "wipe", "right", "punctual", "chest", "until", "meet", "every", "warn", "deafen", "poison", "king", "mankind", "wheat", "leave", "dog", "someone", "variety", "solve", "indeed", "use", "search", "student", "inn", "post", "soldier", "sea", "allow", "shame", "bundle", "split", "liberty", "once", "remember", "snake", "skill", "english", "hall", "push", "hang", "round", "affair", "prefer", "sharp", "permit", "favor", "fan", "soften", "union", "ago", "beard", "ancient", "dig", "door", "material", "person", "awake", "rapid", "unite", "golden", "awkward", "across", "rest", "sorrow", "least", "curse", "invent", "stuff", "regret", "advise", "sea", "flower", "weak", "sun", "kick", "noise", "bind", "past", "preserve", "business", "screen", "indoor", "limb", "force", "deliver", "grand", "council", "ill", "liquid", "calm", "busy", "merchant", "plow", "arrive", "build", "collar", "anyhow", "cave", "skin", "homework", "greet", "simple", "lately", "spirit", "they", "standard", "metal", "accord", "laughter", "field", "honesty", "union", "classify", "toe", "roll", "report", "gray", "taste", "election", "sow", "lead", "gun", "bright", "deliver", "pipe", "theater", "fly", "monkey", "bay", "proud", "side", "village", "mass", "against", "human", "shallow", "sharp", "asleep", "case", "current", "spread", "ahead", "engineer", "make", "hot", "board", "boil", "gap", "turn", "hatred", "flag", "former", "work", "tour", "wish", "oil", "perhaps", "youth", "whose", "thirst", "lean", "cover", "smoke", "grain", "FALSE", "blade", "draw", "sit", "proposal", "police", "pain", "woman", "kitchen", "where", "yellow", "never", "succeed", "neat", "type", "know", "exist", "cheat", "man", "without", "whip", "pad", "except", "anxiety", "disgust", "accuse", "landlord", "often", "loaf", "dry", "attempt", "damp", "behind", "public", "various", "shake", "ditch", "lack", "camp", "ounce", "rush", "justice", "fool", "recent", "sword", "limb", "behavior", "lump", "whatever", "reflect", "awake", "promise", "church", "decisive", "division", "plant", "precious", "offend", "admire", "rivalry", "fat", "approve", "fatten", "universe", "sing", "rubbish", "fork", "correct", "take", "ounce", "thirst", "pack", "strict", "army", "any", "well", "patient", "lovely", "heaven", "mad", "plow", "yellow", "sadden", "arrest", "loosen", "shoulder", "tighten", "try", "one", "mouth", "offer", "fit", "terrible", "less", "daughter", "see", "redden", "whip", "boat", "water", "extend", "public", "backward", "point", "mine", "tell", "about", "cent", "prepare", "relation", "father", "often", "college", "weed", "pleasant", "lose", "cent", "awake", "light", "explain", "lake", "speak", "arrange", "salary", "variety", "sort", "car", "puzzle", "cruel", "sow", "plate", "bring", "close", "clerk", "tell", "someone", "crash", "tie", "rot", "tooth", "direct", "deed", "rank", "hold", "should", "class", "soul", "than", "material", "birth", "patient", "throw", "amuse", "beat", "worship", "elephant", "history", "pay", "hand", "freeze", "active", "own", "motion", "middle", "various", "manner", "milk", "below", "dozen", "bundle", "mineral", "trick", "freeze", "human", "could", "language", "ambition", "lighten", "preserve", "pray", "count", "stone", "admit", "clock", "lazy", "village", "ton", "glad", "before", "hide", "per", "double", "laughter", "wander", "tap", "persuade", "merry", "package", "feast", "agency", "salt", "wait", "peace", "captain", "chain", "bed", "like", "anxious", "only", "daughter", "oppose", "excess", "bath", "tidy", "reach", "judge", "stem", "ribbon", "press", "clay", "criminal", "entire", "instead", "stone", "charm", "but", "horse", "lump", "line", "host", "empty", "sew", "smooth", "caution", "frighten", "confuse", "bribe", "proper", "suggest", "network", "blind", "each", "soup", "particle", "work", "freeze", "yield", "diamond", "may", "market", "rain", "mountain", "quarrel", "poet", "sword", "sad", "down", "inward", "grind", "shoulder", "star", "lie", "bare", "base", "but", "business", "fever", "woman", "pigeon", "circle", "they", "shelter", "line", "spin", "modesty", "too", "poet", "bit", "sweat", "settle", "lean", "complete", "settle", "worm", "mass", "fortune", "prefer", "scarce", "last", "date", "coat", "nothing", "chalk", "depend", "more", "noun", "horizon", "foot", "size", "nice", "worm", "landlord", "office", "study", "problem", "allow", "dear", "advance", "crown", "sour", "flash", "ladder", "strong", "delight", "mile", "dear", "heap", "apply", "few", "loosen", "amongst", "swell", "deer", "why", "ride", "class", "again", "offer", "tear", "thirst", "plant", "amuse", "obey", "review", "sell", "dirt", "affair", "although", "deserve", "distance", "stir", "enclose", "whatever", "sign", "omission", "rough", "pile", "pattern", "river", "content", "minute", "fail", "absence", "electric", "say", "learn", "saddle", "violent", "pause", "sentence", "laughter", "network", "lamp", "tonight", "art", "tailor", "slow", "measure", "divide", "burst", "cover", "lift", "smile", "month", "election", "sign", "duck", "brush", "top", "neat", "balance", "sock", "follow", "feed", "gay", "republic", "because", "whole", "monkey", "neat", "half", "observe", "modesty", "hunger", "merchant", "fault", "remark", "jealous", "unless", "consider", "bowl", "victory", "splendid", "belong", "fate", "black", "taste", "push", "blood", "review", "member", "minister", "oil", "fit", "nation", "proper", "own", "bribe", "people", "hide", "steady", "force", "strong", "engineer", "address", "sky", "lid", "open", "party", "speak", "command", "idle", "one", "attempt", "hollow", "forward", "fade", "here", "deaf", "the", "shorten", "pretend", "but", "copper", "log", "float", "golden", "shelf", "curtain", "barrel", "property", "fun", "favorite", "law", "float", "heart", "shame", "behind", "free", "glass", "crop", "happy", "mind", "musician", "during", "whatever", "want", "scold", "joint", "discuss", "ceremony", "reason", "possess", "indoor", "delivery", "heat", "sailor", "self", "proposal", "advance", "bow", "destroy", "likely", "station", "gentle", "ordinary", "change", "smell", "letter", "skirt", "glad", "color", "surround", "parcel", "visit", "watch", "thing", "cow", "smoke", "salt", "woman", "neighbor", "butter", "home", "solid", "revenge", "believe", "headache", "never", "district", "window", "large", "claim", "secret", "forgive", "secrecy", "swear", "depth", "spit", "treat", "bush", "should", "noise", "she", "this", "guest", "latter", "escape", "bargain", "arrow", "awake", "pocket", "barrel", "put", "friend", "chair", "pigeon", "cattle", "annoy", "comb", "extend", "prefer", "bean", "more", "deaf", "hope", "exchange", "complain", "south", "lot", "which", "shape", "steady", "soul", "former", "airplane", "shoulder", "beat", "post", "delicate", "among", "together", "attempt", "sale", "fur", "there", "handle", "absent", "rank", "avenue", "belt", "bad", "arrange", "ground", "milk", "stage", "shut", "prison", "pupil", "wish", "prompt", "same", "position", "take", "heal", "seat", "remedy", "water", "sample", "clever", "safety", "deep", "calm", "change", "dig", "darken", "guess", "soap", "moreover", "car", "diamond", "company", "dinner", "tongue", "appear", "arm", "beyond", "near", "passage", "heaven", "ocean", "safe", "instant", "avenue", "oil", "which", "bake", "divide", "retire", "each", "most", "spot", "cheer", "still", "science", "receive", "stair", "mention", "waste", "today", "merry", "dress", "bad", "preach", "saucer", "harden", "enjoy", "perform", "great", "nose", "affair", "wicked", "disease", "soil", "pile", "threat", "polite", "shelf", "page", "god", "neglect", "second", "screw", "pastry", "slip", "cousin", "fish", "night", "story", "being", "liar", "yard", "spare", "outside", "poet", "type", "govern", "meat", "weed", "yield", "exercise", "visitor", "equal", "possess", "coward", "work", "event", "bay", "steam", "carry", "weather", "angle", "unit", "yes", "educate", "page", "cruel", "calm", "city", "mother", "grind", "size", "wooden", "raw", "sing", "permit", "customer", "tin", "small", "hang", "mean", "kind", "money", "voyage", "sense", "step", "customer", "loyal", "peculiar", "rust", "fire", "less", "camera", "general", "air", "ornament", "night", "soften", "leather", "kitchen", "cure", "employ", "office", "widen", "top", "alike", "wax", "recent", "eat", "and", "include", "latter", "motion", "account", "few", "raise", "ton", "poor", "you", "great", "trial", "call", "drive", "enemy", "pad", "club", "tidy", "double", "pint", "increase", "hasten", "lake", "own", "society", "deserve", "smoke", "leaf", "maybe", "repair", "fear", "advice", "plenty", "without", "lend", "anyone", "wood", "wipe", "dinner", "wild", "heap", "home", "kind", "chance", "tame", "pan", "own", "delivery", "spend", "god", "fate", "stem", "mother", "glass", "bath", "paste", "tailor", "enjoy", "guest", "mad", "relative", "lung", "future", "sorry", "whip", "arrive", "overflow", "mill", "rule", "extreme", "taxi", "spring", "coarse", "anywhere", "size", "sand", "equal", "roof", "maybe", "radio", "boat", "repair", "basket", "pound", "depend", "salt", "product", "polish", "cupboard", "special", "big", "well", "govern", "view", "hold", "wave", "proposal", "love", "shore", "start", "decrease", "wound", "regard", "read", "border", "which", "join", "salesman", "give", "flavor", "stiffen", "main", "result", "detail", "cat", "power", "woolen", "motherly", "board", "notebook", "criminal", "tip", "dozen", "edge", "cake", "temple", "old", "chance", "gate", "arrest", "escape", "eastern", "master", "applause", "bring", "action", "self", "speed", "confess", "pair", "live", "urgent", "anyhow", "lot", "modesty", "rub", "throw", "universe", "bit", "here", "often", "pick", "print", "bright", "enclose", "citizen", "quarrel", "threat", "drive", "leaf", "wait", "politics", "fast", "preach", "than", "attack", "apply", "brown", "sister", "host", "walk", "capital", "please", "rank", "dream", "behavior", "lesson", "pardon", "those", "sick", "grave", "weapon", "oar", "taste", "shade", "nor", "camp", "content", "verse", "harden", "tender", "few", "still", "cold", "month", "letter", "self", "bucket", "city", "bundle", "hotel", "jump", "soup", "reduce", "spend", "plant", "have", "add", "fish", "cry", "dull", "sake", "above", "accustom", "disagree", "slave", "brave", "smoke", "busy", "trunk", "pale", "curtain", "fine", "occasion", "beg", "yard", "bicycle", "luck", "examine", "coast", "ambition", "stay", "stupid", "camera", "sort", "post", "skin", "tight", "pass", "pupil", "space", "agency", "expect", "quiet", "kind", "wife", "battle", "preach", "nature", "silence", "accident", "wet", "grease", "tidy", "nation", "scorn", "what", "combine", "deed", "actress", "roar", "neighbor", "slave", "guilt", "descend", "urgent", "gay", "complete", "diamond", "loud", "trunk", "decision", "beauty", "secrecy", "sight", "mile", "memory", "lovely", "hello", "branch", "direct", "bathe", "good", "commerce", "world", "set", "age", "whisper", "barber", "fair", "seldom", "anyone", "steel", "wonder", "sight", "desk", "amongst", "let", "neck", "employ", "merchant", "property", "lead", "thunder", "union", "confess", "yield", "agency", "chicken", "snake", "excess", "mat", "defense", "amongst", "conquest", "strong", "mile", "inquiry", "cool", "yes", "serious", "indeed", "ahead", "delay", "desk", "hospital", "division", "duck", "decision", "canal", "hot", "unit", "among", "death", "corn", "fire", "speed", "astonish", "relation", "mineral", "bad", "deer", "elder", "dry", "woolen", "greed", "bunch", "right", "deaf", "lay", "coffee", "idle", "have", "meet", "bean", "praise", "wax", "dead", "grand", "drop", "nurse", "sister", "feather", "royal", "anger", "wherever", "day", "left", "anyone", "brass", "hand", "instead", "calm", "tube", "seldom", "last", "earn", "city", "speed", "believe", "many", "fright", "finish", "marriage", "north", "defense", "common", "sad", "various", "command", "figure", "current", "fun", "arrow", "club", "enjoy", "whom", "neither", "great", "rust", "describe", "upon", "worship", "lock", "western", "winter", "drag", "excuse", "pity", "hit", "even", "hot", "fruit", "struggle", "bush", "trunk", "news", "young", "comb", "speak", "button", "drive", "spoon", "skirt", "drown", "music", "whom", "deep", "empire", "lump", "needle", "upon", "she", "loss", "mouse", "brush", "yet", "reflect", "meat", "build", "number", "sure", "headache", "deceit", "stove", "round", "basic", "complete", "multiply", "tighten", "shallow", "ordinary", "sell", "distance", "calm", "realize", "bridge", "justice", "drown", "path", "wide", "nature", "kind", "ability", "future", "mine", "official", "pretense", "staff", "outline", "brown", "block", "tray", "practice", "journey", "music", "simple", "egg", "thin", "stuff", "water", "private", "blow", "lamp", "rival", "scenery", "alone", "war", "neat", "airplane", "ugly", "slow", "blue", "slow", "dust", "morning", "throw", "guess", "bone", "cent", "horizon", "desk", "sorry", "proud", "rust", "everyone", "then", "fame", "whole", "freedom", "pain", "people", "seldom", "stove", "during", "want", "straw", "know", "pretense", "life", "for", "help", "kiss", "heighten", "shave", "remedy", "think", "event", "think", "tool", "straw", "none", "meantime", "baby", "request", "wander", "jealousy", "liar", "whole", "great", "land", "seed", "material", "mere", "garage", "line", "idle", "weather", "rotten", "fresh", "intend", "that", "mad", "part", "madden", "joke", "just", "profit", "pale", "hasten", "offer", "village", "law", "scene", "stop", "dig", "feel", "ease", "cover", "realize", "barrel", "peace", "horizon", "drive", "but", "refer", "coward", "inward", "hole", "dismiss", "selfish", "snake", "product", "season", "dear", "scorn", "reflect", "alike", "perform", "master", "earn", "scatter", "farm", "sad", "boundary", "hammer", "single", "offer", "pen", "wave", "leaf", "widower", "anybody", "hair", "medicine", "arise", "nice", "hospital", "rate", "loss", "lawyer", "alone", "soften", "cost", "scenery", "explain", "inn", "return", "flower", "fasten", "murder", "crime", "fright", "include", "wild", "against", "shower", "sad", "cap", "explore", "tighten", "union", "overflow", "history", "bake", "advice", "avenue", "strike", "perform", "tire", "listen", "forgive", "class", "cure", "merchant", "autumn", "calm", "rubbish", "develop", "deed", "child", "pain", "return", "teach", "joke", "govern", "noise", "pretend", "dance", "rug", "busy", "early", "worry", "depend", "humble", "standard", "account", "fast", "night", "century", "sand", "sew", "need", "pleasant", "news", "pad", "width", "chalk", "baggage", "dine", "ribbon", "signal", "send", "bell", "get", "hall", "purpose", "smell", "peculiar", "ambition", "bus", "insure", "qualify", "time", "many", "expect", "reflect", "begin", "slope", "rapid", "creep", "marry", "limb", "weekday", "bit", "month", "subject", "consider", "low", "confuse", "firm", "sink", "bite", "sow", "exercise", "weather", "gradual", "curious", "cousin", "omission", "business", "push", "cross", "love", "baggage", "rejoice", "reward", "shell", "host", "oppose", "begin", "someone", "mountain", "handle", "week", "civilize", "pigeon", "age", "taste", "let", "election", "good", "spirit", "wipe", "dust", "worse", "safety", "mouse", "short", "soon", "order", "freeze", "carry", "have", "could", "faith", "surround", "material", "song", "shadow", "industry", "weaken", "priest", "cook", "smell", "seed", "origin", "several", "chicken", "crowd", "officer", "descent", "leaf", "defense", "rule", "rubbish", "race", "today", "quantity", "motion", "event", "wicked", "off", "cattle", "good", "why", "big", "tube", "swell", "weather"]

sentences = []
sentence = []

start = time.time()

for index in range(1, len(words) - 11):
    k = 0
    for f in range(index, len(words) - 11):
        sentence.append(words[index - 1])
        for i in range(k, k + 11):
            sentence.append(words[i + index])
        sentences.append(sentence)
        sentence = []
        k += 1

print(f"Time: {time.time() - start}s")
print(f"Word count: {len(sentences[1])}")
print(f"Total: {len(sentences)}")
