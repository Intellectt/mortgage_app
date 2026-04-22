class CommonApp:
    """Base class for KivyMD example applications."""
    
    def open_menu(self, caller):
        """Opens a menu from the caller widget."""
        print(f"Menu opened from {caller}")
    
    def menu_callback(self, item_text):
        """Callback for menu items."""
        if item_text == "Exit":
            self.stop()
    
    def disabled_widgets(self):
        """Override this method to disable widgets in your app."""
        pass
