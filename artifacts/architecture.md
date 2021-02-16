# Program Organization
# System Context Diagram
![System Context Diagram](https://github.com/tazemaster/GenFive/blob/main/artifacts/diagram_images/System%20Context%20Diagram.jpg)

# System Context Description

The GenFive User uses the GenFive Web System to view their characters and parties, make new characters, make new parties with other users, and fight in the battle sim.

# Container Diagram
![Container Diagram](https://github.com/tazemaster/GenFive/blob/main/artifacts/diagram_images/Container%20Diagram.jpg)
# Component Diagram
![Component Diagram](https://github.com/tazemaster/GenFive/blob/main/artifacts/diagram_images/Component%20Diagram.jpg)

# Components Description

The user will be interacting with the GenFive webapp we have hosted on AWS. There will be a sign-up/sign-in page, as shown in our UI Diagram, that will act as the go between for the user and the security interface. All sign-in information will be stored in the database.

The user, once signed in, will have access to the character creation system where they can make whatever characters they wish. Once a character has been made, it will be sent to the database for storage. The character creation system will also be able to pull from the database to modify any pre-existing characters for higher levels, changes in equipment, etc.

The user will also be able to enter the Battle Simulator. The battle simulator will read character and monster entries from the database as requested by the user to allow for use in the battle sim. As well, the Battle Sim System will write to the database whenever loose items are picked up by the characters from the enemies, including Currency, Weapons, Armor, and other trinkets.

# Code Design

![Class Diagram](https://github.com/tazemaster/GenFive/blob/main/artifacts/diagram_images/Class%20Diagram.jpg)
# Class Descriptions

The User class will constantly be in use. Any user who shows up on the webapp with the intention of using it will be required to sign up/in and the associated user class will be referenced.

The Party class will be used only in cases where multiple Users wish to get to collaborate in the battle simulator. The Party class will be comprised of multiple Users assigned as Players and Dungeon Master.

All other classes in the diagram (Being, Character, Monster, Spell, Feature, Item, Weapon, Armor, Attack, Skill) pertain to Characters associated with Users and Monsters used as pre-generated enemies in the webapp. 

The Being Class will be an abstract super-class for Character and Monster. It should never be instantiated. 

The Character class is a subclass of Being and is used to store information about the User's custom Character made in the Character Creator. This class is composed of other classes pertinent to a character, namely their Items, Skills, Spells, and Features, along with other important details like Armor Class, Health Points, and Movement Speed.

The Item Class is a data storage class, it simply holds information about items held by a Character. 

The Weapon Class is a subclass of Item that pertains specifically to Items used to perform Attacks. They have an additional field called attacks that holds a list of all Attacks the Weapon can perform.

The Attack Class holds information about how much damage an attack will do and what type of damage it will do. Specifically, it stores which dice will be rolled and how many, along with pertinent modifiers for damage bonuses.

The "Armor" Class is a subclass of Item that pertains to defensive Items that boost your Armor Class (AC). It contains an additional field called armorClassBonus that stores the amount that your AC is boosted by wearing the piece of armor.

The Skill Class contains information on what ability the skill is associated with, as well as whether or not the Character is proficient in the skill.

The Spell Class contains information regarding Spell name, Spell level, and Spell description. Some characters will have access to spells (namely spellcasters like Clerics, Wizards, etc.), which will give them access to spell slots. Other characters will not have access to spells (Fighters, Barbarians, etc.) and will not have any listed.

The Feature Class contains information regarding a character's racial and class Features, which act as special abilities that your character can perform, or as special traits that your character has (resistance to fire, etc.).

The Monster Class is a subclass of Being and will be used to store information about non-Player enemies in the battle simulator. Monsters will be used by the Dungeon Master only.

The Effect Class contains information about status effects placed on characters and monsters on the board, namely name and description.


# Data Design

![Data Diagram](https://github.com/tazemaster/GenFive/blob/main/artifacts/diagram_images/Data%20Storage.jpg)

User data will be stored within AWS in the heirarchy illustrated by the above document.

# Business Rules

As we are not a business, there are no external requirements we have to comply with.

# User Interface Design
![User Interface](https://github.com/tazemaster/GenFive/blob/main/artifacts/diagram_images/User%20Interface.jpg)

First, the user needs to login to the website to have access to their account. If they do not have an account they can create one and be automatically logged in. 
Once they are logged in they will be on the screen that shows all the characters they have and all the parties they are in. On that page if they click the plus sign under the parties section it will open a pop-up window that will allow them to make a new party by creating a party name, inviting 2 party members or more clicking the plus sign (they invite party members by display name or email), and selecting if they will be the dm (the dm will control monsters and maps in the battle sim) or selecting an already existing character of theirs to be in the party. If the user clicks the plus sign in the characters section they will be taken to a webpage that will allow them to make a new character. If they click save character it will take them back to the page they are on before and show that new character their in characters section. 
Clicking on one of your parties in the parties section will take you to webpage that shows all the party's members. Clicking go back button will take the user to the previous page. Clicking on the play button will take the user to the battle mode page. Clicking exit battle mode button will take the user to the previous page. 
On the battle mode page it will show the user's character hp, armor class, and speed next to the battle map. The battle will the character's position on the map as well as their party members and enemies. The battle map can enlarged or minimized by dragging it. If user is not a DM they can only move their character on the battle map and they can only act when it is their turn. If a user is a DM they can only move their monsters on the battle map and they can only act when it is one of their monsters turn. Under the battle map is the turn order with everyone on the battle map listed in order of the turn. An icon will indicate whose turn it is. If it is users turn an end turn button will appear under their name in turn order so they can end their turn so the next the person can take their turn. If a character in the turn order has an X over their picture it means they are dead and user can hover a deceased character to see whether or not they can revived by them. The inventory box lists equipped items and items a character has. The features box lists a character's immunities, vulnerabilities, resistances, advantages, and disadvantages. The spells box lists the spell and spell level of a character. The status effects box lists a character's status and the effects of it. The spell slots box list the spell level, spell slots left for that level, and the max spell slots for that level. 
The roll box opens a pop up window where a person types the amount of dice to roll and the type of dice to roll (except d20) so the total will be calculated. The user must add modifiers themselves. A d20 is at the bottom and user must select if they are rolling with advantage, disadvantage, or normally before it is rolled for them. Again a user must add modifiers themself. Clicking the log out button will log a user out of the system and it takes them back to the log in screen.

# Resource Management

Resource management is not a major concern as we do not expect a large number of users.

# Security

Security is not a major concern for our application, as we are not storing any highly sensitive data or financial information. There would be no potential financial benefit to hacking our application. The basic security provided by using AWS Amplify should suffice.

# Performance

Performance is not a major concern in our application. 

# Scalability

Scalability is not a major concern, as we do not expect a large number of users.

# Interoperability

Our application will not share data or resources with external software, only our own database provided through AWS Amplify.

# Internationalization/Localization

Our application will be designed for use only in the United States. The only language supported will be English.

# Input/Output

We will be using a just in time reading scheme. If the user wishes to perform an action that requires input, that input will be immediately asked for. There will be minimal I/O error detection.

# Error Processing

Our application will not stop users from doing things that are against the rules. Because D&D is such an open ended game, and many people play with "homebrew" rules, we could not hope to encapsulate all of the different rulesets and account for all of the possible scenarios. It will be up to the users to know what is allowed in their game and what is not.

# Fault Tolerance

Our application will not need a high fault tolerance as it will not be doing much error detecting.

# Architectural Feasibility

As we do not have strenuous performance or resource requirements, we expect that our architecture will sufficiently meet the demands we have placed on it.

# Overengineering

We will not be overengineering our code to protect against error detection as we will be doing minimal error detection, due to the nature of role playing games.

# Build-vs-Buy Decisions

We do not intend to buy any software for our site. The only thing we would consider buying is a custom URL. We will be using free services, primarily AWS Amplify.

# Reuse

We will not be reusing software.

# Change Strategy

Most of the change to our original design will likely come from implementing additional, original features, rather than modifying existing ones. Because we are using Git, we will always have the option to revert to an earlier state if a change breaks the program in an unexpected or indeterminable way.
