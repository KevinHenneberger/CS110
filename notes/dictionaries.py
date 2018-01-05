"""
Dictionaries:
- mutable
- unique keys
- unordered
"""

def main():

    contacts = {
        "Luke": "657-6789", 
        "John": "523-7532", 
        
    }

    contacts["Meghan"] = "380-2112"

    print(contacts["Luke"])

    for k in contacts:
        print(contacts[k])

    print(contacts.keys())
    print(contacts.values())

main()
