from tkinter import *

import customtkinter
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Controller.admin_dashboard_dbms import fetch_customer_booking


class BookingLineChart:
    def __init__(self, window):
        self.window = window

    def show_chart(self):
        self.chart_window = Toplevel(self.window, bg="#2c2c2c", width=1140, height=400)
        self.chart_window.title("Daily Booking Records")
        self.chart_window.resizable(0,0)

        result = fetch_customer_booking()
        print(result)

        # preparing data for plotting
        dates = []
        bookings = []

        for row in result:
            dates.append(row[0])
            bookings.append(row[1])

        # creating a matplotlib figure
        figure, ax = plt.subplots(figsize=(11.8, 4))
        ax.plot_date(dates, bookings, '-')

        # to set the labels and the title for the chart
        ax.set_xlabel("Date")
        ax.set_ylabel("Total Bookings")
        ax.set_title("Daily Booking Records")

        # creating a canvas for the Matplotlib figure
        canvas = FigureCanvasTkAgg(figure, master=self.chart_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=0, y=0)

        canvas.draw()

if __name__ == '__main__':
    window = Tk()
    # window.geometry("1200x400")

    bookingChart = BookingLineChart(window)
    bookingChart.show_chart()
    window.mainloop()