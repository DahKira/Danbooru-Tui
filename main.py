from pybooru import Danbooru
import random
import os

post_amount = ''

base_tags = ''

tags = ''

loop = 'true'

exit = 0

posts = ''

img_status = 'disabled'

sfw_status = 'disabled'

select = ''

client = ''


def menu():


     global img_status

     global select


     os.system('clear')


     print('(1) search with tags - maximum of 2')

     print(f'(2) toggle SFW mode - currently {sfw_status}')

     print(f'(3) toggle images for posts - currently {img_status}')

     print(f'(any other key) exit')

     select = input(': ')

     os.system('clear')

     update()


def update():

     global sfw_status

     global img_status

     global select


     if select == '1':

          tag_input()


     if select == '2':


          changed = 0

          if sfw_status == 'disabled':

               changed = 1

               sfw_status = 'enabled'


          if changed == 0:


               if sfw_status == 'enabled':


                    sfw_status = 'disabled'

          menu()

     if select == '3':


          changed = 0

          if img_status == 'disabled':

               changed = 1

               img_status = 'enabled'


          if changed == 0:


               if img_status == 'enabled':


                    img_status = 'disabled'

          menu()


def tag_input():


     global base_tags

     select = ''

     os.system('clear')

     if sfw_status == 'disabled':


          base_tags = ''


     if sfw_status == 'enabled':


          base_tags = '-rating:explicit -rating:questionable'


     print('(1) input tags - maximum of 2')

     print('(2) go back')


     select = input(': ')


     if select == '1':

          os.system('clear')

          print('enter tags')

          tags = input(': ')

          base_tags += tags

          post_fetch()

     if select == '2':

          menu()


def post_fetch():

     global client

     global select

     global base_tags

     global img_status

     global posts

     global post_amount


     os.system('clear')

     client = Danbooru('danbooru')

     posts = client.post_list(limit=100, tags=base_tags)

     post_amount = len(posts)

     post_amount -= 1

     post_found = 1


     if post_amount < 1:


         print('No posts found')

         loop = 0

         post_found = 0


     select_post()


def select_post():

      global client

      global posts

      global post_amount

      global base_tags

      global img_status

      os.system('clear')


      selected_post1 = input(f'Select a post (1/{post_amount}): ')

      selected_post = int(selected_post1)

      post_str = str(posts[selected_post])


      link = 'https://danbooru.donmai.us/posts/'

      link += post_str[7:(post_str.find(','))]

      id = post_str[7:(post_str.find(','))]


      artist = post_str[(post_str.find("'tag_string_artist':")):(post_str.find("', 'tag_string_meta':"))]


      image_url = post_str[(post_str.find("file_url': '")):(post_str.find("', 'large"))]

      image_url_final = image_url[12:]


      img_cmd = 'timg '

      img_cmd += image_url_final


      print(' ')
      print('queried tags')
      print('----------')

      print(base_tags)


      print(' ')
      print('Post Link')
      print('----------')

      print(link)


      print(' ')
      print('Artist')
      print('---------')

      print(artist[22:])


      if img_status == 'enabled':

          print(' ')

          os.system(img_cmd)

      print(' ')

      print('(1) select another post')

      print('(2) back to the menu')


      select = input(': ')


      if select == '1':

           select_post()


      if select == '2':

           menu()


menu()
