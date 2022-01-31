pages = ["video essays", "non-fiction", "fiction", "music videos", ]

found_template = False

while not found_template:
    input_str = "which page do you want to edit? (non-fiction, music-videos, etc): "
    page_input = input(input_str)
    gottem = "n"

    for page in pages:
        res = set(page_input).issubset(page)
        if res:
            page_to_edit = page
            gottem = input(
                "is the template you want to edit " + page_to_edit + ".html (y/n)? "
                )

    if gottem.lower() == "y":
        found_template = True
    else:
        print("that doesn't exist.")


option_a = "burn this page to the ground and start adding videos from scratch"
option_b = "add a new video to the top of the page"
option_c = "delete a specific video"

selected_option = False

while not selected_option:
    print("What action do you want to perform on this page?")
    print("\tA. " + option_a)
    print("\tB. " + option_b)
    print("\tC. " + option_c)
    option = input("select action (a/b/c): ")
    if option.lower() in ["a", "b", "c"]:
        selected_option = True
    else:
        print("that's illegal.")

print("fin")
