self.chartbutton = customtkinter.CTkButton(self.innner_main_frame, text="chart", command=self.show_chart_frame, corner_radius=5, width=60, height=18, font=(self.font, 15))

        # self.chartbutton.place(x=600, y=220)

        # self.tablebutton = customtkinter.CTkButton(self.innner_main_frame, text="Bookings", command=self.show_table_frame,
        #                                            corner_radius=5, width=60, height=18, font=(self.font, 15))

        # self.tablebutton.place(x=510, y=220)

        # self.show_table_frame()

    def show_chart_frame(self):
        if not self.table_frame is None:
            self.table_frame.destroy()
            self.table_frame = None

        self.chart_frame = customtkinter.CTkFrame(self.graph_tab, width=1140, height=450, corner_radius=10)
        self.chart_frame.place(x=30, y=260)

        chart_label = customtkinter.CTkLabel(self.chart_frame, text="Daily Booking Records Chart", font=(self.font, 25))
        chart_label.place(relx=0.5, rely=0.056, anchor="center")

        result = fetch_customer_booking()

        # preparing data for plotting
        dates = []
        bookings = []

        for row in result:
            dates.append(row[0])
            bookings.append(row[1])

        # creating a matplotlib figure
        figure, ax = plt.subplots(figsize=(11.8, 3.9))
        ax.set_facecolor('#f0f0f0')  # Set the background color of the chart

        # Plotting the line and getting the first element of the returned list
        line, = ax.plot_date(dates, bookings, '-')

        # to set the labels and the title for the chart
        ax.set_xlabel("Date", fontsize=10)
        ax.set_ylabel("Total Bookings", fontsize=10)

        # Set font size for the line
        ax.tick_params(axis='both', which='major', labelsize=9)

        # Set the y-axis ticks with a step of 5
        plt.yticks(range(0, max(bookings) + 5, 5))

        # creating a canvas for the Matplotlib figure
        canvas = FigureCanvasTkAgg(figure, master=self.chart_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=0, y=60)
        canvas.draw()


        # CREATING A FRAME TO SHOW THE TABLE
        self.table_frame = customtkinter.CTkFrame(self.graph_tab, width=1140, height=440, corner_radius=40)
        self.table_frame.place(x=30, y=10)


