import wx

BG_COLOR = wx.Colour(0, 0, 0)
TEXT_COLOR = wx.Colour(255, 255, 255)

class SettingsDialog(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title="Paramètres", size=(1920, 1080), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.STAY_ON_TOP)
        self.CenterOnScreen()

        # Création d'un panel avec défilement
        self.scrolled_panel = wx.ScrolledWindow(self, size=(1920, 1080), style=wx.VSCROLL | wx.HSCROLL)
        self.scrolled_panel.SetScrollRate(10, 10)  # Définit la vitesse de défilement
        self.scrolled_panel.SetBackgroundColour(BG_COLOR)

        # Initialisation des paramètres
        self.niveau_sonore = 100  
        self.pv = 100  
        self.tirs_par_joueur = 2  
        self.pv_par_tir = 10  
        # Gestion du niveau
        self.current_open_combo = None
        self.niveaux = {
            "Débutant": 1,
            "Intermédiaire": 2,
            "Avancé": 3,
            "Expert": 4
        }
        self.niveau_selectionne = None  # Stocke la valeur du niveau sélectionné

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddStretchSpacer(1)  # Ajoute un espace vide en haut

        # Visée automatique (toggle button)
        self.btn_vise = wx.ToggleButton(self.scrolled_panel, label="Visée automatique : Désactivée")
        self.btn_vise.Bind(wx.EVT_TOGGLEBUTTON, self.on_toggle_vise)
        vbox.Add(self.btn_vise, 0, wx.EXPAND | wx.ALL, 15)

        # Bouton pour afficher le menu de sélection du niveau
        self.btn_niveau = wx.Button(self.scrolled_panel, label="Niveau")
        self.btn_niveau.Bind(wx.EVT_ENTER_WINDOW, self.on_hover_niveau)
        self.btn_niveau.Bind(wx.EVT_BUTTON, self.on_hover_niveau)
        vbox.Add(self.btn_niveau, 0, wx.EXPAND | wx.ALL, 10)

        # Liste déroulante pour choisir le niveau
        self.choice_niveau = wx.ComboBox(self.scrolled_panel, choices=list(self.niveaux.keys()), style=wx.CB_READONLY)
        self.choice_niveau.Bind(wx.EVT_COMBOBOX, self.on_select_niveau)
        self.choice_niveau.Bind(wx.EVT_LEAVE_WINDOW, self.on_leave_combo)
        self.choice_niveau.Hide()
        vbox.Add(self.choice_niveau, 0, wx.EXPAND | wx.ALL, 10)

        # Ajout des sliders avec labels
        self.add_slider(vbox, "Niveau sonore", 0, 100, self.niveau_sonore, self.on_select_son)
        self.add_slider(vbox, "Points de vie", 10, 1000, self.pv, self.on_select_pv, tick=10)
        self.add_slider(vbox, "Nombre de tirs par joueur", 1, 10, self.tirs_par_joueur, self.on_select_tirs)
        self.add_slider(vbox, "Dégâts par tir", 10, 100, self.pv_par_tir, self.on_select_degats, tick=10)

        # Boutons OK / Annuler
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_ok = wx.Button(self.scrolled_panel, wx.ID_OK, label="OK Alt+O")
        btn_cancel = wx.Button(self.scrolled_panel, wx.ID_CANCEL, label="Annuler Alt+A")
        btn_sizer.Add(btn_ok, 0, wx.ALL, 15)
        btn_sizer.Add(btn_cancel, 0, wx.ALL, 15)
        vbox.Add(btn_sizer, 0, wx.ALIGN_CENTER)

        self.scrolled_panel.SetSizer(vbox)

        # Ajout du scrolled panel dans la fenêtre principale
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.scrolled_panel, 1, wx.EXPAND)
        self.SetSizerAndFit(main_sizer)

    def add_slider(self, sizer, label_text, min_val, max_val, initial_value, event_handler, tick=1):
        """ Ajoute un slider avec un titre et un label de valeur dynamique """
        slider_box = wx.BoxSizer(wx.VERTICAL)

        # Ajouter un titre au-dessus du slider
        title_label = wx.StaticText(self.scrolled_panel, label=label_text)
        title_label.SetForegroundColour(TEXT_COLOR)
        slider_box.Add(title_label, 0, wx.LEFT | wx.TOP, 10)

        # Ajouter le slider + valeur actuelle
        slider_row = wx.BoxSizer(wx.HORIZONTAL)
        
        slider = wx.Slider(self.scrolled_panel, value=initial_value, minValue=min_val, maxValue=max_val, style=wx.SL_HORIZONTAL)
        slider.Bind(wx.EVT_SLIDER, event_handler)
        if tick > 1:
            slider.SetTickFreq(tick)
        
        value_label = wx.StaticText(self.scrolled_panel, label=f"{initial_value}")
        value_label.SetForegroundColour(TEXT_COLOR)

        slider_row.Add(slider, 1, wx.EXPAND | wx.ALL, 10)
        slider_row.Add(value_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 10)

        slider_box.Add(slider_row, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(slider_box, 0, wx.EXPAND | wx.ALL, 10)

        # Stocker les éléments pour mise à jour dynamique
        setattr(self, f"slider_{label_text.replace(' ', '_').lower()}", slider)
        setattr(self, f"label_{label_text.replace(' ', '_').lower()}", value_label)

    def update_label(self, label_attr, value):
        """ Met à jour dynamiquement le label de valeur """
        label = getattr(self, label_attr, None)
        if label:
            label.SetLabel(str(value))

    def on_toggle_vise(self, event):
        """ Active ou désactive la visée automatique """
        self.btn_vise.SetLabel("Visée automatique : " + ("Activée" if self.btn_vise.GetValue() else "Désactivée"))

    def on_select_son(self, event):
        """ Met à jour le niveau sonore """
        valeur = self.slider_niveau_sonore.GetValue()
        self.update_label("label_niveau_sonore", valeur)

    def on_select_pv(self, event):
        """ Met à jour les points de vie """
        valeur = self.slider_points_de_vie.GetValue()
        self.update_label("label_points_de_vie", valeur)

    def on_select_tirs(self, event):
        """ Met à jour le nombre de tirs par joueur """
        valeur = self.slider_nombre_de_tirs_par_joueur.GetValue()
        self.update_label("label_nombre_de_tirs_par_joueur", valeur)

    def on_select_degats(self, event):
        """ Met à jour les dégâts par tir """
        valeur = self.slider_dégâts_par_tir.GetValue()
        self.update_label("label_dégâts_par_tir", valeur)

    def on_hover_niveau(self, event):
        """ Affiche la liste déroulante des niveaux lorsqu'on survole le bouton Niveau """
        if self.current_open_combo is not None and self.current_open_combo != self.choice_niveau:
            self.current_open_combo.Hide()
        self.current_open_combo = self.choice_niveau
        self.choice_niveau.Show()
        wx.CallAfter(self.choice_niveau.Popup)
        event.Skip()

    def on_select_niveau(self, event):
        """ Récupère la valeur du niveau sélectionné """
        choix = self.choice_niveau.GetStringSelection()
        self.niveau_selectionne = self.niveaux.get(choix, None)

    def on_leave_combo(self, event):
        """ Cache la liste déroulante lorsqu'on quitte la sélection """
        event.GetEventObject().Hide()
        event.Skip()

if __name__ == "__main__":
    app = wx.App(False)
    frame = SettingsDialog(None)
    frame.Show()
    app.MainLoop()
