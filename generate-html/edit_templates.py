import os
from add_videos import add_videos_loop, get_video_details

pages = ["video-essays", "non-fiction", "fiction", "music-videos", ]

found_template = False
page_to_edit = ""

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
                page_to_edit = page_to_edit + ".html"
                break


option_a = "burn this page to the ground and start adding videos from scratch"
option_b = "add a new video to the top of the page"
option_c = "delete a specific video"

selected_option = False


def do_option_a():
    """
    this function builds a new template from scratch
    """
    lcHtml = "---\nlayout: default\npermalink: /" + page + "/\n---\n"
    lcHtml = lcHtml + "<div id='page-content'>\n\n\n"
    lcHtml = lcHtml + add_videos_loop()
    lcHtml = lcHtml + "</div>\n"
    print(lcHtml)
    
    print()


def do_option_b():
    """
    this function adds new videos to the top of the page
    """
    print("you selected option B")

    import os.path
    f = open(os.path.dirname(__file__) + '/../' + page_to_edit)

    lines = f.readlines()

    heres_a_list = []
    introduction = []
    
    for line in lines:
        heres_a_list.append(line)
        if "<div id='page-content'>" in line:
            introduction = heres_a_list
            heres_a_list = []
    f.close()

    html_injection = add_videos_loop()

    output = introduction
    output += [html_injection]
    output.extend(heres_a_list)

    for line in output:
        print(line)
    
    #var = sys.path.append('../FourEngineHeavyBomber.github.io')
    #var = os.path.join( os.getcwd(), '..', 'foo.txt' )
    #print(var)


def do_option_c():
    """
    this function deletes a specified video from the template
    """
    print()



while not selected_option:
    print("Select an action to perform on this page:")
    print("\tA. " + option_a)
    print("\tB. " + option_b)
    print("\tC. " + option_c)
    option = input("select action (a/b/c): ")
    if option.lower() in ["a", "b", "c"]:
        selected_option = True
        if option.lower() == "a":
            do_option_a()
        elif option.lower() == "b":
            do_option_b()
        else:
            do_option_c()
    else:
        print("that's illegal.")



print("fin")
