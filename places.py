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
        "story": "Welcome to Wonderland!"
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
        "story": "Have a look around!"
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
            }
            {
                "command": "left",
                "next": "05",
                "name": "Sleepy Sasquatch"
            }
        ],
        "story": "Don't forget to top up the electric!"
    },

    {
        "id": "04",
        "location": "Talking Owl",
        "directions": [
            {
                "command": "right",
                "next": "01",
                "name": "back to the Start"
            }
            {
                "command": "left",
                "next": "07",
                "name": "Mad Hatters Barn"
            }
            {
                "command": "potion",
                "next": "06",
                "name": "Secret Door in Wall of Roses"
            }
        ],
        "story": "He's such a hoot!"
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
            }
            {
                "command": "right",
                "next": "09",
                "name": "RabbitHole #1"
            }
        ],
        "story": "Shhhh, don't disturb him!"
    },

    {
        "id": "06",
        "location": "Secret Door in Wall of Roses",
        "directions": [
            {
                "command": "forward",
                "next": "10",
                "name": "RabbitHole #2"
            }
            {
                "command": "left",
                "next": "08",
                "name": "Cheshire Cat"
            }
        ],
        "story": "Congrats! You found the hidden pathway!"
    }

    {
        "id": "07",
        "location": "Mad Hatters Barn",
        "directions": [
            {
                "command": "left",
                "next": "08",
                "name": "Cheshire Cat"
            }
            {
                "command": "right",
                "next": "06",
                "name": "Secret Door in Wall of Roses"
            }
        ],
        "story": "Congrats! You found the hidden pathway!"
    }
]