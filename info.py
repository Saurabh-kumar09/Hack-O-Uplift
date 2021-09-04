username = """
MDTextField:
    hint_text:"Enter your Name"
    pos_hint:{"center_x":0.5,"center_y":0.7}
    size_hint_x:None
    width:300
"""

user_contact = """
MDTextField:
    hint_text:"Enter contact Number"
    pos_hint:{"center_x": 0.5, "center_y": 0.6}
    size_hint_x:None
    width:300

"""

user_Email = """
MDTextField:
    hint_text:"Enter your Email-id"
    helper_text:"Email-id should be in the format @gmail.com"
    helper_text_mode: "on_focus"
    pos_hint:{"center_x": 0.5, "center_y": 0.5}
    size_hint_x:None
    width:300

"""

set_password = """
MDTextField:
    hint_text:"Set your password"
    helper_text:"Password should be in minimum 6 characters and maximum 9 characters"
    helper_text_mode: "on_focus"
    pos_hint:{"center_x": 0.5, "center_y": 0.4}
    size_hint_x:None
    width:300

"""

confirm_password = """
MDTextField:
    hint_text:"Confirm your password"
    helper_text:"Password should be same as set_password"
    helper_text_mode: "on_focus"
    pos_hint:{"center_x": 0.5, "center_y": 0.3}
    size_hint_x:None
    width:300

"""

label = '''
MDLabel:
  text:"ConFeTalk"
  halign:"center"
  text_size:root.width,root.height
  valign:"top"
  theme_text_color:"Custom"
  text_color:(51 / 255.0, 204 / 255.0, 255 / 255.0, 1)
  font_style:"H4" 
  pos_hint:{"center_x":0.5,"center_y":0.4}
'''

idea = '''
MDLabel:
  text:"Talk Fearlessly With Confidence"
  valign:"top"
  text_size:None,root.height
  theme_text_color:"Error"
  font_style:"H6"
  pos_hint:{"center_x":0.5,"center_y":0.3}

'''

btn_v = '''
MDRoundFlatButton:
     text:"proceed"
     pos_hint:{"center_x": 0.5, "center_y": 0.2}
     on_release:self.show_data
'''

content_section = '''
Screen:
    ScrollView:                  
        MDList:
            OneLineIconListItem:
                text:"Content"
                theme_text_color:"Custom"
                text_color:(0,0,1,1)

                    
            OneLineIconListItem:
                text:"Article"
                IconLeftWidget:
                    icon:"arrow-right-thick"
                
            OneLineIconListItem:
                text:"Audio"
                IconLeftWidget:
                    icon:"arrow-right-thick"
                
            OneLineIconListItem:
                text:"Video"
                IconLeftWidget:
                    icon:"arrow-right-thick"
                
            OneLineIconListItem:
                text:"Others"
                IconLeftWidget:
                    icon:"arrow-right-thick"
'''

Task_Section = '''
Screen:
    ScrollView:                  
        MDList:
            OneLineIconListItem:
                text:"Task"
                theme_text_color:"Custom"
                text_color:(0,0,1,1)


            OneLineIconListItem:
                text:"Article"
                IconLeftWidget:
                    icon:"arrow-right-thick"

            OneLineIconListItem:
                text:"Audio"
                IconLeftWidget:
                    icon:"arrow-right-thick"

            OneLineIconListItem:
                text:"Video"
                IconLeftWidget:
                    icon:"arrow-right-thick"

            OneLineIconListItem:
                text:"Others"
                IconLeftWidget:
                    icon:"arrow-right-thick"
'''

navi = '''
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:"vertical"
                    MDToolbar:
                        title:"ConFeTalk"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        elevation:15
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                id:Quotes of the day
                                text:"Quotes of the day"
                                on_release:print("Go to quotes section")
                                
                                IconLeftWidget:
                                    icon:"arrow-right-thick"
                                
                            OneLineIconListItem:
                                text:"Content"
                                IconLeftWidget:
                                    icon:"arrow-right-thick"
                                
                            OneLineIconListItem:
                                text:"Task"
                                IconLeftWidget:
                                    icon:"arrow-right-thick"
                                
                            OneLineIconListItem:
                                text:"Show Your Skills"
                                IconLeftWidget:
                                    icon:"arrow-right-thick"                     
                            
        MDNavigationDrawer:
            id:nav_drawer
            BoxLayout:
                orientation:"vertical"
                
                Image:
                    source:"communication.png"
                
                MDLabel:
                    text:"ConFeTalk"
                    halign:"center"
                    font_style:"H5"
                    size_hint_y:None
                    height:self.texture_size[1]
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"Profile"
                            
                            IconLeftWidget:
                                icon:"face-profile"
                                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"About"
                            
                            IconLeftWidget:
                                icon:"alpha-a-box"
                                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"Home"
                            
                            IconLeftWidget:
                                icon:"alpha-h-box"
                                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"Settings"
                            
                            IconLeftWidget:
                                icon:"alpha-s-box"
                                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"Feedback"
                            
                            IconLeftWidget:
                                icon:"alpha-f-box"
                                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"Logout"
                            
                            IconLeftWidget:
                                icon:"logout"
                

'''

Article = '''
MDLabel:
  text:"Article"
  halign:"left"
  pos_hint:{"center_x": 0.8, "center_y": 0.8}
  a = input(How_To_Talk.docx)
  font_style:"H4"
  size_hint_y:None
  theme_text_color:"Custom"
  text_color:(0,0,1,1)

'''