import tkinter as tk
from tkintermapview import TkinterMapView

class GoogleMapView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Google Map Viewer")

        # Coordinates for Kathmandu, Nepal
        latitude = 27.7172
        longitude = 85.3240

        # Create a TkinterMapView
        self.map_view = TkinterMapView(self, width=800, height=600)
        self.map_view.pack(expand="true")

        # Set the position and zoom level
        self.map_view.set_position(latitude, longitude)
        self.map_view.zoom(12)

if __name__ == "__main__":
    root = tk.Tk()

    # Create a button to open the map window
    open_map_button = tk.Button(root, text="Show Kathmandu Map", command=lambda: GoogleMapView(root))
    open_map_button.pack(pady=20)

    root.geometry("400x300")
    root.title("Tkinter MapView Example")
    root.mainloop()
