import os

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


def print_help():
    print("youtube videos have an ID you can grab from their URL")
    print("in this >> https://youtu.be/tSbSkGoOO8M, the ID is tSbSkGoOO8M")
    print("in this >> https://www.youtube.com/watch?v=2Jn1OeDlNpM&ab_channel=EleannaSiozou")
    print("the ID is 2Jn1OeDlNpM")
    print("it's important you exclude v= and the &channel data")


def get_video_details():
    video_title = input("enter video title: ")
    lcHtml = "<h3 class='video-title'>" + video_title + "</h3>"
    lcHtml = lcHtml + "\n"

    website = input("is this video from youtube or vimeo? (yt/vm): ")
    if website.lower() == "yt":
        link = input(
            "paste video ID - not link - here (for explanation enter H): "
            )
        while link.lower() == "h":
            print_help()
            link = input("paste video ID here (this is for SEO, it will not be visible): ")
        name = input("give the video a name (one word): ")
        name = name.split(" ")[0]
        lkHtml = "<iframe class='video centre' name='" + name + "' src='"
        lkHtml =  lkHtml + "https://www.youtube.com/embed/" + link
        lkHtml =  lkHtml + "' > \n </iframe>\n\n"
        lcHtml = lcHtml + lkHtml

        description = input("enter video description: ")
        lcHtml = lcHtml + "<p class='video-description'>" + description
        lcHtml = lcHtml + "</p>"
        lcHtml = lcHtml + "\n"

    elif website.lower() == "vm":
        link = input("paste video ID here: ")
        name = input("give the video a name (one word): ")
        
        lkHtml = "<iframe name = '" + name
        lkHtml = lkHtml + "' src='https://player.vimeo.com/video/" + link +"?title=0&byline=0&portrait=0'\n"
        lkHtml = lkHtml + "class='video centre' frameborder='0' \n"
        lkHtml = lkHtml + "allow='autoplay; fullscreen; picture-in-picture' allowfullscreen>\n"
        lkHtml = lkHtml + "</iframe>\n\n"
        lcHtml = lcHtml + lkHtml

        description = input("enter video description: ")
        lcHtml = lcHtml + "<p class='video-description'>" + description
        lcHtml = lcHtml + "</p>"
        lcHtml = lcHtml + "\n"

    else:
        print("recalcitrance is UNACCEPTABLE")

    return lcHtml
            


def do_option_a():
    """
    this function builds a new template from scratch
    """
    lcHtml = "---\nlayout: default\npermalink: /" + page + "/\n---\n"
    lcHtml = lcHtml + "<div id='page-content'>\n\n\n"

    add_video = True
    while add_video:
        cont = input("add video? (t/f): ")
        if cont.lower() == "t":
            lcHtml = lcHtml + get_video_details()
        else:
            add_video = False

    lcHtml = lcHtml + "</div>\n"
    print(lcHtml)
    
    print()


def do_option_b():
    """
    this function adds a new video to the top of the page
    """
    print("you selected option B")

    import os.path
    f = open(os.path.dirname(__file__) + '/../' + page_to_edit)

    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()
    
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
