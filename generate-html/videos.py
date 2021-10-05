page = input("which page is this? (non-fiction, music-videos, etc): ")

lcHtml = "---\nlayout: default\npermalink: /" + page + "/\n---\n"
lcHtml = lcHtml + "<div id='page-content'>\n\n\n"

add_video = True

while add_video:
    cont = input("add video? (t/f): ")
    if cont.lower() == "t":

        video_title = input("enter video title: ")
        lcHtml = lcHtml + "<h3 class='video-title'>" + video_title + "</h3>"
        lcHtml = lcHtml + "\n"
        
        website = input("is this video from youtube or vimeo? (yt/vm): ")
        if website.lower() == "yt":
            
            link = input("paste video ID - not link - here (for explanation enter H): ")
            while link.lower() == "h":
                print("youtube videos have an ID you can grab from their URL")
                print("in this >> https://youtu.be/tSbSkGoOO8M, the ID is tSbSkGoOO8M")
                print("in this >> https://www.youtube.com/watch?v=2Jn1OeDlNpM&ab_channel=EleannaSiozou")
                print("the ID is 2Jn1OeDlNpM")
                print("it's important you exclude v= and the &channel data")
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
    else:
        add_video = False

lcHtml = lcHtml + "</div>\n"

f = open("output.html", "w")
f.write(lcHtml)
f.close()

print("done.\ncheck output.html")
