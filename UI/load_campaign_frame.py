import pathlib
from tkinter import *
from classes.Campaign import Campaign

class Load_Campaign_Frame:
    def __init__(self, window, links):
        self.window = window
        self.links = links
        self.frame = Frame(self.window, bg='#000000')
        self.frame.columnconfigure(index=0, weight=1)
        self.frame.rowconfigure(index=0, weight=1)
        self.check_box_dict = {}
        self.select = StringVar()
        self.labels()
        self.print_campaign_list()
        self.button_submit()


    def reset_frame(self):
        self.frame.grid_forget()

    def labels(self):
        font = ("Courrier", 20)
        label_name = Label(self.frame, text="Choose Campaign : ", font=font, bg='#000000',fg='white')
        label_name.grid(column=0,row=0,sticky="news")

    def campaign_list(self):
        campaigns = []
        for path in pathlib.Path("./campaigns/").iterdir():
            campaign = Campaign.load_campaign(path.name.split(".")[0])
            if campaign:
                campaigns.append(campaign)
        return campaigns

    def print_campaign_list(self):
        frame_list_campaign = Frame(self.frame, bg="#000000")
        frame_list_campaign.grid(column=0, columnspan=2, row=1,sticky="ew")
        i = 0
        for campaign in self.campaign_list():
            self.check_box_dict[campaign.campaign_name] = IntVar()
            info_campaign = ""
            for player in campaign.players.values():
                info_campaign = info_campaign +"-" + player.name + " " + player.pc_class + "   "

            check_box = Radiobutton(frame_list_campaign, text = campaign.campaign_name+" : ", variable = self.select, value = campaign.campaign_name,bg="#000000", fg="white")
            check_box.grid(column=0, row=i,sticky="w")
            i =i+1

    def button_submit(self):
        submit_button = Button(self.frame, text="Load", font=("Courrier", 25), bg='#000000',
                               fg='white', command=self.load_campaign)
        submit_button.grid(column=0, columnspan=2, row=2,sticky="ew")

    def load_campaign(self):
        self.links['open_campaign'](Campaign.load_campaign(self.select.get()))