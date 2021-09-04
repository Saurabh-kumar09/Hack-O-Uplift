bvc='''
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

                    MDLabel:
                        text:"Home"
                        halign:"center"
                        font_style:"H4"
                        size_hint_y:None
                        theme_text_color:"Custom"
                        text_color:(0,0,1,1)
                        bold:"true"



                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text:"Quotes of the day"

                                IconLeftWidget:
                                    icon:"arrow-right-thick"
                                MDRaisedButton:
                                    text:"Go"
                                    halign:"right"
                                    pos_hint:{"center_x": 0.7, "center_y": 0.4}
                                    on_release:self.show_data

                            OneLineIconListItem:
                                text:"Content"
                                IconLeftWidget:
                                    icon:"arrow-right-thick"
                                MDRaisedButton:
                                    text:"Go"
                                    halign:"right"
                                    pos_hint:{"center_x": 0.7, "center_y": 0.4}
                                    on_release:self.show_data
     

                            OneLineIconListItem:
                                text:"Task"
                                IconLeftWidget:
                                    icon:"arrow-right-thick"
                                MDRaisedButton:
                                    text:"Go"
                                    halign:"right"
                                    pos_hint:{"center_x": 0.7, "center_y": 0.4}
                                    on_release:self.show_data

                            OneLineIconListItem:
                                text:"Show Your Skills"
                                IconLeftWidget:
                                    icon:"arrow-right-thick"
                                MDRaisedButton:
                                    text:"Go"
                                    halign:"right"
                                    pos_hint:{"center_x": 0.7, "center_y": 0.4}
                                    on_release:self.show_data

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

