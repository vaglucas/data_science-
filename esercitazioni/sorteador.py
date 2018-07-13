import urllib.request
import re
from bs4 import BeautifulSoup
from InstagramAPI import InstagramAPI
import time
from datetime import datetime, date
from random import randint
import json
import time


class Sorteio():
    def sortear(_URL, _name, _pass, _islike, _ismarker, _is_privado, _isFlower):
        start_time = time.time()

        try:
            doc = urllib.request.urlopen(_URL)
        except:
            print("ERROR")
            quit()

        soup = BeautifulSoup(doc)
        result = ''
        print("start for media id")
        media_id = ''
        for tag in soup.findAll("meta"):
            if 'media' in str(tag.get('content')):
                media_id = str((tag.get('content')))

        if '=' in media_id:
            media_id = media_id.split('=')[1]
        # stop conditions, the script will end when first of them will be true
        until_date = date.today()
        count = 50000
        if not _name and not _name:
            API = InstagramAPI("revisaapp", "")
        else:
            API = InstagramAPI(_name, _pass)
        API.login()
        API.getUsernameInfo('revisaapp')
        has_more_comments = True
        max_id = '50000'
        comments = []
        comentHtml = ''
        likers = []
        i = 0
        _ = API.mediaInfo(media_id)
        sizeComments = API.LastJson['items'][0]['comment_count']
        print(sizeComments)
        count = sizeComments
        max_sort = (sizeComments) - 1
        print(max_sort)
        randon = (randint(0, max_sort))
        print(randon)
        max_id = ''
        while has_more_comments:
            _ = API.getMediaComments(media_id, max_id=max_id)
            # comments' page come from older to newer, lets preserve desc order in full list
            for c in API.LastJson['comments']:
                comments.append(c)
                comentHtml = comentHtml + '<li><i class="fa fa-user bg-aqua"></i><div class="timeline-item"><h3 class="timeline-header no-border"> <a target="_blank" href="https://www.instagram.com/' + \
                             c['user']['username'] + '"> @' + c['user']['username'] + '</a>   ' + c[
                                 'text'] + '</h3></div></li>'
            #    has_more_comments = API.LastJson.get('has_more_comments', False)
            # evaluate stop conditions
            if count and len(comments) >= count:
                comments = comments[:count]
                # stop loop
                has_more_comments = False
                # print "stopped by count"
            # next page
            if has_more_comments:
                max_id = API.LastJson.get('next_max_id', '')


        campeao = True

        print(comments[randon])
        id_vencedor = comments[randon]['user_id']
        is_privado = comments[randon]['user']['is_private']
        nome_vencedor = comments[randon]['user']['full_name']
        username = comments[randon]['user']['username']
        userid = comments[randon]['user_id']
        texto = comments[randon]['text']
        imagProfile = comments[randon]['user']['profile_pic_url']
        print(username)
        result = result + '<img src="' + imagProfile + '"style="height: 120px; width: 120px; margin-left: 40%" class=" userimage img-circle" alt="Vencedor"><br><br>'

        result = result + 'Sorteado: ' + nome_vencedor + ' <a target="_blank" href="https://www.instagram.com/' + username + '"> @' + username + '</a>'
        if is_privado and _is_privado:
            campeao = False
            result = result + " nao apto a vencer, perfil privado"

        texto = comments[randon]['text']

        print(not _ismarker)
        if '@' in texto and _ismarker:
            result = result + ", Marcou um AMIGO!!!"
        elif _ismarker:
            campeao = False
            result = result + ",nao marcou um amigo"

        _ = API.userFriendship(userid)
        if _isFlower:
            if not _name and not _name and not API.LastJson['followed_by']:
                result = result + ', nao segue o @revisaapp'
                campeao = API.LastJson['followed_by']
            elif not API.LastJson['followed_by']:
                result = result + ', nao segue o @' + _name
                campeao = API.LastJson['followed_by']

        _ = API.getMediaLikers(media_id)
        for c in reversed(API.LastJson['users']):
            likers.append(c['pk'])
        if id_vencedor in likers and _islike:
            result = result + ", curtiu a foto! "
        elif _islike:
            campeao = False
            result = result + ", nao curtiu a foto"


        if campeao:
            result = result + ". VENCEU O SORTEIO<br><h>" + 'Comentario: ' + texto
        else:
            result = result + ". infelizmente nao cumpre os requisitos do sorteio<br><h>" + 'Comentario: ' + texto
        return result + 'SEPARADOR@TEXTO' + comentHtml
