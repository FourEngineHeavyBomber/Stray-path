page = input("which page is this? (non-fiction, music-videos, etc): ")

lcHtml = "---\nlayout: default\npermalink: /" + page + "/\n---\n"
lcHtml = lcHtml + "<div id='page-content'>\n\n\n"

add_video = True

while add_video:
    cont = input("add video? (t/f): ")
    if cont.lower() == "t":
        website = input("is this video from youtube or vimeo? (yt/vm): ")
        if website.lower() == "yt":
            link = input("paste link here: ")
            name = input("give the video a name (one word): ")
            name = name.split(" ")[0]
            lkHtml = "<iframe class='video centre' name='" + name + "' src='"
            lkHtml =  lkHtml + link + "' > \n </iframe>\n\n"
            lcHtml = lcHtml + lkHtml
        elif website.lower() == "vm":
            link = input("paste link here: ")
            name = input("give the video a name (one word): ")
            lkHtml = "<iframe name = '" + name
            lkHtml = lkHtml + "' src='" + link
            lkHtml = lkHtml + "class='video centre' frameborder='0' " 
            lkHtml = lkHtml + "allow='autoplay; fullscreen; picture-in-picture' allowfullscreen>"
            lkHtml = lkHtml + "</iframe>\n\n"
            lcHtml = lcHtml + lkHtml
        else:
            print("recalcitrance is UNACCEPTABLE")
    else:
        add_video = False

lcHtml = lcHtml + "</div>\n"

f = open("output.html", "w")
f.write(lcHtml)
f.close()

print("done.\ncheck output.html")
