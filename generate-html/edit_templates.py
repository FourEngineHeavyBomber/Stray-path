import os
from add_videos import add_videos_loop, get_video_details
from validation import valid_index

pages = ["presenting", "corporate" "non-fiction", "fiction", "music-videos", ]

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
    lcHtml = "---\nlayout: main\npermalink: /" + page + "/\n---\n"
    lcHtml = lcHtml + "<div id='main'>\n\n\n"
    lcHtml = lcHtml + add_videos_loop()
    lcHtml = lcHtml + "</div>\n"

    f = open("output.html", "w")
    f.write(lcHtml)
    f.close()
    
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

    f = open("output.html", "w")
    f.writelines(output)
    f.close()
    
    #var = sys.path.append('../FourEngineHeavyBomber.github.io')
    #var = os.path.join( os.getcwd(), '..', 'foo.txt' )
    #print(var)


def do_option_c():
    """
    this function deletes a specified video from the template
    """
    print("you selected option C")

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

    videos = []
    curr_video = []

    # separate body into indiv video sections
    for line in heres_a_list:
        curr_video += [line]
        if "/p" in line:
            print("end of video")
            # print(curr_video)
            videos.append(curr_video)
            curr_video = []

    #print(videos[1])
    n = len(videos)
    #print(videos[n-1])

    kill_more = True
    hit_list = []
    print("if the video at the top of the page has index 1, ...")
    while kill_more:
        kill_index = input("select the index of the video you want to delete: ")
        if valid_index(kill_index, n):
            kill_index = int(kill_index)
            hit_list.append(kill_index)
            keep_going = input("do you want to delete any more (y/n): ")
            if keep_going.lower() != "y":
                kill_more = False
            print()

    hit_list = list(dict.fromkeys(hit_list))
    hit_list.sort(reverse = True)
    print("removing videos at the following indexes: " + str(hit_list))

    for element in hit_list:
        videos.pop(element-1)

    print(videos)
    # now I need to flatten the videos list so it's a list (not a list of lists)
    # and append introduction to the start and "</div>" at the end.

    output = introduction

    for thing in videos:
        for thingy in thing:
            output += thingy

    output += ["</div>"]

    f = open("output.html", "w")
    f.writelines(output)
    f.close()



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
        print("I don't know how you've done this but it's illegal.")



print("fin")
