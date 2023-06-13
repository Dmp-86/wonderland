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
                "command": "stay",
                "next": "02",
                "name": "Rest up for the night"
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
                "next": "06",
                "name": "Secret Door in Wall of Roses"
            },
            {
                "command": "up",
                "next": "02",
                "name": "Cave"
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
        ],
        "story": "He's such a hoot!"
    },

    {
        "id": "05",
        "location": "Sleepy Sasquatch",
        "directions": [
            {
                "command": "cave",
                "next": "02",
                "name": "Cave"
            },
            {
                "command": "start",
                "next": "01",
                "name": "back to the Start"
            }
        ],
        "story": "Shhhh, don't disturb him!"
    },

    {
        "id": "06",
        "location": "Secret Door in Wall of Roses",
        "directions": [
            {
                "command": "back",
                "next": "03",
                "name": "Underground Tunnel of Lights"
            }
        ],
        "story": "Congrats! You found the hidden pathway!"
    }
]