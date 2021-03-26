from django.db import models

class Spells(models.Model):
	name = models.CharField(max_length=20)
	
	# ACID_SPLASH = 'acid splash'
    # BLADE_WARD = 'blade ward'
    # CHILL_TOUCH = 'chill touch'
    # DANCING_LIGHTS = 'dancing lights'
    # FIRE_BOLT = 'fire bolt'
    # FRIENDS = 'friends'
    # LIGHT = 'light'
    # MAGE_HAND = 'mage hand'
    # MENDING = 'mending'
    # MESSAGE = 'message'
    # MINOR_ILLUSION = 'minor illusion'
    # POISON_SPRAY = 'poison spray'
    # PRESTIDIGITATION = 'prestidigitation'
    # RAY_OF_FROST = 'ray of frost'
    # SHOCKING_GRASP = 'shocking grasp'
    # TRUE_STRIKE = 'true strike'
	# ALARM = 'alarm'
    # BURNING_HANDS = 'burning hands'
    # CHARM_PERSON = 'charm person'
    # CHROMATIC_ORB = 'chromatic orb'
    # COLOR_SPRAY = 'color spray'
    # COMPREHEND_LANGUAGES = 'comprehend languages'
    # DETECT_MAGIC = 'detect magic'
    # DISGUISE_SELF = 'disguise self'
    # EXPEDITIOUS_RETREAT = 'expeditious retreat'
    # FALSE_LIFE = 'false life'
    # FEATHER_FALL = 'feather fall'
    # FIND_FAMILIAR = 'find familiar'
    # FOG_CLOUD = 'fog cloud'
    # GREASE = 'grease'
    # IDENTIFY = 'identify'
    # ILLUSORY_SCRIPT = 'illusory'
    # JUMP = 'jump'
    # LONGSTRIDER = 'longstrider'
    # MAGE_ARMOR = 'mage armor'
    # MAGIC_MISSILE = 'magic missile'
    # PROTECTION_FROM_GOOD_AND_EVIL = 'protection from good and evil'
    # RAY_OF_SICKNESS = 'ray of sickness'
    # SHEILD = 'sheild'
    # SILENT_IMAGE = 'silent image'
    # SLEEP = 'sleep'
    # TASHAS_HIDEOUS_LAUGHTER = 'tashas hideous laughter'
    # TENSERS_FLOATING_DISK = 'tensers floating disk'
    # THUNDERWAVE = 'thunderwave'
    # UNSEEN_SERVANT = 'unseen servant'
    # WITCH_BOLT = 'witch bolt'
	# ALTER_SELF = 'alter self'
    # ARCANE_LOCK = 'arcane lock'
    # BLINDNESS_DEAFNESS = 'blindess deafness'
    # BLUR = 'blur'
    # CLOUD_OF_DAGGERS = 'cloud of daggers'
    # CONTINUAL_FLAME = 'continual flame'
    # CROWN_OF_MADNESS = 'crown of madness'
    # DARKNESS = 'darkness'
    # DARKVISION = 'darkvision'
    # DETECT_THOUGHTS = 'detect thoughts'
    # ENLARGE_REDUCE = 'enlarge reduce'
    # FLAMING_SPHERE = 'flaming sphere'
    # GENTLE_REPOSE = 'gentle repose'
    # GUST_OF_WIND = 'gust of wind'
    # HOLD_PERSON = 'hold person'
    # INVISIBILITY = 'invisibility'
    # KNOCK = 'knock'
    # LEVITATE = 'levitate'
    # LOCATE_OBJECT = 'locate object'
    # MAGIC_MOUTH = 'magic mouth'
    # MAGIC_WEAPON = 'magic weapon'
    # MELFS_ACID_ARROW = 'melfs acid arrow'
    # MIRROR_IMAGE = 'mirror image'
    # MISTY_STEP = 'misty step'
    # NYSTULS_MAGIC_AURA = 'nystuls magic aura'
    # PHANTASMAL_FORCE = 'phantasmal force'
    # RAY_OF_ENFEEBLEMENT = 'ray of enfeeblement'
    # ROPE_TRICK = 'rope trick'
    # SCORCHING_RAY = 'scorching ray'
    # SEE_INVISIBILITY = 'see invisibility'
    # SHATTER = 'shatter'
    # SPIDER_CLIMB = 'spider climb'
    # SUGGESTION = 'suggestion'
    # WEB = 'web'
	# ANIMATE_DEAD = 'animate dead'
    # BESTOW_CURSE = 'bestow curse'
    # BLINK = 'blink'
    # CLAIRVOYANCE = 'clairvoyance'
    # COUNTERSPELL = 'counterspell'
    # DISPEL_CURSE = 'despel curse'
    # FEAR = 'fear'
    # FEIGN_DEATH = 'feign death'
    # FIREBALL = 'fireball'
    # FLY = 'fly'
    # GASEOUS_FORM = 'gaseous form'
    # GLYPH_OF_WARDING = 'glyph of warding'
    # HASTE = 'haste'
    # HYPNOTIC_PATTERN = 'hypnotic pattern'
    # LEOMUNDS_TINY_HUT = 'leomunds tiny hut'
    # LIGHTNING_BOLT = 'lightning bolt'
    # MAGIC_CIRCLE = 'magic circle'
    # MAJOR_IMAGE = 'major image'
    # NONDETECTION = 'nondetection'
    # PHANTOM_STEED = 'phantom steed'
    # PROTECTION_FROM_ENERGY = 'protection from energy'
    # REMOVE_CURSE = 'remove curse'
    # SENDING = 'sending'
    # SLEET_STORM = 'sleet storm'
    # SLOW = 'slow'
    # STINKING_CLOUD = 'stinking cloud'
    # TONGUES = 'tongues'
    # VAMPIRIC_TOUCH = 'vampiric touch'
    # WATER_BREATHING = 'water breathing'
	# ARCANE_EYE = 'arcane eye'
    # BANISHMENT = 'banishment'
    # BLIGHT = 'blight'
    # CONFUSION = 'confusion'
    # CONJURE_MINOR_ELEMENTALS = 'conjure minor elementals'
    # CONTROL_WATER = 'control water'
    # DIMENSION_DOOR = 'dimension door'
    # EVARDS_BLACK_TENTACLES = 'evards black tentacles'
    # FABRICATE = 'fabricate'
    # FIRE_SHIELD = 'fire sheild'
    # GREATER_INVISIBILITY = 'greater invisibility'
    # HALLUCINATORY_TERRAIN = 'hallucinatory terrain'
    # ICE_STORM = 'ice storm'
    # LEOMUNDS_SECRET_CHESS = 'leomunds secret chess'
    # LOCATE_CREATURE = 'locate creature'
    # MORDENKAINENS_FAITHFUL_HOUND = 'mordenkainens faithful hound'
    # MORDENKAINENS_PRIVATE_SANCTUM = 'mordenkainens private sanctum'
    # OTILUKES_RESILIANT_SPHERE = 'otilukes resiliant sphere'
    # PHANTASMAL_KILLER = 'phantasmal killer'
    # POLYMORPH = 'polymorph'
    # STONE_SHAPE = 'stone shape'
    # STONESKIN = 'stoneskin'
    # WALL_OF_FIRE = 'wall of fire'
	# ANIMATE_OBJECTS = 'animate objects'
    # BIGBYS_HAND = 'bigbys hand'
    # CLOUDKILL = 'cloudkill'
    # CONE_OF_COLD = 'cone of cold'
    # CONJURE_ELEMENTAL = 'conjure elemental'
    # CONTACT_OTHER_PLANE = 'contact other plane'
    # CREATION = 'creation'
    # DOMINATE_PERSON = 'dominate person'
    # DREAM = 'dream'
    # GEAS = 'geas'
    # HOLD_MONSTER = 'hold monster'
    # LEGEND_LORE = 'legend lore'
    # MISLEAD = 'mislead'
    # MODIFY_MEMORY = 'modify memory'
    # PASSWALL = 'passwall'
    # PLANAR_BINDING = 'planar binding'
    # RARYS_TELEPATHIC_BOND = 'rarys telepathic bond'
    # SCRYING = 'scrying'
    # SEEMING = 'seeming'
    # TELEKINESIS = 'telekenisis'
    # TELEPORTATION_CIRCLE = 'teleportation circle'
    # WALL_OF_FORCE = 'wall of force'
    # WALL_OF_STONE = 'wall of stone'
	# ARCANE_GATE = 'arcane gate'
    # CHAIN_LIGHTNING = 'chain lightning'
    # CIRCLE_OF_DEATH = 'circle of death'
    # CONTINGENCY = 'contingency'
    # CREATE_UNDEAD = 'create undead'
    # DISINTEGRATE = 'disintegrate'
    # DRAWMIJS_INSTANT = 'drawmijs instant'
    # SUMMONS = 'summons'
    # EYEBITE = 'eyebite'
    # FLESH_TO_STONE = 'flesh to stone'
    # GLOBE = 'globe'
    # GUARDS_AND_WARDS = 'guards and wards'
    # MAGIC_JAR = 'magic jar'
    # MASS_SUGGESTION = 'mass suggestion'
    # MOVE_EARTH = 'move earth'
    # OTILUKES_FREEZING_SPHERE = 'otilukes freezing sphere'
    # OTTOS_IRRESISTIBLE_DANCE = 'ottos irresistible dance'
    # PROGRAMMED_ILLUSION = 'programmed illusion'
    # SUNBEAM = 'sunbeam'
    # TRUE_SEEING = 'true seeing'
    # WALL_OF_ICE = 'wall of ice'
	# DELAYED_BLAST_FIREBALL = 'delayed blast fireball'
    # ETHEREALNESS = 'etherealness'
    # FINGER_OF_DEATH = 'finger of death'
    # FORCECAGE = 'forcecage'
    # MIRAGE_ARCANE = 'mirage arcane'
    # MORDENKAINENS_MAGNIFICENT_MANSION = 'mordenkainens magnificent mansion'
    # MORDENKAINENS_SWORD = 'mordenkainens sword'
    # PLANE_SHIFT = 'plane shift'
    # PRISMATIC_SPRAY = 'prismatic spray'
    # PROJECT_IMAGE = 'project image'
    # REVERSE_GRAVITY = 'reverse gravity'
    # SEQUESTOR = 'sequestor'
    # SIMULACRUM = 'simulacrum'
    # SYMBOL = 'symbol'
    # TELEPORT = 'teleport'
	# ANTIMAGIC_FIELD = 'antimagic field'
    # ANTIPATHY_SYMPATHY = 'antimagic sympathy'
    # CLONE = 'clone'
    # CONTROL_WEATHER = 'control weather'
    # DEMIPLANE = 'demiplane'
    # DOMINATE_MONSTER = 'dominate monster'
    # FEEBLEMIND = 'feeblemind'
    # INCENDIARY_CLOUD = 'incendiary cloud'
    # MAZE = 'maze'
    # MIND_BLANK = 'mind blank'
    # POWER_WORD_STUN = 'power word stun'
    # SUNBURST = 'sunburst'
    # TELEPATHY = 'telepathy'
    # TRAP_THE_SOUL = 'trap the soul'
	# ASTRAL_PROJECTION = 'atral projection'
    # FORESIGHT = 'foresight'
    # GATE = 'gate'
    # IMPRISONMENT = 'improsonment'
    # METEOR_STORM = 'meteor storm'
    # POWER_WORD_KILL = 'power work kill'
    # PRISMATIC_WALL = 'prismatic wall'
    # SHAPECHANGE = 'shapechange'
    # TIME_STOP = 'timestop'
    # TRUE_POLYMORPH = 'true polymorph'
    # WEIRD = 'wierd'
    # WISH = 'wish'

	# SPELL_CHOICES = [
	# 	(BLADE_WARD, 'blade ward'),
	# 	(DANCING_LIGHTS),
	# 	(FRIENDS),
	# 	(LIGHT),
	# 	(MAGE_HAND),
	# 	(MENDING),
	# 	(MESSAGE),
	# 	(MINOR_ILLUSION),
	# 	(PRESTIDIGITATION),
	# 	(TRUE_STRIKE),
	# 	(VICIOUS_MOCKERY),
	# 	(ANIMAL_FRIENDSHIP),
	# 	(BANE),
	# 	(CHARM_PERSON),
	# 	(COMPREHEND_LANGUAGES),
	# 	(CURE_WOUNDS),
	# 	(DETECT_MAGIC),
	# 	(DISGUISE_SELF),
	# 	(DISSONANT_WHISPERS),
	# 	(FAERIE_FIRE),
	# 	(FEATHER_FALL),
	# 	(HEALING_WORD),
	# 	(HEROISM),
	# 	(IDENTIFY),
	# 	(ILLUSORY_SCRIPT),
	# 	(LONGSTRIDER),
	# 	(SILENT_IMAGE),
	# 	(SLEEP),
	# 	(SPEAK_WITH_ANIMALS),
	# 	(TASHAS_HIDEOUS_LAUGHTER),
	# 	(THUNDERWAVE),
	# 	(UNSEEN_SERVANT),
	# 	(ANIMAL_MESSENGER),
	# 	(BLINDNESS_DEAFNESS),
	# 	(CALM_MOTIONS),
	# 	(CLOUD_OF_DAGGERS),
	# 	(CROWN_OF_MADNESS),
	# 	(DETECT_THOUGHTS),
	# 	(ENHANCE_ABILITY),
	# 	(ENTHRALL),
	# 	(HEAT_METAL),
	# 	(HOLD_PERSON),
	# 	(INVISIBILITY),
	# 	(KNOCK),
	# 	(LESSER_RESTORATION),
	# 	(LOCATE_ANIMALS_OR_PLANTS),
	# 	(LOCATE_OBJECT),
	# 	(MAGIC_MOUTH),
	# 	(PHANTASMAL_FORCE),
	# 	(SEE_INVISIBILITY),
	# 	(SHATTER),
	# 	(SILENCE),
	# 	(SUGGESTION),
	# 	(ZONE_OF_TRUTH),
	# 	(BESTOW_CURSE),
	# 	(CLAIRVOYANCE),
	# 	(DISPEL_MAGIC),
	# 	(FEAR),
	# 	(FEIGN_DEATH),
	# 	(GLYPH_OF_WARDING),
	# 	(HYPNOTIC_PATTERN),
	# 	(LEOMUNDS_TINY_HUT),
	# 	(MAJOR_IMAGE),
	# 	(PLANT_GROWTH),
	# 	(SENDING),
	# 	(SPEAK_WITH_DEAD),
	# 	(SPEAK_WITH_PLANTS),
	# 	(STINKING_CLOUD),
	# 	(TONGUES),
	# 	(COMPULSION),
	# 	(CONFUSION),
	# 	(DIMENSION_DOOR),
	# 	(FREEDOM_OF_MOVEMENT),
	# 	(GREATER_INVISIBILITY),
	# 	(HALLUCINATORY_TERRAIN),
	# 	(LOCATE_CREATURE),
	# 	(POLYMORPH),
	# 	(ANIMATE_OBJECTS),
	# 	(AWAKEN),
	# 	(DOMINATE_PERSON),
	# 	(DREAM),
	# 	(GEAS),
	# 	(GREATER_RESTORATION),
	# 	(HOLD_MONSTER),
	# 	(LEGEND_LORE),
	# 	(MASS_CURE_WOUNDS),
	# 	(MISLEAD),
	# 	(MODIFY_MEMORY),
	# 	(PLANAR_BINDING),
	# 	(RAISE_DEAD),
	# 	(SCRYING),
	# 	(SEEMING),
	# 	(TELEPORTATION_CIRCLE),
	# 	(EYEBITE),
	# 	(FIND_THE_PATH),
	# 	(GUARDS_AND_WARDS),
	# 	(MASS_SUGGESTION),
	# 	(OTTOS_IRRESISTIBLE_DANCE),
	# 	(PROGRAMMED_ILLUSION),
	# 	(TRUE_SEEING),
	# 	(ETHEREALNESS),
	# 	(FORCECAGE),
	# 	(MIRAGE_ARCANE),
	# 	(MORDENKAINENS_MAGNIFICENT_MANSION),
	# 	(MORDENKAINENS_SWORD),
	# 	(PROTECT_IMAGE),
	# 	(REGENERATION),
	# 	(RESURRECTION),
	# 	(SYMBOL),
	# 	(TELEPORT),
	# 	(DOMINATE_MONSTER),
	# 	(FEEBLEMIND),
	# 	(GLIBNESS),
	# 	(MIND_BLANK),
	# 	(POWER_WORD_STUN),
	# 	(FORESIGHT),
	# 	(POWER_WORD_HEAL),
	# 	(POWER_WORD_KILL),
	# 	(TRUE_POLYMORPH),
	# 	(GUIDANCE),
	# 	(RESISTANCE),
	# 	(SACRED_FLAME),
	# 	(SPARE_THE_DYING),
	# 	(THAUMATURGY),
	# 	(BLESS),
	# 	(COMMAND),
	# 	(CREATE_OR_DESTROY_WATER),
	# 	(DETECT_EVIL_AND_GOOD),
	# 	(DETECT_POISON_AND_DISEASE),
	# 	(GUIDING_BOLT),
	# 	(INFLICT_WOUNDS),
	# 	(PURIFY_FOOD_AND_DRINK),
	# 	(SANCTUARY),
	# 	(SHEILD_OF_FAITH),
	# 	(AID),
	# 	(AUGURY),
	# 	(CALM_EMOTIONS),
	# 	(CONTINUAL_FLAME),
	# 	(FIND_TRAPS),
	# 	(GENTLE_REPOSE),
	# 	(PRAYER_OF_HEALING),
	# 	(PROTECTION_FROM_POISON),
	# 	(SPIRITUAL_WEAPON),
	# 	(WARDING_BOND),
	# 	(ANIMATE_DEAD),
	# 	(BEACON_OF_HOPE),
	# 	(CREATE_FOOD_AND_WATER),
	# 	(DAYLIGHT),
	# 	(FEIGN_DEATH),
	# 	(MAGIC_CIRCLE),
	# 	(MELD_INTO_STONE),
	# 	(PROTECTION_FROM_ENERGY),
	# 	(REMOVE_CURSE),
	# 	(REVIVIFY),
	# 	(SPIRIT_GUARDIANS),
	# 	(WATER_WALK),
	# 	(BANISHMENT),
	# 	(CONTROL_WATER),
	# 	(DEATH_WARD),
	# 	(DIVINATION),
	# 	(GUARDIAN_OF_FAITH),
	# 	(STONE_SHAPE),
	# 	(COMMUNE),
	# 	(CONTAGION),
	# 	(DISPEL_EVIL_AND_GOOD),
	# 	(FLAME_STRIKE),
	# 	(HALLOW),
	# 	(INSECT_PLAGUE),
	# 	(BLADE_BARRIER),
	# 	(CREATE_UNDEAD),
	# 	(FORBIDDANCE),
	# 	(HARM),
	# 	(HEAL),
	# 	(HEROS_FEAST),
	# 	(PLANAR_ALLY),
	# 	(WORD_OF_RECALL),
	# 	(CONJURE_CELESTIAL),
	# 	(DIVINE_WORD),
	# 	(FIRE_STORM),
	# 	(PLANE_SHIFT),
	# 	(REGENERATE),
	# 	(ANTIMAGIC_FIELD),
	# 	(CONTROL_WEATHER),
	# 	(EARTHQUAKE),
	# 	(HOLY_AURA),
	# 	(ATRAL_PROJECTION),
	# 	(GATE),
	# 	(MASS_HEAL),
	# 	(TRUE_RESURRECTION),
	# 	(DRUIDCRAFT),
	# 	(PRODUCE_FLAME),
	# 	(SHILLELAGH),
	# 	(THORN_WHIP),
	# 	(ENTANGLE),
	# 	(FOG_CLOUD),
	# 	(GOODBERRY),
	# 	(JUMP),
	# 	(BARKSKIN),
	# 	(BEAST_SENSE),
	# 	(DARKVISION),
	# 	(FLAME_BLADE),
	# 	(FLAMING_SPHERE),
	# 	(GUST_OF_WIND),
	# 	(MOONBEAM),
	# 	(PASS_WITHOUT_TRACE),
	# 	(SPIKE_GROWTH),
	# 	(CALL_LIGHTNING),
	# 	(CONJURE_ANIMALS),
	# 	(SLEET_STORM),
	# 	(WATER_BREATHING),
	# 	(WIND_WALL),
	# 	(BLIGHT),
	# 	(CONJURE_MINOR_ELEMENTALS),
	# 	(CONJURE_WOODLAND_BEINGS),
	# 	(DOMINATE_BEAST),
	# 	(GIANT_INSECT),
	# 	(GRASPING_VINE),
	# 	(ICE_STORM),
	# 	(STONESKIN),
	# 	(WALL_OF_FIRE),
	# 	(ANTILIFE_SHELL),
	# 	(CONJURE_ELEMENTAL),
	# 	(REINCARNATE),
	# 	(TREE_STRIDE),
	# 	(WALL_OF_STONE),
	# 	(CONJURE_FEY),
	# 	(MOVE_EARTH),
	# 	(SUNBEAM),
	# 	(TRANSPORT_VIA_PLANTS),
	# 	(WALL_OF_THORNS),
	# 	(WIND_WALK),
	# 	(REVERSE_GRAVITY),
	# 	(ANIMAL_SHAPES),
	# 	(ANTIPATHY_SYMPATHY),
	# 	(TSUNAMI),
	# 	(SHAPECHANGE),
	# 	(STORM_OF_VENGEANCE),
	# 	(COMPELLED_DUEL),
	# 	(DIVINE_FAVOR),
	# 	(PROTECTION_FROM_GOOD_AND_EVIL),
	# 	(SEARING_SMITE),
	# 	(THUNDEROUS_SMITE),
	# 	(WRATHFUL_SMITE),
	# 	(BRANDING_SMITE),
	# 	(FIND_STEEL),
	# 	(MAGIC_WEAPON),
	# 	(AURA_OF_VITALITY),
	# 	(BLINDING_SMITE),
	# 	(CRUSADERS_MANTLE),
	# 	(ELEMENTAL_WEAPON),
	# 	(AURA_OF_LIFE),
	# 	(AURA_OF_PURITY),
	# 	(STAGGERING_SMITE),
	# 	(BANISHING_SMITE),
	# 	(CIRCLE_OF_POWER),
	# 	(DESCTRUCTIVE_SMITE),
	# 	(ALARM),
	# 	(CURE_FRIENDS),
	# 	(ENSNARING_STRIKE),
	# 	(HAIL_OF_THORNS),
	# 	(HUNTERS_MARK),
	# 	(CORDON_OF_ARROWS),
	# 	(CONJURE_BARRAGE),
	# 	(LIGHTNING_ARROW),
	# 	(COMMUNE_WITH_NATURE),
	# 	(CONJURE_VOLLEY),
	# 	(SWIFT_QUIVER),
	# 	(CHILL_TOUCH),
	# 	(POISON_SPRAY),
	# 	(RAY_OF_FROST),
	# 	(EXPEDITIOUS_RETREAT),
	# 	(FALSE_LIFE),
	# 	(MAGE_ARMOR),
	# 	(MAGIC_MISSILE),
	# 	(RAY_OF_SICKNESS),
	# 	(SHEILD),
	# 	(WITCH_BOLT),
	# 	(ALTER_SELF),
	# 	(BLUR),
	# 	(ENLARGE_REDUCE),
	# 	(LEVITATE),
	# 	(SCORCHING_RAY),
	# 	(WEB),
	# 	(FIREBALL),
	# 	(FLY),
	# 	(GASEOUS_FORM),
	# 	(HASTE),
	# 	(LIGHTNING_BOLT),
	# 	(SLOW),
	# 	(CLOUDKILL),
	# 	(CONE_OF_COLD),
	# 	(CREATION),
	# 	(TELEKINESIS),
	# 	(ARCANE_GATE),
	# 	(CHAIN_LIGHTNING),
	# 	(GLOBE_OF_INVULNERABILITY),
	# 	(DELAYED_BLAST_FIREBALL),
	# 	(FINGER_OF_DEATH),
	# 	(PRISMATIC_SPRAY),
	# 	(INCENDIARY_CLOUD),
	# 	(SUNBURST),
	# 	(METEOR_SWARM),
	# 	(TIME_STOP),
	# 	(WISH),
	# 	(ELDRITCH_BLAST),
	# 	(ARMOR_OF_AGATHYS),
	# 	(ARMS_OF_HADAR),
	# 	(HELLISH_REBUKE),
	# 	(HEX),
	# 	(MISTY_STEP),
	# 	(COUNTERSPELL),
	# 	(HUNGER_OF_HADAR),
	# 	(VAMPIRIC_TOUCH),
	# 	(FLESH_TO_STONE),
	# 	(DEMIPLANE),
	# 	(POSER),
	# 	(ASTRAL_PROJECTION),
	# 	(IMPRISONMENT),
	# 	(ACID_SPLASH),
	# 	(FIRE_BOLT),
	# 	(SHOCKING_GRASP),
	# 	(BURNING_HANDS),
	# 	(CHROMATIC_ORB),
	# 	(COLOR_SPRAY),
	# 	(FIND_FAMILIAR),
	# 	(GREASE),
	# 	(TENSERS_FLOATING_DISK),
	# 	(ARCANE_LOCK),
	# 	(DARKNESS),
	# 	(FLAMING_SPHERE),
	# 	(MELFS_ACID_ARROW),
	# 	(MIRROR_IMAGE),
	# 	(NYSTULS_MAGIC_AURA),
	# 	(RAY_OF_ENFEEBLEMENT),
	# 	(ROPE_TRICK),
	# 	(SPIDER_CLIMB),
	# 	(BLINK),
	# 	(DISPEL_CURSE),
	# 	(NONDETECTION),
	# 	(PHANTOM_STEED),
	# 	(VAMPIRIC_TOUCH),
	# 	(ARCANE_EYE),
	# 	(EVARDS_BLACK_TENTACLES),
	# 	(FABRICATE),
	# 	(FIRE_SHIELD),
	# 	(LEOMUNDS_SECRET_CHESS),
	# 	(MORDENKAINENS_FAITHFUL_HOUND),
	# 	(MORDENKAINENS_PRIVATE_SANCTUM),
	# 	(OTILUKES_RESILIANT_SPHERE),
	# 	(PHANTASMAL_KILLER),
	# 	(BIGBYS_HAND),
	# 	(CONTACT_OTHER_PLANE),
	# 	(PASSWALL),
	# 	(RARYS_TELEPATHIC_BOND),
	# 	(WALL_OF_FORCE),
	# 	(CIRCLE_OF_DEATH),
	# 	(CONTINGENCY),
	# 	(DISINTEGRATE),
	# 	(DRAWMIJS_INSTANT),
	# 	(SUMMONS),
	# 	(GLOBE),
	# 	(MAGIC_JAR),
	# 	(OTILUKES_FREEZING_SPHERE),
	# 	(WALL_OF_ICE),
	# 	(PROJECT_IMAGE),
	# 	(SEQUESTOR),
	# 	(SIMULACRUM),
	# 	(CLONE),
	# 	(MAZE),
	# 	(TELEPATHY),
	# 	(TRAP_THE_SOUL),
	# 	(METEOR_STORM),
	# 	(PRISMATIC_WALL),
	# 	(WEIRD)
	# ]

