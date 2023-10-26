from django import http


def Solution(Default_Argument):
    return http.HttpResponse(
        '''<a href="https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg">100 Days Of Code By CodeWithHarry</a>
            <br>
            <br>
            <a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django Playlist By CodeWithHarry</a>
            <br>
            <br>
            <a href="https://www.youtube.com/watch?v=4tAp9Lu0eDI&t=1488s">Webscraping Tutorial Using BeautifulSoup By CodeWithHarry</a>
        '''
    )

    # pass
