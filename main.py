# working with sets
from pyscript import display, document

grade_7 = {
    "Martin Edwards",
    "Eom Seonghyeon",
    "Ahn Keonho",
    "Kim Juhoon",
    "Zhao James",
}

grade_8 = {
    "Raver Estacio",
    "Kenneth Concepcion",
    "Miguel Jimenez",
    "Santiago Valdez",
    "Jesse Villante",
}

grade_9 = {
    "Destiny Reyes",
    "Franchesca Dela Rosa",
    "MJ Madrelejos",
}

grade_10 = {
    "Chalanie Lumbang",
    "Jia Hadji Gapor",
    "Gurleen Kaur",
}

all_members = grade_7 | grade_8 | grade_9 | grade_10

def update_results():
    names_html = "<br>".join(sorted(all_members))

    document.getElementById("member-list").innerHTML = (
        f"{names_html}"
    )

    document.getElementById("member-total").innerHTML = (
        f"Total members: {len(all_members)}" 
    )

def add_member(event):
    first_name = document.getElementById("first-name").value.strip()
    last_name = document.getElementById("last-name").value.strip()

    full_name = f"{first_name} {last_name}".strip()

    global all_members
    all_members = all_members | {full_name}

    display(
        f"Member added: {full_name}",
        target="message",
        append=False
    )

    document.getElementById("first-name").value = ""
    document.getElementById("last-name").value = ""

    update_results()

update_results()

