PLACES = [
    {
        "id": "01",
        "location": "the Start",
        "directions": [
            {
                "command": "left",
                "next": "04",
                "name": "Talking Owl"
            },
            {
                "command": "right",
                "next": "02",
                "name": "Cave"
            },
            {
                "command": "forward",
                "next": "05",
                "name": "Sleepy Sasquatch"
            }
        ],
        "story": "You're at a crossroads, and you find a scroll with an old map printed on it.\n"
            "Travelling left will bring you to the wise old Talking Owl.\n"
            "If you keep going forward, you will meet a Sleepy Sasquatch.\n"
            "Going right will bring you to the Cave.\n"
    },

    {
        "id": "02",
        "location": "Cave",
        "directions": [
            {
                "command": "down",
                "next": "03",
                "name": "Underground Tunnel of Lights"
            },
            {
                "command": "right",
                "next": "09",
                "name": "RabbitHole #1"
            },
            {
                "command": "forward",
                "next": "05",
                "name": "Sleepy Sasquatch"
            }
        ],
        "story": "Have a look around! No-one can see you hidden in the cave. \n"
        "Are you brave enough to enter Sasquatches lair? \n"
        "Perhaps a euphoric trip to Tunnel of lights sounds better? \n"
        "Or jump down the rabbit hole, to see what adventure lies beneath. \n"
    },

    {
        "id": "03",
        "location": "Underground Tunnel of Lights",
        "directions": [
            {
                "command": "forward",
                "next": "09",
                "name": "RabbitHole #1"
            },
            {
                "command": "left",
                "next": "07",
                "name": "Mad Hatters Barn"
            },
            {
                "command": "right",
                "next": "05",
                "name": "Sleepy Sasquatch"
            }
        ],
        "story": "Don't forget to top up the electric!"
        "You find yourself needing a rest before the next stage of your journey. \n"
        "Will Sasquatch be happy to see you? Will the Mad Hatter be angry at your arrival? \n"
    },

    {
        "id": "04",
        "location": "Talking Owl",
        "directions": [
            {
                "command": "right",
                "next": "01",
                "name": "Back to The Start"
            },
            {
                "command": "left",
                "next": "07",
                "name": "Mad Hatters Barn"
            },
            {
                "command": "potion",
                "next": "06",
                "name": "Secret Door in Wall of Roses"
            }
        ],
        "story": "He's such a hoot! He shares stories of the mythical creatures in Wonderland. \n"
        "But be warned...your journey can take an unexpected turn. \n"
        
    },

    {
        "id": "05",
        "location": "Sleepy Sasquatch",
        "directions": [
            {
                "command": "forward",
                "next": "06",
                "name": "Secret Door in Wall of Roses"
            },
            {
                "command": "left",
                "next": "07",
                "name": "Mad Hatters Barn"
            },
            {
                "command": "right",
                "next": "09",
                "name": "RabbitHole #1"
            }
        ],
        "story": "Shhhh, don't disturb him! \n"
        "Sasquatch doesn't stir, so you quietly look around for clues. \n"

    },

    {
        "id": "06",
        "location": "Secret Door in Wall of Roses",
        "directions": [
            {
                "command": "forward",
                "next": "10",
                "name": "RabbitHole #2"
            },
            {
                "command": "left",
                "next": "08",
                "name": "Cheshire Cat"
            }
        ],
        "story": "Congrats! You found the hidden pathway! \n"
        "This door will lead you past some crazed Flying Monkeys to safety. \n"
        "Will you seek solace in Rabbit Hole #2, or have a chat with Cheshire Cat? \n"
    },

    {
        "id": "07",
        "location": "Mad Hatters Barn",
        "directions": [
            {
                "command": "left",
                "next": "08",
                "name": "Cheshire Cat"
            },
            {
                "command": "right",
                "next": "06",
                "name": "Secret Door in Wall of Roses"
            }
        ],
        "story": "Oh My! It looks likes we've interrupted a Mad Hatter Tea-Party. \n"
        "You don't have time for tea, so you make a quick exit. \n"
    },

    {
        "id": "08",
        "location": "Cheshire Cat",
        "directions": [
            {
                "command": "left",
                "next": "08",
                "name": "END"
            },
            {
                "command": "right",
                "next": "10",
                "name": "RabbitHole #2"
            },
            {
                "command": "forward",
                "next": "11",
                "name": "Secret Door"
            }
        ],
        "story": "Welcome, weary traveller! \n"
        "One of  these options is not like the rest. \n"
        "Left, Right or Forward, which one will you test? \n "
    },

    {
        "id": "09",
        "location": "RabbitHole #1",
        "directions": [
            {
                "command": "tea",
                "next": "08",
                "name": "Cheshire Cat"
            },
            {
                "command": "muffin",
                "next": "09",
                "name": "Nope"
            },
            {
                "command": "stopwatch",
                "next": "11",
                "name": "Secret Door"
            }
        ],
        "story": "You've arrived in the Rabbit Hole, weary and spent. \n"
        "White Rabbit has left some items that he thinks may be useful. \n"
        "Choose wisely, White Rabbit is a trickster. \n"
    },

    {
        "id": "10",
        "location": "RabbitHole #2",
        "directions": [
            {
                "command": "forward",
                "next": "11",
                "name": "Secret Door"
            },
            {
                "command": "right",
                "next": "10",
                "name": "Trapped-END"
            }
        ],
        "story": "You've landed in Rabbit Hole 2. \n"
        "White Rabbit isn't home, so you quickly decide which way to go. \n"
    },

    {
        "id": "11",
        "location": "Secret Door",
        # "directions": [
        #     {
        #         "command": "left",
        #         "next": "08",
        #         "name": "Cheshire Cat"
        #     },
        #     {
        #         "command": "right",
        #         "next": "06",
        #         "name": "Secret Door in Wall of Roses"
        #     }
        # ],
        "story": "You have reached Wonderland! \n"
        "Congratulations on finding your way!"
    },
]