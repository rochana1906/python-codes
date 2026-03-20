from docx import Document
PLACEHOLDER="[name]"

with open ("./Input/Names/invited_names.txt") as name_file:
    names= name_file.readlines()
    print(names)

with open ("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)

        document = Document()
        document.add_paragraph(new_letter)

        document.save(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx")



