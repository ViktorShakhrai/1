import json

data = {
    "shakhrai_family": [
        {"Father":
        {
            "Name": "Vitalij",
            "Surname": "Shakhrai",
            "Age": 46,
            "Date of birth": 1975,
            "Phone number": "+380956143392",
        }
        },
        {"Mother":
        {
            "Name": "Khrystyna",
            "Surname": "Shakhrai",
            "Age": 39 ,
            "Date of birth": 1982,
            "Phone number": "+380990646912",
        }
        },
        {"Sister":
        {
            "Name": "Dana",
            "Surname": "Shakhrai",
            "Age": 18,
            "Date of birth": 2003,
            "Phone number": "+380990646912",
        }
        },
        {"Sister":
        {
            "Name": "Ariadna",
            "Surname": "Shakhrai",
            "Age": 10,
            "Date of birth": 2011,
            "Phone number": "+380989672799",
        }
        },
        {"Brother":
        {
            "Name": "Viktor",
            "Surname": "Shakhrai",
            "Age": 20,
            "Date of birth": 2001,
            "Phone number": "+380925060053",
        }
        },

    ]

}

with open('my_family.json', 'w') as write_file:
    json.dump(data, write_file)