class Proficiencies(models.Model):
	name = models.CharField(max_length=20)
	value = models.IntegerField()

class CharClass(models.Model):
	name = models.CharField(max_length=20)
    # CHARCLASS_CHOICES = [
	# 	(BARBARIAN),
	# 	(BARD),
	# 	(CLERIC),
	# 	(DRUID),
	# 	(FIGHTER),
	# 	(MONK),
	# 	(PALADIN),
	# 	(RANGER),
	# 	(ROGUE),
	# 	(SORCERER),
	# 	(WARLOCK),
	# 	(WIZARD)
	# ]

class Proficiencies(models.Model):
	name = models.CharField(max_length=20)
    # PROFICIENCES_CHOICES = [
	# 	(ATHLETICS),
	# 	(ACROBATICS),
	# 	(SLEIGHT_OF_HAND),
	# 	(STEALTH),
	# 	(ARCANA),
	# 	(HISTORY),
	# 	(INVESTIGATION),
	# 	(NATURE),
	# 	(RELIGION),
	# 	(ANIMAL_HANDLING),
	# 	(INSIGHT),
	# 	(MEDICINE),
	# 	(PERCEPTION),
	# 	(SURVIVAL),
	# 	(DECEPTION),
	# 	(INTIMIDATION),
	# 	(PERFORMANCE),
	# 	(PERSUASION)
	# ]

class Skills(models.Model):
	name = models.CharField(max_length=20)
    # SKILLS_CHOICES = [
	# 	(STRENGTH),
	# 	(DEXTERITY),
	# 	(CONSTITUTION),
	# 	(INTELLIGENCE),
	# 	(WISDOM),
	# 	(CHARISMA)
	# ]

class Character(models.Model):
	name = models.CharField(max_length=100, null=True)
	player = models.CharField(max_length=100, null=True)
	race = models.CharField(max_length=30, null=True)
	charClass = models.CharField(max_length=30, null=True)
	proficiencies = models.ForeignKey(Proficiencies, null=True, on_delete=models.CASCADE)
	spells = models.ForeignKey(Spells, null=True, on_delete=models.CASCADE)
	spellSlots = models.IntegerField(null=True)	